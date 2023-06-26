# Weather Backend

##Local Development
Create a .env file in the /weather-api directory

Copy the API key from your account at [WeatherAPI](https://www.weatherapi.com).

Add the value to the .env file like as `WEATHER_API_KEY`

From the /weather-api directory:

* `docker build -t weather-api .`
* `docker run -d -p 9000:8080 weather-api`
* fire a `POST` to `http://localhost:9000/2015-03-31/functions/function/invocations`

## AWS Deployment
From the /weather-api directory:

* `make docker/push TAG=prod` <= pushes to AWS ECR
* `make docker/run` <= runs a container locally
* `maker docker/test` <= tests a local POST curl command

from the weather-hippo root directory:

* `terraform init`
* `terraform plan -var="env_name=prod"`
* `terraform apply -var="env_name=prod"`

The function should appear [here](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions)

##### To delete the Lambda
* `terraform destroy -var="env_name=prod"`
