# control google chrome from python

## requirements:
* run google chrome full screen or kiosk mode
* allow webcam access to ``http://localhost:8080``
* avoid chrome popups, menus ...

## problems
* restore session popup
* multiple tabs when running multiple times

## instructions
* download [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.38/) and copy it to /usr/local/bin
* ``pip3 install -r requirements.txt``
* ``pip3 ./controlchrome.py``
