from flask import Blueprint

user_route = Blueprint('user', __name__, url_prefix="/user")


@user_route.route('/register')
def register():
    return "회원가입"