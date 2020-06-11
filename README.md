[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Social+, A Social Media App Inspired By Instagram
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/Naereen/StrapDown.js)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# This project was created for learning purposes only, If you wich to contribute you are welcome. 

## Requirements 

This app is using django as backend and django-channels and ajax for front-end for real time communications wich is a good approach without any 3rd parties applications like pusher. 

- For the forms i did include bootstrap but it was modified with a custom css file under the name "style.css".
- For the real time notification in this app an old websocket script was deployed in the front-end, however in the back-end django-channels is working side by side with django-signals and redis server. The reason why i use an old websocket script from django-channels early release is for simplicity as this app get better and better the script will be remover and replaced with a better solution like sockets
- For the chat system websockets was used as front-end receiver and django-channels as the back-end engine.

## How To Setup The Project?
**MacOSX**
> pip install virtualenv

Next navigate to project folder and run
> source bin/activate

Next Install and run redis server with homebrew
> brew install redis
> redis-server

Last Step open a new terminal tap and run the server
> cd root_dir
> python manage.py runserver
The project will be served on: localhost:8000

- You can use alternative options depending on your OS(**Windoms**, **Linux** ..) as long it works.

## Features
- Real time notifications.
- Real time chat system.
- Create, delete, bookmark and like posts.
- Create, update user information including username, email and profile picture.
- Crop profile pictures(server side).
- Website dynamic navigation.
- Easy code structure.
- Easy login, logout and register system.
- Good level of security against hackers (sql injenctions, CSRF, XSS and more).
- Powered by django framework.
- No Front-end frameworks (like react or vuejs).

## WARNING
It is important to run the following commands above in order or the application may not work properly

If you have any question, feel free to contact me on
![Tweeting](https://img.shields.io/twitter/url/http/shields.io.svg?style=social) @riade_b
