from flask import Flask, render_template
app = Flask(__name__)
@app.route('/template/index.html')
def foo(james):
    return render_template('index.html', to=james)