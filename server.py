from flask import Flask, render_template, session, redirect, request # added render_template!
from user import Users
app = Flask(__name__)
app.secret_key="rootroot"

@app.route("/")
def index():
    
    return render_template("create.html")

@app.route('/input_user', methods = ["POST"])
def input():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Users.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/display_users')

@app.route('/display_users')
def display():
    all_users=Users.get_all()
    return render_template("/read.html", all_users = all_users)




if __name__ == "__main__":
    app.run(debug=True)


















# @app.route('/friend/show/<int:friend_id>')
# def show(user_id):
#     # calling the get_one method and supplying it with the id of the friend we want to get
#     user=User.get_one(user_id)
#     return render_template("read.html", user= user)


# @app.route('/users/create', methods=['POST'])
# def create():
#     User.save(request.form)
#     return redirect('/read.html') #unsure about this one

# @app.route('/create')
# def create():
#     return render_template("read.html") #unsure about this one 





