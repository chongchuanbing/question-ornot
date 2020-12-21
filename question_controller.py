#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from flask import Flask, request
import time
import argparse
from flask_cors import *
import configparser
import jieba
import json

from core.api import *

from dto.ResponseVo import ResponseVo
from util.log_common import Logger
from util.json_common import JsonCommon

logger = Logger(level='info').getlog()
logger_error = Logger(filename='error.log', level='error').getlog()

Config = configparser.ConfigParser()
Config.read("config.ini")

model_base_path = Config.get("model", "base_path")
suffix = Config.get("model", "suffix")

json_common = JsonCommon()

questionornot_app = Flask(__name__)
CORS(questionornot_app)

model_name = 'model-' + suffix
tfidf_vectorizer = 'tfidf_vectorizer-' + suffix

tokenizer = jieba.Tokenizer()

cut_result = tokenizer.cut('今天天气好吗')

recognize(' '.join(cut_result), model_name, tfidf_vectorizer)

@questionornot_app.route('/questionOrNot', methods=['POST'])
def question_ornot():

    start_time = time.time()

    param_json = request.get_json()

    if 'question' not in param_json:
        responseVo = ResponseVo('', -1, 'false', '参数为空')
        return json_common.to_json(responseVo)

    question = param_json['question']

    cut_result = tokenizer.cut(question)

    prob = recognize(' '.join(cut_result), model_name, tfidf_vectorizer)

    logger.info('costTime: %4f, question: %s' % (time.time() - start_time, question))

    responseVo = {
        'data': {
            'question': str(question),
            'confidence': float(prob)
        },
        'code': 1,
        'success': True
    }

    result_json = json.dumps(responseVo, ensure_ascii=False)

    return result_json

def parse_args():
    parser = argparse.ArgumentParser(description='question_ornot',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--h', dest='host', help='the server address', nargs="+",
                        default=['localhost'], type=str)
    parser.add_argument('--p', dest='port', help='the server port', nargs="+",
                        default=[5000], type=int)
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    # args = parse_args()
    # host = args.host[0]
    # port = args.port[0]
    # logger.info('the server host : %s, port : %s', host, port)

    from werkzeug.contrib.fixers import ProxyFix
    questionornot_app.wsgi_app = ProxyFix(questionornot_app.wsgi_app)

    questionornot_app.run()
    # app.run(debug=True)
    # app.run(host=host, port=port)

