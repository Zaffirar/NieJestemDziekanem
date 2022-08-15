from types import Question, QuestionsSet, AnswersSet
from typing import Any


class Validator(object):
    _instance = None

    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super(Validator, cls).__new__(cls)
        return cls._instance

    def get_questions_set(self) -> QuestionsSet:
        # TODO: real logic
        question_str1 = "q1"
        question_str2 = "q2"
        question_str3 = "q3"
        question_str4 = "q4"
        question_str5 = "q5"
        answers_str1 = ["ans1", "ans2", "ans3", "ans4"]
        answers_str2 = ["1ans", "2ans", "3ans", "4ans"]
        q1 = Question(question_str1, answers_str1)
        q2 = Question(question_str2, None)
        q3 = Question(question_str3)
        q4 = Question(question_str4, answers_str1)
        q5 = Question(question_str5, answers_str2)
        qs = QuestionsSet(q1, q2, q3, q4, q5)
        return qs
        

    def validate_answers(self, answers: AnswersSet) -> bool:
        for [question, answer] in AnswersSet:
            # TODO: real logic
            if len(question) > 3 and len(answer) > 2:
                return True
            else:
                return False
