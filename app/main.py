from flask import Flask, render_template, request

from app.db_ops import DataBase

APP = Flask(__name__)


@APP.route("/")
def home():
    return render_template("home.html")


@APP.route("/create", methods=["GET", "POST"])
def create():
    db = DataBase()
    name = request.values.get("name")
    if name:
        db.insert({
            "Name": name,
            "Lambda Track": request.values.get("lambda_track"),
            "Web Front End": len(request.values.get("web_front_end") or ""),
            "Web Back End": len(request.values.get("web_back_end") or ""),
            "DS Data Engineer": len(request.values.get("ds_data_engineer") or ""),
            "DS API Engineer": len(request.values.get("ds_api_engineer") or ""),
            "DS ML Engineer": len(request.values.get("ds_ml_engineer") or ""),
        })
    return render_template(
        "create.html",
        track_default="Web",
        options=['☆' * i for i in range(5, 0, -1)],
        default="☆☆☆",
        table=list(db.find_many({})),
        enumerate=enumerate,
    )


@APP.route("/assignments", methods=["GET"])
def assignments():
    db = DataBase()
    return render_template(
        "assignments.html",
        table=list(db.find_many({})),
        enumerate=enumerate,
    )


if __name__ == '__main__':
    APP.run()
