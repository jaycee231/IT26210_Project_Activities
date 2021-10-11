import urllib.parse
import requests

# 3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU
main_api =  "https://www.mapquestapi.com/directions/v2/route?"
orig = "Rome, Italy"
dest = "Frascati, Italy"
key = "3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)