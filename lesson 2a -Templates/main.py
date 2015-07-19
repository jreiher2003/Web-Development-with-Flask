from flask import Flask 
import sys
import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries. as in Virtualenv 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Lib/site-packages'))


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run()