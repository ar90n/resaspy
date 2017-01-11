# -*- coding: utf-8 -*-

"""
resaspy.tourism
~~~~~~~~~~~~

This module implements accessor for tourism API.
"""

from .context import Context

class Tourism( Context ):
    class Foreigners( Context ):
        def for_from( self, year, pref_code, purpose, add_area = None ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'purpose': purpose,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forFrom', param )

        def for_to( self, year, pref_code, region_code, country_code, purpose ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'regionCode': region_code,
                'countryCode': country_code,
                'purpose': purpose
            }

            return self.fetch( 'forTo', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Tourism, self ).__init__( accessor, parent_category )

        self.__foreigners = Tourism.Foreigners( accessor, self.category )

    @property
    def foreigners( self ):
        return self.__foreigners

    def attractions( self, pref_code, city_code ):
        param = {
            'prefCode': pref_code,
            'cityCode': city_code
        }

        return self.fetch( 'attractions', param )
