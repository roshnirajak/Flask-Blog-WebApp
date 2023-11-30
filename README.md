# My First Blog Web App

![Web App Screenshot](/venv/home.png)
Other images are at the bottom of this documentation

## Introduction

This is my first web app, a simple personal blog application built using Flask and MySQL. It allows user to post, edit, and delete blog posts, and also includes an admin login system for managing content.

## Features

- **User-friendly Interface**: An intuitive and easy-to-navigate web interface for reading and managing blog posts.

<!-- - **User Registration**: Users can register accounts to create and manage their own blog posts. -->

- **Admin Login**: Admins have special privileges for managing all blog posts, including editing and deleting any post.

- **MySQL Database**: Data is stored in a MySQL database using SQLAlchemy, ensuring efficient data retrieval and storage.

- **CRUD Operations**: Users can Create, Read, Update, and Delete (CRUD) blog posts.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- MySQL
- Other necessary libraries (check `requirements.txt`)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/roshnirajak/Flask-Blog-WebApp.git
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a MySQL database and update the database configuration in `config.py` with your database details.

4. Run the application:

   ```bash
   python app.py
   ```

5. Access the web app in your browser at `http://localhost:5000`.

## Usage

1. Log in as an admin.
2. Create, edit, or delete your blog posts as needed.
3. Admins can manage blog posts.


## Acknowledgments

- Thanks to the Flask and SQLAlchemy communities for their excellent documentation and support.

---
View Post Page
![Web App Post Screenshot](/venv/post.png)
Admin Panel
![Web App Dashboard Screenshot](/venv/dashboard.png)
Edit Post Page
![Web App Edit Page Screenshot](/venv/edit.png)
Admin Login
![Web App Login Screenshot](/venv/login.png)
