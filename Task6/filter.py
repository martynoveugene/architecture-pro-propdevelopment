import json
import sys
import os

OUTPUT_FILE = "audit-extract.log"

def log_and_print(message, mode='a'):
    print(message)
    with open(OUTPUT_FILE, mode, encoding='utf-16') as f:
        f.write(message + "\n")

def filter_audit(log_file):
    if not os.path.exists(log_file):
        print(f"Error: file {log_file} not found.")
        return

    with open(OUTPUT_FILE, 'w', encoding='utf-16') as f:
        f.write(f"--- Filtering results {log_file} ---\n")

    secrets_access = []
    exec_events = []
    privileged_pods = []

    print(f"File analyze: {log_file}...")

    with open(log_file, 'r', encoding='utf-16') as f:
        for line in f:
            try:
                event = json.loads(line)
                obj_ref = event.get('objectRef', {})
                verb = event.get('verb', '')

                if obj_ref.get('resource') == 'secrets' and verb in ['get', 'list', 'watch']:
                    secrets_access.append(event)

                if verb == 'create' and obj_ref.get('subresource') == 'exec':
                    exec_events.append(event)

                containers = event.get('requestObject', {}).get('spec', {}).get('containers', [])
                for container in containers:
                    if container.get('securityContext', {}).get('privileged') is True:
                        privileged_pods.append(event)
                        break
            except json.JSONDecodeError:
                continue

    sections = [
        ("=== Access to secrets ===", secrets_access),
        ("=== Exec in pod ===", exec_events),
        ("=== Privileged pod ===", privileged_pods)
    ]

    for title, data in sections:
        log_and_print(f"\n{title}")
        for item in data:
            log_and_print(json.dumps(item, indent=2, ensure_ascii=False))

    log_and_print("\n=== Change audit policy ===")
    with open(log_file, 'r', encoding='utf-16') as f:
        for line in f:
            if "audit-policy" in line.lower():
                log_and_print(line.strip())

    print(f"\nResults are in {OUTPUT_FILE}")
    input("\nPress Enter...")

if __name__ == "__main__":
    # Если аргумент не передан, ищем audit.log
    file_path = sys.argv[1] if len(sys.argv) > 1 else 'audit.log'
    filter_audit(file_path)
