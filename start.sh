# test

cur_path=$(pwd)

project_dir=$(cd "$(dirname "$0")"; pwd)

echo "正在下载，请不要关掉终端"

cd $project_dir

python start.py

# remove less than 1 MB
cd resource
unavailable=$(find * -size -1024)
cd $project_dir

for item in $unavailable
do
    echo "$(date) - INFO - 删除无效歌曲: "$item >> log.txt
    rm -rf resource/$item
done

cd $cur_path > /dev/null

echo "下载完成"
