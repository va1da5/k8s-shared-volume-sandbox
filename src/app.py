from flask import Flask, jsonify, redirect, request, url_for
from db import db
from tinydb import Query
from settings import SETTINGS, HOSTNAME
import uuid
from http import HTTPStatus
from logging import getLogger

logger = getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"hostname": HOSTNAME})


@app.route("/todos", methods=["GET"])
def get_todos():
    todos = db.all()
    return jsonify({"todos": todos, "hostname": HOSTNAME})


@app.route("/todos", methods=["POST"])
def create_todos():
    entry = request.get_json()
    id = str(uuid.uuid4())
    db.insert({**entry, **{"id": id}})
    return redirect(url_for("get_todo", uuid=id))


@app.route("/todos/<uuid>", methods=["GET"])
def get_todo(uuid):
    Todo = Query()
    todos = db.search(Todo.id == uuid)
    if len(todos):
        return jsonify({"todo": todos[0], "hostname": HOSTNAME})
    return jsonify({"msg": "Not Found", "hostname": HOSTNAME}), HTTPStatus.NOT_FOUND


@app.route("/todos", methods=["DELETE"])
def delete_todos():
    token = request.args.get("token", "")

    try:
        with open("secrets/admin-token.txt", "r") as in_file:
            admin_token = in_file.read().strip()
            assert token == admin_token
    except Exception as exc:
        logger.error(exc)
        return (
            jsonify(
                {
                    "msg": "Todos deletion was not allowed! Incorrect token!",
                    "hostname": HOSTNAME,
                }
            ),
            HTTPStatus.UNAUTHORIZED,
        )
    db.drop_tables()
    return jsonify({"msg": "Entries removed", "hostname": HOSTNAME})
