from flask import Flask,  render_template
app = Flask(__name__)

@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/aboutus.html')
def about():
    return render_template('aboutus.html')


@app.route('/crop.html')
def crop():
    return render_template('crop.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/disease.html')
def disease():
    return render_template('disease.html')

@app.route('/fertilizers.html')
def fertilizer():
    return render_template('fertilizers.html')

if __name__ == "__main__":
    app.run(debug=True) 