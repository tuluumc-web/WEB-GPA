from flask import Flask, render_template, request

app = Flask(__name__)


def get_iuh_info(grade):
    """Quy đổi điểm hệ 10 sang hệ 4 và xếp loại theo chuẩn IUH"""
    if grade >= 9.0: return 4.0, "Xuất sắc", "A+"
    if grade >= 8.5: return 4.0, "Giỏi", "A"
    if grade >= 8.0: return 3.5, "Khá", "B+"
    if grade >= 7.0: return 3.0, "Khá", "B"
    if grade >= 6.5: return 2.5, "Trung bình", "C+"
    if grade >= 5.5: return 2.0, "Trung bình", "C"
    if grade >= 5.0: return 1.5, "Trung bình yếu", "D+"
    if grade >= 4.0: return 1.0, "Trung bình yếu", "D"
    return 0.0, "Kém", "F"


def get_classification(gpa4):
    """Xếp loại học lực dựa trên GPA hệ 4"""
    if gpa4 >= 3.6: return "Xuất sắc"
    if gpa4 >= 3.2: return "Giỏi"
    if gpa4 >= 2.5: return "Khá"
    if gpa4 >= 2.0: return "Trung bình"
    return "Yếu/Kém"


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        grades = [float(x) for x in request.form.getlist('grade')]
        credits = [int(x) for x in request.form.getlist('credit')]

        total_cre = sum(credits)
        if total_cre > 0:
            # Tính tổng điểm hệ 4 tích lũy
            total_point4 = sum(get_iuh_info(g)[0] * c for g, c in zip(grades, credits))
            gpa4 = round(total_point4 / total_cre, 2)

            # Tính trung bình hệ 10
            total_point10 = sum(g * c for g, c in zip(grades, credits))
            gpa10 = round(total_point10 / total_cre, 2)

            results = {
                'gpa4': gpa4,
                'gpa10': gpa10,
                'rank': get_classification(gpa4),
                'total_cre': total_cre
            }

    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)