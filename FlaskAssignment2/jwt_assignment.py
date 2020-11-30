from flask import Flask, request, make_response
from flask_restful import Resource, Api
import jwt
import datetime
import json
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = "Isthisthereallife"

api = Api(app)

blog = [
    {
        "id":1, "user":"Sam", "content":"ABiofhpaw oefhwaofiwq[efwq[ef[wqe"
    },
    {
        "id":2, "user":"Spurgeon", "content":"ABiofhpaw oefcssdvsdcsewfaefasdfasd"
    }
]

token = None



def Checktoken(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        if not token: return {"token_info":"Token is missing"}
        try: 
            a = jwt.decode(token, app.config['SECRET_KEY'])
        except: 
            return {"token_info":"Token is invalid"}
        return f(*args, **kwargs)
    return wrapper


class Blog(Resource):
    @Checktoken
    def get(self, i):
        return next(filter((lambda x: x["id"] == i) ,blog), None)

api.add_resource(Blog, '/blog/get/i')       

@app.route("/")
def home():
    return '''
    <h>from Home</h1>
    '''
@app.route("/login", methods=['GET'])
def login():
    return '''
    <html>
       <body>
          <form method="POST" action="/auth">
            Name:<input type="text" name="uname">
            Password:<input type="password" name="pass">
            <input type="submit"> 
          </form>
       </body>
    </html>
    '''        
@app.route("/auth", methods=['GET', 'POST'])
def auth():
    print("entered into auth {}".format(request.form))
    uname = request.form["uname"]
    pas = request.form["pass"]
    if pas == "password":
        global token
        token = jwt.encode(payload={"user":123, "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},key=app.config['SECRET_KEY'])          
        return {"token generated":token.decode('utf8')}
    return "invalid"

if __name__ == "__main__":
    app.run(debug=True)

