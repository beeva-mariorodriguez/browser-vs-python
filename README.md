# control google chrome from python

## requirements:
* run google chrome full screen or kiosk mode
* allow webcam access to ``http://localhost:8080``
* avoid chrome popups, menus ...

## problems
* restore session popup
* multiple tabs when running multiple times

## instructions (ubuntu)
* install chromedriver (``sudo apt install chromium-chromedriver``)
* ``pip3 install -r requirements.txt``
* ``./controlchrome.py``
