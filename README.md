# About this Repo
This is  a Django RESTFULL API for creating and updating a Blog post

# Technology used
> Django(python Framework),Sqlite3

# Installation
Python and Django need to be installed
> pip install django

open terminal and type
> git clone https://github.com/MuskanGupta1503/Django_assignment.git

run requirements.txt
> pip install -r requirements.txt

migrate
> python manage.py make migrations
> python manage.py migrate

# Usage
Run
> python manage.py runserver
Then go to the browser and enter the url http://127.0.0.1:8000/

# Constraints:
+ There is an id for every post and it is auto-generated
+ The Blog post can be updated based on this id
+ We can view all the blog post's
+ The blog has a title and description field

# API endpoints:
+ /create - to create a blog post
+ /create/id - to update a blog post,where id is the id for updating the post
+ /all - to show all the blog post

To use these api endpoints simply run
+ http://127.0.0.1:8000/create
+ http://127.0.0.1:8000/create/<:id>
+ http://127.0.0.1:8000/all
