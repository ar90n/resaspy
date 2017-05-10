# -*- coding: utf-8 -*-

"""
resaspy.context
~~~~~~~~~~~~

This module implements api context.
"""

import re


class Context:
    @property
    def category(self):
        category_chars = list(self.__class__.__name__)
        category_chars[0] = category_chars[0].lower()
        return ''.join(category_chars)

    def __init__(self, accessor, parent_category=''):
        self._accessor = accessor
        self._full_category = parent_category + '/' + self.category

    def fetch(self, resource, params={}):
        api_resource = self._full_category + '/' + resource
        beg = re.search('[^/]', api_resource).start()
        api_resource = api_resource[beg:]

        return self._accessor.fetch(api_resource, params)


class DisableCacheContext(Context):
    def fetch(self, resource, params={}):
        with self._accessor.disable_cache():
            return super(DisableCacheContext, self).fetch(resource, params)
