#!/bin/bash
set -o errexit
set -o errtrace
set -o nounset
set -o pipefail

export DEBIAN_FRONTEND="noninteractive"
INIT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

apt-get update && apt-get install -y apg curl
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get update
apt-get install -y docker-ce
usermod -aG docker candidate

cp -R "${INIT_DIR}/src/" /sql/
docker build -t sql /sql/
docker run -d --restart=always --name sql -p 80:5000 sql