"""
This mod contains all the tools for caching pages and loading pages' content
"""
import requests
import os

from utils import log
from hashlib import sha256


def get_content(url, **kwargs):
    """
    Get content from url or cache
    :param url: string, 网址
    :return: 返回网页页面的HTML代码(coding: utf-8)
    """
    u = url
    settings = kwargs['settings']

    # Use requests module to get the html page content
    r = requests.get(u, timeout=3600, **settings)
    r.encoding = 'utf-8'  # must give a coding format, or it will be error
    content = r.text

    return content
