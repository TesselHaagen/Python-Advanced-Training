import requests

url = "http://api.openweathermap.org/data/2.5/weather?"
url += "appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&q=Zwolle"

response = requests.get(url)
decoded = response.json()
print(decoded['main']['temp'])