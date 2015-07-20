from flask import Flask, render_template, request, redirect
app = Flask(__name__)




@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		n = 15
		return render_template('index.html', n=n)

	if request.method == "POST":
		n = request.form['name']
		return redirect('hello', n=n)

if __name__ == "__main__":
	app.run()