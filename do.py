from utils import log
from downloader import ydownload
from videolist import app

if __name__ == "__main__":
    fname = input('please input user ID: ')

    from os.path import exists

    if not exists(f'{fname}.csv'):
        app(fname)

    fname += '.csv'

    info = list()

    with open(fname, mode='r', encoding='utf-8') as f:
        videos = f.readlines()
        for v in videos:
            v = v.strip()

            log(v)
            v = v.split(',')
            url = v[4]
            name = f'{v[0]}-{v[2]}-{v[5]}'
            ydownload(url, name)
        log('----------END----------')    

            
