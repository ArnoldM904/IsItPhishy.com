from flask import Flask, render_template, flash, request
from wtforms import Form, validators, StringField
import url_check

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'ExampleKeyHere'


class ReusableForm(Form):
    name = StringField('Enter URL:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def search_form():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        url = request.form['name']

        if form.validate():
            # Save the comment here.
            flash(url_check.examine(url)) # Check how Phishy the URL is.
        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()
