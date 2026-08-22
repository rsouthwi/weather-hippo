APP_NAME = weather-api
APP_VERSION = 'prod'

.PHONY : docker/build docker/run docker/test zip/build

docker/build :
	docker buildx build --platform linux/amd64 -t $(APP_NAME):$(APP_VERSION) .

zip/build :
	rm -rf build lambda.zip
	pip install -r requirements.txt --target build --platform manylinux2014_x86_64 --only-binary=:all: --implementation cp --python-version 3.12
	cp main.py mappers.py .env build/
	cd build && zip -r ../lambda.zip . -x '__pycache__/*' && cd ..

docker/run : docker/build
	docker run -d -p 9000:8080 $(APP_NAME):$(APP_VERSION)

docker/test :
	@echo "*** testing POST ***"
	curl -XPOST 'http://localhost:9000/2015-03-31/functions/function/invocations' -d '{"location": 22314}'
	@echo "\n\n*** testing GET ***"
	curl 'http://localhost:9000/2015-03-31/functions/function/invocations' -d '{}'