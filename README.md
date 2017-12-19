# cookiecutter-flask_site

v0.0.1

[![Build Status](https://travis-ci.org/bnbalsamo/cookiecutter-flask_site.svg?branch=master)](https://travis-ci.org/bnbalsamo/cookiecutter-flask_site)

My cookiecutter template for basic flask sites, and a jumping off point for more complex sites.

# Whats it get me?
- [Github](https://github.com/) integration
- [TravisCI](https://travis-ci.org/) integration
- [Coveralls](https://coveralls.io/) integration
- [Dockerization](https://www.docker.com/)
- A minimal README
- A virtual environment (python >= 3.3)
- A reasonable code template
- Packages for common development tasks
    - [pip](https://pip.pypa.io/en/latest/)
    - [bumpversion](https://github.com/peritus/bumpversion)
    - [wheel](http://pythonwheels.com/)
    - [flake8](http://flake8.pycqa.org/en/latest/)
    - [coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/)
    - [pytest](https://docs.pytest.org/en/latest/)
    - [twine](https://pypi.python.org/pypi/twine)
    - [check-manifest](https://github.com/mgedmin/check-manifest)
- A very minimal wsgi.ini script, if you prefer that route

# Quickstart

- Requirements For These Instructions
    - [Cookiecutter](https://github.com/audreyr/cookiecutter)
    - [Github](https://github.com/) account
    - [TravisCI](https://travis-ci.org/) account
    - [Coveralls](https://coveralls.io/) account
- Steps
    - Create a github repo named $YOUR_PROJECT_NAME
    - Enable repository monitoring on Travis
    - Enable repository monitoring on coveralls
    - ```$ cookiecutter https://github.com/bnbalsamo/cookiecutter-flask_api_template```
    - Fill in the prompts
    - ```$ cd $YOUR_PROJECT_NAME```
    - ```$ source venv/bin/activate```
        - if python < 3.3 create your own venv here
    - ```$ pip install -r requirements_dev.txt```
    - ```$ git init```
    - ```$ git add */.*```
    - ```$ git commit -m "first commit"```
    - ```$ git remote add origin $YOUR_REPO_ADDRESS```
    - ```$ git push -u origin master```
    - Begin developing your site!

# Package Layout
- ```$slug_name/__init__.py``` 
    - Defines the "app" callable and error handling.
- ```$slug_name/blueprint/__init___.py```
    - Defines the application blueprint. Where the majority 
    of the logic for the application resides.
- ```$slug_name/blueprint/exceptions.py```
    - Defines errors/exceptions that will be handled
        by the blueprints errorhandler decorated function.

## Why bother with a blueprint?

For more information about blueprints see [here](http://flask.pocoo.org/docs/0.12/blueprints/).

Formatting the site as a blueprint means that in the future anybody's application callable
can use ```Flask.register_blueprint()``` to run your site in concert with other blueprints,
if required. It also provides a starting point which requires minimal refactoring in the event
that the site begins to become complex enough to warrant implementing multiple blueprints.

# Functionalities

Any of the following can be run off the bat from the project root

* ```./quick_test.sh```: Run tests, generate coverage stats, run flake8
* ```py.test```: Run tests
* ```bumpversion $PART```: Bump the version number of the project
    * ```git push && git push --tags``` to upload/release to git
* ```autopep8 .```: Automatically fix some pep8 errors
* ``` check-manifest .```: Check that your manifest file is correct
    * the ```-c``` option will create one, if it doesn't exist
    * the ```-u``` option will update an existing file, or create one


# Running Your Application Server
There are a multitude of ways to run a WSGI application in both development and production
environments.

See [here](flask.pocoo.org/docs/latest/deploying/) for the Flask documentation on the topic.

This cookiecutter is unopinionated, it doesn't include any of the standalone python wsgi
containers, however both a ```$yourapplication.wsgi``` file and a ```wsgi.ini``` are included
into the repositories root in order to facilitate the use of different deployments if required.

By default, the Dockerization is based on [bnbalsamo/flask_stack](https://hub.docker.com/r/bnbalsamo/flask_stack/) ([github](https://github.com/bnbalsamo/docker-flask_stack)), which utilizes a gunicorn server bound to a filesystem socket being served via an nginx proxy.

## Uploading to pypi

I'll not hazard a short answer here, as there are too many options.

[This](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) blog
entry provides a good breakdown of uploading a package to pypi. All of the referenced
tools should be installed by a ```pip -r requirements_dev.txt``` in your project
virtualenv.



Inspiration (and some code) taken from [audreyr's pypackage template](https://github.com/audreyr/cookiecutter-pypackage), this cookiecutter is based heavily on the one I originally created for Flask APIs, located [here](https://github.com/bnbalsamo/cookiecutter-flask_api_template).

For a more general template for any python package see [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage)
