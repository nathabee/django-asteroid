 
# Django Asteroid Project

![Work In Progress](https://img.shields.io/badge/status-work%20in%20progress-yellow)



## Overview

This project is a web-based game where players control a rocket to dodge asteroids and compete for high scores on a leaderboard. It integrates multiple technologies including Python, Django, JavaScript, a web server, and a database.

## ⚠️ Work In Progress

**This project is currently under development and is not yet stable.**

We are actively working on new features and improvements. Please be aware of the following:

- **Features**: Not all planned features are implemented yet.
- **Stability**: There may be bugs and incomplete functionalities.
- **Documentation**: The documentation is a work in progress and may not cover all aspects of the project.



## Project Structure

- `asteroid_game/`: Django project directory.
- `game/`: Django app directory containing models, views, and migrations.
- `db_scripts/`: SQL scripts for setting up and seeding the database.
- `frontend/`: Placeholder for frontend code if using a separate framework (e.g., React).
- `static/`: Static files (CSS, JavaScript, images) used in templates.
- `templates/`: HTML templates used by Django views.
- `tools/`: some tools to manage the project



## 🛠️ Current Status

- Initial setup complete
- Basic functionality implemented
- Ongoing development and testing

## 📈 Future Plans

- Complete feature set
- Extensive testing
- Enhanced documentation

## 🚀 Getting Started

To get started with this project, follow the instructions in the setup files.

 

0. project will be initialized from github (take the code from git in tools/setup_project_server.sh)

chmod +x setup_project_server.sh
./setup_project_server.sh
cd django_asteroid_project
chmod +x tools/*.sh



1. installation from apache, python, mysql :
 
cd django_asteroid_project
tools/setup_environment.sh   
=> by installing the database :  dbname astrodb, user astro


2. Set up your Python virtual environment and install dependencies from `requirements.txt`. it will also configure django app

cd django_asteroid_project
tools/setup_django.sh 


3. Run the database scripts in `db_scripts/` to initialize the database.

4. Start the Django development server using `python manage.py runserver`.


 


## 📢 Contributing

Feel free to contribute by submitting issues or pull requests. Your feedback is appreciated!

## 📧 Contact

For any inquiries, please contact [nathabee123@gmail.com](mailto:nathabee123@gmail.com).

---

**Thank you for your patience and understanding!**



## License

MIT License

Copyright (c) 2024 Natha Bee
