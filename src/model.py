import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pickle

# CSV の読み込み（raw文字列でエスケープシーケンスを回避）
df = pd.read_csv(r"..\database\data.csv", encoding="utf-8", on_bad_lines='skip')

# CSV の例:
# age,nationality,product_A,product_B,product_C
# 25,jp,4,3,5
# 30,th,2,5,1
# ...

# 前処理：国籍 "jp" / "th" を one-hot encoding（drop_first=True で "nationality_th" のみ残る）
df_encoded = pd.get_dummies(df, columns=["nationality"], drop_first=True)

# 特徴量と目的変数の設定
X = df_encoded.drop(["product_A", "product_B", "product_C"], axis=1)
y = df_encoded[["product_A", "product_B", "product_C"]]

# データ分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 基本モデルの構築（max_iter を1000に増やして収束しやすくする）
base_estimator = LogisticRegression(solver="lbfgs", max_iter=1000)
multi_target_model = MultiOutputClassifier(base_estimator)
multi_target_model.fit(X_train, y_train)

# 予測の実行
y_pred = multi_target_model.predict(X_test)

# 各商品の評価結果を個別に表示
for idx, col in enumerate(y.columns):
    print(f"=== Classification Report for {col} ===")
    print(classification_report(y_test[col], y_pred[:, idx]))
    acc = accuracy_score(y_test[col], y_pred[:, idx])
    print(f"Accuracy for {col}: {acc:.2f}\n")

# 学習済みモデルの保存
with open("spiciness_multi_model.pkl", "wb") as f:
    pickle.dump(multi_target_model, f)

print("モデルの学習と保存が完了しました。")
