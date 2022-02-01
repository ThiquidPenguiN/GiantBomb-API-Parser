import requests
import api_key_giantbomb
import pprint
import json
from collections import defaultdict
import codecs
import os


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


### METHODS ###

class PublishedGames:
	def published_games_by_company():
		# build api string published games
		getPublishedGames = baseUrl+moduleCompany+companyCodeTake2+"/?"+formatJson+"&"+publishedGamesField+"&"+apiKey
		print ("request url " + getPublishedGames)
		# send get request for published games
		responsePublishedGames = requests.get(getPublishedGames, headers=headers)
		# convert output to iterable dictionary
		outputGamesDict = responsePublishedGames.json()
		
		return outputGamesDict

class ParseData:
    
	def game_reviews(reviewsJson, title):
		# construct review dictionary
		gameReviewDictionary = {}
		gameReviewDictionary[title] = {'ReviewsByScore':[]}

		buildReviewDict = defaultdict(list)

		for n in range(len(reviewsJson['results'])):
			
			reviewScore = reviewsJson['results'][n]['score']
			
			reviewTitle = reviewsJson['results'][n]['deck']
			reviewReviewer = reviewsJson['results'][n]['reviewer']
			reviewDate = reviewsJson['results'][n]['date_added']
			reviewIsDLC = reviewsJson['results'][n]['dlc']
			
			blockOfReviewData = {'Title' : reviewTitle, 'Reviewer' : reviewReviewer, 'ReleaseDate' : reviewDate, 'IsDLC' : reviewIsDLC}
			
			buildReviewDict[reviewScore].append(blockOfReviewData)

		gameReviewDictionary[title]['ReviewsByScore'].append(buildReviewDict)
		return gameReviewDictionary

	def get_game_id(publishedApi):		
		gameID = publishedApi['results']['published_games'][gameIndex]['id']
		return gameID

	def get_game_title(publishedApi):		
		gameTitle = publishedApi['results']['published_games'][gameIndex]['name']
		return gameTitle

	def query_reviews(publishedApi):
		#store gameID
		varId = ParseData.get_game_id(publishedGamesDict)
		#query by game uid
		getGameReviews = baseUrl+moduleReviews+"/?"+formatJson+"&"+gamesGuidFilter+companyCodePrefix+str(varId)+"&"+apiKey
		print ("request url " + getGameReviews)
		#send get request for game reviews by ID
		response = requests.get(getGameReviews, headers=headers)
		# convert response to iterable dictionary
		outputReviewsDict = response.json()
		return outputReviewsDict

	def write_data_json(jsonFile, dictData):
		# write dictionary in JSON format
		with open(jsonFile, 'wb') as f:
			json.dump(dictData, codecs.getwriter('utf-8')(f), ensure_ascii=False)     
		return
     
### PROCESS ###

# get and convert published games output to iterable dictionary
publishedGamesDict = PublishedGames.published_games_by_company()

# start building JSON file dictionary for export
reviewsAppendJson = {}

# iterate through published game results to build JSON dictionary
for gameIndex in range(len(publishedGamesDict['results']['published_games'])):
    # query api string game reviews by ID
    gameReviewsDict = ParseData.query_reviews(publishedGamesDict)
    
    # check if review ids match game filter (bug with giantbomb API reporting incorrect user reviews from some filters)
    try:
        checkGameID = gameReviewsDict['results'][0]['game']['id']
        if checkGameID == ParseData.get_game_id(publishedGamesDict):
            # append to JSON Dictionary
            reviewsAppendJson.update(ParseData.game_reviews(gameReviewsDict, ParseData.get_game_title(publishedGamesDict)))
    except:
        print("no data for " + ParseData.get_game_title(publishedGamesDict))

# process outputs
try:
	os.mkdir('./outputs')
except:
    print('outputs already exists')

# write dictionary in JSON format
print('writing JSON data')
ParseData.write_data_json('outputs/published_games.json', publishedGamesDict)
ParseData.write_data_json('outputs/game_reviews.json', reviewsAppendJson)
