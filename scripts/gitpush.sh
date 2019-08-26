#!/bin/bash
# Program:
#       This program will push code to github
# History:
# 2019/08/26  Peter Lien  First releases 
# cd /mnt/c/Users/lienc/Projects/EI-Stack/my_sanic_app
read -p "Commit description: " desc
git add . && \
git add -u && \
git commit -m "$desc" && \
git push origin

