[dmtsai@study bin]$ vim create_3_filename.sh
#!/bin/bash
# Program:
#	Program creates three files, which named by user's input and date command.
# History:
# 2015/07/16	VBird	First release

# 1. 讓使用者輸入檔案名稱，並取得 fileuser 這個變數；
echo -e "I will use 'touch' command to create a file." # 純粹顯示資訊
read -p "Please input your filename: " filename         # 提示使用者輸入

# 2. 為了避免使用者隨意按 Enter ，利用變數功能分析檔名是否有設定？
filename=${filename:-"filename"}           # 開始判斷有否設定檔名

# 3. 開始利用 date 指令來取得所需要的檔名了；
date=$(date +%Y%m%d)                      # 今天的日期
file=${filename}${date}                   # 設定檔名


# 4. 將檔名建立吧！
touch "${file}"                           # 建立檔案
