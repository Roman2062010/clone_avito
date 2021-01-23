from flask import Flask, request, render_template
from webapp.forms import LoginForm
from webapp.model import db, Ad, Location, User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

        
    @app.route("/")
    def index():
        products = Ad.query.all()
        users = User.query.all()
        locations = Location.query.all()
        return render_template("products_list.html", products=products, users=users, locations=locations)

    
    @app.route('/login')
    def login():
        title = "Авторизация" 
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    
    @app.route("/product/<product_id>/")
    def product(product_id):
        product = Ad.query.filter(Ad.id == product_id).first()
        return render_template("product.html", product=product)


    @app.route("/locations/<location_id>/")
    def regions(location_id):
        products = Ad.query.join(Location,Ad.location_id == Location.id).filter(Location.id == location_id).all()
        locations = Location.query.all()
        return render_template("products_list.html", products=products, locations=locations)


    @app.route("/users/<user_id>/")
    def users(user_id):
        products = Ad.query.join(User,Ad.user_id == User.id).filter(User.id == user_id).all()
        users = User.query.all()
        return render_template("products_list.html", products=products, users=users)
 

    return app
