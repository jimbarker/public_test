terraform {
  required_version = "~> 0.13.3"

  required_providers {
    aws = {
      version = ">= 3.8.0"
      source  = "hashicorp/aws"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "eu-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-a4b950c3"
  instance_type = "t2.micro"
  tags = {
    Repo      = "public_test"
    CreatedBy = "Terraform"
  }
}
