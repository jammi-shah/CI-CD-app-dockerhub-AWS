from flask import Flask
app = Flask(__name__)
@app.route("/")
### message on asking the question. ###
def main():
### default message on homepage. ###
    return "Welcome!"
@app.route('/how are you')
### message on asking the question. ###
def hello():
### message on asking the question. ###
    return 'I am good, how about you?'
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
