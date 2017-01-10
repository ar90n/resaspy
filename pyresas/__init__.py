# -*- coding: utf-8 -*-

"""
pyresas is a simple utility for RESAS api(https://opendata.resas-portal.go.jp).
usage:

   >>> from pyresas import Pyresas
   >>> resas = pyresas( key )
   >>> r = resas.prefectures()
   >>> r.result

:copyright: (c) 2016 by Masahiro Wada.
:license: MIT, see LICENSE for more details.
"""

__title__ = 'pyresas'
__version__ = '0.0.1'
__build__ = 0x021204
__author__ = 'Masahiro Wada'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Masahiro Wada'

from .pyresas import Pyresas
