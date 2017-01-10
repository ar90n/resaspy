# -*- coding: utf-8 -*-

"""
resaspy.api
~~~~~~~~~~~~

This module implements accessor for API.
"""

import requests

def fetch( key, version,  path ):
    api_url = 'https://opendata.resas-portal.go.jp/api/%s/%s' % ( version, path )
    print( api_url );
    return requests.get( api_url, headers = { 'X-API-KEY': key } )
