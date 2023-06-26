terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~>4.0"
        }
    }
}

provider "aws" {
    region = "us-east-1"
}

variable "env_name" {
  description = "Environment name"
}

data "aws_ecr_repository" "weather_backend_ecr_repo" {
  name = "weather-api"
}

resource "aws_lambda_function" "weather_backend_function" {
  function_name = "weather-api"
  timeout       = 5 # seconds
  image_uri     = "${data.aws_ecr_repository.weather_backend_ecr_repo.repository_url}:${var.env_name}"
  package_type  = "Image"

  role = aws_iam_role.weather_backend_function_role.arn

  environment {
    variables = {
      ENVIRONMENT = var.env_name
    }
  }
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
