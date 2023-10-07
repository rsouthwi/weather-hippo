APP_NAME = weather-api
APP_VERSION = 'prod'

AWS_ECR_ACCOUNT_ID ?= 910120794347
AWS_ECR_REGION ?= us-east-1
AWS_ECR_REPO = $(APP_NAME)

TAG ?= $(APP_VERSION)

.PHONY : docker/build docker/push/run docker/test

docker/build :
	docker buildx build --platform linux/amd64 -t $(APP_NAME):$(APP_VERSION) .

docker/push : docker/build
	aws ecr get-login-password --region $(AWS_ECR_REGION) | docker login --username AWS --password-stdin $(AWS_ECR_ACCOUNT_ID).dkr.ecr.$(AWS_ECR_REGION).amazonaws.com
	docker tag $(APP_NAME):$(APP_VERSION) $(AWS_ECR_ACCOUNT_ID).dkr.ecr.$(AWS_ECR_REGION).amazonaws.com/$(AWS_ECR_REPO):$(TAG)
	docker push $(AWS_ECR_ACCOUNT_ID).dkr.ecr.$(AWS_ECR_REGION).amazonaws.com/$(AWS_ECR_REPO):$(TAG)


docker/run :
	docker run -d -p 9000:8080 $(AWS_ECR_ACCOUNT_ID).dkr.ecr.$(AWS_ECR_REGION).amazonaws.com/$(AWS_ECR_REPO):$(TAG)

docker/test :
	@echo "*** testing POST ***"
	curl -XPOST 'http://localhost:9000/2015-03-31/functions/function/invocations' -d '{"location": 22314}'
	@echo "\n\n*** testing GET ***"
	curl 'http://localhost:9000/2015-03-31/functions/function/invocations' -d '{}'