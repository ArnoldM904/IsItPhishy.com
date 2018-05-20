from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = f"Pretend I checked if '{text}' was phishy or not please."
    return processed_text


if __name__ == '__main__':
    app.run(debug=True)  # Debug shows your changes instantly.
