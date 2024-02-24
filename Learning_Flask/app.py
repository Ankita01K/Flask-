from flask import Flask, redirect , url_for
app=Flask(__name__) #WSGI Application:

@app.route('/')
def welcome():
    return 'Hii going to learn flask web framework'

@app.route('/enjoy')
def enjoy():
    return 'enjoying this so much'

# building url dynmically
@app.route('/success/<int:score>')
def success(score):
    return 'the person is passed adn the marks is '+ str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return 'the person is failed adn the marks is '+ str(score)


@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks <18:
        result='fail'
    else:
        result='success'

    return redirect(url_for(result,score=marks))




if __name__=='__main__':
    app.run(debug=True)

 # question: why we  write above thing(8) why important   