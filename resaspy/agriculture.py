# -*- coding: utf-8 -*-

"""
resaspy.agriculture
~~~~~~~~~~~~

This module implements accessor for atriculture API.
"""

from .context import Context

class Agriculture( Context ):
    class Sales( Context ):
        def ship_value( self, pref_code, city_code, old_city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'shipValue', param )

        def ship_ratio( self, pref_code, city_code, old_city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'shipRatio', param )

    class Land( Context ):
        def for_stacked( self, pref_code, city_code, old_city_code, section_code, disp_type, agricultural_land_type, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'sectionCode': section_code,
                'dispType': disp_type,
                'agriculturalLandType': agricultural_land_type,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forStacked', param )

        def ratio( self, pref_code, city_code, old_city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'Ratio', param )

        def for_mobility( self, pref_code, city_code, old_city_code, agricultural_lang_type, matter ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'agriculturalLandType': agricultural_lang_type,
                'matter': matter
            }

            return self.fetch( 'forMobility', param )

        def for_abandonment( self, pref_code, city_code, old_city_code, matter ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'matter': matter
            }

            return self.fetch( 'forAbandonment', param )

    class All( Context ):
        def for_stacked( self, year, pref_code, city_code, old_city_code, add_area = None ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forStacked', param )

    class Crops( Context ):
        def working_days( self, pref_code, city_code, old_city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'workingDays', param )

        def working_days( self,  pref_code, city_code, old_city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'workingDays', param )

        def sales( self, pref_code, city_code, old_city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'sales', param )

        def farmers_age_structure( self, pref_code, city_code, old_city_code, farmers_type, gender_type,  matter,  add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'farmersType': farmers_type,
                'genderType': gender_type,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'farmersAgeStructure', param )

        def farmers_average_age( self, pref_code, city_code, old_city_code, farmers_type, gender_type,  matter,  add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'farmersType': farmers_type,
                'genderType': gender_type,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'farmersAverageAge', param )

        def related_business( self, pref_code, city_code, old_city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'relatedBusiness', param )

        def average_of_corporate( self, pref_code, city_code, old_city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'oldCityCode': old_city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'averageOfCorporate', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Agriculture, self ).__init__( accessor, parent_category )

        self.__sales = Agriculture.Sales( accessor, self.category )
        self.__land = Agriculture.Land( accessor, self.category )
        self.__all = Agriculture.All( accessor, self.category )
        self.__crops = Agriculture.Crops( accessor, self.category )

    @property
    def sales( self ):
        return self.__sales

    @property
    def land( self ):
        return self.__land

    @property
    def all( self ):
        return self.__all

    @property
    def crops( self ):
        return self.__crops

class Forestry( Context ):
    class Income( Context ):
        def for_stacked( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forStacked', param )

        def for_sales( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forSales', param )

        def for_contract_revenue( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forContractRevenue', param )

        def for_sales_ratio( self, pref_code, city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forSalesRatio', param )

        def for_contract_revenue_ratio( self, pref_code, city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'forContractRevenueRatio', param )

        def all_portfolio( self, year, pref_code, city_code, area_type, add_area = None ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'cityCode': city_code,
                'areaType':area_type
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'allPortfolio', param )

        def all_for_stacked( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'allForStacked', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Forestry, self ).__init__( accessor, parent_category )

        self.__income = Forestry.Income( accessor, self.category )

    @property
    def income( self ):
        return self.__income

class Fishery( Context ):
    class Sea( Context ):
        def staple( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'staple', param )

        def total_sales( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'totalSales', param )

        def management_unit_sales( self, pref_code, city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'managementUnitSales', param )

        def sales( self, pref_code, city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'sales', param )

        def ship_value( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'shipValue', param )

        def ship_ratio( self, pref_code, city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'shipRatio', param )

        def aquaculture_total_sales( self, pref_code, city_code, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'aquacultureTotalSales', param )

        def aquaculture_management_unit_sales( self, pref_code, city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'aquacultureManagementUnitSales', param )

        def aquaculture_sales( self, pref_code, city_code, matter, add_area = None ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'matter': matter
            }
            if add_area is not None:
                param['addArea'] = ','.join( map( lambda area: '_'.join( map( str, area ) ) ) )

            return self.fetch( 'aquacultureSales', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Fishery, self ).__init__( accessor, parent_category )

        self.__sea = Fishery.Sea( accessor, self.category )

    @property
    def sea( self ):
        return self.__sea
