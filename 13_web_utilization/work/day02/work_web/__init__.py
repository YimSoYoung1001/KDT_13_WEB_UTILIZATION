from flask import Flask, render_template, url_for 

def create_app():
    app = Flask(__name__)

    from flask import Blueprint
    from .views import data_view

    app.register_blueprint(data_view.data_BP)

    # 테스트 기능
    with app.test_request_context():
        print(url_for('static', filename = 'css/my.css'))

    return app