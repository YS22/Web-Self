from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid,models
from forms import LoginForm
from models import User
from forms import LoginForm, CommentForm
from models import User, Git_comment,Python_comment,Javascript_comment
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = CommentForm()
    if form.validate_on_submit():
        comment1 = Git_comment(body=form.comment.data, timestamp=datetime.utcnow(), author=g.user)
        db.session.add(comment1)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('index'))
    comments1= models.Git_comment.query.all()

       
    return render_template('index.html',
                           title='Home',
                           form=form,
                           comments1=comments1)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/python', methods=['GET', 'POST'])
@login_required
def python():
    form = CommentForm()
    if form.validate_on_submit():
        comment2 = Python_comment(body=form.comment.data, timestamp=datetime.utcnow(), author=g.user)
        db.session.add(comment2)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('python'))
    comments2= models.Python_comment.query.all()

       
    return render_template('python.html',
                           title='Home',
                           form=form,
                           comments2=comments2)



@app.route('/javascript', methods=['GET', 'POST'])
@login_required
def javascript():
    form = CommentForm()
    if form.validate_on_submit():
        comment3 = Javascript_comment(body=form.comment.data, timestamp=datetime.utcnow(), author=g.user)
        db.session.add(comment3)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('javascript'))
    comments3= models.Javascript_comment.query.all()

       
    return render_template('javascript.html',
                           title='Home',
                           form=form,
                           comments3=comments3)
