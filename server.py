from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret_counter'

@app.route('/')
def counter_page():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    count = session['counter']

    # counts how many time the user visits the page
    if 'true_counter' in session:
        session['true_counter'] += 1
    else:
        session['true_counter'] = 1
    true_count = session['true_counter']
    
    return render_template('index.html', count=count, true_count=true_count)

@app.route('/increment')
def increment_count():
    session['counter'] += 1
    return redirect('/')

@app.route('/custom_increment', methods=['post'])
def cusomt_increment():
    session['counter'] += int(request.form['count_plus'])-1
    # if 'count_plus' not in request.form:
    #    session['count_plus'] += -1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.pop('counter')
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)