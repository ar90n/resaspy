# -*- coding: utf-8 -*-

"""
pyresas.common
~~~~~~~~~~~~

This module implements common api wrapper.
"""

from .context import Context

class Common( Context ):
    def prefectures(self):
        path = self.__parent_path + '/' + 'prefectures'
        return self.__accessor.fetch( path )
