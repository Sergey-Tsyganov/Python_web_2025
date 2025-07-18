from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import SubmitField
from wtforms.fields.simple import EmailField, TextAreaField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    email = EmailField('Почта',validators=[DataRequired('Введите корректный E-mail')])
    password  =PasswordField('Пароль',validators=[DataRequired('Пароль обязателен')])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired('Пароль надо ввести 2 раза')])
    name=StringField('Ваше имя', validators=[DataRequired('Введите имя')])
    about = TextAreaField('напишите про себя')
    submit = SubmitField('Регистрация')

