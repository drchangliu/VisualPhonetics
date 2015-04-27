# Visual Phonetics
Vowel Visualization Web Application
===================================

This is still under active development. Stay tuned for improvements!

### Installation

To facilitate development, we suggest setting up [virtualenvs](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Use pip to install!

    pip install -r requirements.txt

This project was developed using Python 2.7

### Usage

After installing the requirements, you can start the server by issuing

`python manage.py runserver portnumber`. It defaults to port 8000.

A superuser can be created with `python manage.py createsuperuser`.

Superusers can access `/admin/`.

To deploy locally, change `VowelCat.settings.DEPLOY` to `False`; conversely, set it to `True` to deploy to Heroku.

### Changelog

##### 0.0.1

+ Added documentation.

### To Do

* Improve User model

### Questions & Support

If you have any questions, bugs, or suggestions, please
report them via Github Issues. We'd love to hear your feedback and ideas!

### Contributing
This is an open source project and we love involvement from the community! Hit us up with pull requests and issues.
