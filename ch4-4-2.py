import requests

# https://www.sgx.com/securities/securities-prices?code=all
# url = "https://www.psck.net/api/?con=api&act=diskList&lang=null"
url = "https://api.sgx.com/securities/v1.1?excludetypes=bonds&params=nc%2Cadjusted-vwap%2Cbond_accrued_interest%2Cbond_clean_price%2Cbond_dirty_price%2Cbond_date%2Cb%2Cbv%2Cp%2Cc%2Cchange_vs_pc%2Cchange_vs_pc_percentage%2Ccx%2Ccn%2Cdp%2Cdpc%2Cdu%2Ced%2Cfn%2Ch%2Ciiv%2Ciopv%2Clt%2Cl%2Co%2Cp_%2Cpv%2Cptd%2Cs%2Csv%2Ctrading_time%2Cv_%2Cv%2Cvl%2Cvwap%2Cvwap-currency"
r = requests.get(url)
print(r.text)
