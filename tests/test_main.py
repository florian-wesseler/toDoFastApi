import unittest
from unittest.mock import patch
from app import main, schema


class TestTodos(unittest.TestCase):

    @patch("app.service.get_toDoItems")
    def test_read_todos_success(self, mock_get_toDoItems):
        mock_get_toDoItems.return_value = [
            schema.ToDoItem(id=1, title="Test Todo 1", done=False),
            schema.ToDoItem(id=2, title="Test Todo 2", done=True),
        ]

        response = main.read_todos(mock_get_toDoItems)

        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response, mock_get_toDoItems.return_value)
        assert response[1].done

    @patch("app.service.get_toDoItems")
    def test_read_one_todo_success(self, mock_get_toDoItems):
        mock_get_toDoItems.return_value = schema.ToDoItem(id=1, title="Test Todo", done=False)

        response = main.read_todos(mock_get_toDoItems)

        assert response.title == "Test Todo"
        assert not response.done
