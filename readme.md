# Automatic Task Categorization

## Architecture
* TodoRepository


## Features
* create_todo <br> 
-> title and description must not be null, they are used to train the classification algorithm
* delete_todo_by_id
* delete_todo_by_state


## Task Classification
* LinearSVC from *sklearn*
* input: task + description


(Code basis from https://github.com/michadozent25/python_databases/tree/main/06_todolist_rest_v02)


## Guide:
1. Get the model dumps as .joblib files:
* Run _utils>train_classifiers.py_
2. Connect with SQLite DB dump:
* Define name of the dump in _database>db_session.py_
* Run _main.py_ to start the RESTful service
* Enter some data
* Connect the locally saved SQLite dump on your system with a DB client (e.g. DBeaver)
3. Run commands/functions on RESTful service, and view your changes in the SQLite DB
<br><br>
4. That's it!