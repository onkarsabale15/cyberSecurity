import requests

# Replace the URL with the target you want to test
target_url = input("Enter the url to scan: ")

# Replace the payload with a simple script for demonstration
payload = "<script>alert('XSS');</script>"

# Send a POST request with the payload in the body
res = requests.get(target_url)

print(res)

if payload in res.text:
    print(f"XSS vulnerability detected in {target_url}")
else:
    print(f"No XSS vulnerability found in {target_url}")