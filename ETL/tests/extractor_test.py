import unittest
from datajob.etl.extract.apartment_sale_price import ApartmentSalePrice
from datajob.etl.extract.local_code import LocalCode
from datajob.etl.extract.own_transfer_by_nationality import OwnTransferByNationality
from datajob.etl.extract.own_transfer_by_local_foreigner_corp import OwnTransferByLocalForeignerCorp
from datajob.etl.extract.own_transfer_by_gender_age import OwnTransferByGenderAge
from datajob.etl.extract.own_transfer_by_address import OwnershipTransferByAddress

# test command : python3 -W ignore -m unittest tests.extractor_test.MTest.test1
class MTest(unittest.TestCase):

    def test1(self):
        OwnershipTransferByAddress.extract_data(10)
    
    def test2(self):
        OwnTransferByGenderAge.extract_data()

    def test3(self):
        OwnTransferByLocalForeignerCorp.extract_data()
    
    def test4(self):
        OwnTransferByNationality.extract_data()

    def test5(self):
        ApartmentSalePrice.extract_data(69)  # 69 : 2017 ~ 저번달

    def test6(self):
        LocalCode.extract_data()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    unittest.main()
