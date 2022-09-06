from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ='ume'

@app.route('/')
def create_session():
    session['counter_num'] = 0
    return redirect('/count')

@app.route('/count')
def display_counter():
    session['counter_num'] += 1
    return render_template('index.html')

@app.route('/reset')
def reset_counter():
    session.pop('counter_num', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)