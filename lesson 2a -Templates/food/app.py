from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

def fizzbuzz(number):
    number = int(number)
    if number < 1:
        raise ValueError()

    output = []
    for i in range(1, number + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                value = 'fizzbuzz'
            else:
                value = 'fizz'
        elif i % 5 == 0:
            value = 'buzz'
        else:
            value = i
        output.append(value)
    return output

@app.route('/')
def fiz():
	return render_template('fizzbuzz.html')

@app.route('/fizzbuzz/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        rounds = request.form['rounds']
        results = fizzbuzz(rounds)
        # return render_template('fizzbuzz.html', results=results)
        return render_template('answer.html', results=results)

    return render_template('form.html')


@app.route('/food/', methods=['POST', 'GET'])
def food():
    if request.method == 'POST':
        items = request.form.getlist('food')
        return render_template('food.html', items=items)
    return render_template('food.html')


if __name__ == '__main__':
	app.run(debug=True)