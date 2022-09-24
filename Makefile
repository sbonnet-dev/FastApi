include ${PWD}/Environments/${ENV}.env

azure_container_lower = $(shell echo ${AZURE_CONTAINER_REGISTRY_NAME} | awk '{print tolower($$0)}')

up: login build push

login:
	docker login \
	${azure_container_lower}.azurecr.io \
	-u $$(az acr credential show -n ${AZURE_CONTAINER_REGISTRY_NAME} --query="username" -o tsv) \
	-p $$(az acr credential show -n ${AZURE_CONTAINER_REGISTRY_NAME} --query="passwords[0].value" -o tsv)

build-m1:
	docker build \
	-f ./Docker/Dockerfile \
	-t ${azure_container_lower}.azurecr.io/apiservice:v1 --build-arg ENV=${ENV} ${PWD}

build:
	docker build \
	--platform linux/amd64 \
	-f ./Docker/Dockerfile \
	-t ${azure_container_lower}.azurecr.io/apiservice:v1 --build-arg ENV=${ENV} ${PWD}

local:
	./Scripts/starter.sh

deploy:
	echo "deploy"