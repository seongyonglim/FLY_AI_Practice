from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix
import myutils as my
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_iris(mode=None):
    iris = pd.read_csv('iris.csv')
    df = iris.drop(['Id'], axis=1).copy()
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
   
    if(mode == 'bin'):
        df = df.loc[df['species'] != 'Iris-virginica']
       
    df['species']= df['species'].map({
        'Iris-setosa':0,
        'Iris-versicolor':1,
        'Iris-virginica':2
    })
    X = df.drop(['species'], axis=1)
    y= df['species']

    
    return train_test_split(X, y, test_size=0.2, random_state=2022)

# 평가 지표 : metrics
# 알고리즘의 성능평가

def print_score(y_true, y_pred, average='binary'):
    acc = accuracy_score(y_true, y_pred)
    pre = precision_score(y_true, y_pred, average=average)
    rec = recall_score(y_true, y_pred, average=average)
    
    print('accuracy : ', acc)
    print('precision : ', pre)
    print('recall : ', rec)
    
    



    
def plot_confusion_matrix(y_true, y_pred):
    cfm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5,5))
    sns.heatmap(cfm, annot=True, cbar=False, fmt='d')
    plt.xlabel('Predicted Class')
    plt.ylabel('True Class')
    plt.show()