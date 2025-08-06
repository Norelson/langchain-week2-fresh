import requests

url = "https://8f3eb638-96b0-40bc-8d53-786110a28a2f-00-1bv71jzqcdax2.kirk.replit.dev/"
response = requests.get(url)

try:
    print(response.json())
except Exception as e:
    print("Failed to parse JSON:")
    print("Raw response:", response.text)