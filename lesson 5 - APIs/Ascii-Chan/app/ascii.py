import datetime
from app import app, db
from app.models import AsciiArt
from flask import render_template, request, url_for, redirect
  

@app.route("/", methods=["GET","POST"])
def hello():
    all_art = AsciiArt.query.all()
    if request.method == 'POST':
        one = AsciiArt(title=request.form['title'], art=request.form['art'])
        db.session.add(one)
        db.session.commit()
        return redirect(url_for('hello', all_art=all_art))
    return render_template("base.html", all_art=all_art)

