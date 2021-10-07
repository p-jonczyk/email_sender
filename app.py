import os
from flask import render_template, request, redirect, flash, url_for, Flask
import smtplib
from werkzeug.utils import secure_filename
from email.message import EmailMessage
import file_handling
import email_handling
import const

app = Flask(__name__)


app.secret_key = const.SECRET_KEY
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jankowskijan640@gmail.com'
app.config['MAIL_PASSWORD'] = '(Jan)Jankowski0192!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['UPLOAD_FOLDER'] = './static/uploads'
app.config['TRAP_HTTP_EXCEPTIONS'] = True


@app.route("/")
def index():
    flash("")
    return render_template("upload.html")


@app.route("/send")
def send_mail():
    flash("")
    return render_template("send.html")


@app.route("/result")
def result():
    flash("")
    return render_template("result.html")


@app.route('/', methods=['POST', 'GET'])
def upload_file():
    file = request.files['file']
    if file and file_handling.allowed_file(file.filename):
        # clean uploads dir before upload new file
        file_handling.clean_uploads(app.config['UPLOAD_FOLDER'])
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # change into json
        filepath = file_handling.get_filepath(app.config['UPLOAD_FOLDER'])
        json_string = file_handling.excel_to_json(filepath)
        email_msg_pairs = email_handling.get_email_msg(json_string)
        # validate if email contain '@' and '.'
        invalide_emails = email_handling.check_email(email_msg_pairs)

        return render_template('send.html',
                               table=enumerate(email_msg_pairs),
                               invalide_emails=invalide_emails)
    else:
        flash('Allowed file type: .xlsx ')
        return redirect(request.url)


@app.route("/result", methods=['POST', 'GET'])
def send():
    # get from form
    email_from = request.form.get("emailfrom")
    password = request.form.get("password")
    subject = request.form.get("subject")
    signature = request.form.get("signature")

    # get data
    filepath = file_handling.get_filepath(app.config['UPLOAD_FOLDER'])
    json_string = file_handling.excel_to_json(filepath)
    email_msg_pairs = email_handling.get_email_msg(json_string)

    # sending
    try:
        server = smtplib.SMTP(
            app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
        server.starttls()
        server.login(email_from, password)
        for num, data_tuple in enumerate(email_msg_pairs):
            msg = EmailMessage()
            msg['SUBJECT'] = subject
            msg['FROM'] = email_from
            msg['TO'] = f'{data_tuple[0]}'
            msg.set_content(f"{data_tuple[1]}\n\n{signature}")
            server.send_message(msg)
        server.quit()
        return render_template('result.html')
    except Exception:
        error_msg = f"{msg['TO']}"
        return render_template("fail_result.html", error_msg=error_msg)


@app.errorhandler(Exception)
def error(e):
    return render_template("fail_result.html", error_msg=const.other_error_msg)


if __name__ == '__main__':
    app.run(debug=True)
