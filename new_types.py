from typing import List, Dict, Optional


PossibleAnswers = Optional[List[str]]


class Question:
    _question: str
    # None -> open-ended question, List -> list of answers in closed-ended question
    _possible_answers: PossibleAnswers

    def __init__(self, question: str, answers: PossibleAnswers = None) -> None:
        self._question = question
        self._possible_answers = answers

    def to_dict(self) -> Dict[str, PossibleAnswers]:
        return {self._question: self._possible_answers}


class QuestionsSet:
    _questions: List[Question]

    # TODO: establish how many questions do we need
    def __init__(self, questions) -> None:
        self._questions = questions

    def to_dict(self) -> Dict[str, PossibleAnswers]:
        _dict: Dict[str, PossibleAnswers] = {}
        for q in self._questions:
            _dict |= q.to_dict()
        return _dict


AnswersSet = Dict[str, str]
