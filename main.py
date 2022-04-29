from flask import Flask, request, render_template, session
import json, urllib.request
import time
import get_token
import wordstat_reports
import keywords_finder


app = Flask(__name__)

actual_data = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/article')
def article():
    return render_template('find-header.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    # data = header_definer.sumextract(request.form.get('article'), 1)
    data, count = keywords_finder.get_keywords(request.form.get('article'))
    session['data'] = data[:2]
    return render_template('result.html', data=data[:5], count=count)


@app.route('/wordstat-report', methods=['GET', 'POST'])
def wordstat_report():
    data = session.get('data', None)
    report_id = wordstat_reports.create_report(get_token.token, [' '.join(data)])
    time.sleep(10)
    new_report = wordstat_reports.get_report(get_token.token, report_id)
    if new_report != -1:
        new_report = wordstat_reports.phrase_choose(new_report)
    return render_template('wordstat_report.html', report=new_report)


if __name__ == '__main__':
    app.secret_key = 'grippingsecretkey'
    app.run(debug=True)
