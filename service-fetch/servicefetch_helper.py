# this file provides just some basic helper functions
# that if they were put in the main script would just
# make it a little hard to read/understand


# imports
from servicefetch_api import get_area_json
from servicefetch_service import get_services_info
from servicefetch_image import add_images


# print usage and exit with a given code
def print_usage(code=1, msg=None):
    # print error messages if there are any
    if msg:
        print("Error:")
        print("\t" + msg + "\n")

    # print usage
    print("Usage:")
    print("\tpython3 servfetch.py --option1 value1 --option2 value2. . .\n")

    # print mandatory arguments
    print("Mandatory options:")
    print("\t--apikey value : A RapidApi travel-advisor api key.")
    print("\t--nelat value : Latitude of north east point of the border box.")
    print("\t--nelon value : Longitude of north east point of the border box.")
    print("\t--swlat value : Latitude of south west point of the border box.")
    print("\t--swlon value : Longitude of south west point of the border box.\n")

    # print optional arguments
    print("Optional options:")
    print("\t--srvfile value : Name of the file to store info about the images.")
    print("\t--imgfile value : Name of the file to store info about the services.")
    print("\t--help or -h : Print this help menu.")

    # exit with an error/success code
    sys.exit(code)


# function that returns a data structure filled with services' info 
# that belong to a map border box
def get_services(api_key, ne_lat, ne_lon, sw_lat, sw_lon):
    print("\t+ Requesting area json...")
    result_obj = get_area_json(api_key, ne_lat, ne_lon, sw_lat, sw_lon)
    print("\t+ Area json response successfully recieved.")

    print("\t+ Getting services' info, this step may take a long time please be patient...")
    services = get_services_info(result_obj)
    print("\t+ Services' info successfully fetched.")
    
    print("\t+ Getting services' images, this step may take a long time please be patient...")
    services = add_images(services, api_key)
    print("\t+ Services' images successfully fetched.")

    return services