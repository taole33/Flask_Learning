from flask import Flask
app = Flask(__name__)

@app.route('/')
def HELLO():
    hello = "hello world"
    return hello

if __name__ == "__main__":
    app.run()