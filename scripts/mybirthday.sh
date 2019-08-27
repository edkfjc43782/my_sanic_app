#!/bin/bash
# Program:
#       How many days is your birthday?
# History:
# 2019/08/26  Peter Lien  First releases

# 1.輸入生日(需判斷符不符合格式)
read -p "Please input your birth day(mm/dd): " date
date_d=$(echo ${date} |grep '[0-1][]\{8\}') 
if [ "${date_d}" == "" ]; then
	echo "You input the wrong date format...."
	exit 1
fi
# 2.找出當前日期
# 3.判斷生日是否已過(生日大於或小於當前日期)
# 4.大於則加一年，小於則使用今年
# 5.生日減當前日期算出有多少天
