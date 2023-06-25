from data_base import DataBase

if __name__ == '__main__':
    db = DataBase()
    data_file = 'questions.json'
    ans_file = 'answers.json'

    exam = db.load(data_file)

    ans = {}

    name = input('Write your name: ')
    surname = input('Write your surname: ')
    ans.update({"students_name": name, "studens_surname": surname})
    ans.update({"answers": {}})

    for key, value in exam['exam_content'].items():
        print(key, value)
        ans_let = input('Write answer: ')
        answer = {value["question"]: value[ans_let]}
        ans["answers"].update(answer)
        db.save(ans, ans_file)
