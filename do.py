from utils import log
from downloader import ydownload

if __name__ == "__main__":
    fname = input('please input user ID: ')
    fname += '.csv'

    info = list()

    with open(fname, mode='r', encoding='utf-8') as f:
        videos = f.readlines()
        for v in videos:
            v = v.strip()

            log(v)
            url = v.split(',')[4]
            ydownload(url)
        log('----------END----------')    

            
