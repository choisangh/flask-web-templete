from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

user_route = Blueprint('user', __name__, url_prefix="/user")


@user_route.route('/register')
def register():
    return "회원가입"