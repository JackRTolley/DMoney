from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
   user = {"username": "James"}
   return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug = True)
