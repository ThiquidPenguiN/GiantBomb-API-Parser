# GiantBomb API Parser
 Query giant bomb api for take2 interactive published games, with reviews

### ----------------------------------------------------------------------------------

## Setup For Use

### Notice: Be sure to install python 3.8.x, 3.9.x, or 3.10.x, as this was tested in those environments.

### 1) Create `api_key_giantbomb.py` for api key (use code snippet below)
- you can obtain an API key here: https://www.giantbomb.com/api/

`api_key_giantbomb.py`
```
#python file that exports the api_key
api_key = 'place api key here'
```


### 2) Installing Prerequisits
- Install pip
	- Ubuntu: `sudo apt-get install python3-pip`
	- Windows: `python get-pip.py`
- Run to install virtualenv `python3 -m pip install --user virtualenv`
- More info below [How to install virtualenv](#-How-to-install-virtualenv:)

### 3) Initialize Virtual Environment. [Details on it's setup in Dev Notes](###-Dev-notes)
- Run `python -m venv path/to/project/root/venv` within root folder of project to initialize virtual environment. Note: You may need to install additional packages like `python3-venv`.
- Activate the Virtual Environment
	- On Unix or MacOS, using the bash shell: `source /path/to/venv/bin/activate`
	- On Unix or MacOS, using the csh shell: `source /path/to/venv/bin/activate.csh`
	- On Unix or MacOS, using the fish shell: `source /path/to/venv/bin/activate.fish`
	- On Windows using the Command Prompt: `path\to\venv\Scripts\activate.bat`
	- On Windows using PowerShell: `path\to\venv\Scripts\Activate.ps1`
- If successful, your terminal will have the "(venv)" prefix. Example: `$ (venv) D:\git\GiantBomb-API-Parser>`
- if you are having issues setting up virtual environments, please follow the instructions below on [How to install virtualenv](#-How-to-install-virtualenv:). Be sure to run `deactivate` in terminal to exit the virtual enviroment. Remove the `venv/` directory and its contents before troubleshooting.

### 4) Install requirements for virtual environment
- Run `pip install -r requirements.txt`. This may take a couple of moments as it is installing virtual environment requirements, please be patient. Note: Be sure to be using `pip` associated with `python 3`, like `pip3`.
- if you are still having issues setting up virtual environments, please follow the instructions below on [How to install virtualenv](#-How-to-install-virtualenv:). Be sure to run `deactivate` in terminal to exit the virtual enviroment. Remove the `venv/` directory and its contents before troubleshooting.

### 5) Run Parser
- Call `python .\giantbomb-api-parser.py` to run API script. This will generate an `outputs/` directory in the root of the project. Be sure `python` is 
- This will generate these JSON files: `published_games.json` and `game_reviews.json`.

### ------------------------------------------------------------------------------- 

### Dev notes

#### Website: [Setup venv for python](`https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b`)

 - run `pip freeze > requirements.txt` when adding new libraries.

 - use `venv\scripts\activate` within root folder of project to activate virtual environment

 #### ! Furture Development !
 - Need to add more basic error handling. So far, script depends on system to throw errors.

 - Add dynamic publisher searching.

 - Seperate `### PROCESS ###` portion of `giantbomb-api-parser.py` into its own module.

### --------------------------------------------------------------------------------

# How to install virtualenv:

### Install **pip** first

    - Ubuntu: `sudo apt-get install python3-pip`
	- Windows: `python get-pip.py`

### Then install **virtualenv** using pip3

    `python3 -m pip install --user virtualenv`

### Now create a virtual environment 

    virtualenv venv 

>you can use any name insted of **venv**
  
### Active your virtual environment:    
    
    source venv/bin/activate

### To deactivate:

    deactivate

