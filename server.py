from random import random
from shutil import move
from turtle import st
from flask import Flask, render_template,request, redirect,session

app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'
log=[]
win=[]


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/submit', methods=['POST'])
def submit():

    if session.get('your_gold')==None:
        log.clear()
        win.clear()
        session['moves']=1
        session['has_won']="False"
        session['finished']="False"
        if request.form['source']=='farm':
            earned=int(random()*10+10)
            session['your_gold']=earned
            log.insert(0,"Earned "+str(earned)+" golds from the farm!")
            session['log']=log
            win.insert(0,"True")
            session['win']=win
            print(session)
            

        elif request.form['source']=='cave':
            log.clear()
            earned=int(random()*5+5)
            session['your_gold']=earned
            log.insert(0,"Earned "+str(earned)+" golds from the cave!")
            session['log']=log
            win.insert(0,"True")
            session['win']=win
            print(session)
        elif request.form['source']=='house':
            log.clear()
            earned=int(random()*2+3)
            session['your_gold']=earned
            log.insert(0,"Earned "+str(earned)+" golds from the house!")
            session['log']=log
            win.insert(0,"True")
            session['win']=win
        elif request.form['source']=='casino':
            cWin=random()
            if cWin<0.5:
                session['your_gold']=0
                log.insert(0,"You didnt earn anything from the casino, you should go home ")
                session['log']=log
                win.insert(0,"False")
                session['win']=win
            else:
                log.clear()
                earned=int(random()*50)
                session['your_gold']=earned
                log.insert(0,"Earned "+str(earned)+" golds from the casino!")
                session['log']=log
                win.insert(0,"True")
                session['win']=win


    else:
        session['moves']+=1
        if request.form['source']=='farm':
            earned=int(random()*10+10)
            session['your_gold']+=earned
            log.insert(0,"Earned "+str(earned)+" golds from the farm!")
            session['log']=log
            win.insert(0,"True")
            session['win']=win
            print(session)
        elif request.form['source']=='cave':
            earned=int(random()*5+5)
            session['your_gold']+=earned
            log.insert(0,"Earned "+str(earned)+" golds from the cave!")
            session['log']=log
            win.insert(0,"True")
            session['win']=win
            print(session)

        elif request.form['source']=='house':
            earned=int(random()*2+3)
            session['your_gold']+=earned
            log.insert(0,"Earned "+str(earned)+" golds from the house!")
            session['log']=log
            win.insert(0,"True")
            session['win']=win
        elif request.form['source']=='casino':
            cWin=random()
            if cWin<0.5:
                earned=int(random()*50)
                session['your_gold']-=earned
                log.insert(0,"you lost "+str(earned)+" golds to the casino HAHAHA!!! ")
                session['log']=log
                win.insert(0,"False")
                session['win']=win
            else:
                earned=int(random()*50)
                session['your_gold']+=earned
                log.insert(0,"Earned "+str(earned)+" golds from the casion!")
                session['log']=log
                win.insert(0,"True")
                session['win']=win

    print(session['moves'])
    if session['moves']==15:
        session['finished']="True"
    if session['your_gold']>=500:
        session['has_won']="True"
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)