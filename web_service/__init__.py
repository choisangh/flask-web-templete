from flask import Flask
from flask import render_template
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    print('run: create_app()')
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'test'
    app.config['SESSION_COOKIE_NAME'] = 'tomproject'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dndo159753!@localhost/test?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    """DB INIT"""
    db.init_app(app)

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)


    # 개발자 모드에서 캐시 유효기간 1초 처리
    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
    """ROUTES INIT """
    from web_service.views import base_route
    from web_service.views import auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    """CSRF INIT"""
    csrf.init_app(app)

    @app.errorhandler(404)
    def page_404(error):
        return render_template("404.html"), 404

    return app
