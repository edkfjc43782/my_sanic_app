#!/bin/bash
# Program:
#       This program will build docker image and push to docker hub
# History:
# 2019/08/26  Peter Lien  First releases
read -p "Please input repo: " repo      
read -p "Please input tag: " tag 
docker build --rm -f "Dockerfile" -t ${repo}:${tag}
docker push ${repo}:${tag}