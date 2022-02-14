from flask import Flask
import sqlalchemy

from flask import (
    make_response,
    redirect,
    render_template,
    escape,
    abort,
    request,
    session,
    url_for,
    flash,
)
from datetime import datetime, timedelta

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(_):
    return render_template("zaglushka.html"), 404


@app.route('/')
def mainpage():
    return render_template('mainpage.html')


@app.route('/mainpage.html')
def mainpage1():
    return render_template('mainpage.html')


@app.route('/catalogpage.html')
def catalogpage():
    return render_template('catalogpage.html')


@app.route('/zaglushka.html')
def zaglushkapage():
    return render_template('zaglushka.html')


@app.route('/loginpage.html')
def loginpage():
    return render_template('loginpage.html')


@app.route('/infopage.html')
def infopage():
    return render_template('infopage.html')

@app.route('/good/<good>')
def typepage(good):
    t = good
    return render_template('good.html', item = t)


if __name__ == '__main__':
    app.run(debug=True)
