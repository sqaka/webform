from datetime import datetime
import os
import re
from flask import Flask, render_template, request, send_from_directory

from utils.auto_eraser import main as auto_eraser
from utils.evaluate_tsv import evaluate_tsv

DATA_PATH = 'static/data/'

app = Flask(__name__)


@app.route('/')
def index():
    auto_eraser()
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def recbutton():
    if request.method == 'POST':
        now = datetime.now()
        dt_txt = '{0:%Y%m%d%H%M%S}'.format(now)
        f = request.files['file']
        tsv_path = os.path.join('{}{}.tsv'.format(DATA_PATH, dt_txt))
        f.save(tsv_path)
        result, img_path = evaluate_tsv(dt_txt, tsv_path)
        img_path = re.sub('static/image/', 'image/', img_path)
        return render_template('result.html', result=result, path=img_path)
    else:
        return render_template('index.html')


def main():
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
