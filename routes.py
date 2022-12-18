from app import app, db
from flask import request, render_template
from check_validate import validate_email, validate_login, validate_password
from models import Users


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return "You are on the main page. <br> Вы находитесь на главной странице."


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    result = ''
    if request.method == 'POST':
        email = request.form['email']
        login = request.form['login']
        password = request.form['password']
        confirm_password = request.form['conf_password']
        if confirm_password == password:
            if validate_email(email) and validate_login(login) and validate_password(password):
                user = Users(email=request.form['email'],
                             login=request.form['login'],
                             password=password)
                user_test_email = Users.query.filter_by(email=user.email).first()  # checking data in the table
                user_test_login = Users.query.filter_by(login=user.login).first()
                if user_test_email is None and user_test_login is None:
                    db.session.add(user)
                    db.session.commit()
                    result = 'User has been created. Пользователь был создан.'
                else:
                    result = 'There is a user with this login/email. Уже есть пользователь с таким логином/почтой.'
            else:
                result = 'Something went wrong! Check all forms. Что-то пошло не так! Проверьте все заполненные формы.'
        else:
            result = 'Check passwords. Проверьте соответствие паролей.'
    return render_template('/registration.html', result=result)
