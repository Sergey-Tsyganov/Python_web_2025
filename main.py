# Введение во Flask
# MVC-(Model View Controller)
# GET - запрашивает данные (read)
# POST - отправляет данные на сервер (submit)
# PUT - заменяет всё на сервере из контекста запроса ("заменить")
# DELETE - удаляет указанные данные ("удалить")
# PATCH - частичное изменение данных
# JINJA - переменные, условия, циклы и т.д.
# ORM  - Object relational mapping
# DBeaver - универсальный софт для работы с БД
import os.path

from openpyxl.styles.builtins import title

from forms.loginform import LoginForm
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename
import sqlite3
from data import db_session
from data.users import User
from data.news import News
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'zip', 'jpg', 'png']
debug = False


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# обработчик 404 ошибки
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', title='не найдено')



@app.route('/')
@app.route('/index')
def index():
    params = {}
    params['user'] = 'слушатель'
    params['title'] = 'приветствие'
    params['weather'] = 'Сегодня хорошая погода'
    return render_template('index.html',
                           **params)


@app.route('/about')
def about():
    return render_template('about.html',
                           title='Про нас')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html',
                           title='Свяжитесь с нами')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return 'Форма отправлена'
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)


@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='images/python.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Картинка Питона</title>
            </head>
            <body>
                <img src="{url_for('static', filename='images/python.jpg')}" alt="Python">
            </body>
            </html>
    """


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()


# Так делать мы не будем
# x = 5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)

# <string> - по умолчанию строка
# <int:number> - целое
# <float:number> - дес. дробь
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX-формате)
@app.route('/greeting/<string:user>/<int:id_num>')
def greeting(user, id_num):
    return f'Привет, {user} c id={id_num}'


@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return f'<a href="http://localhost:5000/get-user/{id_num}">ФИО</a>'
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    # print(result)
    name, city = result
    cur.close()
    con.close()
    return f'''<table border="1">
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>'''


@app.route('/form-test', methods=['POST', 'GET'])
def form_test():
    if request.method == 'GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form)
        return 'Форма успешно отправлена'


@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    if request.method == 'GET':
        with open('upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        # print(request.files)
        if 'file' not in request.files:
            return 'Файл не был выбран!!!'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не был выбран!!!'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} успешно загружен!'
    return "Ошибка загрузки"


@app.route('/numbers/')
@app.route('/numbers/<int:num>')
def odd_even(num=None):
    if num is None:
        return render_template('numbers.html',
                               title='Нет числа', number='')
    return render_template('numbers.html',
                           title='Чет-нечёт', number=num)


@app.route('/deals')
def printlist():
    deal = ['Помыть посуду', 'Выгулять собаку',
            'Снять показания счётчика', 'Сходить в магазин']
    return render_template('printlist.html', deals=deal)


@app.route('/queue')
def queue():
    # loop.index - номер итерации, начиная с 1
    # loop.index0 - номер итерации, начиная с 0
    # loop.first - True, если первая итерация
    # loop.last - True, если последняя итерация
    return render_template('vars.html', title='Стоим в очереди')


# вывод всех публичных новостей
@app.route('/news')
def news():
    db_sess = db_session.create_session()
    all_news = db_sess.query(News).filter(News.is_private != True).all()
    print(all_news)
    return render_template('news.html',totle='Новости', news =all_news)




if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='127.0.0.1', port=5000, debug=debug)
#     #user = User()
#     db_sess = db_session.create_session()
#   #  first = db_sess.query(User).first()
#   #  first = db_sess.query(User).all()
#   #  first = db_sess.query(User).filter(User.id>'1').all()
# # вылавливаем сзапись и меняем ее
#     #user = db_sess.query(User).filter(User.id ==2).first()
#     #user.set_username ('Васек')
#     #user = db_sess.query(User).filter(User.id == 4).delete()
#     # user.name = 'Sergey4'
#     # user.about = 'Какие то данные'
#     # user.email = 'tsysn3@gmail.com'
#     # db_sess = db_session.create_session()
#     # db_sess.add(user)
#     user = db_sess.query(User).filter(User.id == 1).first()
#
#     news = News(title = 'First New', content = 'New Conternt', user_id = user.id, is_private = False)
#
#     print(news.content)
#     #user.name = 'Sergey4'
#     #news.title = 'Новая новость'
#     #news.content = 'Что то'
#     #news.user_id = '1'
#     # db_sess = db_session.create_session()
#     db_sess.add(news)
#     user = db_sess.query(User).filter(User.id == 1).first()
#     news = News(title='Second New', content='Second Conternt', user_id=user.id, is_private=False)
#     db_sess.add(news)
#     for news in user.news:
#         print(news.content)
#     db_sess.commit()
#     #print(first)
