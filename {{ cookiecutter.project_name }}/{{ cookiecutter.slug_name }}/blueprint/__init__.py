"""
{{ cookiecutter.slug_name }}
"""
import logging

from flask import Blueprint, render_template


__author__ = "{{ cookiecutter.author }}"
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"


log = logging.getLogger(__name__)


BLUEPRINT = Blueprint('{{ cookiecutter.slug_name }}', __name__,
                      template_folder='templates',
                      static_folder='static')


@BLUEPRINT.route("/")
def root():
    return render_template("default.html", content="It works!")
