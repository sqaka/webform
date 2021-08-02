import pandas as pd
from sklearn import metrics
import matplotlib


BASE_PATH = 'static/basedata/answer.tsv'
PLOT_PATH = 'image/'


def evaluate_tsv(dt_txt, tsv_path):
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    base_df = pd.read_table(BASE_PATH)
    pred_df = pd.read_table(tsv_path)
    base_y = base_df.answer
    pred_y = pred_df.answer
    fpr, tpr, thresholds = metrics.roc_curve(base_y, pred_y, pos_label=1)
    result = round(metrics.auc(fpr, tpr), 3)
    plt.plot(fpr, tpr, marker='o')
    plt.xlabel('FPR: False positive rate')
    plt.ylabel('TPR: True positive rate')
    plt.grid()
    img_path = '{}{}.png'.format(PLOT_PATH, dt_txt)
    plt.savefig('static/{}'.format(img_path))

    return result, img_path
