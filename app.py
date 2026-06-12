from flask import Flask, render_template, request

app = Flask(__name__)

# Данные группы
group_data = {
    "name": "Забей и Пой",
    "genre": "Рок",
    "former_names": ["СиП (Серп и Молот)", "До.Ли.На", "Хор Нищих", "Фантазия Гитариста"],
    "members": [
        {"name": "Кирилл Мусиенко (Кира)", "role": "Лидер группы, ритм-гитарист, вокалист", "bio": "Основатель группы, автор текстов песен. Обладает уникальным харизматичным вокалом и неповторимым стилем игры на гитаре.", "photo": "kira.jpg"},
        {"name": "Роман Самойлов", "role": "Соло-гитарист, второй вокалист", "bio": "Виртуозный гитарист, создающий сложные и красивые гитарные партии. Основной двигатель музыкального прогресса группы.", "photo": "roman.jpg"},
        {"name": "Иван Каменцев", "role": "Барабанщик (бывший)", "bio": "Основатель группы, создавший её первоначальный состав. Точный и мощный барабанщик, задающий ритм.", "photo": "ivan.jpg"},
        {"name": "Илья Синченко", "role": "Басист", "bio": "Таинственный басист, чья игра придаёт музыке глубину и основательность.", "photo": "ilya.jpg"}
    ],
    "songs": [
    {
        "title": "Чернобыльский колобок", 
        "release_date": "22 июня 2023",
        "description": "Дебютный трек группы с глубоким философским подтекстом и запоминающимся риффом",
        "file": "chernobylskiy-kolobok.mp3"  # ← Это поле обязательно
    },
    {
        "title": "Майка КиШ", 
        "release_date": "23 сентября 2023",
        "description": "Оммаж классикам русского рока с современной интерпретацией",
        "file": "mayka-kish.mp3"  # ← Это поле обязательно
    },
    {
        "title": "Забей и Пой", 
        "release_date": "14 октября 2023",
        "description": "Гимн поколения, ставший визитной карточкой коллектива",
        "file": "zabei-i-poy.mp3"  # ← Это поле обязательно
    },
    {
        "title": "Славный парень", 
        "release_date": "17 ноября 2023",
        "description": "НА ДАННЫЙ МОМЕНТ ЛУЧШАЯ ПЕСНЯ",
        "file": "slavnyy-paren.mp3"  # ← Это поле обязательно (даже если файла нет)
    }
    ],
    "concerts": [
        {"date": "2023", "location": "Школа №65", "description": "Два первых концерта группы, на которых они представили свои первые треки живой аудитории."}
    ],
    "equipment": {
    "Кира": [
        "Белый Stratocaster с уникальным дизайном (огонь и надпись 'Забей и Пой')",
        "Les Paul цвета санберст (Fabio)"
    ],
    "Роман": [
        "Акустическая гитара Cort",
        "Гитара формы Flying V (Caraya)"
    ],
    "Илья": [
        "Бас цвета санберст (Maxwood)"
    ],
    "Иван": [
        "Электронная барабанная установка"
    ]
    },
    "news": [
    {
        "date": "1 сентября 2024",
        "title": "Сходка музыкантов",
        "description": "Группа провела первую сходку музыкантов",
        "media": {
            "type": "video",
            "source": "meeting.mp4",
        }
    },
    {
        "date": "14 октября 2023",
        "title": "Релиз нового сингла",
        "description": "Вышел новый сингл группы",
        "media": {
            "type": "video", 
            "source": "single-release.mp4",
        }
    },
    {
        "date": "23 сентября 2023",
        "title": "Концерт в школе",
        "description": "Группа выступила с концертом",
        "media": {
            "type": "video",
            "source": "concert.mp4",
        }
    }
    ],
    "socials": {
        "telegram": "https://t.me/zabejipoj",
        "youtube": "https://youtube.com/@zabejipoj?si=BzSMMSl8pHLSQJgR",
        "vk": "https://vk.com/public220645241"
    },
    "facts": [
        "Все посты в Telegram канале начинаются с 'Панки, хой!' - ставшей культовой фразы",
        "Группа провела сходку музыкантов 1 сентября 2024 года",
        "Участники создают мемы по мотивам жизни группы"
    ]
}

# Маршруты
@app.route('/')
def index():
    return render_template('index.html', group=group_data)

@app.route('/about')
def about():
    return render_template('about.html', group=group_data)

@app.route('/music')
def music():
    return render_template('music.html', group=group_data)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', group=group_data)

@app.route('/news')
def news():
    return render_template('news.html', group=group_data)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = [
        {
            "question": "Какое было первоначальное название группы?",
            "options": ["СиП", "До.Ли.На", "Хор Нищих", "Фантазия Гитариста"],
            "correct": 0
        },
        {
            "question": "Кто является автором большинства гитарных соло в группе?",
            "options": ["Кира", "Роман", "Иван", "Илья"],
            "correct": 1
        },
        {
            "question": "Как называется невыпущенная песня группы?",
            "options": ["Чернобыльский колобок", "Майка КиШ", "Забей и Пой", "Славный парень"],
            "correct": 3
        },
        {
            "question": "С какой фразы начинаются все посты в Telegram канале?",
            "options": ["Рок жив!", "Панки, хой!", "Забей и пой!", "Музыка - наше всё!"],
            "correct": 1
        },
        {
            "question": "На каком инструменте играл Илья в музыкальной школе?",
            "options": ["Гитара", "Бас-гитара", "Саксофон", "Барабаны"],
            "correct": 2
        }
    ]
    
    if request.method == 'POST':
        score = 0
        answers = []
        for i, q in enumerate(questions):
            user_answer = request.form.get(f'q{i}')
            if user_answer and int(user_answer) == q['correct']:
                score += 1
            answers.append({
                "question": q['question'],
                "user_answer": q['options'][int(user_answer)] if user_answer else "Не ответил",
                "correct_answer": q['options'][q['correct']],
                "is_correct": user_answer and int(user_answer) == q['correct']
            })
        return render_template('quiz.html', group=group_data, questions=questions, show_results=True, score=score, total=len(questions), answers=answers)
    
    return render_template('quiz.html', group=group_data, questions=questions, show_results=False)

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html', group=group_data)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', group=group_data)

if __name__ == '__main__':
    app.run(debug=True)