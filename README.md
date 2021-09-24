# todos-web-app

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style"which are enclosed in brackets [ ] instead of parentheses ( ).
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#tech-stack">Tech Stack</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

A TO-DO full stack web app with user authentication and a SQL database

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

You need to have installed the following:

- git
- python
- pip

### Installation

1. Clone the repo

```sh
git clone https://github.com/ianselley/todos-web-app.git
```

2. cd into that directory named as the repo

```sh
cd todos-web-app
```

3. Create a virtual environment (the last "venv" is the name of the
   virtual env, you can call it whatever you like)

```sh
python -m venv venv
```

4. Activate that new virtual environment

- In windows:

```
.\venv\Scripts\activate
```

- In Linux/Mac:

```sh
source venv/bin/activate
```

5. Install python modules

```sh
pip install -r requirements.txt
```

6. Run main.py

```sh
python main.py
```

Now you just have to go to http://localhost:5000 and you are in the website

<!-- TECH STACK -->

## Tech stack

- [Python 3](https://www.python.org)
- [JavaScript](https://www.javascript.com)
- [SQLite3](https://docs.python.org/3.10/library/sqlite3.html)
- [Flask](https://flask.palletsprojects.com/en/2.0.x)
- [FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Google Material Icons](https://fonts.google.com/icons)
- [Font Awesome](https://fontawesome.com)
- [Google Fonts](https://fonts.google.com)
- [Tailwind](https://tailwindcss.com)
