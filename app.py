from flask import Flask, render_template, request
app=Flask(__name__)
n=0
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/login')
def login():
    return render_template('login.html')
     
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login_validation', methods=['POST'])
def login_validation():
    global n
    n+=1
    return "The name is {} and the password is".format(n)

if __name__=="__main__":
    app.run(debug=True)
