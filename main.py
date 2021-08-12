from flask import Flask, render_template, request, redirect, url_for
import smtplib
EMAIL = "dwiden223@gmail.com"
PASSWORD = "GES#)D3)4Rt!yds"
TO_ADDRESS = "dwidwnbrahmaa222@gmail.com"

my_app = Flask(__name__)


@my_app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        req = request.form
        name = req['name']
        email = req['email']
        comment = req['comment']
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                to_addrs=TO_ADDRESS,
                from_addr=EMAIL,
                msg=f"subject:People\n name: {name}\nemail: {email}\ncomment: {comment}"
            )

        return redirect(url_for('home'))
    return render_template("index.html")


if __name__ == "__main__":
    my_app.run(debug=True)