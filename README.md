# Project "Item Catalog"

This code is the result I achieved for ***[Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004) - Project 3: Item Catalog***.
Instructions on how to run the application can be found at the bottom of
this README text.

This code has been *reviewed by me*. According to me, based on the rubric
used by the Udacity reviewer, this code at least:
- [x] Meets Specifications: Page does implement an JSON endpoint with
  all required content.
- [x] Meets Specifications: Page does read category and item information
  from a database.
- [x] Meets Specifications: Page does include a form allowing users to
  add new items and correctly processes submitted forms.
- [x] Meets Specifications: Page does include a function to edit/update
  a current record in the database table and correctly processes submitted
  forms.
- [x] Meets Specifications: Page does include a function to delete a
  current record.
- [x] Meets Specifications: Page does implement a third-party
  authentication and authorization service; and create, delete and update
  operations doe consider authorizations tatus prior to execution.
- [x] Meets Specifications: Code is ready for personal review and neatly
  formatted.
- [x] Meets Specifications: Comments are present and effectively explain
  longer code procedures.
- [x] Meets Specifications: A README file is included detailing all
  steps required to successfully run the application.

A list of websites, books, forums, blog posts, Github repositories etcetera
that I have referred to or used in this submission can be found in the
[references.txt](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/blob/master/references.txt)
file.

## Origin and Modifications
This code is based on the [repository provided by Udacity](https://github.com/udacity/fullstack-nanodegree-vm)
with common code for the Relational Databases and Full Stack Fundamentals
courses.
There are several things I've added or modified:

1. [Table definitions](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/blob/master/vagrant/catalog/database_setup.py) have been implemented for the database structure, and [fixtures](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/blob/master/vagrant/catalog/database_init.py) have been added, to have some items in the catalog to start with. The database backend of choice is PostgreSQL.
2. Deployment of the database and the web application has been automated with a [Puppet script](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/blob/master/manifests/default.pp), which is using some (included) [open source Puppet modules](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/tree/master/modules). This script will automatically run when creating the virtual environment with ```vagrant up```.
3. [Templates](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/tree/master/vagrant/catalog/templates) have been included from scratch.
4. This catalog has multiple main categories, with each multiple (sub) categories in them. The main purpose for the main categories is to have grouping of (sub) categories, and have a hierarchical overview of categories. Items can only be linked to the (sub) categories.
5. OAuth 2.0 with Google+ has been implemented.
6. The front-end has been implemented with Bootstrap. The menu for the categories has been put in a Navbar on top of the web application. A Modal has been implemented for signing in to the web application. When a user is logged in, the link for signing in will change into the name of the user, with a Glyphicon of a user.
7. A decorator has been implemented for functionalities that need a user to be logged in.
9. And more...

## Run the application
1. Make sure Git, Vagrant and VirtualBox have been installed on your computer
2. Make sure your computer is connected to the internet
3. Clone this repository to a directory on your computer
4. Change directory to the ```vagrant``` directory in the repository
5. Issue ```vagrant up``` to start the virtual environment and let
   Vagrant and Puppet prepare the database for this project. Puppet will
   automaticaly start the web application.
6. The virtual environment is ready now, with a running web application.
   Finally, to check the web application, open http://localhost:5000/catalog/
   in your web browser.
