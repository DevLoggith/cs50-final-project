# CS50 Final Project - SkillSift
This is my submission for the final project of the CS50: Introduction to Computer
Science course by Harvard. 

Inspired by what I wish would have existed when I was starting my journey into
software engineering, I created SkillSift. It's a web app that takes a users job
title and location then scrapes their local job boards, returning a list and
graphs of the most sought after tech skills for their locale.

Reverse engineering the job search and first starting with what skills and knowledge
are most sought after where you live gives you a much more concrete and defined 
direction to go in. It helps you create a solid foundation from the start, catered
to putting you in the best position possible to land your first job as a developer.

## Features

## Technologies Used
- HTML
- CSS
- Bootstrap
- JavaScript
- Google Charts
- Python
- Flask
- Selenium
- Jinja
- APIs
    - Geolocation API (W3C)
    - Nominatum API (reverse geocoding)

## Developer Instructions
### Configuring and running locally
#### Clone repo and create/start virtual environment
After forking the repo to your GitHub profile, run the following commands to clone the project to your local machine and 'cd' into the project folder.
```bash
git clone https://github.com/DevLoggith/cs50-final-project
cd cs50-final-project
```
Once inside the  project folder, create the virtual environment and start it.
```bash
python -m venv venv
python source venv/bin/activate # or venv\Scripts\activate on Windows
```
<hr/>

#### Install dependencies
Once the 'venv' is installed and activated, install the project dependencies by running:
```bash
pip install -r requirements.txt
```
<hr/>

#### Create .env file
In the root of your project folder, create your .env file.
```bash
touch .env
```
Once created, open the file in your code editor and add this key-value pair to the file with your email address within the parentheses:
```
NOMINATIM_USER_AGENT=SkillSift/1.0 (<your_email@domain.com>)
```
Not only will this will keep your email separate from the source code, an email address is needed by Nominatim to keep track of API requests. This info will be sent to Nominatim via the request header when making a call to the API. This provides a way for them to contact you if there is any issues with the program accessing the API. 
<hr/>

#### If you are on a Mac with Apple silicone
For the `undetected_chromedriver` to work properly on any Mac computers using the
M series chips, Rosetta2 needs to be installed. To do this, run the command:
```bash
softwareupdate --install-rosetta --agree-to-license
```
<hr/>
