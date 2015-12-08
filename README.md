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

1. [Table definitions](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/blob/master/vagrant/catalog/database_setup.py)
   have been implemented for the database structure, and [fixtures](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/blob/master/vagrant/catalog/database_init.py)
   have been added to have some items in the catalog to start with. The
   database backend of choice is PostgreSQL.
2. Deployment of the database and the web application has been automated with
   a [Puppet script](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/blob/master/manifests/default.pp),
   which is using some (included) [open source Puppet modules](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/tree/master/modules).
   This script will automatically run when creating the virtual environment
   with ```vagrant up```.
3. [Templates](https://github.com/swesterveld/udacity-nd004-p3-item-catalog/tree/master/vagrant/catalog/templates)
   have been created from scratch, with the use of Flask and Bootstrap.
4. This catalog has a hierarchy of categories; categories for items are
   grouped in main categories, to keep a better overview. This hierarchy is
   reflected in the menu on the top of the page, and in the category selector
   of the item-form.
5. User registration and authentication has been implemented, based on
   OAuth 2.0 with Google+.
6. A decorator function has been implemented for functionalities that require
   a user to be logged in.
7. And more...

## Run the application
1. Make sure Git, Vagrant and VirtualBox have been installed on your computer
2. Make sure your computer is connected to the internet
3. Clone this repository to a directory on your computer
4. Change directory to the ```vagrant``` directory in the repository
5. Issue ```vagrant up``` to start the virtual environment. Provisioning will
   be completed automatically by Vagrant and Puppet. Puppet will also load
   some fixtures into the database and start the web application for you.
6. The virtual environment is ready now, with a running web application.
   Finally, to check the web application, open <http://localhost:5000/catalog/>
   in your web browser.
