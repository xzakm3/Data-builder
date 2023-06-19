Data builder
--------------------------

This project contains several parts:
- server part that sits in `src` folder as entry point
- script `generate_predictions` generating predictions 

## Prerequisites
You need to have installed `python3.10`.
Assure in root folder, you created `data` folder where you placed your data `texts.csv` to be processed.

## How to 
### Develop

Go to root directory and type following command in terminal:
```
make venv & source .venv/slido_assignment/bin/activate
```
It will install all necessary dependencies for you into `slido_assignment` virtual environment. Get to  virtual env with executing following command
```
source .venv/slido_assignment/bin/activate
```
and from now on, you can use this virtual env for further developing.


**Note**: If you want to manually install all dependencies, go to project root directory and execute command
```
make reqs
```

### Run
As first, exec to virtual env as defined above
#### Run server
In one terminal session, go to `src` directory and run `flask run` with corresponding parameters. If there is an issue with running Flask server,
you need to export several environment variables.

When you are on linux:
```
export FLASK_ENV=development
export FLASK_APP=app.py
```
When you are on Windows:
```
set FLASK_ENV=development
set FLASK_APP=app.py
```

If nothing fails, server is running on localhost with port 5000.
#### Run script generating predictions
Go to root directory and run
```
python generate_predictions.py --help
```
to see how to run this script

It requires two parameters:
    - input path, that points to csv file with texts to be language predicted. Path is relative with respect to root folder
    - output path, that is path to result folder. There will stored result_predictions.csv with all predicted results. Path is relative with respect to root folder


So if you run script as follows
```
python generate_predictions.py -ip './data/texts.csv' -op 'results'
```
it loads csv file from `<root_path>/data/texts.csv`. All prediction results will be stored into `<root_path>/results/resultpredictions.csv` file
### Run tests
Go to root directory and run command
```
tox tests
```

If you have any questions, contact me on email: zakyz.martin@gmail.com
<3