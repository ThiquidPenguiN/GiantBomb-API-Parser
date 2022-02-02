# GiantBomb API Query
 Query giant bomb api for take2 interactive published games, with reviews


## Setup For Use

### 1) Create `api_key_giantbomb.py` for api key (use code snippet below)
```
#python file that exports the api_key
api_key = 'place api key here'
```

### 2) Initialize Virtual Environment. [Details on it's setup in Dev Notes](###-Dev-notes)
- Use `venv\scripts\activate` within root folder of project to activate virtual environment. No need to import libraries :)

### 3) Run Parser
- Call `python .\giantbomb-api-parser.py` to run API script. This will generate an `outputs/` directory in the root of the project.
- This will generate these JSON files: `published_games.json` and `game_reviews.json`.



### Dev notes

[Setup venv for python](`https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b`)

 - run `pip freeze > requirements.txt` when adding new libraries

 - use `venv\scripts\activate` within root folder of project to activate virtual environment

 #### ! Furture Development !
 - Need to add more basic error handling. So far, script depends on system to throw errors.

 - Add dynamic publisher searching.

 - Seperate `### PROCESS ###` portion of `giantbomb-api-parser.py` into its own module.

