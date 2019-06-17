# Inbuild Functions
from flask import Flask, json, render_template, url_for, request

from main import speechrecognition

# Local Functions
app = Flask(__name__)


# Home Folder
@app.route("/speech")
def speech():
    returnval = speechrecognition()
    return render_template("index.html", file=retnshowjson)

if __name__ == "__main__":

#     app.jinja_env.filters['split_space'] = split_space
#     app.jinja_env.filters['split_dot'] = split_dot

    app.run(debug=True)
