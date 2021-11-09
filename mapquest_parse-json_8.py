import urllib.parse
import requests
import tkinter  as tk
from tkinter import *
root = Tk()
root.title("WELCOME TO MAPQUEST API")
  
w = Label(root, width =50, height = 50 ,text='Mapquest API applicaiton!',font=("Arial", 25))
w.pack()
root.mainloop()


# 3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU
# main_api =  "https://www.mapquestapi.com/directions/v2/route?"
main_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
# secondary_api = "http://www.mapquestapi.com/directions/v2/alternateroutes?"
# orig = "Washington, D.C."
# dest = "Baltimore, Md"
key = "3Rguwll95IyFGzeG9Rhvf3BJdmKIECHU"

print("Welcome to the Mapquest API Application.")
print("a. Start")
print("b. Exit")
selection = input("Enter a letter: ")
if selection == 'a' or selection == 'A':
    while True:
        orig = input("Starting Location: ")
        if orig == "quit" or orig == "q":
            break
        dest = input("Destination: ")
        if dest == "quit" or dest == "q":
            break

        max_routes = input("Enter how many routes to return? ")
        print("Select a type of route to use: ")
        print("1. Fastest")
        print("2. Shortest")
        print("3. Pedestrian")
        print("4. Bicycle")
        route = input("Enter name of the route: ")
        if route == '1':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'fastest'})
        elif route == '2':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'shortest'})
        elif route == '3':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'pedestrian'})
        elif route == '4':
            url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "maxRoutes":max_routes, "routeType": 'bicycle'})
        else:
            print("Enter number from 1 - 4 only")
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
        
            alternative = input("Do you want to know an alternative route?(Y/N) ")
            if alternative == 'Y' or alternative == 'y':
                for alternativeRoute in json_data["route"]["alternateRoutes"]:
                    for alternatives in json_data["route"]["legs"][0]["maneuvers"]:
                        print((alternatives["narrative"])  + " (" + str("{:.2f}".format((alternatives["distance"])*1.61) + " km)"))
                break
            if alternative == 'N' or alternative == 'n':
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
elif selection == 'b' or selection == 'B':
    quit()
else: 
    print("Enter letter a to b only.")
