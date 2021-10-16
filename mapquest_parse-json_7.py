import urllib.parse
import requests

# 3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU
# main_api =  "https://www.mapquestapi.com/directions/v2/route?"
main_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
# secondary_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
# orig = "Washington, D.C."
# dest = "Baltimore, Md"
key = "3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    max_routes = input("Enter how many routes to return? ")
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes})
    # second_url = secondary_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
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
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]) * 3.78)))
        print("Route Type: " + (json_data["route"]["options"]["routeType"]))
        print("Max Routes: " + (json_data["route"]["maxRoutes"]))
        # print("Max Routes: " + (json_data["route"]["alternateRoutes"]["route"]))
        print("=============================================")

        print("What do you want to use as a transportation mode? ")
        print("1. Auto")
        print("2. Walking")
        print("3. Bicycle")
        transportation = input("Enter a number: ")

        if transportation == '1':
            # transport = 'BICYCLE'
            # {"transportMode": transport}
            # print(json_data["route"]["legs"][0]["maneuvers"]["transportMode"])
            
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                each["transportMode"] = 'AUTO'
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                print("Time: " + str("{:.2f}".format((each["time"]) / 60)  + " minutes"))
                print("Using " + each["transportMode"] + " as a means of transportation.\n")
            break
        elif transportation == '2':
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                each["transportMode"] = 'WALKING'

                # if each["transportMode"] == 'WALKING':
                for transport in json_data["route"]["legs"][0]["maneuvers"]:
                    print((transport["narrative"]) + " (" + str("{:.2f}".format((transport["distance"])*1.61) + " km)"))
                # each["transportMode"] = 'WALKING'
                    print("Time: " + str("{:.2f}".format((transport["time"]) / 60)  + " minutes"))
                    print("Using " + each["transportMode"] + " as a means of transportation.\n")
            break
        elif transportation == '3':
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                each["transportMode"] = 'BICYCLE'
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                print("Time: " + str("{:.2f}".format((each["time"]) / 60)  + " minutes"))
                print("Using " + each["transportMode"] + " as a means of transportation.\n")
            break
        else:
            print("Enter number from 1 - 3")
        
        alternative = input("Do you want to know an alternative route?(Y/N) ")
        if alternative == 'Y' or alternative == 'y':
            # if json_data["route"]["alternateRoutes"] == True:
            #    print ("Alternate Routes: " + count(json_data["route"]["alternateRoutes"]["route"]["legs"][0]["maneuvers"]["narrative"]))
            for alternativeRoute in json_data["route"]["alternateRoutes"]:
                for alternatives in json_data["route"]["legs"][0]["maneuvers"]:
                    print((alternatives["narrative"])  + " (" + str("{:.2f}".format((alternatives["distance"])*1.61) + " km)"))
            break
        if alternative == 'N' or alternative == 'n':
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                print("Using " + each["transportMode"] + " as a means of transportation.\n")
            break
        print("=============================================\n")
    
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