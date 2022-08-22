# DTS_PMS
DTS Project Management System

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django?color=%23386e9d&label=Python&logo=python&logoColor=%23ffcf3f)
![GitHub repo size](https://img.shields.io/github/repo-size/KyleAndrey/DTS_PMS?label=Size)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/KyleAndrey/DTS_PMS/main?color=%230f3e2e&logo=git&logoColor=white)
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FKyleAndrey%2FDTS_PMS&label=Visitors&countColor=%23263759&style=flat)

Project Management System for Electronics and Telecommunication Parts and Equipment Retailing Company. A system with which the current business flow can be integrated, automating record tracking and reducing time-consuming tasks. The objective is to eliminate discrepancies and ensure maximum efficiency.

## Deployed Version
![Website](https://img.shields.io/website?down_message=Offline&label=Website&up_message=Online&url=https%3A%2F%2Fdtsmgmtsystem.ml%2F)

Be sure to check if the status is **Online** before visiting the website. You may need to create an account first and wait for Administrator approval. (https://dtsmgmtsystem.ml)

## Setup

The method of setting up a local version of the system can be broken down into two different parts:

### Initial Setup

1) Download the .zip file on the main page of the GitHub and extract the .zip file to your desired location.
2) Once extracted, open [Visual Studio Code Terminal](https://code.visualstudio.com/docs/terminal/basics) (or [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-5.1)).
3) On the prompt, change to the DTS_ManagementSystem directory:
  e.g. - `cd C:\Users\Username\Downloads\DTS_ManagementSystem`
4) Next, to create a virtual environment and install dependencies (you can also create a requirements file from here), enter in the following:
  e.g. - `python env.py`
5) After building a virtual environment, you can activate it using:
  e.g. - `env/scripts/activate.ps1`
6) Now, you will need to install [XAMPP](https://www.apachefriends.org/download.html) to easily access and manage **MySQL** database using **phpMyAdmin**.
7) Open XAMPP Control Panel then start **Apache** and **MySQL** modules.
8) Click Admin on **MySQL**. A **phpMyAdmin** tab should pop up.
9) Create a new database and name it **`dts`**.
10) Go to the SQL tab then paste the following before pressing Go:
  e.g. - `GRANT ALL PRIVILEGES ON dts.* TO 'root'@'localhost';`
11) Next, open the Import tab then upload the .sql file within the .zip that you have extracted on the first step. Leave everything as default and click Go.
12) Finally, you can go back to the terminal and run the local server:
  e.g. - `python manage.py runserver`

> :bulb: **Tip:** Type in `deactivate` to exit out of the virtual environment.

> :memo: **Note:** You may need to have [Virtualenv](https://pypi.org/project/virtualenv) installed in order for the virtual environment creation to work properly.

### Succeeding Setups

1) The steps here would vary depending on which part you intend to update.
2) To update the source code, you should refer to steps 2-4 from the Initial Setup.
3) Should you plan to update the database, you could refer to step 11 from the Initial Setup.
4) To access the system, you will need to create a superuser (do not forget to activate virtual environment first):
  e.g. - `python manage.py createsuperuser`
5) You will then have to access the `/admin` by typing it on the url.
6) From there you must assign Administrator as the Account Type of the superuser that you have just created.

> :memo: **Note:** You must use the same database name indicated on the settings.py to avoid getting an `Unknown database` error.

## DTS Folder, system Folder, and env.py

There are 3 things within the DTS_ManagementSystem directory that you should take note of.

- **`DTS Folder`** -> The project folder which contains the settings.py, urls.py and other files that define a **Django** project. There should only be one project folder inside a certain project.

- **`system Folder`** -> An app folder which contains the files you will be working with the most. There can be multiple of these app folders in a project, each should have a different name and must be referenced in the settings.py.

- **`env.py`** -> A script that I have created to make virtual environment management easier. It needs to be on the same folder with req.py in order to function properly.
