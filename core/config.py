# -*- coding: utf-8 -*-
"""
CONFIG
------
对配置的封装
"""
config_instance = None


class Config:

    def __init__(self):
        self.config_dict = {
            'interrogative': {
                'corpus_path': 'Params/question_recog_2h.csv',
                'tfidf_vectorizer_path': 'Params/{}.model',
                'test_path': 'Params/test.conll',
                'test_process_path': 'Params/test.Params'
            },
            'model': {
                'max_depth': [4, 5, 6],
                'eta': [0.1, 0.05, 0.02],
                'subsample': [0.5, 0.7, 1.0],
                'max_iterations': 100,
                'objective': ['binary:logistic'],
                'silent': [1],
                'num_boost_round': 2000,
                'nfold': 5,
                'stratified': 1,
                'metrics': 'auc',
                'early_stopping_rounds': 10,
                'model_path': 'Params/{}.model'
            }
        }

    def get(self, section_name, arg_name):

        return self.config_dict[section_name][arg_name]


def get_config():
    global config_instance
    if not config_instance:
        config_instance = Config()
    return config_instance
