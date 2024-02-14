# Jr_Data_Analyst_Exercise

Hello everyone! In this tutorial we are going to explain step by step what you need to know in order to get running our web application
using **Django**.

Our web application is a form with two fields. We use SQLite database system and we are able to retrieve all the information from our schema
using another view of our app. In the entry fields, we will have basic error handling so the user inputs are valid data.

## Instructions to run web application locally

1.- Download the files that are in this [repository](https://github.com/HenryTorres110/Jr_Data_Analyst_Ex) as a zip file or using a bash terminal. 
For the sake of simplicity we would take the first option as it is the easiest way. You can download the zip file by clicking the green button at the right corner of the code area and select
the **zip file** option.

2.- Once you have your zip file you must unzip it somewhere in your computer´s disk. We **strongly recommend** to do it on the Desktop. Once you decompress your
file, remove any extra parent directory so you only have something like this: Parent_Directory/Luis_Project.

3.- Before going any further you should check that you have any version from *Python 3.9.6* or superior running in your computer. This will increase the chances of preventing
compatibility issues. If you are using a machine that doesn´t have python interpreter, please follow the next link to download the latest version of python: [Download Python Here](https://www.python.org/downloads/).

4.- Now, it is **strongly suggested** that you generate a virtual environment in order to avoid conflicts between requirements of the packages and modules of our application and the ones in your computer. 
To do so please follow the instructions listed [here](https://docs.python.org/3/tutorial/venv.html) and when you are done getting ready to set your virtual environment create and activate your virtual environment in the same path as *Luis_project* so you would have a structure like this one: 

Parent_Directory
- Luis_Project
- Virtual_Env

after doing so, run the following command to install all the requirements we use for this specific project: **pip install -r requirements.txt** (First navigate to Luis_Project/mysite, in that directory is the .txt file). The .txt file is available for you to see what dependencies and versions were necessary to build this project. 

5.- Now that you are all set navigate to the following path using cd in your terminal: (venv) cd Parent_Directory/Luis_Project/mysite. There you will have a python file called *manage.py*, which you will use to run our server. 

6.- Now you will need to run the following command: **python manage.py runserver**, if everything was done correctly you will receive some information that looks like this:

*Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 13, 2024 - 22:47:25
Django version 4.2.10, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK*

You will just need to copy and paste the *development server* (in our example is http://127.0.0.1:8000/) into your favorite browser. You should see a simple form asking for a name and an email along with some text and a button to send the data. 

7.- After you pressed the button you should see another of our views where the data that has been introduced is shown in a list fashion. 

You can inspect any module you wish and even though we are not good enough web designers to make a beautiful CSS, hopefully it meets the fundamental requirements. Thanks in advance.

*If I can count with more time to continue developing the web app with the extra requirements please let me know to begin inmediatly*
