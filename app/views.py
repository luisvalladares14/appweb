from flask import Blueprint
from flask import render_template, request
from .forms import LoginForm

page = Blueprint('page', __name__)


@page.app_errorhandler(404)
def not_founded(error):
       return render_template('errors/404.html', title='ERROR'), 404

@page.route('/productos')
def productos():
    return render_template('productos.html', title='Products')

@page.route('/')
def index():
    return render_template('index.html', title = 'Home')

@page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        print(form.username.data)
        print(form.password.data)
        print(form.age.data)
        print('Nueva sesion creada')
    return render_template('auth/login.html', title='Login', form=form)

@page.route('/historia')
def hist():
    return render_template('historia.html', title='Historia')

@page.route('/log')
def log():
    return render_template('auth/log.html', title='Log')
