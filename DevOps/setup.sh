# Terraform install
sudo apt update

# Hashicorp GPG Key
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -

# Hashicorp Linux repository
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"

# Update and install
sudo apt-get update && sudo apt-get install terraform

# Verify
terraform -help

# Install AWS CLI and set up kubectl

sudo apt update
sudo apt install awscli
echo "enter access key, secret key, region eu-west-1 within aws configure on next command"
aws configure 

curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.22.6/2022-03-09/bin/linux/amd64/kubectl

chmod +x ./kubectl

mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin

echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc

kubectl version --short --client
