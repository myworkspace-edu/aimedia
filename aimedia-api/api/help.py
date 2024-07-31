from flask_appbuilder.api import BaseApi, expose

class HelpApi(BaseApi):
    @expose('/')
    def help(self):
        return self.response(200, message="Go to 'https://myworkspace.vn/portal/site/intern-ai'")