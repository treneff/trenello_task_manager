# Trenello Task Manager

A full stack application developed on Flask with the main goal to track projects and enable a more
efficient task management for the users involved.

## Contents

-   [Technologies](#technologies)
-   [Brief](#brief)
-   [Installation](#installation)

<br>
<img width="1680" alt="Screenshot 2023-01-12 at 12 39 36" src="https://user-images.githubusercontent.com/65739239/212072601-5e59dbbf-a60a-4e16-8bfb-d0efd791c034.png">
<img width="1680" alt="Screenshot 2023-01-12 at 12 39 47" src="https://user-images.githubusercontent.com/65739239/212072633-a5e268d2-d47d-4e4e-832d-af1695ded915.png">

## Technologies

Main technologies utilised in the development of the project

Python, Flask, Jinja, HTML5, CSS

<br>

## Brief

After the initial few weeks of training with CodeClan\_ it was time to independently develop a full
stack mobile first Flask application following the CRUD model. As a follow up of my endeavours to
reduce my digital footprints I have developed a Project/Task management application for local use.
<br> In the development of the application the following brief was used.

**MVP**

*The app should allow the user to track projects and tasks associated with those projects as needing
completing and as completed.<br> *The user should be able to create new tasks and add them to
projects.<br> *The user should be able to create and delete projects.<br> *The user should be able
to amend the status of a task in the project from needing completing to completed.<br>

**Extensions**

*Incorporate additional field allowing tasks to be tracked while in progress.<br> *Add an option to
pin important tasks to the top of the list.<br> *Allow completed tasks to be archived and able to be
accessed for future reference.<br> *Enable the tracking of a Date the task is due by.<br>

Disclaimer: Some of the features are currently in development. <br>

## Installation

python3, postgreSQL and Flask installations will be required to run the application

To build the database structure and seed with starter data follow the steps in your terminal.

1. createdb trenello_task_manager
2. psql -d trenello_task_manager -f db/task_manager.sql
3. python3 console .py

Then to initiate the application:

flask --app app --debug run

The application will be initiated on port:5000 Therefore, can be accessed on http://127.0.0.1:5000/

A basic structure of projects and the tasks associated with them has been initiated for
demonstration purposes, but is fully customizable
