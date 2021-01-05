from flask import Flask, render_template
from webapp.model import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

        
@app.route("/")
def index():
    products = {}
        
    
    return render_template("products_list.html")

print(product_list)
if __name__ == "__main__":
    app.run()
