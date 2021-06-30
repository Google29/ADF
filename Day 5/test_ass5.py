import os

import day5
import pytest
import unittest
class TestMethods(unittest.TestCase):
    def test_method1(self):
        user = day5.New()
        user.get_first_name('ar')
        user.get_middle_name('*')
        user.get_last_name('H')
        user.get_dob('1990-02-02')
        user.get_gender('male')
        user.get_nationality('Indian')
        user.get_current_city('Namakkal')
        user.get_state('Tamil Nadu')
        user.get_pin_code(620002)
        user.get_qualification('B.arch')
        user.get_salary(30000)
        user.get_pan_number('BHU2412300')
        assert user.test_str=='Invalid first name'


    def test_method2(self):
        user=day5.New()
        user.get_first_name('Nithish')
        user.get_middle_name('*')
        user.get_last_name('B')
        user.get_dob('2043-11-08')
        user.get_gender('male')
        user.get_nationality('Indian')
        user.get_current_city('Coimbatore')
        user.get_state('Tamil Nadu')
        user.get_pin_code(623892)
        user.get_qualification('UG')
        user.get_salary(30000)
        user.get_pan_number('907GHU9O8K')
        assert user.test_str == 'Invalid DOB'

    def test_method3(self):
        user=day5.New()
        user.get_first_name('Ravi')
        user.get_middle_name('Teja')
        user.get_last_name('P')
        user.get_dob('1995-12-07')
        user.get_gender('male')
        user.get_nationality('American')
        user.get_current_city('Coimbatore')
        user.get_state('Tamil Nadu')
        user.get_pin_code(623802)
        user.get_qualification('UG')
        user.get_salary(42000)
        user.get_pan_number('JD39IU8902')
        assert user.test_str=='Not eligible to raise request today'

    def test_method4(self):
        user=day5.New()
        user.get_first_name('Raghul')
        user.get_middle_name('*')
        user.get_last_name('J')
        user.get_dob('2000-06-29')
        user.get_gender('malo')
        user.get_nationality('American')
        user.get_current_city('Salem')
        user.get_state('Tamil Nadu')
        user.get_pin_code(620092)
        user.get_qualification('UG')
        user.get_salary(38000)
        user.get_pan_number('907GH67YH8')
        assert user.test_str=='Invalid gender'

    def test_method5(self):
        user=day5.New()
        user.get_first_name('Krisha')
        user.get_middle_name('*')
        user.get_last_name('R')
        user.get_dob('1995-11-17')
        user.get_gender('male')
        user.get_nationality('Indian')
        user.get_current_city('Coimbatore')
        user.get_state('Tamil Nadu')
        user.get_pin_code(62892)
        user.get_qualification('UG')
        user.get_salary(15000)
        user.get_pan_number('8K0GHU668K')
        assert user.test_str=='Invalid pin code'

    def test_method7(self):
        user=day5.New()
        user.get_first_name('Boopathy')
        user.get_middle_name('*')
        user.get_last_name('M')
        user.get_dob('1999-10-19')
        user.get_gender('Male')
        user.get_nationality('Indian')
        user.get_current_city('Coimbatore')
        user.get_state('Tamil Nadu')
        user.get_pin_code(612892)
        user.get_qualification('UG')
        user.get_salary(39000)
        user.get_pan_number('AL04M93O8')
        assert user.test_str=='Invalid PAN number'

    def test_method8(self):
        user=day5.New()
        user.get_first_name('Joe')
        user.get_middle_name('muthaiya')
        user.get_last_name('L')
        user.get_dob('1999-07-30')
        user.get_gender('Male')
        user.get_nationality('American')
        user.get_current_city('Goida')
        user.get_state('Assam')
        user.get_pin_code(625892)
        user.get_qualification('UG')
        user.get_salary(25000)
        user.get_pan_number('8K0G09KK8K')
        assert user.test_str=='Age is not eligible'

    def test_method9(self):
        user=day5.New()
        user.get_first_name('Raghul')
        user.get_middle_name('Dravid')
        user.get_last_name('V')
        user.get_dob('1997-09-10')
        user.get_gender('Male')
        user.get_nationality('Russian')
        user.get_current_city('Moscok')
        user.get_state('Odisha')
        user.get_pin_code(620194)
        user.get_qualification('HSC')
        user.get_salary(41000)
        user.get_pan_number('8K0GHU90I8')
        assert user.test_str=='Nationality is not eligible'

    def test_method10(self):
        user=day5.New()
        user.get_first_name('Hari')
        user.get_middle_name('Sudhan')
        user.get_last_name('O')
        user.get_dob('1995-08-19')
        user.get_gender('Male')
        user.get_nationality('Indian')
        user.get_current_city('Sira')
        user.get_state('Assam')
        user.get_pin_code(610914)
        user.get_qualification('HSC')
        user.get_salary(40000)
        user.get_pan_number('B5U8P910I8')
        assert user.test_str=='State is not eligible'

    def test_method11(self):
        user=day5.New()
        user.get_first_name('Balu')
        user.get_middle_name('Gopal')
        user.get_last_name('M')
        user.get_dob('1992-11-21')
        user.get_gender('Male')
        user.get_nationality('Indian')
        user.get_current_city('Kaba')
        user.get_state('Madhya Pradesh')
        user.get_pin_code(618904)
        user.get_qualification('UG')
        user.get_salary(5000)
        user.get_pan_number('AS890134FV')
        assert user.test_str=='Salary is not eligible'

    def test_method12(self):
        user=day5.New()
        user.get_first_name('Ravi')
        user.get_middle_name('Teja')
        user.get_last_name('P')
        user.get_dob('1995-12-07')
        user.get_gender('male')
        user.get_nationality('American')
        user.get_current_city('Coimbatore')
        user.get_state('Tamil Nadu')
        user.get_pin_code(623802)
        user.get_qualification('UG')
        user.get_salary(42000)
        user.get_pan_number('JD39IU8902')
        assert user.test_str=='Eligible'

unittest.main
