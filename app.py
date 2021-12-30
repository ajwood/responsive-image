import os
from flask import Flask, render_template, send_file

app = Flask(__name__)

# constants based on how the images were rendered (the image dimension, and how
# many grid positions exist)
WIDTH_PX = 432
HEIGHT_PX = 432
HEIGHT_N = 21
WIDTH_N = 21


@app.route("/")
def index(img="0000"):
    return render_template(
        "base.html",
        img=img,
        w=WIDTH_PX,
        h=HEIGHT_PX,
        wn=WIDTH_N,
        hn=HEIGHT_N,
    )

@app.route("/images/<img>")
def images(img):
    """Static image server"""
    return send_file(os.path.join("images.002", f"{img}.jpg"), mimetype="image/jpeg")
