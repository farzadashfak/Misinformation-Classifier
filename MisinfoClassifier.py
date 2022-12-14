import pandas as pd
import numpy as np
import itertools

from google.colab import files
uploaded = files.upload()

data = pd.read_csv("news.csv")
print(data.shape)
data.head()

labels = data.label
labels.head()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(data["text"],data["label"],test_size=0.2,random_state=7)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)

from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])

