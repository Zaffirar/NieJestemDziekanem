from .new_types import Question, QuestionsSet, AnswersSet
from typing import Any
import random
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE


class Validator(object):
    _instance = None
    
    data = pd.read_excel("Desktop/dane_do_modelu.xlsx")
    data_res = data['wynik']
    data = data.drop('wynik', axis=1)

    student_questions = [4, 8, 9, 15, 23, 31, 42, 45, 50]
    employee_questions = [2, 7, 19, 24, 25, 34, 53, 55, 56, 58, 59]
    blocker_questions = [10, 11, 17, 28, 30, 57]
    combine_questions = sorted(student_questions + employee_questions)

    questions_dict = {
        2: 'Jaki adres ma Instytut Informatyki (nazwa ulicy i numer)?',
        'Jaki adres ma Instytut Informatyki (nazwa ulicy i numer)?': 2,
        4: 'Jakie jest najpopularniejsze miejsce we Wrocławiu, gdzie możesz legalnie napić się piwa na świeżym powietrzu?',
        'Jakie jest najpopularniejsze miejsce we Wrocławiu, gdzie możesz legalnie napić się piwa na świeżym powietrzu?': 4,
        7: 'Na co dzieli się administracyjnie Instytut Informatyki?',
        'Na co dzieli się administracyjnie Instytut Informatyki?': 7,
        8: 'Ile przedmiotów obowiązkowych jest na I stopniu studiów (licencjat/inżynier)?',
        'Ile przedmiotów obowiązkowych jest na I stopniu studiów (licencjat/inżynier)?': 8,
        9: 'Jakim jednym przedmiotem można zaliczyć efekty kształcenia SO (systemy operacyjne) i ASK (architektura systemów komputerowych)?',
        'Jakim jednym przedmiotem można zaliczyć efekty kształcenia SO (systemy operacyjne) i ASK (architektura systemów komputerowych)?': 9,
        10: 'Jak nazywa się coroczny, zimowy obóz organizowany przez studentów Instytutu Informatyki?',
        'Jak nazywa się coroczny, zimowy obóz organizowany przez studentów Instytutu Informatyki?': 10,
        11: 'Gdy student zadeklaruje zadanie, którego nie zrobił, to może dostać za nie dużego…',
        'Gdy student zadeklaruje zadanie, którego nie zrobił, to może dostać za nie dużego…': 11,
        15: 'Ile wynosi kaucja za kluczyk do szafki?',
        'Ile wynosi kaucja za kluczyk do szafki?': 15,
        17: 'Który przedmiot jest uważany za najtrudniejszy do zdania na I stopniu studiów i dużo studentów go powtarza, nawet kilka razy?',
        'Który przedmiot jest uważany za najtrudniejszy do zdania na I stopniu studiów i dużo studentów go powtarza, nawet kilka razy?': 17,
        19: 'Jak nazywa się ulica od strony parkingu ze szlabanem przy Instytucie Informatyki?',
        'Jak nazywa się ulica od strony parkingu ze szlabanem przy Instytucie Informatyki?': 19,
        23: 'Jaki jest maksymalna liczba ECTS na semestr w systemie zapisów?',
        'Jaki jest maksymalna liczba ECTS na semestr w systemie zapisów?': 23,
        24: 'Kto jest dyrektorem Instytutu Informatyki?',
        'Kto jest dyrektorem Instytutu Informatyki?': 24,
        25: 'Ilu zastępców ma dyrektor Instytutu Informatyki?',
        'Ilu zastępców ma dyrektor Instytutu Informatyki?': 25,
        28: 'Ile maksymalnie punktów można oddać na jeden przedmiot w głosowaniu?',
        'Ile maksymalnie punktów można oddać na jeden przedmiot w głosowaniu?': 28,
        30: 'Co oznacza, że na liście osób zapisanych na przedmiot widać tylko nr indeksu danej osoby?',
        'Co oznacza, że na liście osób zapisanych na przedmiot widać tylko nr indeksu danej osoby?': 30,
        31: 'Ile godzin bonusu zapewnia jeden punkt oddany na dany przedmiot w głosowaniu?',
        'Ile godzin bonusu zapewnia jeden punkt oddany na dany przedmiot w głosowaniu?': 31,
        34: 'Jak nazywa się wydział, do którego należy Instytut Informatyki?',
        'Jak nazywa się wydział, do którego należy Instytut Informatyki?': 34,
        42: 'Na jakim przedmiocie, aby go zdać, będziesz musiał grać w gry komputerowe?',
        'Na jakim przedmiocie, aby go zdać, będziesz musiał grać w gry komputerowe?': 42,
        45: 'W jaki dzień tygodnia dziekanat Instytutu Informatyki jest zamknięty?',
        'W jaki dzień tygodnia dziekanat Instytutu Informatyki jest zamknięty?': 45,
        50: 'Na jakim przedmiocie piszemy programy w języku Racket?',
        'Na jakim przedmiocie piszemy programy w języku Racket?': 50,
        53: 'Jak nazywa się dziekan naszego wydziału?',
        'Jak nazywa się dziekan naszego wydziału?': 53,
        55: 'W jakich latach budowano Instytut Informatyki?',
        'W jakich latach budowano Instytut Informatyki?': 55,
        56: 'Jak nazywa się obecny rektor UWr?',
        'Jak nazywa się obecny rektor UWr?': 56,
        57: 'Jak nazywa się kampus, na którym znajduje się Instytut Informatyki?',
        'Jak nazywa się kampus, na którym znajduje się Instytut Informatyki?': 57,
        58: 'Ile jest zakładów w Instytucie Informatyki?',
        'Ile jest zakładów w Instytucie Informatyki?': 58,
        59: 'Jak nazywa się jedyna pracownia, będąca jednostką administracyjną Instytutu Informatyki?',
        'Jak nazywa się jedyna pracownia, będąca jednostką administracyjną Instytutu Informatyki?': 59}

    answers_dict = {
        2: None,
        4: None,
        7: ['Zespoły', 'Wydziały', 'Katedry', 'Zakłady'],
        8: [6, 7, 8, 9],
        9: None,
        10: None,
        11: None,
        15: [10, 20, 30, 50],
        17: None,
        19: None,
        23: [40, 45, 50, 60],
        24: None,
        25: [1, 2, 3, 4],
        28: [1, 3, 5, 10],
        30: ['Osoba jest z erasmusa', 'Osoba jest doktorantem', 'Osoba już nie studiuje', 'Osoba ukryła swoje dane osobowe'],
        31: [12, 24, 48, 72],
        34: None,
        42: None,
        45: ['Jest otwarty od poniedziałku do piątku', 'Poniedziałek', 'Środa', 'Piątek'],
        50: None,
        53: None,
        55: ['2000-2002', '2004-2006', '2008-2010', '2012-2014'],
        56: None,
        57: ['Przy Odrze', 'Wschodni', 'Grunwaldzki', 'Matematyczny'],
        58: [7, 8, 9, 10],
        59: ['Pracownia Grafiki Komputerowej', 'Pracownia Złożoności Obliczeniowej i Algorytmów', 'Pracownia Metod Numerycznych', 'Pracownia Optymalizacji Kombinatorycznej']}


    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super(Validator, cls).__new__(cls)    
        return cls._instance

    def get_employee_questions_part(self) -> list:
        mutually_exclusive_questions = [7, 58]
        normal_employee_questions = [q for q in self.employee_questions if q not in mutually_exclusive_questions]

        first_question = random.sample(mutually_exclusive_questions, 1)
        rest_of_question = random.sample(normal_employee_questions, 4)

        return first_question + rest_of_question


    def get_questions_set(self) -> QuestionsSet:
        student_questions_part = random.sample(self.student_questions, 5)
        employee_questions_part = get_employee_questions_part()
        blocker_questions_part = random.sample(self.blocker_questions, 3)
        questionnaire = student_questions_part + employee_questions_part + blocker_questions_part
        random.shuffle(questionnaire)

        questions_and_answers = []

        for question_id in questionnaire:
            questions_and_answers.append(Question(self.questions_dict[question_id], self.answers_dict[question_id]))

        qs = QuestionsSet(questions_and_answers)
        return qs


    def validate_answer(self, question_id, answer):
        answer = str(answer)
        polish_letters_to_english = str.maketrans('ęóąśłżźćń', 'eoaslzzcn')
        answer = answer.lower()
        answer = answer.trnaslate(polish_letters_to_english)
        answer = answer.strip()

        if question_id == 2:
            keywords = ['joliot', 'curie', '15']
            if all(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 4:
            keywords = ['wyspa', 'slodowa']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 7:
            if answer == 'zaklady':
                return 1
            else:
                return 0
        elif question_id == 8:
            if answer == '7':
                return 1
            else:
                return 0
        elif question_id == 9:
            keywords = ['syk', 'systemy komputerowe']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 10:
            keywords = ['zosia', 'zimowy oboz studentow informatyki', 'zoska', 'zofia']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 11:
            keywords = ['grzyb', 'grzib', 'grzymbol']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 15:
            if answer == '20':
                return 1
            else:
                return 0
        elif question_id == 17:
            keywords = ['aisd', 'algorytmy i struktury danych']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 19:
            keywords = ['polaka']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 23:
            if answer == '45':
                return 1
            else:
                return 0
        elif question_id == 24:
            keywords = ['jma', 'marcinkowski']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 25:
            if answer == '4':
                return 1
            else:
                return 0
        elif question_id == 28:
            if answer == '3':
                return 1
            else:
                return 0
        elif question_id == 30:
            if answer == 'osoba ukryla swoje dane osobowe':
                return 1
            else:
                return 0
        elif question_id == 31:
            if answer == '24':
                return 1
            else:
                return 0
        elif question_id == 34:
            keywords = ['matematyki i informatyki', 'wmi']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 42:
            keywords = ['testowanie gier', 'tg']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 45:
            if answer == 'piatek':
                return 1
            else:
                return 0
        elif question_id == 50:
            keywords = ['mp', 'metody programowania', 'metody prog']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 53:
            keywords = ['jurdzinski', 'tju']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 55:
            if answer == '2004-2006':
                return 1
            else:
                return 0
        elif question_id == 56:
            keywords = ['olkiewicz']
            if any(keyword in answer for keyword in keywords):
                return 1
            else:
                return 0
        elif question_id == 57:
            if answer == 'grunwaldzki':
                return 1
            else:
                return 0
        elif question_id == 58:
            if answer == '7':
                return 1
            else:
                return 0
        elif question_id == 59:
            if answer == 'pracownia grafiki komputerowej':
                return 1
            else:
                return 0
        else:
            return 0


    def get_model(self, list_of_features):
        x = self.data.copy()
        y = self.data_res.copy()

        for feature in self.combine_questions:
            if feature not in list_of_features:
                x = x.drop(feature, axis=1)

        sm = SMOTE(random_state=0)
        x_sm, y_sm = sm.fit_resample(x, y)

        return LogisticRegression().fit(x_sm, y_sm)


    def classify_person(self, answers: AnswersSet) -> bool:
        answers_list = []

        for [question, answer] in AnswersSet:
            answer_result = validate_answer(self.questions_dict[question], answer)
            answers_list.append((self.questions_dict[question], answer_result))

        blocker_result = 0

        for question_id, answer_result in answers_list:
            if question_id in self.blocker_questions:
                blocker_result = blocker_result + answer_result
                answers_list.remove([question_id, answer_result])

        if blocker_result < 2:
            return 0

        answers_list = sorted(answers_list)
        model = get_model([question_id for question_id, answer_result in answers_list])
        input_to_model = [answer_result for question_id, answer_result in answers_list]

        treshold = 0.66

        if model.predict_proba(input_to_model)[0][1] > treshold:
            return 1
        else:
            return 0
