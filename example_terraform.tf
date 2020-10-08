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
    CreatedBy = "Terraform"
    Owner     = "Test Project"
  }
}

resource "aws_instance" "foo" {
  ami           = "ami-0ff8a91507f77f867"
  instance_type = "t1.2xlarge" # invalid type!
}
