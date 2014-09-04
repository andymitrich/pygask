from application import app
from application import views


app.add_url_rule('/', 'home', view_func=views.home)