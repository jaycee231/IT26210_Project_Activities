import urllib.parse
import requests

# 3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU
main_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"

key = "3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    try:
        max_routes = input("Enter max route: ")
        if max_routes == "quit" or max_routes == "q":
            break
    except:
        print("Enter numbers only!")
    print("Select a type of route to use: ")
    print("1. Fastest")
    print("2. Shortest")
    print("3. Pedestrian")
    print("4. Bicycle")
    print("5. Exit")
    
    route = input("Enter number of the route: ")
    if route == '1':
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'fastest'})
    elif route == '2':
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'shortest'})
    elif route == '3':
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'pedestrian'})
    elif route == '4':
        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'bicycle'})
    elif route == '5':
        break
    else:
        print("Enter number from 1 - 5 only")
        break
    # json_data = requests.get(url).json()
# print(json_data)
    print("URL: " + (url))
    # print("Second URL: " + (second_url))
    json_data = requests.get(url).json()
    # json_data2 = requests.get(second_url).json()
    json_status = json_data["info"]["statuscode"]

    # print("Max Routes: " + (json_data2["maxRoutes"]))

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A sucessfull route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))
        if ["routeType"] == 'fastest' or ["routeType"] == 'shortest':
            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78)))
        print("Route Type: " + (json_data["route"]["options"]["routeType"]))
        print("Max Routes: " + (json_data["route"]["maxRoutes"]))
        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("Time: " + str("{:.2f}".format((each["time"]) / 60)  + " minutes"))
            print("Using " + each["transportMode"] + " as a means of transportation.\n")
        if max_routes == '3' or route == 'pedestrian' or route == 'bicycle':
            try:
                alternative = input("Do you want to know an alternative route?(Y/N) ")
                if alternative == 'Y' or alternative == 'y':
                    for alternativeRoute in json_data["route"]["alternateRoutes"]:
                        for alternatives in json_data["route"]["legs"][0]["maneuvers"]:
                            print((alternatives["narrative"])  + " (" + str("{:.2f}".format((alternatives["distance"])*1.61) + " km)"))
                    break
                if alternative == 'N' or alternative == 'n':
                    break
            except:
                print("\nThere's no alternative routes\n")
            
        print("=============================================\n")
        break

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")