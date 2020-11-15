from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
