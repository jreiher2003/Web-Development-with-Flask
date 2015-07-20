from flask import Flask, render_template, request, redirect
app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
def hello():
	items = ''
	if request.method == 'GET':
		return render_template('index.html', items=items)

	
