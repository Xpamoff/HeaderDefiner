from flask import Flask, request, render_template
import wordstat_reports
import header_definer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/article')
def article():
    return render_template('find-header.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    data = request.form.get('article')

    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run()
