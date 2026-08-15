terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "terraform"
      Compliance  = "CMS-9115-0057"
    }
  }
}

module "s3" {
  source      = "./modules/s3"
  environment = var.environment
  project     = var.project_name
}

module "dynamodb" {
  source      = "./modules/dynamodb"
  environment = var.environment
  project     = var.project_name
}

module "vpc" {
  source      = "./modules/vpc"
  environment = var.environment
  project     = var.project_name
  vpc_cidr    = var.vpc_cidr
}

module "documentdb" {
  source         = "./modules/documentdb"
  environment    = var.environment
  project        = var.project_name
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.private_subnet_ids
  instance_class = var.documentdb_instance_class
}

module "eks" {
  source             = "./modules/eks"
  environment        = var.environment
  project            = var.project_name
  vpc_id             = module.vpc.vpc_id
  subnet_ids         = module.vpc.private_subnet_ids
  node_instance_type = var.eks_node_instance_type
}

module "apigateway" {
  source      = "./modules/apigateway"
  environment = var.environment
  project     = var.project_name
}
