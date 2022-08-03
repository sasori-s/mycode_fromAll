from distutils.log import debug
from pip import main
from flask import Flask
app = Flask( _name___)
@app.route(' /')
def hello_world() :
    return ' Hello, World! '

if __name__ == "__main__":
    app.run(debug=True )