from flask import Flask, render_template, request

app = Flask(__name__)

quiz = [
    {"term": "astronomer", "choices": ["天文学者", "宇宙飛行士", "科学者", "人文学者"], "correct": "A"},
    {"term": "development", "choices": ["建設", "発展", "計画", "開発者"], "correct": "B"},
    {"term": "heliocentric", "choices": ["中心的な", "偏心的な", "地動説の", "太陽系の"], "correct": "C"},
    {"term": "theory", "choices": ["理論", "仮説", "実験", "概念"], "correct": "A"},
    {"term": "model", "choices": ["計画", "模型", "方式", "型"], "correct": "B"}
]

@app.route('/')
def index():
    return render_template('index.html', question=quiz[0], question_number=0)

@app.route('/submit', methods=['POST'])
def submit():
    question_number = int(request.form['question_number'])
    selected_choice = request.form['choice']
    correct_choice = quiz[question_number]['correct']
    is_correct = selected_choice == correct_choice

    next_question_number = question_number + 1
    next_question = quiz[next_question_number] if next_question_number < len(quiz) else None

    return render_template('result.html', is_correct=is_correct, next_question=next_question, question_number=next_question_number)

if __name__ == '__main__':
    app.run(debug=True)
