#!/bin/bash
# Program:
#       This program will push code to github
# History:
# 2019/08/26  Peter Lien  First releases 
# cd /mnt/c/Users/lienc/Projects/EI-Stack/my_sanic_app
read -p "Please input commit desc: " desc  
git add -A
git commit -m "$desc"
git push origin