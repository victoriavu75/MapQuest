import project3_API
import project3_input
import urllib.parse
import urllib.request
import json

class stepsMap:
    def print_info(self, route:dict):
        result = ''
        result = 'DIRECTIONS\n'
        for item in route['route']['legs']:
            for step in item['maneuvers']:
                result += step['narrative'] +'\n'
        
        return result
    
class total_distanceMap:
    def print_info(self,route:dict):
        result = ''
        distance = route['route']['distance']
        distance = round(distance)
        result = 'TOTAL DISTANCE: '+str(distance)+' miles\n'
        return result
    
class total_timeMap:
    def print_info(self,route:dict):
        result = ''
        time = route['route']['formattedTime']
        minutes = time.find(':')
        newtime = int(time[minutes+1:minutes+3])
        if int(time[minutes+4:]) >= 30:
            newtime += 1
        if int(time[:minutes]) > 0:
            hours = 60 * int(time[:minutes])
            newtime += hours
        result = 'TOTAL TIME: '+str(newtime)+' minutes\n'
        return result
    
class latlongMap:
    def print_info(self,route:dict):
        result = ''
        result = 'LATLONGS\n'
        for key in route['route']['locations']:
            if round(key['latLng']['lat'],2) > 0:
                result += '{:.2f}'.format(round(key['latLng']['lat'],2))+'N '
            else:
                latitude = '{:.2f}'.format(round(key['latLng']['lat'],2)).replace('-','')
                result += latitude +'S '
            if round(key['latLng']['lng'],2) > 0:
                result += '{:.2f}'.format(round(key['latLng']['lng'],2))+'E'
            else:
                longitude = '{:.2f}'.format(round(key['latLng']['lng'],2)).replace('-','')
                result += longitude +'W'
            result += '\n'
        return result
    
class elevationMap:
    def print_info(self,route:dict):
        result = ''
        result = 'ELEVATIONS\n'
        for url in project3_API.build_elevation_url(project3_API.list_of_latlng(route)):
            elevation = project3_API.download_result(url)
            if elevation != None:
                for key in elevation['elevationProfile']:
                    result += str(round(key['height']))+'\n'
            else:
                pass
        if result != 'ELEVATIONS\n':
            return result
        else:
            result = '\nMAPQUEST ERROR'
            return result
        
def run_maps(maps:['Map'], result:dict):
    results = []
    for a_map in maps:
        current_location = a_map.print_info(result)
        results.append(current_location)
    if '\nMAPQUEST ERROR' not in results:
        for result in results:
            print(result)
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    else:
        print('\nMAPQUEST ERROR')
