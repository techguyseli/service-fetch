# imports
from servicefetch_api import get_restaurant_json, get_attraction_json, get_hotel_json


# function that adds images to service list passed through parameters
def add_images(services, api_key):
    for service in services:
        content_id = service['content_id']
        service_type = service['type']
        images = get_images(content_id, service_type, api_key)
        service["images"] = images
    return services


# function that gets services' images from specific apis depending on service type
def get_images(content_id, service_type, api_key):
    images = list()
    if service_type == "restaurant":
        images = get_restaurant_images(content_id, api_key)
    elif service_type == "hotel":
        images = get_hotel_images(content_id, api_key)
    elif service_type == "attraction":
        images = get_attraction_images(content_id, api_key)
    else:
        print("Error! unknown service type.")
        sys.exit(1)
    return images


# function that gets images from attractions' api
def get_attraction_images(content_id, api_key):
    attraction_obj = get_attraction_json(content_id, api_key)
    images = filter_images(attraction_obj)
    return images


# function that gets images from restaurants' api
def get_restaurant_images(content_id, api_key):
    restaurant_obj = get_restaurant_json(content_id, api_key)
    images = filter_images(restaurant_obj)
    return images


# function that gets images from hotels' api
def get_hotel_images(content_id, api_key):
    hotel_obj = get_hotel_json(content_id, api_key)
    images = filter_images(hotel_obj)
    return images


# filter images' urls from api image request response
def filter_images(obj):
    if obj is None:
        print("image error ass")
    images = list()
    necessary_data = obj["data"]["AppPresentation_queryAppDetailV2"][0]["sections"][0]["albumPhotos"]
    if necessary_data:
        if len(necessary_data) > 1:
            for item in necessary_data:
                sizes_count = len(item["data"]["sizes"])
                images.append(item["data"]["sizes"][sizes_count - 1]['url'])
    return images