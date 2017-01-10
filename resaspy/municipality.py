# -*- coding: utf-8 -*-

"""
resaspy.municiplality
~~~~~~~~~~~~

This module implements accessor for municiplality API.
"""

from .context import Context

class Municipality( Context ):
    class Company( Context ):
        def per_year( self, pref_code, city_code, sic_code, simc_code ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perYear', param )

    class Plant( Context ):
        def per_year( self, pref_code, city_code, sic_code, simc_code ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perYear', param )

    class Foundation( Context ):
        def per_year( self, pref_code, city_code ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code
            }
            return self.fetch( 'perYear', param )

    class Taxes( Context ):
        def per_year( self, pref_code, city_code ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code
            }
            return self.fetch( 'perYear', param )

    class Job( Context ):
        def per_year( self, pref_code, isco_code, ismco_code ):
            param = {
                'prefCode': pref_code,
                'iscoCode': isco_code,
                'ismcoCode': ismco_code
            }
            return self.fetch( 'perYear', param )

    class Manufacture( Context ):
        def per_year( self, pref_code, city_code, sic_code, simc_code ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perYear', param )

    class Employee( Context ):
        def per_year( self, pref_code, city_code, sic_code, simc_code ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perYear', param )

    class Value( Context ):
        def per_year( self, year, pref_code, city_code, sic_code, simc_code ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perYear', param )

    class Labor( Context ):
        def per_year( self, year, pref_code, city_code, sic_code, simc_code ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perYear', param )

    class Surplus( Context ):
        def per_year( self, year, pref_code, city_code, sic_code, simc_code ):
            param = {
                'year': year,
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code
            }
            return self.fetch( 'perYear', param )

    class Wages( Context ):
        def per_year( self, pref_code, sic_code, simc_code, wages_age ):
            param = {
                'prefCode': pref_code,
                'sicCode': sic_code,
                'simcCode': simc_code,
                'wagesAge': wages_age
            }
            return self.fetch( 'perYear', param )

    class Sales( Context ):
        def per_year( self, pref_code, city_code, sic_code, simc_code, disp_type ):
            param = {
                'prefCode': pref_code,
                'cityCode': city_code,
                'sicCode': sic_code,
                'simcCode': simc_code,
                'dispType': disp_type
            }
            return self.fetch( 'perYear', param )

    def __init__( self, accessor, parent_category = '' ):
        super( Municipality, self ).__init__( accessor, parent_category )

        self.__company = Municipality.Company( accessor, self.category )
        self.__plant = Municipality.Plant( accessor, self.category )
        self.__foundataion = Municipality.Foundation( accessor, self.category )
        self.__taxes = Municipality.Taxes( accessor, self.category )
        self.__job = Municipality.Job( accessor, self.category )
        self.__manufacture = Municipality.Manufacture( accessor, self.category )
        self.__employee = Municipality.Employee( accessor, self.category )
        self.__value = Municipality.Value( accessor, self.category )
        self.__labor = Municipality.Labor( accessor, self.category )
        self.__surplus = Municipality.Surplus( accessor, self.category )
        self.__wages = Municipality.Wages( accessor, self.category )
        self.__sales = Municipality.Sales( accessor, self.category )

    @property
    def company( self ):
        return self.__company

    @property
    def plant( self ):
        return self.__plant

    @property
    def foundation( self ):
        return self.__foundataion

    @property
    def taxes( self ):
        return self.__taxes

    @property
    def job( self ):
        return self.__job

    @property
    def manufacture( self ):
        return self.__manufacture

    @property
    def employee( self ):
        return self.__employee

    @property
    def value( self ):
        return self.__value

    @property
    def labor( self ):
        return self.__labor

    @property
    def surplus( self ):
        return self.__surplus

    @property
    def wages( self ):
        return self.__wages

    @property
    def sales( self ):
        return self.__sales
