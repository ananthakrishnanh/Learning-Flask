from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html',message = 'Aloha, Aloha!!')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'Gordon' and password == 'Ramsay':
            return render_template('index.html',message = 'Login Successful')
        else:
            error_message = 'Hint: He curses a lot'
            return render_template('football.html', message = error_message)

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
