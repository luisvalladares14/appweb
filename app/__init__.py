from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL
from flask import render_template, request

bootstrap = Bootstrap()
csrf = CSRFProtect()
app = Flask(__name__)
db = MySQL(app)

from .views import page

def create_app(config):

    csrf.init_app(app)
    app.config.from_object(config)
    bootstrap.init_app(app)
    app.register_blueprint(page)
    return app



@page.route('/libros')
def listar_libros():
    try:
        cursor= db.connection.cursor()
        sql='SELECT isbn, titulo, anoedicion FROM libro ORDER BY titulo ASC'
        cursor.execute(sql)
        data=cursor.fetchall()
        data = {
            'libros':data
        }
        #return 'Ok. Número de libros = {0}'.format(len(data))
        return render_template('libros.html', data=data, title='libros')
    except Exception as ex:
        raise Exception(ex)
