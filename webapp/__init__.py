from flask import Flask, render_template
from webapp.model import db, Ad

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

        
    @app.route("/")
    def index():
        products = Ad.query.all()
        return render_template("products_list.html", products=products)

    return app