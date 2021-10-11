import urllib.parse
import requests

# 3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU
main_api =  "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
# print(json_data)
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A ssucessfull route call.\n")