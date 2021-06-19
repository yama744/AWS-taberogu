# This Python file uses the following encoding: utf-8

from flask import Flask, render_template ,send_file, make_response, send_from_directory #Flaskと、HTMLをレンダリングするrender_templateをインポート
from flask import request

app = Flask(__name__) # Flask の起動

@app.route('/') # localhost:50000/を起動した際に実行される
def index():
    return render_template('index.html') #index.htmlをレンダリングする

@app.route('/run') # localhost:50000/を起動した際に実行される
def run():
    import test
    return render_template('index2.html')

@app.route("/download")
def downloadzip():
    response = make_response()
    response.data  = open('data.xlsx', "rb").read()
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = 'attachment; filename=data.xlsx'
    return response
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 50000) #ローカルホスト50000番でサーバーを立てる