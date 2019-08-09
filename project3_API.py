import urllib.parse
import urllib.request
import urllib.error
import json

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route'
MAPQUEST_ELEVATION = 'http://open.mapquestapi.com/elevation/v1/profile'
MAPQUEST_API_KEY= 'OR8ehUwfgeyY8XeH9sCGajJfmpLcSBEb'

def build_search_url(locations:list) -> str:
    to_locations = []   
    for location in locations[1:]:
        place = ('to', location)
        to_locations.append(place)
    query_parameters = [
        ('key', MAPQUEST_API_KEY),
        ('from', locations[0])]
    query_parameters.extend(to_locations)
    return BASE_MAPQUEST_URL + '?' + urllib.parse.urlencode(query_parameters)



def list_of_latlng(route:dict) -> list:
    result =[]
    for key in route['route']['locations']:
        latlng = []
        latlng.append(key['latLng']['lat'])
        latlng.append(key['latLng']['lng'])
        result.append(latlng)
    return result

def build_elevation_url(latlngs:list) -> list:
    result = []
    for latlng in latlngs:
        collection = ''
        collection += str(latlng[0])+','+str(latlng[1])
        query_parameters = [
            ('key', MAPQUEST_API_KEY),
            ('unit', 'f'),
            ('latLngCollection', collection)]
        url = MAPQUEST_ELEVATION + '?' + urllib.parse.urlencode(query_parameters)
        result.append(url)
    return result

def download_result(url:str) -> dict:

    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)
    
    except urllib.error.HTTPError:
        return None

    except urllib.error.URLError:
        return None
    
    except json.decoder.JSONDecodeError:
        return None

    except TimeoutError:
        return None
    
    finally:
        if response != None:
            response.close()


    



