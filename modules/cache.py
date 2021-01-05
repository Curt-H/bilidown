"""
This mod contains all the tools for caching pages and loading pages' content
"""
import requests
import os

from utils import log
from hashlib import sha256


def get_content(url, **kwargs):
    """
    Request url content 
    Parameters
    ----------
    url: str
        request url
    kwargs: dict
        contains all the setting request package needed
        such as proxy, headers and others

    Return
    ----------
    content: str
        page HTML code(coding: utf-8)
    """
    u = url
    settings = kwargs['settings']

    # Use requests module to get the html page content
    r = requests.get(u, timeout=3600, **settings)
    r.encoding = 'utf-8'  # must give a coding format, or it will be error
    content = r.text

    return content
