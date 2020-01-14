import random

from flask import redirect, render_template, send_from_directory

from application import application
from forms import InputForm
from rpg import char_gen


@application.route('/')
def home():
    return render_template("home.html")


@application.route('/resume')
def resume():
    return send_from_directory('uploads', 'Resume.pdf',
                               mimetype='application/pdf', as_attachment=True)


@application.route('/char_gen_form', methods=['GET', 'POST'])
def char_gen_form():
    form = InputForm()

    if form.validate_on_submit():
        random.seed(form.name_input)
        char_num = "%0.16d" % random.randint(0, 9999999999999999)
        char_dict = char_gen.main(form.name_input, char_num)

        return render_template("char-gen-result.html", form=form,
                               char_dict=char_dict)

    return render_template("char-gen-form.html", form=form)
