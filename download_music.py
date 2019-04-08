# encoding=utf8
import os
import requests
from setting import HEADERS, RESOURCE_PATH,TIME_OUT
import urllib
import threading
from setting import logger, MAX_DEEP
import time
import re
import socket
socket.setdefaulttimeout(TIME_OUT)

pattern = re.compile('[\ /\\?@#$&|]')


def download_music(music_item, deep=1):
    try:
        url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(
            music_item.id)

        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        filename = os.path.join(
            RESOURCE_PATH, re.sub(pattern, '_', music_item.name) + ".mp3")

        if os.path.exists(filename):
            logger.info(filename + '已经存在，无需下载')
            return

        logger.info('开始下载: ' + music_item.name)

        urllib.request.urlretrieve(url, filename)

        logger.info("下载完成 " + music_item.name)

    except:
        logger.info(music_item.name + " 重新下载")

        if deep < MAX_DEEP:
            time.sleep(2)
            download_music(music_item, deep + 1)
        else:
            logger.info(music_item.name + " 下载失败")
