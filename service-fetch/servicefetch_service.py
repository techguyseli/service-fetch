# this file has all the functions that help in filtering and returning
# info about services from the api json response


# imports
import sys


# function that returns a structured list of services, from the api 
# response data structure that's  filled with shit load of nodes and 
# all types of data structures
def get_services_info(result_obj):
    res = result_obj.get("data", None)

    if res is None:
        print("Somehow there was no response from the api, please make sure the args you provided are valid. (e.g. valid api key, coordinates format. . .)")
        sys.exit(1)

    print("\t+ Fetching services' map pins...")
    map_pins = get_map_pins(result_obj)
    print("\t+ Services' map pins successfully fetched.")

    print("\t+ getting services' content...")
    pins_content = get_pins_content(result_obj)
    print("\t+ Services' content successfully fetched.")

    services = list()
    print("\t+ Adding coordinates from map pins...")
    services = get_coordinates__id(map_pins)
    print("\t+ Coordinates successfully added.")

    print("\t+ Adding and fetching titles and types from services' contents...")
    services = add_title__contentId__type(services, pins_content)
    print("\t+ Services' titles and types successfully fetched.")

    return services


# function that returns map pins from api response data structure
def get_map_pins(result_obj):
    pins = result_obj["data"]["AppPresentation_queryNearToALocation"]["mapSections"][0]["pins"]
    return pins


# function that returns services content from api response data structure
def get_pins_content(result_obj):
    content = result_obj["data"]["AppPresentation_queryNearToALocation"]["mapSections"][1]["content"]
    return content


# function that adds titles and types of services from service content 
# datastructure to the service list passed
def add_title__contentId__type(services, contents):
    length = len(services)

    if length != len(contents):
        print("Error: query error, pins and contents aren't the same length!")
        sys.exit(1)

    for i in range(length):
        id = contents[i]["saveId"]["id"]

        if id != services[i]["id"]:
            print("Error: query error, pins and contents don't match order!")
            sys.exit(1)

        title = contents[i]["cardTitle"]["string"]

        content_id = contents[i]["cardLink"]["route"]["typedParams"]["contentId"]

        type = contents[i]["cardLink"]["route"]["typedParams"]["contentType"]

        services[i]["title"] = title

        services[i]["content_id"] = content_id
        
        services[i]["type"] = type

    return services


# function that adds coordinates of services from service content 
# datastructure to the list of services passed to parameters
def get_coordinates__id(pins):
    services = list()

    for pin in pins:
        latitude = pin["geoPoint"]["latitude"]

        longitude = pin["geoPoint"]["longitude"]

        id = pin["saveId"]["id"]

        services.append({
            "id" : id,
            "latitude" : latitude,
            "longitude" : longitude
        })

    return services