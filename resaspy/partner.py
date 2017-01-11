# -*- coding: utf-8 -*-

"""
resaspy.partner
~~~~~~~~~~~~

This module implements accessor for partner API.
"""

from .context import Context

class Partner( Context ):
    class Navitime( Context ):
        def congestion( self, node = None, node_type = None, direction = None, ratio = None, date_from = None, date_to = None ):
            param = {}
            if node is not None:
                param['node'] = '.'.join( map( str, node ) ) if isinstance( node, list ) else node
            if node_type is not None:
                param['node-type'] = '.'.join( node_type ) if isinstance( node_type, list ) else node_type
            if direction is not None:
                param['direction'] = direction
            if ratio is not None:
                param['ratio'] = ratio
            if date_from is not None:
                param['date-from'] = date_from
            if date_to is not None:
                param['date-to'] = date_to

            return self.fetch( 'congestion', param )

    class Nightley( Context ):
        def cities( self, target_type, pref_code, year, season_code, period_of_time ):
            param = {
                'targetType': target_type,
                'prefCode': pref_code,
                'year': year,
                'seasonCode': season_code,
                'periodOfTime': period_of_time
            }

            return self.fetch( 'cities', param )

        def places( self, target_type, city_code, year, season_code, period_of_time ):
            param = {
                'targetType': target_type,
                'cityCode': city_code,
                'year': year,
                'seasonCode': season_code,
                'periodOfTime': period_of_time
            }

            return self.fetch( 'places', param )

    class Urecon( Context ):
        def search( self, q, category_code = None, fields = None):
            param = { 'q': q }
            if category_code is not None:
                param['category_code'] = category_code
            if fields is not None:
                param['fields'] = fields

            return self.fetch( 'search', param )

        def items( self, q, category_code = None, fields = None ):
            param = { 'q': q }
            if category_code is not None:
                param['category_code'] = category_code
            if fields is not None:
                param['fields'] = fields

            return self.fetch( 'items', param )

        def categories( self, level, code, q = None, limit = None, recommend = None ):
            param = {
                'level': level,
                'code': code,
            }
            if q is not None:
                param['q'] = q
            if limit is not None:
                param['limit'] = limit
            if recommend is not None:
                param['recommend'] = recommend

            return self.fetch( 'categories', param )

        def __trend_impl( self, resource, item_code, ended_on = None, fields = None ):
            param = { 'item_code': item_code }
            if ended_on is not None:
                param['ended_on'] = ended_on
            if fields is not None:
                param['fields'] = fields

            return self.fetch( resource, param )

        def time_trend( self, item_code, ended_on, fields ):
            return self.__trend_impl( 'timeTrend', item_code, ended_on, fields )

        def week_trend( self, item_code, ended_on, fields ):
            return self.__trend_impl( 'weekTrend', item_code, ended_on, fields )

        def area( self, item_code, ended_on, fields ):
            return self.__trend_impl( 'area', item_code, ended_on, fields )

        def ratio( self, item_code, ended_on, fields ):
            return self.__trend_impl( 'ratio', item_code, ended_on, fields )

        def average_price_trend( self, item_code, ended_on, fields ):
            return self.__trend_impl( 'averagePriceTrend', item_code, ended_on, fields )

        def ranking( self, item_code, ended_on = None, fields = None, limit = None, area_ids = None ):
            param = { 'item_code': item_code }
            if ended_on is not None:
                param['ended_on'] = ended_on
            if fields is not None:
                param['fields'] = fields
            if limit is not None:
                param['limit'] = limit
            if area_ids is not None:
                param['area_ids'] = ','.join( map( str, area_ids ) )

            return self.fetch( 'ranking', param )

    class Experian( Context ):
        def mosaic_group( self, pref_code, city_code ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code
            }

            return self.fetch( 'mosaicGroup', param )

    class Asutomo( Context ):
        def event( self, page = None, count = None, kwd = None, kwd_mode = None, cities = None, disable = None, lat = None, lon = None, dist = None, event_id = None ):
            param = {}
            if page is not None:
                param['page'] = page
            if count is not None:
                param['count'] = count
            if kwd is not None:
                param['kwd'] = kwd
            if kwd_mode is not None:
                param['kwd_mode'] = kwd_mode
            if cities is not None:
                param['cities'] = '|'.join( cities )
            if disable is not None:
                param['disable'] = disable
            if lat is not None:
                param['lat'] = lat
            if lon is not None:
                param['lon'] = lon
            if dist is not None:
                param['dist'] = dist
            if event_id is not None:
                param['event_id'] = event_id

            return self.fetch( 'event', param )

    class Docomo( Context ):
        def inbound( self, year, month, pref_code, period_of_time ):
            param = {
                'year': year,
                'month': month,
                'prefCode': pref_code,
                'periodOfTime': period_of_time
            }

            return self.fetch( 'inbound', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Partner, self ).__init__( accessor, parent_category )

        self.__navitime = Partner.Navitime( accessor, self.category )
        self.__nightley = Partner.Nightley( accessor, self.category )
        self.__urecon = Partner.Urecon( accessor, self.category )
        self.__experian = Partner.Experian( accessor, self.category )
        self.__asutomo = Partner.Asutomo( accessor, self.category )
        self.__docomo = Partner.Docomo( accessor, self.category )

    @property
    def navitime( self ):
        return self.__navitime

    @property
    def nightley( self ):
        return self.__nightley

    @property
    def urecon( self ):
        return self.__urecon

    @property
    def experian( self ):
        return self.__experian

    @property
    def asutomo( self ):
        return self.__asutomo

    @property
    def docomo( self ):
        return self.__docomo
