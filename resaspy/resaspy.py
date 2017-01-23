# -*- coding: utf-8 -*-

"""
This module implements context class.
"""
import requests
import requests_cache

from .context import Context
from .industry import Industry
from .agriculture import Agriculture, Fishery, Forestry
from .tourism import Tourism
from .population import Population
from .municipality import Municipality
from .partner import Partner

class Resaspy( Context ):
    class Accessor:
        def __init__( self, key, version, cache_name = None ):
            self.__key = key
            self.__version = version
            self.__endpoint = 'https://opendata.resas-portal.go.jp'
            if cache_name is not None:
                requests_cache.install_cache(cache_name);

        def fetch( self, resource, params = {} ):
            api_url = '%s/api/%s/%s' % ( self.__endpoint, self.__version, resource )
            return requests.get( api_url, params = params,  headers = { 'X-API-KEY': self.__key } ).json()

    class Industries( Context ):
        def broad(self):
            return self.fetch( 'broad' )

        def middle(self, sic_code):
            params = { 'sicCode': sic_code }
            return self.fetch( 'middle', params )

        def narrow(self, simc_code):
            params = { 'simcCode': simc_code }
            return self.fetch( 'narrow', params )

    class Jobs( Context ):
        def broad(self):
            return self.fetch( 'broad' )

        def middle(self,isco_code):
            params = { 'iscoCode': isco_code }
            return self.fetch( 'middle', params )

    class Patents( Context ):
        def broad(self):
            return self.fetch( 'broad' )

        def middle(self, tec_code):
            params = { 'tecCode': tec_code }
            return self.fetch( 'middle', params )

        def locations(self, pref_code, city_code):
            params = { 'prefCode': pref_code, 'cityCode': city_code }
            return self.fetch( 'locations', params )

    class Regions( Context ):
        def broad(self):
            return self.fetch( 'broad' )

        def middle(self, region_code):
            params = { 'regionCode': region_code }
            return self.fetch( 'middle', params )

        def agriculture_departments( self ):
            return self.fetch( 'agricultureDepartments' )

    class TradeInfoItemTypes( Context ):
        def broad( self ):
            return self.fetch( 'broad' )

        def middle( self, item_code1 ):
            params = { 'itemCode1': item_code1 }
            return self.fetch( 'middle', params )

        def narrow( self, item_code1, item_code2 ):
            params = { 'itemCode1': item_code1, 'itemCode2': item_code2 }
            return  self.fetch( 'narrow', params )

    @property
    def category( self ):
        return ''

    def __init__( self, key, cache_name = None ):
        accessor = self.Accessor( key, 'v1', cache_name )
        super( Resaspy, self ).__init__( accessor )

        self.__industries = Resaspy.Industries( accessor )
        self.__jobs = Resaspy.Jobs( accessor )
        self.__patents = Resaspy.Patents( accessor )
        self.__regions = Resaspy.Regions( accessor )
        self.__trade_info_item_types = Resaspy.TradeInfoItemTypes( accessor )

        self.__industry = Industry( accessor )
        self.__agriculture = Agriculture( accessor )
        self.__fishery = Fishery( accessor )
        self.__forestry = Forestry( accessor )
        self.__tourism = Tourism( accessor )
        self.__population = Population( accessor )
        self.__municipality = Municipality( accessor )
        self.__partner = Partner( accessor )

    def prefectures(self):
        return self.fetch( 'prefectures' )

    def cities(self, pref_code):
        params = { 'prefCode': pref_code }
        return self.fetch( 'cities', params )

    def old_cities( self, pref_code, city_code ):
        params = { 'prefCode': pref_code, 'cityCode': city_code }
        return self.fetch( 'oldCities', params )

    def customs( self, pref_code ):
        params = { 'prefCode': pref_code }
        return self.fetch( 'customs', params )

    @property
    def industries( self ):
        return self.__industries

    @property
    def jobs( self ):
        return self.__jobs

    @property
    def patents( self ):
        return self.__patents

    @property
    def regions( self ):
        return self.__regions

    @property
    def trade_info_item_types( self ):
        return self.__trade_info_item_types

    @property
    def industry( self ):
        return self.__industry

    @property
    def agriculture( self ):
        return self.__agriculture

    @property
    def fishery( self ):
        return self.__fishery

    @property
    def forestry( self ):
        return self.__forestry

    @property
    def tourism(self):
        return self.__tourism

    @property
    def population(self):
        return self.__population

    @property
    def municipality(self):
        return self.__municipality

    @property
    def partner(self):
        return self.__partner
