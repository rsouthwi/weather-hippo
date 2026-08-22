terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

variable "env_name" {
  description = "Environment name"
}

resource "aws_lambda_function" "weather_backend_function" {
  function_name    = "weather-api"
  timeout          = 10  # seconds
  memory_size      = 256 # MB, up from the 128 default to speed up cold starts
  filename         = "${path.module}/weather-api/lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/weather-api/lambda.zip")
  handler          = "main.lambda_handler"
  runtime          = "python3.12"
  package_type     = "Zip"

  role = aws_iam_role.weather_backend_function_role.arn

  environment {
    variables = {
      ENVIRONMENT = var.env_name
    }
  }
}

resource "aws_lambda_permission" "allow_api_gateway_invoke" {
  statement_id  = "apigateway-invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.weather_backend_function.function_name
  principal     = "apigateway.amazonaws.com"

  # the "weather-api" REST API (id y61am9ahph) is set up outside this
  # Terraform config; this grants it invoke access so a Lambda replacement
  # (e.g. the package_type change) doesn't silently strip that permission again
  source_arn = "arn:aws:execute-api:us-east-1:910120794347:y61am9ahph/*/*/*"
}

resource "aws_iam_role" "weather_backend_function_role" {
  name = "weather-api"

  assume_role_policy = jsonencode({
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}
