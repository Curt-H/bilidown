import os 
import time
from pyaria2 import Aria2RPC
from utils import log

def download(link, filename):
    jsonrpc = Aria2RPC()
    set_dir = os.path.dirname(__file__)
    options = {
        "dir": set_dir,
        "out": filename,
        "load-cookies" : 'e:\\1.txt',
    }

    try:
        res = jsonrpc.addUri([link], options=options)
        log(res)
    except ConnectionRefusedError:
        log('Aria2c is not running, try to start')
        # run_aria2()
        # download(link, filename)

def run_aria2():
    path = 'D:\\Aria2\\aria2.exe'

    os.system(path)

if __name__=='__main__':
   link = f'https://web-img.benq.com.cn/files/prod/monitor/SW270C/20200527144342_SW270C_UM.zip'
   file_name = 'x.zip'

   download(link, file_name)