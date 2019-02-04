# python-rest-api-docker


curl --header "Content-Type: application/json" \
--request POST \
--data '{"name": "naren"}' \
http://10.20.150.130:5152/v1/api


sudo docker build -t nonpci-peg-dockreg01.prod.cdps.local:5000/simulator/simple .
sudo docker push nonpci-peg-dockreg01.prod.cdps.local:5000/simulator/simple


http://blog.luisrei.com/articles/flaskrest.html
https://docs.python.org/2/library/xml.etree.elementtree.html

steps to run the sample rest service on docker -

1. Clone the Repository - git clone https://github.com/nanic/python-rest-api-docker.git

2. Move to the directory - cd python-rest-api-docker

3. Build the docker image - docker build -t python-rest .

4. Create and run a container - docker run -d -p 5000:5000 python-rest

5. Navigate to http://0.0.0.0:5000/ to get hello world'd

Note: If the image is built inside a private network, you can mention gateway to proxy through
      Ex: docker build --build-arg proxy=<hostname:port> -t python-rest .

A Sample Client --

import requests
r = requests.post('http://0.0.0.0:5000/v1/api',verify=False, json={"name": "naren"})
headers = {'Content-type': 'application/json'}
print(r.status_code)
if r.ok:
    print r.content
