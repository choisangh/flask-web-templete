from flask import Flask, render_template
from controllers.user_route import user_route

app = Flask(__name__)
app.register_blueprint(user_route)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='8080')
