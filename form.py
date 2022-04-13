from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    data = request.form.get('article')
    return render_template('get_data.html', data=data)


if __name__ == '__main__':
    app.run()