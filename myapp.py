from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def first():
    return 'My Demo Web'

@app.route('/whereami')
def whereami():
    return 'Ghana'

@app.route('/numbers')
def numbers():
    return 'In a class of 30 people only 15 came ouch'

@app.route('/webpages')
def index():
    return render_template('index.html')

@app.route('/linki')
def mainp():
    return render_template('link.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')