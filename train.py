import jieba
from core.api import *
import time

time_struct = time.strftime("%Y%m%d%H%M%S", time.localtime())

model_name = 'model-' + time_struct
tfidf_vectorizer = 'tfidf_vectorizer-' + time_struct

train(model_name=model_name, tfidf_vectorizer=tfidf_vectorizer)

