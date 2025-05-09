# Notes FastAPI Tutorial
A simple RESTful API built with FastAPI for managing notes, using MySQL and SQLAlchemy. This project demonstrates CRUD operations (Create, Read, Update, Delete) with pagination and data validation.

## Installation
* git clone https://github.com/nghiaphunng18/fastapi-note-crud-example
* cd fastapi-note-crud-example
* pip install -r requirements.txt
* set up MySQL
  * CREATE DATABASE notes_fastapi_tutorial;
  * CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
* python app/main.py