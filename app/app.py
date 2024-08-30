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

if __name__ == "__main__":
    app.run(debug=True) 