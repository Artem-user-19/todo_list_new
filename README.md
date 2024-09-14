This is a Django-based todo list web application that allows users to manage tasks efficiently. The application provides a user-friendly interface to add, update, delete, and mark tasks as complete. Additionally, it supports task tagging, enabling users to categorize their tasks by themes.

## Features

- **Task Management:**
  - Add new tasks with content, creation datetime, and optional deadline.
  - Mark tasks as complete or undo the completion status.
  - Edit and delete tasks.
  - Tasks are displayed from newest to oldest, with incomplete tasks shown first.

- **Tagging:**
  - Assign multiple tags to tasks.
  - Manage tags (add, edit, and delete tags).
  - View all tags on a dedicated tag list page.

- **Responsive UI:**
  - Sidebar navigation for quick access to the home page and tag list page.
  - Bootstrap-styled interface for a modern look and feel.

## Installation

### Prerequisites
- Python 3.10+
- Django 5.1+
- Git

### Steps to Set Up the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-list-project.git
   enter in code redactor
   write python manage.py migrate
   than python manage.py runserver
