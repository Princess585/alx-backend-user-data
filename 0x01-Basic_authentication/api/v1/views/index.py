#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status() -> str:
    """
    Return the status jsonify 'OK'
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats/", strict_slashes=False)
def stats() -> str:
    """
    Return jsonify status
    """
    from models.user import User

    stats = {}
    stats["users"] = User.count()
    return jsonify(stats)


@app_views.route("/unauthorized", methods=["GET"], strict_slashes=False)
def unauthorized():
    """api is unathorized"""
    abort(401)


@app_views.route("/forbidden", methods=["GET"], strict_slashes=False)
def forbidden():
    """The forbidden 403 endpoint"""
    abort(403)
