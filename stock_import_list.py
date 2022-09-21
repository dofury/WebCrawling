import requests
import json 
from pandas.io.json import json_normalize 
import warnings
warnings.simplefilter(action='ignore',category = FutureWarning)
url = 'http://api.finance.naver.com/service/itemSummary.nhn?itemcode=097520'
json_data = json.loads(requests.get(url).text)

df = json_normalize(json_data)
df.to_excel("123.xlsx")
