from time import gmtime, strftime


def quest_data():
    return [
        {
            "task_num": 0,
            "question": "Тут мало бути перше питання",
            "answers": [
                {
                    "text": "Answer1",
                    "callback_data": "wrong_answer",
                    "correct": False
                },
                {
                    "text": "Answer2",
                    "callback_data": "wrong_answer",
                    "correct": False
                },
                {
                    "text": "Answer3",
                    "callback_data": "wrong_answer",
                    "correct": False
                },
                {
                    "text": "Correct answer",
                    "callback_data": "correct_answer_1",
                    "correct": True
                }
            ],
            "task": "Молодець! Шукай кодове слово тут https://bit.ly/35tDY27 або"
                    " тут https://bit.ly/3k9mfB6 і відправляй його мені",
            "answer": "1"
        },
        {
            "task_num": 1,
            "question": "Second question here",
            "answers": [
                {
                    "text": "Answer1",
                    "callback_data": "wrong_answer",
                    "correct": False
                },
                {
                    "text": "Answer2",
                    "callback_data": "wrong_answer",
                    "correct": False
                },
                {
                    "text": "Answer3",
                    "callback_data": "wrong_answer",
                    "correct": False
                },
                {
                    "text": "Correct answer",
                    "callback_data": "correct_answer_1",
                    "correct": True
                }
            ]
        }
    ]


def start_msg():
    return {"text": "*ЦИФРОВА* гра скоро почнеться!, назва квесту: *кіберпостіронічнийквест 7027*"}


def wrong_answer():
    return {"text": "Wrong!"}


def info_msg():
    return {"text": "Info about any stuff here"}


def first_question_msg():
    return {"text": "First question about the letter"}


async def grats_msg_template(tg_id, time):
    return {"text": f"Gratz, your time is {time}"}


def msg_template(text, time_first, first_p, time_second, second_p, time_third, third_p):
    return f"""*ЗАВДАННЯ!*

{text}

*{strftime("%M:%S", gmtime(time_first))}*: {'_Ще недоступна_' if first_p is None else first_p}
*{strftime("%M:%S", gmtime(time_second))}*: {'_Ще недоступна_' if second_p is None else second_p}
*{strftime("%M:%S", gmtime(time_third))}*: {'_Ще недоступна_' if third_p is None else third_p}
    """
