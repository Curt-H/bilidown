from __future__ import unicode_literals
import youtube_dl
from utils import progress_bar, log

class MyLogger(object):
    def debug(self, msg):
        # print(msg)
        pass

    def warning(self, msg):
        log(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'downloading':
        if d['speed'] is None:
            speed = 0
        else:
            speed = d['speed']//1000
        progress_bar(d['downloaded_bytes'], d['total_bytes'], d['total_bytes']//1000000, speed)

    if d['status'] == 'finished':
        log(f'{d["filename"]} dowloaded')

def ydownload(url_list):

    ydl_opts = {
        'format': 'bestaudio/best',
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'sleep_interval': 20,
        'max_sleep_interval': 60,
        'outtmpl': '.\\downloads\\%(title)s-%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_list])


if __name__ == "__main__":
    url='https://www.bilibili.com/video/BV13V411Y7Sw?spm_id_from=333.851.b_7265706f7274466972737431.7'

    ydl_opts = {
        'format': 'bestaudio/best',
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'outtmpl': '.\\downloads\\%(title)s-%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

        #         'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '320',
        # }],