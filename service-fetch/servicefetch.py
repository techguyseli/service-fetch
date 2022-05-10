#!/usr/bin/python3


################ SCRIPT INFO ##################
#                                             #
# name : servfetch                            #
#                                             #
# creation date : 09-05-2022                  #
#                                             #
# version : V1.2                              #
#                                             #
# description : This script fetches           #
#       Tripadvisor services with image urls, #
#       and stores their data in a file       #
#       with csv formatting, using RapidApi   #
#       travel-advisor api.                   #
#                                             #
# author : Selaiman Kassou                    #
#                                             #
# issues : The maximum number of services     #
#       that the api can fetch per request is #
#       30, but this is currently being       #
#       remedied in servfetch V1.3.           #
#                                             #
###############################################


# imports
import sys
import getopt
from servicefetch_helper import get_services, print_usage
from servicefetch_csv import export_csvs

# main
def main(argv):
    # api key
    api_key = None

    # north east point coordinates of the border box
    ne_lat = None
    ne_lon = None

    # south west point coordinates of the border box
    sw_lat =  None
    sw_lon = None

    # output filenames
    services_filename = "services.csv"
    images_filename = "images.csv"

    # getting command line args and checking for getopt errors
    try:
        opts, args = getopt.getopt(argv,"h",["help", "apikey=", "nelon=", "nelat=", "swlon=", "swlat=", "imgfile=", "srvfile="])
    except getopt.GetoptError:
        print_usage(msg="Unknown options were passed.")

    # fill args to local variables
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_usage(code=0)
        elif opt == "--apikey":
            api_key = arg
        elif opt == "--nelon":
            ne_lon= float(arg)
        elif opt == "--nelat":
            ne_lat = float(arg)
        elif opt == "--swlon":
            sw_lon = float(arg)
        elif opt == "--swlat":
            sw_lat = float(arg)
        elif opt == "--imgfile":
            images_filename = arg
        elif opt == "--srvfile":
            services_filename = arg

    # check missing mandatory args
    mandatory_arg_missing = not (api_key and ne_lat and ne_lon and sw_lat and sw_lon)
    if mandatory_arg_missing:
        print_usage(msg="One or more mandatory option is missing.")

    # gets information about services that are in the border box
    services = get_services(api_key, ne_lat, ne_lon, sw_lat, sw_lon)

    # create csv file for the services
    print("\t+ Exporting csv files...")
    export_csvs(services_filename, images_filename, services)

    # success message
    print("Files:")
    print("\t" + services_filename)
    print("\t" + images_filename)
    print("created successfully.")

    sys.exit(0)


# execute main
if __name__ == "__main__":
   main(sys.argv[1:])
