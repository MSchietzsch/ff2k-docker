# haproxy
Dockerfile is based on https://github.com/docker-library/haproxy/tree/9da24940385e6178f987737305ff499734437c90
but with dev release v1.9-dev5

Added automatic creation of Let's encrypt cert. You need to create a 'aws-config' file here. 
See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#best-practices-for-configuring-credentials

