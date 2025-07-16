from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)

# Папка для сохранения загруженных файлов
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return f'Файл загружен: {file.filename}'
        return 'Файл не выбран'

    # Простая форма на главной странице
    return render_template_string('''
        <h1>Загрузка файла</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Загрузить">
        </form>
    ''')


if __name__ == '__main__':
    app.run(debug=True)