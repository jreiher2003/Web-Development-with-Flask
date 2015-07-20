from flask import Flask, render_template, request
app = Flask(__name__)


form_input = """<form>
		<h2>Add a Food</h2>
		<input type="text" name="food">
		%s
		<button>Add</button>
	</form>"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

item_html = "<li>%s</li>"

shopping_list_html = """
<br><br><h2>Shopping List</h2>
<ul>%s</ul>"""

@app.route("/", methods=["GET", "POST"])
def hello():
	output = form_input
	output_hidden = ""

	items = request.form['food']
	if items:
		for item in items:
			output_hidden += hidden_html % item
			output_items += item_html % item

		output_shopping = item_html % output_items
		output += output_shopping
	output = output % output_hidden
	return output

if __name__ == "__main__":
	app.run()