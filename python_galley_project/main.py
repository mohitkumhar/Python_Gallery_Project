from flask import Flask, request, render_template, session, redirect
import json
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import math
from flask_login import login_user, login_manager, LoginManager


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

app.secret_key = 'my_secret_key'
app.config['UPLOAD_FOLDER'] = params['image_upload_location']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/my_album_project'
db = SQLAlchemy(app)


class Gallery(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    memories = db.Column(db.String(500),unique=False, nullable=False)
    slug = db.Column(db.String(500), nullable=False)
    img_file = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=True)




@app.route('/')
def pagination():
    if 'user' in session and session['user'] == params['admin_user']:
        photo = Gallery.query.filter_by().all()
        page = request.args.get('page')
        last = math.ceil(len(photo)/int(params['noOfPhoto_onHomePage']))
        if(not str(page).isnumeric()):
            page=1
        page=int(page)
        photo = photo[(page-1)*int(params['noOfPhoto_onHomePage']):(page-1)*int(params['noOfPhoto_onHomePage'])+int(params['noOfPhoto_onHomePage'])]
        # PAGINATION LOGIC
        # FIRST PAGE
        if(page==1):
            next = "/?page="+ str(page+1)
            prev ="#"
        elif(page==last):
            next = "#"
            prev = "/?page="+ str(page-1)
        else:
            next = "/?page="+ str(page+1)
            prev = "/?page="+ str(page-1)

        return render_template('index.html', params=params, photo=photo, next=next, prev=prev)
    return render_template("login.html", params=params)





@app.route('/basic-actions')
def basicactions():
    return render_template('basic_actions.html', params=params)


@app.route('/view/<string:view_slug>', methods = ['GET'])
def photos(view_slug):

    photo = Gallery.query.filter_by(slug=view_slug).first()
    return render_template('view.html', params=params, photo=photo)
    
@app.route('/basic-actions/<string:add_photo>', methods = ['GET', 'POST'])
def add_photo(add_photo):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            sno = request.form.get('sno')
            memo = request.form.get('memo')
            slug = request.form.get('slug')
            img_file = request.form.get('img_file')
            date = datetime.now()
            if add_photo == 'add-photo':
                photo = Gallery(sno=sno, memories=memo, slug=slug, img_file=img_file, date=date)
                db.session.add(photo)
                db.session.commit()
            return render_template('add.html', params=params)
    return render_template('add.html', params=params)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if (request.method == 'POST'):
            f= request.files['upload']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return redirect('/basic-actions')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

@app.route('/delete/<string:slug>', methods = ['POST', 'GET'])
def delete(slug):
    photo = Gallery.query.filter_by(slug=slug).first()
    db.session.delete(photo)
    db.session.commit()
    return redirect('/')



@app.route('/edit/<string:slug>', methods = ['POST', 'GET'])
def edit(slug):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            sno = request.form.get('sno')
            memo = request.form.get('memo')
            slug = request.form.get('slug')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if slug == 'add-photo':
                    photo = Gallery(sno=sno, memories=memo, slug=slug, img_file=img_file, date=date)
                    db.session.add(photo)
                    db.session.commit()
            else:
                photo = Gallery.query.filter_by(slug=slug).first()
                photo.sno = sno
                photo.memories = memo
                photo.slug = slug
                photo.img_file = img_file
                photo.date = date
                db.session.add(photo)
                db.session.commit()
                return redirect('/edit/'+slug)

        photo = Gallery.query.filter_by(slug=slug).first()
        return render_template('edit.html', photo=photo, params=params)
    return render_template('login.html', params=params)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    photo = Gallery.query.filter_by().all()

    if 'user' in session and session['user'] == params['admin_user']:
        return render_template('index.html', params=params, photo=photo)

    if request.method == 'POST':
        # username = request.form['username']
        # password = request.form['password']
        username = request.form.get('username')
        password = request.form.get('password')

        if (username == params['admin_user'] and password == params['admin_password']):
            session['user'] = username
            return render_template('index.html', params=params, photo=photo)
        
    return render_template('login.html', photo=photo, params=params)

app.run(debug=True)
