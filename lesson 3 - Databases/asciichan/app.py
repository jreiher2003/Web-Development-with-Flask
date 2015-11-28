from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('front.html')

	if request.method == 'POST':
		title = request.form['title']
		art = request.form['art']
		error = 'need a title and art'
		success ="Thanks for submitting"
		return render_template('front.html', title=title, art=art, error=error, success=success)

if __name__ == '__main__':
    app.run(debug=True)
