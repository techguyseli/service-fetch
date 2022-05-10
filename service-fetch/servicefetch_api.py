# imports
import requests
import json

# get all services in the specified area
def get_area_json(api_key, ne_lat, ne_lon, sw_lat, sw_lon):
    url = "https://travel-advisor.p.rapidapi.com/locations/v2/list-nearby"

    querystring = {"currency":"USD","units":"km","lang":"en_US"}

    payload = {
        "contentId": "cc8fc7b8-88ed-47d3-a70e-0de9991f6604",
        "contentType": "restaurant",
        "filters": [
            {
                "id": "placetype",
                "value": ["hotel", "attraction", "restaurant"]
            },
            {
                "id": "minRating",
                "value": ["30"]
            }
        ],
        "boundingBox": {
            "northEastCorner": {
                "latitude": ne_lat,
                "longitude": ne_lon
            },
            "southWestCorner": {
                "latitude": sw_lat,
                "longitude": sw_lon
            }
        }
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    return json.loads(response.text)


# function that requests hotel info from api
def get_hotel_json(content_id, api_key):
    url = "https://travel-advisor.p.rapidapi.com/hotels/v2/get-details"

    querystring = {"currency":"USD","units":"km","lang":"en_US"}

    payload = {
        "contentId": content_id,
        "checkIn": "2022-03-03",
        "checkOut": "2022-03-05",
        "rooms": [
            {
                "adults": 2,
                "childrenAges": [2]
            },
            {
                "adults": 2,
                "childrenAges": [3]
            }
        ]
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return json.loads(response.text)


# function that requests attraction info from api
def get_attraction_json(content_id, api_key):
    url = "https://travel-advisor.p.rapidapi.com/attractions/v2/get-details"

    querystring = {"currency":"USD","units":"km","lang":"en_US"}

    payload = {
        "contentId": content_id,
        "startDate": "2022-06-30",
        "endDate": "2022-07-01",
        "pax": [
            {
                "ageBand": "ADULT",
                "count": 2
            }
        ]
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return json.loads(response.text)


# function that requests restaurant info from api
def get_restaurant_json(content_id, api_key):
    url = "https://travel-advisor.p.rapidapi.com/restaurants/v2/get-details"

    querystring = {"currency":"USD","units":"km","lang":"en_US"}

    payload = {
        "contentId": content_id,
        "reservationTime": "2022-03-07T20:00",
        "partySize": 2
    }
    
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    return json.loads(response.text)