from flask import Flask
from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder import AppBuilder, SQLA
from api.help import HelpApi

app = Flask(__name__)
db = SQLA(app)

appbuilder = AppBuilder(app, db.session)
appbuilder.add_api(HelpApi)

app.run(host="0.0.0.0", port=5555, debug=True)

print('Try to open URL http://127.0.0.1:5555/api/v1/helpapi')