from flask import render_template, send_from_directory
from app import app


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/resume')
def resume():
    return send_from_directory('uploads', 'Resume.pdf',
                               mimetype='application/pdf', as_attachment=True)


@app.route('/char-gen')
def char_gen():
    return render_template("char_gen.html")
