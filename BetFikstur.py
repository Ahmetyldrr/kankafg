import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd
import json


def Fikstür(date1,date2):
    
    url = "https://api.betmines.com/betmines/v1/fixtures/web?"
    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["Accept"] = "application/json, text/plain, */*"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    headers["sec-ch-ua-platform"] = "Windows"
    headers["Origin"] = "https://betmines.com"
    headers["Sec-Fetch-Site"] = "same-site"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Referer"] = "https://betmines.com/"
    headers["Accept-Language"] = "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5"
    ek = 'T21:00:00Z'
    
    params = {

        'dateFormat':'extended',
        'platform':'website',
        'from':date1+str(ek),
        'to':date2+str(ek)
    }
    
    resp = requests.get(url,params=params,headers=headers)
    v=json.loads(resp.text)
    data = pd.json_normalize(v)
    
    return data

