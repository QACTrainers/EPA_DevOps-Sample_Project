variable "AWS_REGION" {
  default = "eu-west-1"
}

variable "secret_key" {
  default = ""
  # sensitive = true means Terraform won't output the value of this variable 
  sensitive = true
}

variable "access_key" {
  default = ""
  # sensitive = true means Terraform won't output the value of this variable 
  sensitive = true
}
