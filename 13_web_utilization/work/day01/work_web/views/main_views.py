from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/') 

@bp.route('my_part')
def main_about():
    return "ABOUT MAIN"

@bp.route('/')
def main_page():
    return render_template('file1.html')