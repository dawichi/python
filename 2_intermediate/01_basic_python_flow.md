## Python virtual environments

```bash
$ mkdir new_folder
$ cd new_folder
$ git init

# py -module venv 'folder_name'
(master) $ py -m venv venv

(master) $ source venv/bin/activate # Linux / MacOS
(master) $ .\venv\Scripts\activate # Windows

(venv) (master) $ ...
# Now your current instance of terminal is working with the python virtual environment!

(venv)(master) $ deactivate # to exit the environment

# Is also recommended to generate an alias to avoid type the activation route every time, as:
$ alias avenv = source venv/bin/activate
```



## Common external python modules

````bash
# PIP - Package Installer for Python
Common external packages:
    * Requests
    * BeautifulSoup4 
    * Pandas
    * Numpy
    * Pytest
````



## Workflow with dependencies

````bash
$ pip install [package]				# Install dependencies
$ pip freeze						# See our installed dependencies
$ pip freeze > requirements.txt		# Save our dependencies in the txt file
$ pip install -r requirements.txt	# Install the dependencies of the file
````



## Alternative: anaconda

````bash
# Python distro specifically focused in data science (not backend or cybersecurity!)
# Install: https://www.anaconda.com/products/individual


````


## List & dictionary comprehensions

````py

# [ element for element in iterable if condition ]
[ i**2 for i in range(1, 101) if i % 3 != 0 ]

# { key : value for value in iterable if condition }
{ i: i**2 for i in range(1, 101) if i % 3 != 0 }

````

