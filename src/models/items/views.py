from flask import Blueprint

__author__ = 'nebby85'


item_blueprint = Blueprint('items', __name__)


@item_blueprint.route('/item/<string:name>')
def item_page():
    pass
