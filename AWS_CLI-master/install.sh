sudo apt-get update
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker ubuntu
newgrp docker
docker pull sequenceiq/ambari:1.7.0
# curl -Lo .amb j.mp/docker-ambari-170 && . .amb

##Server Node
docker run -d --dns 127.0.0.1 -p 8080:8080 -p 7373:7373 -p 7946:7946 --entrypoint /usr/local/serf/bin/start-serf-agent.sh -e KEYCHAIN= --name amb0 -h amb0.mycorp.kom sequenceiq/ambari:1.7.0 --tag ambari-server=true 
##Client Node

docker run -d -e SERF_JOIN_IP=172.17.0.6 -p 7373:7373 -p 7946:7946 --dns 127.0.0.1 --entrypoint /usr/local/serf/bin/start-serf-agent.sh -e KEYCHAIN= --name amb2 -h amb2.mycorp.kom sequenceiq/ambari:1.7.0 --log-level debug
