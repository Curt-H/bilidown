from __future__ import unicode_literals
import youtube_dl
from utils import progress_bar, log


class MyLogger(object):
    def __init__(self, url, name=None):
        self.url = url
        self.name = name

    def debug(self, msg):
        pass

    def warning(self, msg):
        # log(msg)
        pass

    def error(self, msg):
        log(msg)
        return ydownload(self.url, self.name)


def my_hook(d):
    if d['status'] == 'downloading':
        if d['speed'] is None:
            speed = 0
        else:
            speed = d['speed'] // 1000
        progress_bar(d['downloaded_bytes'], d['total_bytes'],
                     d['total_bytes'] // 1000000, speed)

    if d['status'] == 'finished':
        log(f'{d["filename"]} dowloaded')


def ydownload(url_list, name=None):

    if name is not None:
        path = f'.\\downloads\\{name}.%(ext)s'
    else:
        path = '.\\downloads\\%(title)s-%(id)s.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio/best',
        'logger': MyLogger(url_list),
        'progress_hooks': [my_hook],
        'sleep_interval': 5,
        'max_sleep_interval': 10,
        'outtmpl': path,
        'ignoreerrors': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_list])


if __name__ == "__main__":
    while True:
        url = input(">>>")

        ydl_opts = {
            'format': 'bestaudio/best',
            'logger': MyLogger(url, None),
            'progress_hooks': [my_hook],
            'outtmpl': '.\\downloads\\%(title)s-%(id)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])