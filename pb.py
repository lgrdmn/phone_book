from flask import Flask, render_template, request
import main

app = Flask(__name__)

INDEX_PATH = "index.html"


@app.route('/')
def index():
    return render_template(INDEX_PATH)


@app.route('/send')
def web_send():
    phone = request.args.get('phone')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    street_name = request.args.get('street_name')
    house_number = request.args.get('house_number')
    if request.args.get('submit_button') == " Найти ":
        result = main.find_subscriber(phone)
    elif request.args.get('submit_button') == " Добавить ":
        result = main.add_subscriber(phone, first_name, last_name, street_name, house_number)
    elif request.args.get('submit_button') == " Удалить ":
        result = main.del_subscriber(phone)
    elif request.args.get('submit_button') == " Изменить ":
        result = main.update_subscriber(phone, first_name, last_name, street_name, house_number)
    return render_template(INDEX_PATH, message=result[0], phone_number=result[1],
                           first_name=result[2], last_name=result[3],
                           street_name=result[4], house_number=result[5])


if __name__ == '__main__':
    app.run()

