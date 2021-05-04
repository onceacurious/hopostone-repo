from flask import Flask, render_template, request


app =Flask(__name__)


@app.route('/')
def cover_page():
    return render_template('cover.html')

@app.route('/inquire')
def enquiry_page():
    return render_template('inquiry.html')