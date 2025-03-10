import pickle
import pandas as pd

# ① 学習済みモデルの読み込み
with open("..\src\spiciss_model.pkl", "rb") as f:
    model = pickle.load(f)

# ② ユーザ入力の取得
try:
    age = float(input("年齢を入力してください: "))
except ValueError:
    print("数値を入力してください。")
    exit()

nationality_input = input("国籍を入力してください（タイ or 日本）: ").strip()
# 数値にエンコード（タイ: 0, 日本: 1）
if nationality_input == "日本":
    nationality = 1
elif nationality_input == "タイ":
    nationality = 0
else:
    print("無効な国籍です。")
    exit()

# ③ 各商品の辛さは、実際はデータベースから取得しますが、ここでは例として固定値を使用
product1_spiciness = 7
product2_spiciness = 5
product3_spiciness = 9

# ④ 入力データのDataFrame作成
input_data = pd.DataFrame({
    'age': [age],
    'nationality': [nationality],
    'product1_spiciness': [product1_spiciness],
    'product2_spiciness': [product2_spiciness],
    'product3_spiciness': [product3_spiciness]
})

# ⑤ 予測の実行
prediction = model.predict(input_data)
# prediction は 2次元配列（例: [[1, 0, 1]]）となるので各商品の判定を取得
pred_labels = prediction[0]
result_mapping = {1: "Yes", 0: "No"}

print("予測結果:")
print(f"商品1: {result_mapping[pred_labels[0]]}")
print(f"商品2: {result_mapping[pred_labels[1]]}")
print(f"商品3: {result_mapping[pred_labels[2]]}")
