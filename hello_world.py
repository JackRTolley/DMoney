from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
   projects = [
      {'name': 'Help Cats', 'score': 50},
      {'name': 'Help Dogs', 'score': 50}
   ]
   return render_template('index.html', title='Home', projects=projects)

if __name__ == '__main__':
    app.run(debug = True)
