from typing import Dict
from flask import Flask, Response, request, render_template
from .validator import Validator
from .new_types import AnswersSet
import json
app = Flask(__name__)

Validator: Validator = Validator()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/questions', methods=['GET'])
def send_questions():
    dict_to_send = Validator.get_questions_set().to_dict()
    json_to_send = json.dumps(dict_to_send, indent=4,
                              ensure_ascii=False).encode('utf8')
    res = Response(json_to_send, status=200)
    res.headers["Content-Type"] = "application/json; charset=utf-8"
    res.headers["Content-Language"] = "pl-PL"
    return res


@app.route('/answers', methods=['POST'])
def validate():
    answers = request.get_json()
    print(answers)
    res = Validator.classify_person(answers)
    return str(res)

