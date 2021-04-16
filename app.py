from datetime import timedelta,date
from flask import Flask, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from model import *
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:reddy123@localhost:5432/book'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main():
    db.create_all()
   
    
    
if __name__ == "__main__":
    with app.app_context():
        main()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login")
def login():
    return render_template("SignIn.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/SignIn",methods=["POST"])
def SignIn():
    name = request.form.get("name")
    password = request.form.get("password")
    users = User.query.all()
    for user in users:
        if user.name == name:
            return render_template("search.html",name=name)
        else:
            continue
    return render_template("test.html")
@app.route("/search", methods=["POST"])
def search():
    name = request.form.get("name")
    user = Test.query.all()
    for i in user:
        if i.isbn==name:
            return render_template("book_details.html",isbn = i.isbn,title=i.title,author=i.author,year=i.year)
        else:
            return render_template("search.html")

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "GET":
        return "Please submit the form"
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        mobile = request.form.get("mobile")
        dob = request.form.get("dob")
        email = request.form.get("email")
        gender = request.form.get("gender")
        t = datetime.now()
        user = User(name=name, password=generate_password_hash(password, method='sha256'), mobile=mobile, dob=dob, email=email,gender=gender,timestamp=t)
        
        db.session.add(user)
        db.session.commit()
        
        
        return render_template("admin.html",users = User.query.all())

        #return render_template("submit.html", name=name, password=generate_password_hash(password, method='sha256'), mobile=mobile, dob=dob, email=email, gender=gender)
       
        #return render_template("admin.html", name=name, password=generate_password_hash(password, method='sha256'),timestamp=date.today())

