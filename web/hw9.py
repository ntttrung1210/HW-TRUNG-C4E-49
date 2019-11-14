from hw9db import  get_all_bikes,add_new_bike
from flask import Flask, render_template, redirect,request,url_for
app = Flask(__name__)
@app.route('/new_bike', methods=['POST'])
def new_bikes():
    a=request.form.get('mode')
    b=request.form.get('fee')
    c=request.form.get('anh')
    d=request.form.get('date')
    add_new_bike(a,b,c,d)
    return redirect(url_for("new_bikes"))
@app.route('/new_bike')
def bike():
    return render_template('bikerental.html')
print(get_all_bikes)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 