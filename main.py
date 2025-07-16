# введение во Flask
#MVC - model view controller
# get - запрашивает данные не меняя состояния сервера
# post - отправляет данные на сервер(submit)
# PUT - принулительно заменяет все на сервере из контекста запроса
# Delete - удаляет указанные данные
# patch  - частичное изменение данных
import sqlite3
from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')

def index():
    return 'Привет ,Flask'

@app.route('/about')
def about():
#    print('Вызвана функция about')
    return 'О нас'

@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)

@app.route('/image')
def show_image():
    return f'<img src="{url_for('static',filename='images/vinny.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Картинка Виннни-Пуха</title>
        </head>
        <body>
            <img src="{url_for('static',filename='/images/vinny.jpg')}" alt="Vinny">
        </body>
        </html>
        """


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html','r',encoding='utf-8') as html:
        return html.read()


# <string> - по умолчанию строка
# <int:number> - целое
# <float:number> - вещественное
# <path:p> - может содержать / для указания пути
# <uuid:id> - строка идентификатор (16 байт в hex - формате)



@app.route('/greeting/<user>/<int:idnum>')
def greeting(user, idnum):
    return f'Привет, {user} c id={idnum}'


@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    if id_num is None:
        return 'Нет номера записи'
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

@app.route('/form-test', methods=['POST','GET'])
def form_test():
    if request.method=='GET':
        with open('form.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        print(request.form['gender'])
        print(request.form['email'])
        print(request.form['about'])
        print(request.form['level'])
        print(request.form['accept'])
        print(request.form)
        return 'Форма успешно отправлена'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
