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

* *Defining a Single To-Do*

Our main components that is stored in our Single To-Do:

1. Description: How do you describe this to-do?
2. Priority: What priority does this to-do have over the rest of your to-dos?
3. Done: Is this to-do done?

Our sample To-Do data structure:

```[json]
todo = {
  "Description": "Finish cooking bolognese",
  "Priority": 4,
  "Done": True,
}
```

The *"Description"* key stores a string describing the current to-do. The *"Priority"* key can take three possible values: *1* for *high*, *2* for *medium*, and *3* for *low* priority. The *"Done"* key holds True when you've completed the to-do and False otherwise.

* *Communicating with the CLI*

1. *todo*: The dictionary holding the information for the current to-do
2. *error*: The return or error code confirming if the current operation was successful or not.

* For our To-Do model controller, we subclassed *NamedTuple* from the typing module as this allows us to create named tuples with type hints for their named fields.

* *Communicate with the Database*

1. *todo_list*: The to-do list you'll write to and read from the database
2. *error*: An integer number representing a return code related to the current database operation.

* *Write the Controller Class, Todoer*

In order to connect our DatabaseHandler logic with our application's CLI, you'll write a class called Todoer. This class will be able to replicate the behaviour similarly to a controller in the Model-View-Controller pattern

Our *Todoer* class uses the *__composition__* OOP design pattern, in which it has a DatabaseHandler component to facilitate direct communication with the to-do database.

## Adding and Listing To-Dos Functionalities

* *Define Unit Tests for Todoer.add()*

On our add functionality of our To-Do CLI application, think of what *'.add()'* method really does:

1. Get a to-do *description* and *priority*
2. Create a dictionary to hold the *to-do information*
3. Read the to-do list from the *database*
4. Append the *new to-do* to the current to-do list
5. Write the *updated to-do list* back to the database.
6. Return the *newly added to-do* along with a return code back to the caller.

* A common practice in TDD is to start with the main functionality of a given method or function. We will start by creating test cases to check if .add() properly adds new to-dos to the database.

* To test .add(), we must be able to create a Todoer instance with a proper JSON file as the target database. In order to provide the file, we will use a pytest *fixture*

### Sample test cases for the .add() functionality

```[python]
(cli_to_do_dev) C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli>py -m pytest --verbose tests/
================================================= test session starts =================================================
platform win32 -- Python 3.9.0, pytest-6.2.4, py-1.11.0, pluggy-0.13.1 -- C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\creyes24\Real-World-Python\CLI_projects\to_do_cli
collected 3 items

tests/test_crtodo.py::test_version PASSED                                                                        [ 33%]
tests/test_crtodo.py::test_add[description0-1-expected0] FAILED                                                  [ 66%]
tests/test_crtodo.py::test_add[description1-2-expected1] FAILED                                                  [100%]

====================================================== FAILURES =======================================================
_________________________________________ test_add[description0-1-expected0] __________________________________________

mock_json_file = WindowsPath('C:/Users/creyes24/AppData/Local/Temp/pytest-of-creyes24/pytest-0/test_add_description0_1_expect0/todo.json')
description = ['get', 'some', 'coffee', 'kick', 'smoothie'], priority = 1
expected = ({'Description': 'Get some Coffee Kick Smoothie.', 'Done': False, 'Priority': 1}, 0)

    @pytest.mark.parametrize(
        "description, priority, expected",
        [
            pytest.param(
                test_data1["description"],
                test_data1["priority"],
                (test_data1["todo"], SUCCESS),
            ),
            pytest.param(
                test_data2["description"],
                test_data2["priority"],
                (test_data2["todo"], SUCCESS),
            ),
        ],
    )
    def test_add(mock_json_file, description, priority, expected):
        todoer = crtodo.Todoer(mock_json_file)
>       assert todoer.add(description, priority) == expected
E       AttributeError: 'Todoer' object has no attribute 'add'

tests\test_crtodo.py:72: AttributeError
_________________________________________ test_add[description1-2-expected1] __________________________________________

mock_json_file = WindowsPath('C:/Users/creyes24/AppData/Local/Temp/pytest-of-creyes24/pytest-0/test_add_description1_2_expect0/todo.json')
description = ['Wash the car'], priority = 2
expected = ({'Description': 'Wash the car.', 'Done': False, 'Priority': 2}, 0)

    @pytest.mark.parametrize(
        "description, priority, expected",
        [
            pytest.param(
                test_data1["description"],
                test_data1["priority"],
                (test_data1["todo"], SUCCESS),
            ),
            pytest.param(
                test_data2["description"],
                test_data2["priority"],
                (test_data2["todo"], SUCCESS),
            ),
        ],
    )
    def test_add(mock_json_file, description, priority, expected):
        todoer = crtodo.Todoer(mock_json_file)
>       assert todoer.add(description, priority) == expected
E       AttributeError: 'Todoer' object has no attribute 'add'

tests\test_crtodo.py:72: AttributeError
=============================================== short test summary info ===============================================
FAILED tests/test_crtodo.py::test_add[description0-1-expected0] - AttributeError: 'Todoer' object has no attribute 'add'
FAILED tests/test_crtodo.py::test_add[description1-2-expected1] - AttributeError: 'Todoer' object has no attribute 'add'
============================================= 2 failed, 1 passed in 0.43s =============================================
```

## Implementing the add CLI Command

* Every time the to-do application runs, it needs to be accessed from the Todoer class and connect the CLI with the database. To accomplish this requirement, we will create a __get_todoer()__ function.

## Implementing the list Command

![list the to-do items in cool blue font!](C:\Users\Clarence Vinzcent\Real-World-Python\Command-Line-Tool-Typer\images\typer_list_command.png "Typer CLI todo list table")

## Implementing the To-Do Completion Functionality

![completing to-do items on our to-do list!](C:\Users\Clarence Vinzcent\Real-World-Python\Command-Line-Tool-Typer\images\typer_complete_command.png "Typer CLI complete todo list items")

## Implementing the Remove To-Dos functionality

### Implementing the __remove__ CLI command

![removing to-do items on our to-do list!]C:\Users\Clarence Vinzcent\Real-World-Python\Command-Line-Tool-Typer\images\typer_remove_command.png "Typer CLI remove todo list items")

### Implementing the __clear__ CLI command

![clearing all to-do items on our to-do list!](C:\Users\Clarence Vinzcent\Real-World-Python\Command-Line-Tool-Typer\images\typer_clear_command.png "Typer CLI clear todo list items")

## Possible feature additions to the minimal To-Do CLI Application

* *Add support for dates and deadlines*
* *Write more unit tests*
* *Packing the application and publishing it to PyPI*
