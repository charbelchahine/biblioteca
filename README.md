# 343-F18
Software Architecture &amp; Design Project.

# Team Members
- Nomaan Ahmed ID#27284187
- Mathew Plouffe ID#27532733
- Peter Irshad ID#40029852
- Luca Popesco ID#27742339
- Gabriel Valentini ID#27549407
- Charbel Chahine ID#40001788
- James Bergeron ID#26293328
- Valentin Perrot ID#27321775

# Setting up your local dev environment

* Install Homebrew
* Install python 2.7, python >=3.6, and mysql with homebrew (`brew install python@2`, `brew install python`, `brew install mysql`)
* Using pip, install virtualenv: `pip3 install virtualenv`
* Clone this repository
* inside the repo root, run `virtualenv env` then `source env/bin/activate`
* Run `pip3 install django`, and `pip3 install mysqlclient`
* Go to https://www.miniwebtool.com/django-secret-key-generator/ and generate a new secret
* Copy soen343\_project/settings.py.template to soen343\_project/settings.py
* Open soen343\_project/settings.py. Paste your new secret after "SECRET\_KEY="
* Set your DB username and password under the database section
* From the root directory of the project, run `python manage.py check` to ensure everything is correct
* Run `python3 manage.py runserver`. Your server is now running on localhost:8000
