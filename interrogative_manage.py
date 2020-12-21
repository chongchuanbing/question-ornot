# -*- coding: utf-8 -*-

import jieba
from core.api import *
import time

# 七万数据量 (1.2s)
sufffix = '201905311500'

# 三万数据量(1.0s)
sufffix = '20190714112043'

# 一万数据量(880ms)
sufffix = '20190714134618'

# 1k(800ms)
# sufffix = '20190714140231'

# 200(700ms)
# sufffix = '20190714140531'

model_name = 'model-' + sufffix
tfidf_vectorizer = 'tfidf_vectorizer-' + sufffix

# train(model_name=model_name, tfidf_vectorizer=tfidf_vectorizer)

# tag = recognize(u'今天 来 点 兔子 吗')

# text = '今天天气怎么样'
text = '最近好吗'
# text = '在吗'
text = '谁能教我怎么样和别人聊天'

tokenizer = jieba.Tokenizer()

start_time = time.time();

cut_result = tokenizer.cut(text)

end_time = time.time()

print('cut costTime: %f' % (time.time() - start_time))

prob = recognize(' '.join(cut_result), model_name, tfidf_vectorizer)

print('rec costTime: %f' % (time.time() - end_time))

output = '是疑问句' if prob > 0.5 else '不是疑问句'
print(output, prob)


# import pandas as pd
#
#
# def judge_question(content):
#     cut_result = tokenizer.cut(content)
#     prob = recognize(' '.join(cut_result), model_name, tfidf_vectorizer)
#
#     # print(content, prob)
#
#     return prob
#
# def validate_test(file_path, key):
#
#     df = pd.read_csv(file_path, encoding='utf-8')
#
#     df['prob'] = df[key].astype(str).apply(judge_question)
#     df['is_question'] = df['prob'].values > 0.5
#
#     df[[key, 'prob', 'is_question']].to_csv('./Params/question_test.csv', encoding='utf-8')
#
#
# # validate_test('./Params/question_recog_7w.csv', 'content')
# # validate_test('./Params/baidu_valid_question.csv', 'content')
# validate_test('./Params/test_sentence.csv', 'sentences')


# df = pd.read_csv('./Params/question_recog_7w.csv', encoding='utf-8')
# print(df['content'].count)

# df = pd.read_csv('./Params/question_test.csv', encoding='utf-8')
# # df = pd.read_csv('./Params/baidu_valid_question.csv', encoding='utf-8')
#
# df = df.loc[df['label'].values != df['judge'].values]
#
# print(df)



# from sklearn.feature_extraction.text import TfidfVectorizer
#
# def analyzer(x):
#     return x.split()
#
#
# df = pd.read_csv('./Params/question_recog_7w.csv', encoding='utf-8')
# df['tokens'] = df.loc[:5, 'content'].astype('str').apply(lambda x: list(tokenizer.cut(x)))


# a = ' '.join(list(tokenizer.cut('谁能教我怎么样和别人聊天')))
# print(a)
# b = ' '.join(list(tokenizer.cut('最近好吗')))
# print(b)
#
# result = []
# result.append(a)
# result.append(b)
# print(result)

# result = df.loc[:5, 'tokens'].apply(lambda x: ' '.join(x)).tolist()
#
# print(result[0])
# print(result[1])
# print(result[2])
# print(result[3])
# print(result[4])
# print(result[5])
#
# vectorizer = TfidfVectorizer(smooth_idf=True,
#                                      analyzer=analyzer,
#                                      ngram_range=(1, 1),
#                                      min_df=1, norm='l1')
# sparse_vector = vectorizer.fit_transform(result[0:5])
#
# print(sparse_vector)
# print(vectorizer.get_params())