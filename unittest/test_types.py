from NieJestemDziekanem.types import Question, QuestionsSet


def test_Question_dict_generation_with_open_ended_question():
    question_str = "question1"
    q1 = Question(question_str, None)
    assert q1.to_dict() == {question_str: None}


def test_Question_dict_generation_with_open_ended_question_without_passing_answers():
    question_str = "question2"
    q2 = Question(question_str)
    assert q2.to_dict() == {question_str: None}


def test_Question_dict_generation_with_closed_ended_question():
    question_str = "question3"
    answers_str = ["ans1", "ans2", "ans3", "ans4"]
    q3 = Question(question_str, answers_str)
    assert q3.to_dict() == {question_str: answers_str}


def test_QuestionsSet_dict_generation_with_all_questions_in_constructor():
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
    assert qs.to_dict() == q1.to_dict() | q2.to_dict() | \
        q3.to_dict() | q4.to_dict() | q5.to_dict()
