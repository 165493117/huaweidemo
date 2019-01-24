from flask import Flask, request,  render_template

app = Flask(__name__,template_folder='static/views')

@app.route('/')
def hello_world():
    return render_template('index.html')

# 动态路由
@app.route('/hello/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello %s' % username

# http请求
@app.route('/login',methods=['GET', 'POST'])
def login():
    #判断是post还是get
    print(request.method)
    if request.method=='POST':
        return 'Your input: Username: '+request.form['username']+" Password: "+request.form['password']
    else:
        print('get')
        return '''
                <form action="/login" method="post">
                    Username: <input name="username" type="text" />
                    Password: <input name="password" type="password" />
                    <input value="Login" type="submit" />
                </form>
            '''

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run( host='0.0.0.0',port=8080)