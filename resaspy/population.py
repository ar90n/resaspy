# -*- coding: utf-8 -*-

"""
resaspy.population
~~~~~~~~~~~~

This module implements accessor for population API.
"""

from .context import Context

class Population( Context ):
    class Composition( Context ):
        def per_year( self, pref_code, city_code, add_area = [] ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ), add_area ) )

            return self.fetch( 'perYear', param )

        def pyramid( self, pref_code, city_code, year_left, year_right, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'yearLeft': year_left,
                'yearRight': year_right,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ), add_area ) )

            return self.fetch( 'pyramid', param )

    class Sum( Context ):
        def per_year( self, pref_code, city_code, add_area = [] ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ), add_area ) )

            return self.fetch( 'perYear', param )

        def estimate( self, pref_code, city_code, add_area = [] ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ), add_area ) )

            return self.fetch( 'estimate', param )

    class Future( Context ):
        def cities( self, year, pref_code ):
            param = {
                'year': year,
                'prefCode': pref_code,
            }
            return self.fetch( 'cities', param )

    def nature( self, pref_code, city_code, age_from, age_to ):
        param = {
            'prefCode': pref_code,
            'cityCode': city_code,
            'ageFrom': age_from,
            'ageTo': age_to
        }
        return self.fetch( 'nature', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Population, self ).__init__( accessor, parent_category )

        self.__composition = Population.Composition( accessor, self.category )
        self.__sum = Population.Sum( accessor, self.category )
        self.__future = Population.Future( accessor, self.category )

    @property
    def composition( self ):
        return self.__composition

    @property
    def sum( self ):
        return self.__sum

    @property
    def future( self ):
        return self.__future
