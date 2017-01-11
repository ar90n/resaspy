# -*- coding: utf-8 -*-

"""
resaspy.industry
~~~~~~~~~~~~

This module implements accessor for industry API.
"""

from .context import Context

class Industry( Context ):
    class Patent( Context ):
        def list( self, year, mode, pref_code, city_code, patent_holder_id, sort1, sort2, offset, add_tec = [] ):
            param = {
                'year': year,
                'mode': mode,
                'prefCode': pref_code,
                'cityCode': city_code,
                'patentHolderId': patent_holder_id,
                'sort1': sort1,
                'sort2': sort2,
                'offset': offset
            }
            if add_tec is not None:
                param['addTec'] = ','.join( map( lambda tec: '_'.join( map( str, tec ) ), add_tec ) )

            return  self.fetch( 'list', param )

    class Export( Context ):
        def from_to( self, year, data_type, unit_type, disp_type, region_code, country_code, item_code1, item_code2, item_code3, customs_code1, customs_code2  ):
            param = {
                'year': year,
                'dataType': data_type,
                'unitType': unit_type,
                'dispType': disp_type,
                'regionCode': region_code,
                'countryCode': country_code,
                'itemCode1': item_code1,
                'itemCode2': item_code2,
                'itemCode3': item_code3,
                'customsCode1': customs_code1,
                'customsCode2': customs_code2
            }
            return  self.fetch( 'fromTo', param )

    class Globalmarket( Context ):
        def per_pref( self, year, disp_type, region_code, country_code, sic_code, simc_code ):
            param = {
                'year': year,
                'dispType': disp_type,
                'regionCode': region_code,
                'countryCode': country_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perPref', param )

    class Power( Context ):
        def for_industry( self, year, pref_code, city_code, sic_code ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code
            }
            return self.fetch( 'forIndustry', param );

        def for_area( self, year, pref_code, area_type, disp_type, sic_code, simc_code, add_industry = [] ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'areaType': area_type,
                'dispType': disp_type,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            if add_industry is not None:
                param['addIndustry'] = ','.join( map( lambda industry: '_'.join( map( str, industry ) ) ,add_industry ) )

            return self.fetch( 'forArea', param )

        def for_manufacturer_establishments( self, pref_code, sic_code, simc_code, add_area = [] ):
            param = {
                'prefCode': pref_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ), add_area ) )

            return self.fetch( 'forManufacturerEstablishments', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Industry, self ).__init__( accessor, parent_category )

        self.__patent = Industry.Patent( accessor, self.category )
        self.__export = Industry.Export( accessor, self.category )
        self.__global_market = Industry.Globalmarket( accessor, self.category )
        self.__power = Industry.Power( accessor, self.category )

    @property
    def patent( self ):
        return self.__patent

    @property
    def export( self ):
        return self.__export

    @property
    def global_market( self ):
        return self.__global_market

    @property
    def power( self ):
        return self.__power
