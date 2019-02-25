[![Build Status](https://travis-ci.org/MSchietzsch/test-ff2k-docker.svg?branch=master)](https://travis-ci.org/MSchietzsch/test-ff2k-docker)
# ff2k-docker
Django based webapp with ELK stack infrastruckture for docker-compose

Start with 

``docker-compose build && docker-compose up --scale elasticsearch-node=2 --scale web=12 --scale redis=3  && docker-compose rm -f``


## ELK Stack
ELK stack is copied and slightly modified from

https://github.com/deviantony/docker-elk
