# -*- coding: utf-8 -*-

"""
resaspy is a simple utility for RESAS api(https://opendata.resas-portal.go.jp).
usage:

   >>> from resaspy import Resaspy
   >>> resas = Resaspy( key )
   >>> r = resas.prefectures()
   >>> r.result

:copyright: (c) 2016 by Masahiro Wada.
:license: MIT, see LICENSE for more details.
"""

__title__ = 'resaspy'
__version__ = '0.2.0'
__build__ = 0x021204
__author__ = 'Masahiro Wada'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Masahiro Wada'

from .resaspy import Resaspy
