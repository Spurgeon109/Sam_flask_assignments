from flask import Flask, request, flash, redirect, render_template, url_for
from login_forms import SignInForms, SignUpForms
import emailp 
import time
from datetime import date
import bcrypt
import json
import os

curr_email = ""
pas = ""

SECRET_KEY = '123sam90@^'
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY



@app.route("/")
@app.route("/home")
def home():
    # with open('posts.json') as f:
    #     if os.stat('posts.json').st_size != 0:
    #         data = json.load(f)
    #         for i in data.keys():
    #             temp = {}
    #             temp = {
    #               "user":i,
    #               "date":data[i]["date"],
    #               "title":data[i]["title"],
    #               "content":data[i]["content"]      
    #             }
    with open('posts.json') as f:
        data = json.load(f)
    return render_template('home.html', post=data)


@app.route("/login", methods = ['POST', 'GET'])
def login():
    return render_template('login.html', form=SignInForms())

@app.route("/SignUp", methods=['POST', 'GET'])
def signUp():
    return render_template('SignUp.html', form=SignUpForms())

@app.route("/Posts")
def Posts():
    return render_template('posts.html')

@app.route("/auth", methods=['GET', 'POST'])
def auth():
    global curr_email, pas
    d = request.form.to_dict()
    if d.__contains__("SignUp"):
        if emailp.check_email(request.form["Email"]):
            if emailp.check(request.form["Password"]):
                if request.form["Password"] != request.form["CPassword"]:
                    flash("Password doesnt match")
                else:
                    curr_email, pas = request.form["Email"], bcrypt.hashpw(request.form["Password"].encode("utf8"), bcrypt.gensalt())
                    #user_pas[curr_email] = pas.decode()
                    temp_dict = {curr_email: pas.decode()}
                    with open('user_pass.json', 'r') as f:
                        if os.stat('user_pass.json').st_size == 0:
                            j_data  = temp_dict
                        else:
                           j_data = json.load(f)
                           j_data.update(temp_dict)
                    with open('user_pass.json', 'w') as f:
                        json.dump(j_data, f)
                    flash("Account created. Navigate to login page to post")
                    return redirect(url_for('signUp'))

            else:
                flash("Choose a strong Password")
                return redirect(url_for('signUp'))
        else:
            flash("Enter a valid email")
            return redirect(url_for('signUp'))
    else:
        curr_email, pas = request.form['Email'], request.form['Password']
        with open(r'E:\pre-intern-training\python_trn\FlaskProject\user_pass.json') as f:
            json_data = json.load(f)
        for i in json_data.keys():
            if i == curr_email:
                print(json_data[i].encode("utf8"))
                if bcrypt.checkpw(pas.encode("utf8"), json_data[i].encode("utf8")):
                    flash("Log In successful. Navigate to post to write your post.")
                    return redirect(url_for('login'))
                else:
                    flash("Please Enter the Correct Password")
                    return redirect(url_for('login'))
            else:
                flash("Please Enter the Correct Email Address")
                return redirect(url_for('login'))




@app.route("/post-content", methods=['POST', 'GET'])
def post_content():
    global curr_email
    if curr_email == "":
        flash("Please log in first to post")
        return redirect(url_for('Posts'))
    else:
        d = {
           curr_email:{"date": str(date.today()),
           "title": request.form["title"],
           "content":request.form["Post"]}
        }
        # UP.append(d)
        with open('posts.json', 'r') as f:
            if os.stat('posts.json').st_size == 0:
                j_data  = d
            else:
                j_data = json.load(f)
                j_data.update(d)
        with open('posts.json', 'w') as f:
            json.dump(j_data, f)
        flash("Your post has been posted.")
        return redirect(url_for('Posts'))


if __name__ == "__main__":
    app.run()
