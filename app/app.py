from flask import Flask,  render_template
app = Flask(__name__)

@app.route('/index2.html')
def home():
    return render_template('index2.html')


@app.route('/aboutus.html')
def about():
    return render_template('aboutus.html')


if __name__ == "__main__":
    app.run(debug=True) 