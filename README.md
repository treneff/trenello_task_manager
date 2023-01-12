 # Trenello Task Manager

A full stack application developed on Flask with the main goal to track projects and enable a more efficient task management for the users involved. 

## Contents 

* [Technologies](#technologies)
* [Brief](#brief)
* [Installation](#installation)

<br>


## Technologies

Main technologies utilised in the development of the project

Python, Flask, Jinja, HTML5, CSS 

<br>


## Brief

After the initial few weeks of training with CodeClan_ it was time to independently develop a full stack mobile first Flask application following the CRUD model. As a follow up of my endeavours to reduce my digital footprints I have developed a Project/Task management application for local use.
<br>
In the development of the application the following brief was used.

**MVP**

*The app should allow the user to track projects and tasks associated with those projects as needing completing and as completed.<br>
*The user should be able to create new tasks and add them to projects.<br>
*The user should be able to create and delete projects.<br>
*The user should be able to amend the status of a task in the project from needing completing to completed.<br>


**Extensions**

*Incorporate additional field allowing tasks to be tracked while in progress.<br>
*Add an option to pin important tasks to the top of the list.<br>
*Allow completed tasks to be archived and able to be accessed for future reference.<br>
*Enable the tracking of a Date the task is due by.<br>

Disclaimer: Some of the features are currently in development.
<br>


## Installation

python3, postgreSQL and Flask installations will be required to run the application

To build the database structure and seed with starter data follow the steps in your terminal.
1. access the project within the backend folder
2. createdb trenello_task_manager
3. psql -d trenello_task_manager -f db/task_manager.sql
4. python3 console .py


Then to initiate the application: 

flask --app app --debug run

The application will be initiated on port:4999 Therefore, can be accessed on http://127.0.0.1:4999/

A basic structure of projects and the tasks associated with them has been initiated for demonstration purposes, but is fully customizable
