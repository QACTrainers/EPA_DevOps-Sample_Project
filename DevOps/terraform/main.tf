provider "aws" {
  region     = var.AWS_REGION
  access_key = var.access_key
  secret_key = var.secret_key
}

module "vpc-igw-1" {
  source = "./vpc"
}

module "ec2_1" {
  source        = "./ec2"
  vpc_id_ec2    = module.vpc-igw-1.vpc_id
  subnet_id_ec2 = module.vpc-igw-1.subnet_id
}

