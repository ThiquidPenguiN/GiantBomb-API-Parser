import requests
import api_key_giantbomb
import pprint
import json
from collections import defaultdict
import codecs


#URI Formation
baseUrl = 'https://www.giantbomb.com/api'
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
getPublishedGames = baseUrl+moduleCompany+companyCodeTake2+"/?"+formatJson+"&"+publishedGamesField+"&"+apiKey
print ("request url " + getPublishedGames)

#send get request for published games
responsePublishedGames = requests.get(getPublishedGames, headers=headers)
# pprint.pprint(responsePublishedGames.json())


#build api string game reviews by ID
getGameReviews = baseUrl+moduleReviews+"/?"+formatJson+"&"+gamesGuidFilter+companyCodePrefix+gameID+"&"+apiKey
print ("request url " + getGameReviews)

#send get request for game reviews by ID
responseGameReviews = requests.get(getGameReviews, headers=headers)




### Sample parsing examples GAME REVIEWS
gameReviewsDict = responseGameReviews.json()

#print(gameReviewsDict['results'][0]['score'])

def game_reviews(reviewsJson):
    # construct review dictionary
	gameTitle = reviewsJson['results'][0]['game']['name']
	#gameReviewDictionary = defaultdict(set)
	gameReviewDictionary = {}
	gameReviewDictionary[gameTitle] = {'ReviewsByScore':[]}

	buildReviewDict = defaultdict(list)

	for n in range(len(reviewsJson['results'])):
		
		reviewScore = reviewsJson['results'][n]['score']
		
		reviewTitle = reviewsJson['results'][n]['deck']
		reviewReviewer = reviewsJson['results'][n]['reviewer']
		reviewDate = reviewsJson['results'][n]['date_added']
		reviewIsDLC = reviewsJson['results'][n]['dlc']
		
		blockOfReviewData = {'Title' : reviewTitle, 'Reviewer' : reviewReviewer, 'ReleaseDate' : reviewDate, 'IsDLC' : reviewIsDLC}
		
		buildReviewDict[reviewScore].append(blockOfReviewData)

	gameReviewDictionary[gameTitle]['ReviewsByScore'].append(buildReviewDict)
	return gameReviewDictionary


### PROCESS ###

reviewsAppendJson = game_reviews(gameReviewsDict)
#print((json.loads(json.dumps(reviewsAppendJson))))


with open('game_reviews.json', 'wb') as f:
    json.dump(reviewsAppendJson, codecs.getwriter('utf-8')(f), ensure_ascii=False)
	
#pprint.pprint(json.loads(json.dumps(gameReviewDictionary)))
#print(gameReviewDictionary)
    

    



#------------------------------------------------------

# ### Sample parsing examples PUBLISHED GAMES
# publishedGamesDict = responsePublishedGames.json()

# #returns 108 items
# print(len(publishedGamesDict['results']['published_games']))

# #returns first item as string
# print(publishedGamesDict['results']['published_games'][0])

# #returns first item's url
# print(publishedGamesDict['results']['published_games'][0]['api_detail_url'])

# #returns first item's id
# print(publishedGamesDict['results']['published_games'][0]['id'])

# #returns first item's game name
# print(publishedGamesDict['results']['published_games'][0]['name'])








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