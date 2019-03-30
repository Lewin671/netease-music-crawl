# encoding=utf8

PLAY_LIST_ID = 2217611952

HEADERS = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

import os
BASE_PATH = os.path.abspath(os.path.dirname(__name__))
RESOURCE_PATH = os.path.join(os.path.abspath(
    os.path.dirname(__name__)), 'resource')

LOG_PATH = os.path.join(BASE_PATH,'log.txt')

if not os.path.exists(RESOURCE_PATH):
    os.mkdir(RESOURCE_PATH)

if not os.path.exists(LOG_PATH):
    os.mknod(LOG_PATH)

MAX_THREAD_NUMBER = 2

MAX_DEEP = 10

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=os.path.join(BASE_PATH, 'log.txt'))
logger = logging.getLogger(__name__)
