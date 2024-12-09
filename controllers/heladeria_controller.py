from models.heladeria import User,Producto 
from flask import Blueprint, render_template, request, flash, redirect, url_for, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
global COOKIE_TIME_OUT

#from app import db


heladeria_blueprint = Blueprint('heladeria_bp', __name__)
COOKIE_TIME_OUT = 60 * 1 #60 * 5  # 5 minutos

from werkzeug.security import generate_password_hash
print(generate_password_hash("demo123"))



@heladeria_blueprint.route('/')
def index():
    if 'email' in session:
        user_rs = User.query.filter_by(email=session['email']).first()
        return render_template('index.html', user_rs=user_rs)
    return redirect(url_for('heladeria_bp.login'))

@heladeria_blueprint.route('/index')
def login():
    return render_template('login.html')

 
@heladeria_blueprint.route('/login', methods=["GET", "POST"])
def login_submit():
    if request.method == 'POST':
        _email = request.form.get('inputEmail')
        _password = request.form.get('inputPassword')

        if not _email or not _password:
            flash('Correo y contraseña son obligatorios.', 'error')
            return redirect(url_for('heladeria_bp.login'))

        user = User.query.filter_by(email=_email).first()

        if user:
            if check_password_hash(user.password_hash, _password):
                session['email'] = user.email
                return redirect(url_for('heladeria_bp.index'))
            else:
                flash('Contraseña incorrecta. Inténtalo de nuevo.', 'error')
        else:
            flash('Usuario no encontrado bd heladeria. Verifica tu correo electrónico.', 'error')

        return redirect(url_for('heladeria_bp.login'))
 
 
    return render_template('login.html')

@heladeria_blueprint.route('/logout')
def logout():
    session.pop('email', None)
    resp = make_response(redirect(url_for('heladeria_bp.login')))
    resp.delete_cookie('email')
    resp.delete_cookie('pwd')
    return resp


#para pruebas 
@heladeria_blueprint.route('/empleados')
def empleados():
    # Verifica si el usuario ha iniciado sesión
    if 'email' not in session:
        flash('Acceso restringido. Por favor, inicia sesión primero.', 'error')
        return redirect(url_for('heladeria_bp.login'))

    # Si el usuario está en sesión, renderiza la página de empleados
    return render_template('empleados.html')



#@public_bp.route("/error")
@heladeria_blueprint.route('/error')
def show_error():
    res = 1 / 0
    posts = Post.get_all() # type: ignore
    return render_template("public/index.html", posts=posts)




""" @heladeria_blueprint.route('/producto')
def ver_productos():
    productos = Producto.query.all()
    #return render_template("listar_users.html",listar)
    return render_template ("productos.html",productos=productos) # ("listar_users.html",heladerheladerias=heladerias)
 """

@heladeria_blueprint.route('/ver_productos')
def ver_productos():
    productos = Producto.query.all()
    # Verifica si el usuario ha iniciado sesión
    if 'email' not in session:
        flash('Acceso restringido a Productos. Por favor, inicia sesión primero.', 'error')
        return redirect(url_for('heladeria_bp.login'))
    # Si el usuario está en sesión, renderiza la página de productos
    return render_template('productos.html',productos=productos)