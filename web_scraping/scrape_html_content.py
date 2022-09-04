import requests
# URL = "https://realpython.github.io/fake-jobs/"
URL = "https://www.amazon.com/bandaids/s?k=bandaids"
page = requests.get(URL)
print(page.text)