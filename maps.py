from pprint import pprint
import os
from urllib import response
import googlemaps
# import win32com.client as win32

API_KEY = open('API_KEY.txt').read()
map_client = googlemaps.Client(API_KEY)

def get_place_into(location_name):
    try:        
    # location_name = 'Lanxess Arena Koln'
        response = map_client.places(query=location_name)
        results = response.get('results')
        return results
    except Exception as e:
        print(e)
        return None

results[0]['business_status']
results[0]['formatted_address']
results[0]['name']
results[0]['place_id']
results[0]['ranting']
results[0]['user_ratting_total']

