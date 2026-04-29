сбор логов, все комманды запускать из директории Task6:
запуск чистого миникуб:
minikube delete
minikube start
minikube status

потом копирование в куб дополнительного policy:
minikube cp .\config\audit-policy.yaml /var/lib/minikube/certs/audit-policy.yaml

применение полиси:
.\start.ps1

перенаправление логов на хост:
.\logging.ps1

запуск инцидентов в другом терминале
.\simulate-incident.sh

парсинг логов:
python filter.py audit.log

