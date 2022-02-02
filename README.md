# GiantBomb API Parser
 Query giant bomb api for take2 interactive published games, with reviews


## Setup For Use

### Notice: Be sure to install python 3.9.x

### 1) Create `api_key_giantbomb.py` for api key (use code snippet below)
```
#python file that exports the api_key
api_key = 'place api key here'
```

### 2) Initialize Virtual Environment. [Details on it's setup in Dev Notes](###-Dev-notes)
- Run `python -m venv path/to/project/root/venv` within root folder of project to initialize virtual environment.
- Run `venv\scripts\activate` within root folder of project to activate virtual environment.
- If successful, your terminal will have the "(venv)" prefix. Example: `$ (venv) D:\git\GiantBomb-API-Parser>`

### 3) Install requirements for virtual environment
- Run `pip install -r requirements.txt`. This may take a couple of moments as it is installing virtual environment requirements, please be patient.

### 4) Run Parser
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

