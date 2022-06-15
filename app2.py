from flask import Flask
app2 = Flask(__name__)
@app2.route('/')
def home():
    print("Server received request for Home page...")
    return '"Welcome to my Home page!"'
@app2.route('/about')
def about():
    print("Server received request for 'Home' page...")
    return '"Welcome to my Home page!"'
if __name__ == "__main__":
    app2.run(debug=True)
