from flask import Blueprint, render_template


bp = Blueprint('main', __name__, url_prefix='')


@bp.route('/')
def main():
  return '<h1>Main Page</h1>'
