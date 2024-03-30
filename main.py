from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL, Email
from wtforms import PasswordField, SubmitField, StringField, EmailField

app = Flask(__name__)
app.config["SECRET_KEY"] = "DAVIDISHIM"


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
