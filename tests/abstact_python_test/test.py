from abstract_python.abstract import VatAPI, IpAPI, ExchangeRatesAPI
import dotenv
import os


dotenv.load_dotenv(".../.env")

vat_api_key = os.environ.get("VAT_API_KEY", "")
ip_api_key = os.environ.get("IP_API_KEY", "")
exchange_api_key = os.environ.get("EXCHANGE_API_KEY", "")


vat = VatAPI(vat_api_key)
ip = IpAPI(ip_api_key)
exchange = ExchangeRatesAPI(exchange_api_key)
