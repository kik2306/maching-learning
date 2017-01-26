# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline 
from sklearn.linear_model import SGDClassifier

def read_text(file):   
    length_file = len(file.readlines())
    file.seek(0)
    mas_text = []
    for i in range(0, length_file):
        mas_text.append(file.readline())
    file.seek(0)
    return mas_text

def read_text_without_a_category(file): 
    length_file = len(file.readlines())
    file.seek(0)
    mas_text = []
    for i in range(0, length_file):
        a = file_train.readline().strip().split()
        a.pop(0)
        c = ' '
        a = c.join(a)
        mas_text.append(a)
    file.seek(0)
    return mas_text

def category_and_target(file): 
    category = []
    target_of_category = []
    length_file = len(file.readlines())
    file.seek(0)
    for i in range(0,length_file):
        category.append(file.readline().strip().split()[0])
        target_of_category.append(find_target(category[i]))
    file.seek(0)
    return category,target_of_category

def find_target(word):  
    for i in range(0,10):
        if word == categories[i]:
            return target[i]

if __name__ == '__main__':
    categories = ['science', 'style', 'culture', 'life', 'economics', 'business', 'travel', 'forces', 'media', 'sport']
    target = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    file_train = open('C:\\Users\\1\\Desktop\\maching learning\\news_train.txt',
                      encoding='utf8')
    file_for_prediction = open(
        'C:\\Users\\1\\Desktop\\maching learning\\news_test.txt',
        encoding='utf8')
    data = read_text_without_a_category(file_train) # исходные данные без категории
    data_for_prediction = read_text(file_for_prediction) # данные, для которых делается предсказание категорий
    mas_categories, mas_target = category_and_target(file_train) 
    vectorizer = CountVectorizer()  # токенизация
    x_train = vectorizer.fit_transform(data)  #строит словарь индексов признаков
    tfidf_transformer = TfidfTransformer()  # обратная частота слова
    x_train_tfidf = tfidf_transformer.fit_transform(x_train)    
    clf = SGDClassifier().fit(x_train_tfidf, mas_target) # обучение классификатора методом опорных векторов
    text_clf = Pipeline([('vectorizer', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier())])
    text_clf = text_clf.fit(data, mas_target) # обучение
    prediction = text_clf.predict(data_for_prediction) # предсказание
    output_file = open('C:\\Users\\1\\Desktop\\maching learning\\Results.txt','w')
    # запись в файл, предназначенный для предсказанных результатов
    for i in range(len(prediction)):
        output_file.write(categories[prediction[i]]+'\n')
    file_train.close()
    file_for_prediction.close()
    output_file.close()

