from flask import Flask 
myapp = Flask(__name__)

@myapp.route("/")
def index():
    return "<h1 style='color:blue'>Hello, World!!</h1>"

if __name__ == '__main__':
    print("__name__  == ",__name__) 
    myapp.run(host='0.0.0.0')
