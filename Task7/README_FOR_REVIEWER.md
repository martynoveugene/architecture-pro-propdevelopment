# запускаем чистый куб
minikube stop                                                                                                                                                            
minikube delete                                                                                                                                                          
minikube start

# создаем неймспейс
kubectl apply -f .\01-create-namespace.yaml                                                                                                                              

# проверяем, что без gatekeeper создаются insecure pods
.\verify\verify-admission.sh
.\verify\validate-security.sh

# удаляем созданное
minikube kubectl -- delete pod pod-host-path -n audit-zone
minikube kubectl -- delete pod pod-privileged -n audit-zone
minikube kubectl -- delete pod pod-root-user -n audit-zone
minikube kubectl -- delete pod pod-host-path-fixed -n audit-zone
minikube kubectl -- delete pod pod-privileged-fixed -n audit-zone
minikube kubectl -- delete pod pod-root-user-fixed -n audit-zone

# устанавливаем gatekeeper
minikube kubectl -- apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/deploy/gatekeeper.yaml 

# применяем темплейты и констрейнты

kubectl apply -f .\gatekeeper\constraint-templates\hostpath.yaml                                                                                                         
kubectl apply -f .\gatekeeper\constraint-templates\privileged.yaml                                                                                                       
kubectl apply -f .\gatekeeper\constraint-templates\runasnonroot.yaml                                                                                                     

kubectl apply -f .\gatekeeper\constraints\hostpath.yaml
kubectl apply -f .\gatekeeper\constraints\privileged.yaml
kubectl apply -f .\gatekeeper\constraints\runasnonroot.yaml   

# проверяем еще раз - insecure не создаются, secure создаются
.\verify\verify-admission.sh
.\verify\validate-security.sh
