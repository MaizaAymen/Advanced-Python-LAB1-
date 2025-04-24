"""
HTTP Requests Tutorial - Python requests Module
Complete with Code Examples and Expected Outputs

Following the course material by Wahid Hamdi
"""

import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

def main():
    print("=== PYTHON REQUESTS MODULE DEMO ===\n")
    
    # 1. GET Request
    print("""1. GET REQUEST
Code:
import requests
url = "https://www.example.com"
response = requests.get(url)
print(response)  # Shows HTTP status code
print(response.status_code)

Output:""")
    url = "https://www.example.com"
    response = requests.get(url)
    print(f"<Response [{response.status_code}]>")
    print(response.status_code)
    print("-"*50)

    # 2. HTTP Status Codes
    print("""\n2. HTTP STATUS CODES
Code:
print("2XX: Success")
print("3XX: Redirection")
print("4XX: Client Errors")
print("5XX: Server Errors")

Output:""")
    print("2XX: Success")
    print("3XX: Redirection")
    print("4XX: Client Errors")
    print("5XX: Server Errors")
    print("-"*50)

    # 3. Request Content
    print("""\n3. REQUEST CONTENT
Code:
print(response.content[:100])  # First 100 bytes

Output:""")
    print(response.content[:100])
    print("-"*50)

    # 4. POST Request
    print("""\n4. POST REQUEST
Code:
data = {"name": "Salah", "message": "Hello!"}
post_url = "https://httpbin.org/post"
post_response = requests.post(post_url, json=data)
print(post_response.json())

Output:""")
    data = {"name": "Salah", "message": "Hello!"}
    post_url = "https://httpbin.org/post"
    post_response = requests.post(post_url, json=data)
    print(post_response.json())
    print("-"*50)

    # 5. Handling Errors
    print("""\n5. ERROR HANDLING
Code:
error_response = requests.get("https://httpbin.org/status/404")
if error_response.status_code != 200:
    print(f"HTTP Error: {error_response.status_code}")

Output:""")
    error_response = requests.get("https://httpbin.org/status/404")
    if error_response.status_code != 200:
        print(f"HTTP Error: {error_response.status_code}")
    print("-"*50)

    # 6. Setting Timeout
    print("""\n6. TIMEOUT SETTING
Code:
try:
    requests.get("https://httpbin.org/delay/10", timeout=5)
except requests.exceptions.Timeout as err:
    print(err)

Output:""")
    try:
        requests.get("https://httpbin.org/delay/10", timeout=5)
    except requests.exceptions.Timeout as err:
        print(err)
    print("-"*50)

    # 7. HTTP Request Headers
    print("""\n7. REQUEST HEADERS
Code:
headers = {
    "Authorization": "Bearer test_token",
    "Custom-Header": "PythonDemo"
}
headers_response = requests.get("https://httpbin.org/headers", headers=headers)
print(headers_response.json()['headers'])

Output:""")
    headers = {
        "Authorization": "Bearer test_token",
        "Custom-Header": "PythonDemo"
    }
    headers_response = requests.get("https://httpbin.org/headers", headers=headers)
    print(headers_response.json()['headers'])
    print("-"*50)

    # 8. Web Scraping with BeautifulSoup
    print("""\n8. WEB SCRAPING
Code:
from bs4 import BeautifulSoup
response = requests.get("https://www.example.com")
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.text
first_paragraph = soup.find('p').text if soup.find('p') else "No paragraph"
links = [a.get('href', '') for a in soup.find_all('a')][:3]
print(f"Title: {title}")
print(f"First paragraph: {first_paragraph[:100]}...")
print(f"Sample links: {links}")

Output:""")
    response = requests.get("https://www.example.com")
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.text if soup.title else "No title"
    first_paragraph = soup.find('p').text if soup.find('p') else "No paragraph"
    links = [a.get('href', '') for a in soup.find_all('a')][:3]
    print(f"Title: {title}")
    print(f"First paragraph: {first_paragraph[:100]}...")
    print(f"Sample links: {links}")
    print("-"*50)

    # 9. Requests vs urllib
    print("""\n9. REQUESTS VS URLLIB
Code:
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")
req = urllib.request.Request("https://httpbin.org/post", data=data, method="POST")
with urllib.request.urlopen(req) as response:
    print(response.read().decode("utf-8")[:200] + "...")

Output:""")
    data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")
    req = urllib.request.Request("https://httpbin.org/post", data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8")[:200] + "...")
    print("-"*50)

    # 10. Feature Comparison
    print("""\n10. LIBRARY COMPARISON
Feature         requests        urllib
Ease of Use     🟢              🔴
Built-in        🔴              🟢""")

if __name__ == "__main__":
    main()
    print("\n=== END OF DEMO ===")