resource "aws_security_group" "ssh_allowed" {
  vpc_id = var.vpc_id_ec2

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = [var.open_internet]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.open_internet]
  }

  tags = {
    Name = "ssh_allowed"
  }
}

resource "aws_security_group_rule" "http" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks       = [var.open_internet]
  security_group_id = aws_security_group.ssh_allowed.id
}

resource "aws_security_group_rule" "jenkins" {
  type              = "ingress"
  from_port         = 8080
  to_port           = 8080
  protocol          = "tcp"
  cidr_blocks       = [var.open_internet]
  security_group_id = aws_security_group.ssh_allowed.id
}

resource "aws_instance" "example" {
  ami                    = var.ami_uk
  instance_type          = var.type
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.ssh_allowed.id]
  subnet_id              = var.subnet_id_ec2
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCV8ki93lhlc2VxePxim9iBe/S4vvt1DQoRDytfHrf8gJZp2LCpk0IsYvrrFdgBRoET09C5SUxfh+c5lLnJsh+Fhqi1a6CJx1DQpEC7Lw0ttbNhfowsW0D2L3NmqApURKEG7tJBp6VNm5yOr4ETKa5OLTJxNnyhWPYV5e8SyPRUXae9jJsnCsPuU8gWv87pj0JuqoIn66ZGj8xhFjvUsXFTqe2QIC6s0Ueio1Jgia6gaSDbLO4nbGTfY1q/D0Wm9WvN0A9b6lMCoEQ4GmRcWIOuJ2SMXSgl0YbGMTCBrJfxs9+2RUpfRRSVQ1Asqkg+FEQfQS0jVJt2U3bxPicFPefaH8DLDeJWIlxGRiVpsNmUiWoRIY5C8Ue2WZ97PFEtXTY2ZZBaZvB5MsVedtjAdBlADUxQTD6xAwxy/MYStUoXd/xveEb01oR+t7SOby9IvHbbXaOmiIrNQUTNNW11Lmxz3xdPufxoSSzCU/W91A3fzXR320eC8NwkxVW1u2e3GOs= ubuntu@ip-172-31-34-84"
}