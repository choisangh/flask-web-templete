from flask import Flask, render_template
from web_service.views import user_route

app = Flask(__name__)
app.register_blueprint(user_route)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/resgister')
def register():
    return render_template('resgister.html')


if __name__ == '__main__':

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + "dbfile"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.run(host='0.0.0.0', port='8080', debug=True)


