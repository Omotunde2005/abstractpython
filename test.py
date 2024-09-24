from src.abstract_python.abstract import *
import unittest
import dotenv
import os


dotenv.load_dotenv()



#API KEYS
vat_api_key = os.environ.get("VAT_API_KEY", "")
ip_api_key = os.environ.get("IP_API_KEY", "")
exchange_api_key = os.environ.get("EXCHANGE_API_KEY", "")

# Class objects
vat = VatAPI(vat_api_key)
ip = IpAPI(ip_api_key)
exchange = ExchangeRatesAPI(exchange_api_key)


# Test class
class TestExchangeAPI(unittest.TestCase):
    
    def test_live(self):
        self.assertIsNotNone(exchange.live("USD"))
    def test_convert(self):
        self.assertIsNotNone(exchange.convert("USD", "BRL"))
    def test_historical(self):
        self.assertIsNotNone(exchange.historical("USD", "2022-02-02"))

class TestIpAPI(unittest.TestCase):
    def test_ip_info(self):
        self.assertIsNotNone(ip.ip_info())

class TestVatAPI(unittest.TestCase):
    def test_validate(self):
        self.assertIsNotNone(vat.validate("345678"))

    def test_calculate(self):
        self.assertIsNotNone(vat.calculate("720", "AF"))

    def test_categories(self):
        self.assertIsNotNone(vat.categories("AZ"))


if __name__ == "__main__":
    unittest.main()