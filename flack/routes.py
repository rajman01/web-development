from flack import app
from flask import render_template
from flack.forms import LoginForm, RegistrationForm, RequestResetForm, ResetPasswordForm, ContactUsForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/reset_password')
def reset_request():
    form = RequestResetForm()
    return render_template('reset-request.html', title='Reset password', form=form)


@app.route('/reset_password/token')
def reset_token():
    form = ResetPasswordForm()
    return render_template('reset-token.html', title='Reset password', form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/service')
def service():
    return render_template('service.html', title='Service')


@app.route('/contact')
def contact():
    form = ContactUsForm()
    return render_template('contact.html', title='Contact', form=form)


@app.errorhandler(404)
def error_404():
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500():
    return render_template('500.html'), 500
