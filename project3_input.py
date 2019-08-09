import project3_API
import project3_outputs

def run() -> None:
    locations = get_locations()
    information = ask_for_info()
    url = project3_API.build_search_url(locations)
    result = project3_API.download_result(url)
    if result == None:
        print('\nMAPQUEST ERROR')
    else:
        if result['info']['statuscode'] == 402:
            print('\nNO ROUTE FOUND')
        elif result['info']['statuscode'] == 608:
            print('\nNO ROUTE FOUND')
        elif result['info']['statuscode'] == 606:
            print('\nNO ROUTE FOUND')
        elif result['info']['statuscode'] == 612:
            print('\nNO ROUTE FOUND')
        elif result['info']['statuscode'] == 605:
            print('\nNO ROUTE FOUND')
        elif result['info']['statuscode'] == 604:
            print('\nNO ROUTE FOUND')
        elif result['info']['statuscode'] == 609:
            print('\nNO ROUTE FOUND')
        else:
            print_information(result,information,locations)


def get_locations() -> list:
    num_of_locations = input()
    list_of_locations = []
    for i in range(int(num_of_locations)):
        location = input()
        list_of_locations.append(location)
    return list_of_locations

def ask_for_info()->list:
    while True:
        try:
            num_of_outputs = int(input())
            if num_of_outputs == '':
                print('Invalid number of requests.Must be 1-5')
                pass
            elif int(num_of_outputs) <=0 or int(num_of_outputs) > 5:
                print('Invalid number of requests.Must be 1-5')
                pass
            else:
                break
        except ValueError:
            print('Invalid type of request. Must be and integer from 1-5')
    information = []
    for i in range(int(num_of_outputs)):
        information.append(input())
    return information

def print_information(result:dict, information: list, locations: list) -> None:
    maps = []
    for item in information:
        if item.upper() == 'STEPS':
            maps.append(project3_outputs.stepsMap())
        elif item.upper() == 'TOTALDISTANCE':
            maps.append(project3_outputs.total_distanceMap())
        elif item.upper()  == 'TOTALTIME':
            maps.append(project3_outputs.total_timeMap())
        elif item.upper() == 'LATLONG':
            maps.append(project3_outputs.latlongMap())
        elif item.upper() == 'ELEVATION':
            maps.append(project3_outputs.elevationMap())
    project3_outputs.run_maps(maps,result)
    

if __name__ == '__main__':
    run()
