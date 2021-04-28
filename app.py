from flask import Flask, render_template

app = Flask(__name__, template_folder='template',static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/priority_queue')
def pq():
    return render_template('queue.html')



if __name__ == '__main__':
    app.run(debug=True)
