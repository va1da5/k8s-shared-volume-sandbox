.PHONY: push deploy pv

push:
	cd src; \
	docker build -t todo-app:latest .

deploy:
	@kubectl create ns todos;\
	kubectl config set-context --current --namespace=todos ;\
	kubectl apply -f kubernetes/pvc.yml; \
	kubectl apply -f kubernetes/configmap.yml;\
	kubectl apply -f kubernetes/secret.yml;\
	kubectl apply -f kubernetes/deployment.yml;\
	kubectl apply -f kubernetes/service.yml;\
	kubectl patch deployment todo-deploy -p "{\"spec\": {\"template\": {\"metadata\": { \"labels\": {  \"redeploy\": \"$(shell date +%s)\"}}}}}"

remove:
	kubectl delete -f kubernetes/deployment.yml;\
	kubectl delete -f kubernetes/pvc.yml;\
	kubectl delete -f kubernetes/configmap.yml;\
	kubectl delete -f kubernetes/secret.yml;\
	kubectl delete -f kubernetes/service.yml;\
	kubectl delete ns todos
	kubectl config set-context --current --namespace=default

pv:
	kubectl apply -f kubernetes/pv.yml