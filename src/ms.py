import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 例: CSVファイルに 'ingredients'（成分表）と 'spiciness'（辛さスコア）のカラムがあるとする
data = pd.read_csv('src/food_spiciness_data.csv')

# 特徴量（成分表）とラベル（辛さスコア）に分ける
X = data['ingredients']
y = data['spiciness']

# TF-IDFベクトル化（カンマや句読点で分割するカスタムトークナイザーを利用）
vectorizer = TfidfVectorizer(tokenizer=lambda x: x.replace("、",",").split(','))
X_vectorized = vectorizer.fit_transform(X)

# 訓練用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# 線形回帰モデルの訓練
model = LinearRegression()
model.fit(X_train, y_train)

# テストデータで予測し、評価
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("テストデータでのRMSE:", rmse)

# 例: ハイパーパラメータのチューニング（必要に応じて他のモデルで試す）
param_grid = {'fit_intercept': [True, False], 'normalize': [True, False]}
grid_search = GridSearchCV(LinearRegression(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print("最適なパラメータ:", grid_search.best_params_)
