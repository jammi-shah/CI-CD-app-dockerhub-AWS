###
This code represents a small flask app that picks up questions asked through query parameters then answers them 
Questions that can be asked are: 1. how are you
###

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
###
default message on homepage
###
    return "Welcome!"

@app.route('/how are you')
def hello():
###
message on asking the question
###
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
