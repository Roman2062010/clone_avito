from flask import Flask, render_template
from webapp.model import db, Ad, Location, User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

        
    @app.route("/")
    def index():
        products = Ad.query.all()
        return render_template("products_list.html", products=products)
    

    @app.route("/product/<product_id>/")
    def product(product_id):
        product = Ad.query.filter(Ad.id == product_id).first()
        return render_template("product.html", product=product)


    @app.route("/<region_name>/")
    def region(region_name):
        print(region_name)
        products = Ad.query.join(Location,Ad.location_id == Location.id).filter(Location.name == region_name).all()
        return render_template("products_list.html", products=products)


    @app.route("/<user_name>/")
    def user(user_name):
        print(user_name)
        products = Ad.query.join(User,Ad.user_id == User.id).filter(User.username == user_name).all()
        return render_template("products_list.html", products=products)


    return app
