from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def all_links(page_name):
    return render_template(page_name)

def store_in_text(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f'\n{name}, {email}, {message}')

def srore_in_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_message', methods=['POST', 'GET'])
def message():
    if request.method == "POST":
        data = request.form.to_dict()
        srore_in_csv(data)
        return redirect('./thankyou.html')
    else:
        return 'Message NOT Sent!! Try Again!!!'


