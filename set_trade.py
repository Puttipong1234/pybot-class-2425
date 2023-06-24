from settrade_v2 import Investor

investor = Investor(
                app_id="podzKYoZPAcfv6Ov",                                 
                app_secret="AMaNJsFXVIzH4rcfB/FidA7pE1MYW4h0PBSW2MN1Aavi", 
                broker_id="SANDBOX",
                app_code="SANDBOX",
                is_auto_queue = False)

deri = investor.Derivatives(account_no="pyybott-D")
equity = investor.Equity(account_no="pyybott-E")

port = deri.get_portfolios()
print(port)