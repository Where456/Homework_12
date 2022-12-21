import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import search_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_words = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = search_word(search_words)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', query=search_words, posts=posts)

