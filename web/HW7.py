from flask import Flask, render_template, redirect
import os
app = Flask(__name__)


@app.route('/about-me/')
def aboveme():
    return '''
    Nguyen Thanh Trung
    <br>
    School: HUST   
    '''
@app.route('/school')
def hello():
    return redirect("http://techkids.vn",code=302)

@app.route('/bmi/<a>/<b>')
def bmi1(a,b):
    a=int(a)
    b=int(b)
    c=float(b/100)
    d=float(a/(c*c))
    # if d<16:
    #     return 'Severely underweight'
    # elif d<18.5:
    #     return 'Underweight'
    # elif d<25:
    #     return 'Normal'
    # elif d<30:
    #     return 'Overweight'
    # else:
    #     return 'Obese'
    return render_template("bmi.html",data=d)
@app.route('/user/<a>')
def iden(a):
    user1={
        'huy':{
                "name":'Nguyen Quang Huy',
                'age': '29'
              },
        'tuananh':{
                "name":"Huynh Tuan Anh",
                'age': '22'
              },
        'trung':{
                "name":"Nguyen Thanh Trung",
                'age': '19'
                }
        }
    d=0
    for v in user1:
        if a==v:
            d=1
            break
    if d==1:
        return render_template("index.html",data=user1[v])
    else:
        return 'Not found'
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 