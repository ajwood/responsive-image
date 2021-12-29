import os
from flask import Flask, render_template, send_file, request

app = Flask(__name__)

WIDTH_PX = 432
HEIGHT_PX = 432
HEIGHT_N = 11
WIDTH_N = 11


@app.route("/")
def index(img="0000"):
    return render_template(
        "base.html",
        img0=make_img(img, id="baseimage", usemap=None),
        img1=make_img(img),
        w=WIDTH_PX,
        h=HEIGHT_PX,
        wn=WIDTH_N,
        hn=HEIGHT_N,
    )


def make_img(img, id="mycanvas", usemap="#imgmap"):
    usemap = "" if usemap is None else f'usemap="{usemap}"'
    elt = f'<img style="position:absolute; top:0; left:0;" src="images/{img}" width="{WIDTH_PX}" height="{HEIGHT_PX}" {usemap} />'
    return elt


@app.route("/hx/imgmap")
def hx_imgmap():
    img = request.args["img"]
    return make_img(img)


@app.route("/images/<n>")
def images(n):
    """Static image server"""
    return send_file(os.path.join("images.jpg", f"{n}.jpg"), mimetype="image/png")
