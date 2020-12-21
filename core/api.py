# -*- coding: utf-8 -*-
"""
API
----
ALL application can be use
"""
from core.model import get_model

__all__ = ["train", "recognize"]


def train(model_name='model', tfidf_vectorizer='tfidf_vectorizer'):
    """
    model training
    """
    model = get_model()

    model.train(model_name, tfidf_vectorizer)


def recognize(sentence, model_name='model', tfidf_vectorizer='tfidf_vectorizer'):
    """
    interrogative sentence recognize
    """
    model = get_model()
    prob = model.predict(sentence, model_name, tfidf_vectorizer)[0]
    return prob
