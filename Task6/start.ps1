#minikube start \
#  --mount \
#  --mount-string="minikube-config.yaml:/etc/ca-certificates/audit-policy.yaml" \
#  --extra-config=apiserver.audit-policy-file=/etc/ca-certificates/audit-policy.yaml \
#  --extra-config=apiserver.audit-log-path=/var/log/audit.log

#  --extra-config=apiserver.audit-log-maxsize=10
$env:MSYS_NO_PATHCONV = 1

minikube start `
  --extra-config=apiserver.audit-policy-file=/var/lib/minikube/certs/audit-policy.yaml `
  --extra-config=apiserver.audit-log-path=-
#  --extra-config="apiserver.feature-gates=LegacyAudit=true"

#  --memory=4096 --cpus=2 `
#  --mount `
#  --mount-string="C:\Users\eugene\IdeaProjects\architecture-pro-propdevelopment\Task6\config:/data" `

minikube status

#minikube start \
#  --extra-config="apiserver.audit-policy-file=C:/Users/eugene/IdeaProjects/architecture-pro-propdevelopment/Task6/config/audit-policy.yaml" \
#  --extra-config="apiserver.audit-log-path=/audit.log" \
#  --extra-config="apiserver.feature-gates=LegacyAudit=true"

# read -p "Нажмите Enter, чтобы продолжить..."
