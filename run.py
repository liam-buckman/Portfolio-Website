from flask import Flask, render_template, url_for

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_me')
def about():
    return render_template('About_me.html')

if __name__ == '__main__':
    app.run(debug=True)


