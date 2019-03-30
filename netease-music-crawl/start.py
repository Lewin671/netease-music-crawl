# encoding=utf8

import download_list
import download_music
import threading
import time
from setting import MAX_THREAD_NUMBER
from setting import logger


music_items = list(download_list.download_list())

for music_item in music_items[:10]:

    while threading.active_count() > MAX_THREAD_NUMBER:
        time.sleep(1)

    t = threading.Thread(
    target=download_music.download_music, args=(music_item,))
    t.start()


