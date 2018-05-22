from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'ExampleKeyHere'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def my_form():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        name = request.form['name']

        if form.validate():
            # Save the comment here.
            flash(f'{name} is phishy because reasons.')
        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()
