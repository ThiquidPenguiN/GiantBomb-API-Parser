import requests
import api_key_giantbomb
import pprint
import json
from collections import defaultdict


#URI Formation
base_url = 'https://www.giantbomb.com/api'
moduleCompany = "/company"
moduleReviews = "/user_reviews"
companyCodeTake2 = "/3010-450" #company code can only be acquired by navigating with a web browser to giantbomb.com, finding the company profile, and inspecting the URL.
#query constructors
publishedGamesField = "field_list=published_games"
gamesGuidFilter = "filter=game:"
companyCodePrefix = "3030-"
formatJson = "format=json"
apiKey = "api_key=" + api_key_giantbomb.api_key
#required params
headers={ "user-agent": "pyhton request module" }
#One off
gameID = "36765"


#build api string published games
getPublishedGames = base_url+moduleCompany+companyCodeTake2+"/?"+formatJson+"&"+publishedGamesField+"&"+apiKey
print ("request url " + getPublishedGames)

#send get request for published games
responsePublishedGames = requests.get(getPublishedGames, headers=headers)
# pprint.pprint(responsePublishedGames.json())


#build api string game reviews by ID
getGameReviews = base_url+moduleReviews+"/?"+formatJson+"&"+gamesGuidFilter+companyCodePrefix+gameID+"&"+apiKey
print ("request url " + getGameReviews)

#send get request for game reviews by ID
responseGameReviews = requests.get(getGameReviews, headers=headers)




### Sample parsing examples GAME REVIEWS
gameReviews_dict = responseGameReviews.json()




#print(gameReviews_dict['results'][0]['score'])

# construct review dictionary
gameTitle = gameReviews_dict['results'][0]['game']['name']
gameReviewDictionary = {}
gameReviewDictionary =  {'GameTitle': gameTitle, 'ReviewsByScore': []}

buildReviewDict = defaultdict(list)

for n in range(len(gameReviews_dict['results'])):
    
    reviewScore = gameReviews_dict['results'][n]['score']
    
    reviewTitle = gameReviews_dict['results'][n]['deck']
    reviewReviewer = gameReviews_dict['results'][n]['reviewer']
    reviewDate = gameReviews_dict['results'][n]['date_added']
    reviewIsDLC = gameReviews_dict['results'][n]['dlc']
    
    blockOfReviewData = {'Title' : reviewTitle, 'Reviewer' : reviewReviewer, 'ReleaseDate' : reviewDate, 'IsDLC' : reviewIsDLC}
    
    buildReviewDict[reviewScore].append(blockOfReviewData)
    

    
pprint.pprint(buildReviewDict)
    

    



#------------------------------------------------------

# ### Sample parsing examples PUBLISHED GAMES
# publishedGames_dict = responsePublishedGames.json()

# #returns 108 items
# print(len(publishedGames_dict['results']['published_games']))

# #returns first item as string
# print(publishedGames_dict['results']['published_games'][0])

# #returns first item's url
# print(publishedGames_dict['results']['published_games'][0]['api_detail_url'])

# #returns first item's id
# print(publishedGames_dict['results']['published_games'][0]['id'])

# #returns first item's game name
# print(publishedGames_dict['results']['published_games'][0]['name'])








# https://www.giantbomb.com/api/user_reviews/?format=json&filter=game:3030-36765 ----------------REVIEWS OF THE GAME
# https://www.giantbomb.com/api/company/3010-450/?format=json&field_list=published_games
# https://www.giantbomb.com/api/company/3010-450/?format=json&field_list=published_games&api_key=1c6309afefdb77a9ba01da868ed7afc3b3d140e7
# https://www.giantbomb.com/api/reviews/?format=json&filter=guid:3030-20827



# {"$LabelName": {"ReviewsByScore": [
#       "5": [ {"Title": "Title Name", "Reviewer": "Reviewer Name", "ReleaseDate": "01/01/2019"}],
#       "4": [ {"Title": "Title Name", "Reviewer": "Reviewer Name", "ReleaseDate": "01/01/2019", "IsDlc": true}]
#     ]
#   }
# }