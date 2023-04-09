import requests
import re 

url = "http://www.techutilize.com"

payload = {
    "key1": "value1",
    "key2": "value2",
}

response = requests.post(url, data=payload)

text = response.text

urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print(f'{urls}\n')

# from bs4 import BeautifulSoup

# url = "http://www.techutilize.com"

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# data = {}
# for tag in soup.find_all("div"):
#     if "class" in tag.attrs:
#         if "example-class" in tag["class"]:
#             data[tag.text] = tag.attrs

# print(data)