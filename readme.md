# Automatic Task Categorization

## Architecture
* TodoRepository


## Features
* create_todo <br> 
-> title and description must not be null, they are used to train the clustering algorithm
* delete_todo


## Task Clustering
* KMeans from *sklearn*
* input: task + description


(Code basis from https://github.com/michadozent25/python_databases/tree/main/06_todolist_rest_v02)