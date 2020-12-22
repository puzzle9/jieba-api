from flask import Flask, request

from datetime import datetime

import jieba

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
        'datas': (','.join(data)).split(','),
    }


if __name__ == '__main__':
    app.run(debug=True)
