import requests
import api_key_giantbomb
import pprint
import json


#URI Formation
base_url = 'https://www.giantbomb.com/api'
moduleCompany = "/company"
companyCodeTake2 = "/3010-450" #company code can only be acquired by navigating with a web browser to giantbomb.com, finding the company profile, and inspecting the URL.
#query constructors
fields = "field_list=published_games"
formatJson = "format=json"
api_key = "api_key=" + api_key_giantbomb.api_key
#required params
headers={ "user-agent": "pyhton request module" }


#build api string
get_publishedGames = base_url+moduleCompany+companyCodeTake2+"/?"+formatJson+"&"+fields+"&"+api_key
print ("request url " + get_publishedGames)

#send get request
query_response = requests.get(get_publishedGames, headers=headers)
# pprint.pprint(query_response.json())

output_dict = query_response.json()


### Sample parsing examples
#returns 108 items
print(len(output_dict['results']['published_games']))

#returns first item as string
print(output_dict['results']['published_games'][0])

#returns first item's url
print(output_dict['results']['published_games'][0]['api_detail_url'])

#returns first item's id
print(output_dict['results']['published_games'][0]['id'])

#returns first item's game name
print(output_dict['results']['published_games'][0]['name'])






#https://www.giantbomb.com/api/company/3010-450/?format=json&field_list=published_games
#https://www.giantbomb.com/api/company/3010-450/?format=json&field_list=published_games&api_key=1c6309afefdb77a9ba01da868ed7afc3b3d140e7