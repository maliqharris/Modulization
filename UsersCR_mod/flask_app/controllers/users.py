
from flask_app import app, render_template, redirect, request
from flask_app.models.users import Users


# CREATE
@app.route("/new")
def new():
    return render_template('new.html')

@app.route("/create", methods=['post'])
def create_friend():
    print(request.form)
    Users.save(request.form)
    return redirect('/')



#  READ ALLL
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = Users.get_all()
    print(users)
    return render_template("index.html", users = users)



# READ ONE
@app.route('/user/<int:id>')
def info(id):
    data = {'id':id}
    users = Users.get_one(data)

    return render_template('info.html', users = users)
   



# UPDATE
@app.route('/user/edit/<int:id>')
def edit(id):

    data = {'id':id}
    
    users = Users.get_one(data)
    
    return render_template('edit.html', users = users)
@app.route('/update', methods = ['post'])
def update_user():
    Users.update(request.form)


    return redirect('/')


#Delete
@app.route('/user/delete/<int:id>')
def delete(id):
    Users.delete(id)
    return redirect('/')

            
