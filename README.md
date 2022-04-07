# Python Typer CLI tutorial by @Real Python

* Building a Real-world application by building a To-Do application on the command-line interface using the *Typer* library.

* In this project, we will be able to learn how to:

1. Build a functional *to-do application* with a *Typer CLI* in Python
2. Use Typer to add *commands*, *arguments*, and *options* to your to-do app
3. Test your Python to-do application with Typer's *CliRunner* and *Pytest*

* We will also be able to practice our skills related to processing *JSON files* by using Python's JSON module and managing *configuration files* with Python's __configparser__ module.

## Project Overview

* Helpful commands and options that the user's of this CLI will be able to perform:

* *-v* or *--version* shows the current version and exits the application
* *--help* shows the global help message for the entire application

* Here are other important options for the to-do application that the user can be able to accomplish:

| Command          | Description                                          |
|------------------|------------------------------------------------------|
| init             | Initializes the application's to-do database         |
| add DESCRIPTION  | Adds a new to-do to the database with a description  |
| list             | Lists all the to-dos in the database                 |
| complete TODO_ID | Lists all the to-dos in the database                 |
| complete TODO_ID | Completes a to-do by setting it as done using its ID |
| remove TODO_ID   | Removes a to-do from the database using its ID       |
| clear            | Removes all the to-dos by clearing the database      |

* Here are the following tasks that we need to accomplish in order to build a Minimum Viable Product (MVP) for our users:

1. Build a *command-line interface* capable of taking and processing commands, options and arguments.
2. Select an appropriate *data type* to represent your to-dos
3. Implement a way to *persistenly store* your to-do list
4. Define a way to *connect* that user interface with the to-do data

* In the following tasks that we have stated above, we have taken into consideration a very well-known architectural pattern known as the *Model-View-Controller* design.

* In this pattern, the *model* takes care of the data, the *view* deals with the user interface, and the *controller* connects both ends to make the application work.

* Using this pattern in this CLI To-Do application and projects provides *separation of concerns (SOC)*, in which it is making different parts of your code deal with specific concepts independently.

## The software stack to be used in the CLI To-Do Application

1. [*Typer*](https://github.com/tiangolo/typer) library to build the to-do application's CLI
2. *Named tuples* and *dictionaries* to handle the to-do data
3. Python's *json* module to manage persistent data storage
4. Using *configparser* module from the Python standard library to handle the application's initial settings in a configuration file.
5. Using *pytest* testing framework to test our CLI application

## Setting-up the Working Environment

```[python]
(cli_to_do_dev) C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli>
```

## Defining our Project Layout

| Command         | Description                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------|
| __init__.py     | Enables our to_do_cli/ to be a Python package                                                        |
| __main__.py     | Provides an entry-point script to run the app from the package using the python -m to_do_cli command |
| cli.py          | Provides the Typer command-line interface for the application                                        |
| config.py       | Contains code to handle the application's configuration file                                         |
| database.py     | Contains code to handle the application's to-do database                                             |
| todo_connect.py | Provides code to connect the CLI with the to-do database                                             |

* We will also be creating a tests/ directory containing a __init__.py to turn also our test directory into a package and test_crtodo.py file to hold unit testing for the CLI To-Do application.

## Application Layout Structure


to_do_cli/
│
├── crtodo/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config.py
│   ├── database.py
│   └── todo_connect.py
│
├── tests/
│   ├── __init__.py
│   └── test_crtodo.py
│
├── README.md
└── requirements.txt

## Initial Look for our CLI To-Do application

```[python]
(cli_to_do_dev) C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli>py -m crtodo -v
crtodo v0.1.0

(cli_to_do_dev) C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli>py -m crtodo --help
Usage: crtodo [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.
```

## Setting up Initial CLI Tests with pytest

* Typer class that suits well with testing CLI application -> CliRunner

* *NOTE*: Always type in the flag 'py -m crtodo' in order to run your module

```[python]
(cli_to_do_dev) C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli>py -m pytest --verbose tests/
================================================= test session starts =================================================
platform win32 -- Python 3.9.0, pytest-6.2.4, py-1.11.0, pluggy-0.13.1 -- C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli
collected 1 item

tests/test_crtodo.py::test_version PASSED                                                                        [100%]

================================================== 1 passed in 0.07s ==================================================
```

## Preparing the To-Do Database for Use

* Setting up the directory path for our configuration file to store our database data objects.
* In order for our database to be ready for use, we need to setup two things:

1. We need a way to retrieve the database file path from the application's configuration file.
2. We need to initialize the database to hold JSON content.

## Implementing the init CLI Command

```[python]
(cli_to_do_dev) C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli>py -m crtodo init
to-do database location? [C:\Users\creyes24\.creyes24_todo.json]: C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli\._todo.json
The to-do database is C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli\._todo.json
```

## Setting up the To-Do App Back End