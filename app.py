from time import sleep

from flask import Flask, request

from datetime import datetime

import jieba, jieba.posseg

app = Flask(__name__, static_folder='jieba')


@app.route('/', methods=['GET'])
def index():
    return {
        'time': datetime.now(),
    }


@app.route('/', methods=['POST'])
def start():
    form = request.form.to_dict()

    mode = form.get('mode', 'cut_for_search')
    body = form.get('body', 'hello')
    cut_all = bool(form.get('is_cut_all', False))

    data = {
        'cut': jieba.cut(body, cut_all),
        'cut_for_search': jieba.cut_for_search(body),
    }.get(mode)

    return {
        'mode': mode,
        'datas': list(data),
    }


@app.route('/posseg', methods=['POST'])
def posseg():
    form = request.form.to_dict()

    possegs = jieba.posseg.cut(form.get('body', 'hello'))

    datas = {}
    words = []

    for info in possegs:
        flag = info.flag
        word = info.word

        if flag not in datas:
            datas[flag] = []

        datas[flag].append(word)
        words.append(word)

    return {
        'datas': datas,
        'words': words,
    }


@app.route('/search', methods=['POST'])
def search():
    form = request.form.to_dict()

    body = form.get('body', 'hello')

    possegs = jieba.posseg.cut(body)

    datas = {}

    for info in possegs:
        flag = info.flag
        word = info.word

        if flag not in datas:
            datas[flag] = []

        datas[flag].append(word)

    search = list(jieba.cut_for_search(body))

    return {
        'posseg': datas,
        'search': search,
    }


if __name__ == '__main__':
    app.run(debug=True)
