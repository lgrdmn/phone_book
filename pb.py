from flask import Flask, render_template, request
import main

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/find')
def web_find():
    phone = request.args.get('phone')
    result = main.find_subscriber(phone)
    return render_template("index.html", message=result[0], phone_number=result[1],
                           first_name=result[2], last_name=result[3],
                           street_name=result[4], house_number=result[5])


@app.route('/add')
def web_add():
    phone = request.args.get('phone')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    street_name = request.args.get('street_name')
    house_number = request.args.get('first_name')
    result = main.add_subscriber(phone, first_name, last_name, street_name, house_number)
    return render_template("index.html", message=result)


if __name__ == '__main__':
    app.run()
