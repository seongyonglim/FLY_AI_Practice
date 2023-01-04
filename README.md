# FLY AI 수업

## 12/19 

+ conda 가상환경 3.8 - colab 맞추기

+ jupyter lab 에서 flyai 가상환경 제작
```
python -m ipykernel install --user --name flyai --display-name "flyai"
jupyter lab
```
+ numpy 버전 1.21.0
```
pip install numpy==1.21.0
```
## 12/20

+ pandas 버전 최신버전
```
!pip install pandas --upgrade  #jupyter lab에서 설치하려면 앞에 ! 를 붙인다
```
+ 구글 드라이브에서 다운 받아오는 모듈
```
!pip install gdown
```
## 12/21
+ matplotlib 최신버전
```
!pip install --upgrade --user matplotlib
```
+ pillow 최신버전 설치 (이미지 처리)
```
!pip install pillow
```
+ seaborn 최신버전 설치
```
!pip install seaborn --upgrade --user
```

## 12/22~12/29
+ COVID 확진 판정으로 인해 수업 불참

## 12/30
+ kaggle.com 에서 다른 사람의 데이터 처리 방식 확인 하는 법
+ imbalanced-learn 설치
```
!pip install imbalanced-learn
```
+ XGboost 설치
```
!pip install xgboost
```
+ LightGBM 설치
```
!pip install lightgbm
```
+ kaggle titanic 다른 분들의 작성 코드 학습

## 1/2
+ LinearRegression (선형 회귀)
+ Gradient Descent (경사 하강법)
+ LogisticRegression (로지스틱 회귀)
+ Perceptron (퍼셉트론)
+ Backpropagation (오차 역전파) *** 중요

## 1/3
+ Binary, Multi Classification (이중, 다중 분류)
+ Model 제작 
```
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
```
+ Confusion Matrix

## 1/4
+ Fully Connected Layer (완전연결층)
+ 이미지 분류