# -*- coding: utf-8 -*-
import time

from utils import log
from modules.cache import get_content
from modules.json_parse import js_page_count, js_get_posts, js_get_post_info

from settings import SETTINGS
SETTINGS = SETTINGS

api_posts = 'https://api.bilibili.com/x/space/arc/search?mid={}&ps=30&tid=0&pn={}&order=pubdate&jsonp=jsonp'
api_p = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'
url_download1 = 'https://www.bilibili.com/video/{}'
url_download2 = 'https://www.bilibili.com/video/{}?p={}'


def check_multi_p(data):
    d = data
    count = 0

    for p in d:
        bvid = p['bvid']
        p['url'] = list()
        p['name'] = list()
        p['title'] = p['title'].replace(',', ' ')

        content = get_content(api_p.format(bvid), settings=SETTINGS)
        info = js_get_post_info(content)

        for i in range(len(info)):
            if i == 0:
                p['url'].append(url_download1.format(bvid))
            else:
                p['url'].append(url_download2.format(bvid, i + 1))

            if info[i]['part'] == "":
                p['name'].append(p['title'])
            else:
                p['name'].append(p['title'] + '-' + info[i]['part'])

            count += 1
            log(f'{count} Check the {bvid} P{i} ')
        time.sleep(1)

    log(f'Get {count} videos')
    return d


def dump_to_csv(data):
    time.sleep(5)
    log('Prepare to dump all the data')

    ds = data
    with open(f'{ds[0]["mid"]}.csv', 'w', encoding='utf-8-sig') as f:
        for d in ds:
            info_list = [d['author'], str(d['mid']), str(d['created'])]
            for i in range(len(d['url'])):
                line = ','.join((*info_list, d['name'][i], d['url'][i])) + '\n'

                f.write(line)
                log(line)
                # time.sleep(0.25)


def get_posts(up_id):
    uid = up_id

    # at first, search api to get the page number
    content = get_content(api_posts.format(uid, 1), settings=SETTINGS)
    pages = js_page_count(content)

    # start to collect all the info
    index = 1
    posts = list()

    while index <= pages:
        content = get_content(api_posts.format(uid, index), settings=SETTINGS)

        posts += js_get_posts(content)

        log(f'Have load page{index}')

        index += 1
        time.sleep(1)

    return posts


def app():
    up_id = input('User ID: ')

    list_posts = get_posts(up_id)
    data = check_multi_p(list_posts)

    dump_to_csv(data)


# from requests import *

if __name__ == '__main__':
    print('*' * 30)
    while 1:
        app()
    print('*' * 30)
