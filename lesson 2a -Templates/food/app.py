from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	n = request.args['n']
	if n:
		n = int(n)
	return render_template("form.html", n=n)

if __name__ == '__main__':
	app.run()