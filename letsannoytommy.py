import requests
import random

url = "https://billing.embernodes.com/credits"

paymenter_token = "ABC123"
paymenter_session = "123ABC"

data = {
    "_token": paymenter_token,
    "amount": random.randint(80, 100),
    "gateway": random.choice([11, 15])
}

cookies = {
    "paymenter_session": paymenter_session
}

response = requests.post(url, data=data, cookies=cookies)


