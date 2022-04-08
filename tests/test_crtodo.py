# Testing script for our CR To-Do Application
# tests/test_crtodo.py

import json

import pytest
from typer.testing import CliRunner

from crtodo import (
    __app_name__, 
    __version__, 
    cli,
    DB_READ_ERROR,
    SUCCESS,
    crtodo
)

# ======================= Initializing Test Data Variables
test_data1 = {
    "description": ["get", "some", "coffee", "kick", "smoothie"],
    "priority": 1,
    "todo": {
        "Description": "Get some Coffee Kick Smoothie.",
        "Priority": 1,
        "Done": False,
    },
}
test_data2 = {
    "description": ["Wash the car"],
    "priority": 2,
    "todo": {
        "Description": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}

# ========================= Initialize testing environment
runner = CliRunner()

# ========================== Function Test Definitions
def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
    
@pytest.fixture
def mock_json_file(tmp_path):
    todo = [{"Description": "Get some Coffee Kick Smoothie.", "Priority": 1, "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file

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
    assert todoer.add(description, priority) == expected
    read = todoer._db_handler.read_todos()
    assert len(read.todo_list) == 2
