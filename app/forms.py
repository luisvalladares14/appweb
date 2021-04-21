from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, IntegerField


class LoginForm(Form):
    username = StringField(u'Username', [
    validators.Required(), validators.length(min=4, max=20, message='El username no cumple con los requisitos')
    ])
    password = PasswordField(u'Password', [
    validators.Required(), validators.length(min=8, max=15, message='Contraseña no valida')
    ])
    age = IntegerField(u'Age', [validators.Required(message='Por favor llena este campo')])
