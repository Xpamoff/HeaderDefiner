from flask import Flask, request, render_template
import wordstat_reports
import keywords_finder
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/article')
def article():
    return render_template('find-header.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    #data = header_definer.sumextract(request.form.get('article'), 1)
    data, count = keywords_finder.get_keywords(request.form.get('article'))
    keywords = wordstat_reports.
    return render_template('result.html', data=data, count=count)


if __name__ == '__main__':
    app.run()
