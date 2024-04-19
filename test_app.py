import pytest
from app import app, tasks

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_task(client):
    # Add a new task
    client.post('/add', data={'title': 'Test Task', 'description': 'Description for Test Task'})
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Test Task'
    assert tasks[0]['description'] == 'Description for Test Task'

def test_edit_task(client):
    # Add a new task
    client.post('/add', data={'title': 'Test Task', 'description': 'Description for Test Task'})
    assert len(tasks) == 1

    # Edit the task
    client.post('/edit/0', data={'title': 'Updated Task', 'description': 'Updated description'})
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Updated Task'
    assert tasks[0]['description'] == 'Updated description'

def test_delete_task(client):
    # Add two tasks
    client.post('/add', data={'title': 'Task 1', 'description': 'Description for Task 1'})
    client.post('/add', data={'title': 'Task 2', 'description': 'Description for Task 2'})
    assert len(tasks) == 2

    # Delete the first task
    client.post('/delete/0')
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Task 2'
