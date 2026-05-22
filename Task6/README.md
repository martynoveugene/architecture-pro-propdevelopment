сбор логов, все комманды запускать из директории Task6:

запуск чистого миникуб:
```sh
minikube delete
minikube start
minikube status
```

потом копирование в куб дополнительного policy:
```sh
minikube cp .\config\audit-policy.yaml /var/lib/minikube/certs/audit-policy.yaml
```

применение полиси:
```sh
.\start.ps1
```

перенаправление логов на хост:
```sh
.\logging.ps1
```

запуск инцидентов в другом терминале
```sh
.\simulate-incident.sh
```

парсинг логов:
```sh
python filter.py audit.log
```

