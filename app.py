from flask import Flask, render_template, url_for, request, redirect
import os

app = Flask(__name__)

# Production configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

@app.route('/')
def root():
    name = 'Klein'
    return render_template('index.htm', name = name)

@app.errorhandler(404)
def error404(e):
    title = "Error 404"
    return render_template('404.html', title = title), 404

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form['user_name']
        if name == 'flag.txt':
            return redirect(url_for('flag'))
        else:
            return redirect(url_for('user',usr=name))

@app.route('/submit/<usr>')
def user(usr):
    text = usr[::-1]

    return f"""<body style='background-color: rgb(131, 28, 103);color:white;align-items:center;text-align:center;'><h1>Hi! <b>{text}</b> <i> I reverse the text you input haha</h1><br>
            want to play again? go back <a href='/../flag.txt' style='color:green'><b>here</b></a></i></body>"""


@app.route('/f/l/a/g')
def flag():
    return "CTF{you_got_me_haha}"

if __name__ == '__main__':
    # Use PORT environment variable provided by Render, fallback to 5000 for local dev
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)