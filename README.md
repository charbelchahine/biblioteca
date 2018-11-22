# 343-F18
Software Architecture &amp; Design Project.

Live website can be found at http://soen343.live

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

### For Mac:
* Install Homebrew.
* Open Terminal.
* Install Python 2.7, Python >=3.6, and MySQL with Homebrew (`brew install python@2`, `brew install python`, `brew install mysql`). Pip (Python package manager) will come installed with Python.
* Using pip, install virtualenv: `pip3 install virtualenv`.
* Clone this repository wherever you'd like on your machine.
* `cd` to the repo root (/343-F18/) and create a virtual environment named "env" using `virtualenv env`. The reason for this is to isolate all the Python packages inside this virtual environment.
* Activate the virtual environment using `source env/bin/activate` (again, must be inside the repo root).
* You are now working inside the virtual environment (`(env)` on the left side). You will never need to re-create the virtual environment again, but if you close the Command Prompt, you'll need to activate it again to access it. Do so by navigating to the repo root and running `source env/bin/activate`.
* **Within the virtual environment**, install Django and MySQL using `pip3 install django  mysqlclient pycontracts`
* Go to https://www.miniwebtool.com/django-secret-key-generator/ and generate a new secret key.
* Copy, from the repo, /soen343_project/settings.py.template to /soen343_project/settings.py
* Open /soen343_project/settings.py. Paste your new secret after `"SECRET\_KEY="`.
* Set your DB username and password (provided to you directly) under the database section.
* From the repo root, run `python manage.py check` to ensure everything is correct
* Run `python3 manage.py runserver`. Your server is now running on localhost:8000 in your browser.

### For Windows:
* Install Python 2.7, Python 3.7 and MySQL via their installer from their respective websites. Pip (Python package manager) will come installed with Python.
* Using pip, install virtualenv: `pip3 install virtualenvwrapper-win`.
* Clone this repository wherever you'd like on your machine.
* Open Command Prompt as an administrator.
* `cd` to the repo root (/343-F18/) and create a virtual environment named "env" using `virtualenv env`. The reason for this is to isolate all the Python packages inside this virtual environment.
* Activate the virtual environment using `workon env` (again, must be inside the repo root).
* You are now working inside the virtual environment (`(env)` on the left side). You will never need to re-create the virtual environment again, but if you close the Command Prompt, you'll need to activate it again to access it. Do so by navigating to the repo root and running `workon env`.
* **Within the virtual environment**, install Django and MySQL using `pip3 install django mysqlclient pycontracts`.
* Go to https://www.miniwebtool.com/django-secret-key-generator/ and generate a new secret key.
* Copy, from the repo, /soen343_project/settings.py.template to /soen343_project/settings.py
* Open /soen343_project/settings.py. Paste your new secret after `"SECRET\_KEY="`.
* Set your DB username and password (provided to you directly) under the database section.
* From the repo root, run `python manage.py check` to ensure everything is correct
* Run `python3 manage.py runserver`. Your server is now running on localhost:8000 in your browser.

# Making changes to the styling

### For Mac:
* Make sure you’re running an up-to-date version of ruby: `ruby -v`.
* If number is lower than 2.0.0 then update: `sudo gem install ruby`.
* Install SASS `sudo gem install sass`.

### For Windows:
* Go to http://rubyinstaller.org/downloads/ and download the appropriate version.
* Be sure to select “Add Ruby executables to your PATH” in the installer.
* Confirm that Ruby is installed: `ruby -v`.
* Install SASS `gem install sass`.

### Compilation:
* Open a new terminal window and `cd` to the repo root (/343-F18/).
* Run `sass --watch biblioteca/static/styling/scss/index.scss:biblioteca/static/styling/css/index.css`.
* You can now make changes to any `.scss` file.
