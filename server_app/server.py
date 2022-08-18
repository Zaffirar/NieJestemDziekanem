from flask import Flask, request, render_template
from .validator import Validator
from .new_types import QuestionsSet, AnswersSet
app = Flask(__name__)

Validator: Validator = Validator()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/questions')
def say_hello():
    return Validator.get_questions_set().to_dict()
