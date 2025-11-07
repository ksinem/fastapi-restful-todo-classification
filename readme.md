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