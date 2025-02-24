import pandas as pd

# 食品データセットの作成
data = [
    ["タイチップス", "じゃがいも,唐辛子,塩", "唐辛子", 3],
    ["わさびせんべい", "米,わさび,醤油", "わさび", 4],
    ["トムヤムクン味スナック", "小麦粉,唐辛子,レモングラス", "唐辛子,レモングラス", 4],
    ["カラムーチョ", "じゃがいも,唐辛子,塩", "唐辛子", 5],
    ["プリッツ（トムヤム味）", "小麦粉,唐辛子,塩", "唐辛子", 3],
    ["コイケヤスコーン（激辛チリ味）", "とうもろこし,唐辛子,塩", "唐辛子", 5],
    ["激辛ラーメンスナック", "小麦粉,唐辛子,胡椒", "唐辛子,胡椒", 5],
    ["わさびポテトチップス", "じゃがいも,わさび,塩", "わさび", 4],
    ["サテ味スナック", "小麦粉,唐辛子,ピーナッツ", "唐辛子", 3],
    ["チリペッパーポテト", "じゃがいも,唐辛子,塩", "唐辛子", 4],
    ["四川風麻辣スナック", "小麦粉,花椒,唐辛子", "花椒,唐辛子", 5],
    ["ハバネロチップス", "じゃがいも,ハバネロ,塩", "ハバネロ", 5],
    ["トッポギスナック", "小麦粉,唐辛子,砂糖", "唐辛子", 3],
    ["タコスチップス（スパイシー）", "とうもろこし,唐辛子,チリパウダー", "唐辛子,チリパウダー", 4],
    ["韓国ラーメンスナック", "小麦粉,唐辛子,にんにく", "唐辛子", 4],
    ["カレースナック", "小麦粉,カレー粉,唐辛子", "カレー粉,唐辛子", 3],
    ["タイスパイシークラッカー", "米,唐辛子,にんにく", "唐辛子", 4],
    ["スパイシーフィッシュスナック", "魚,唐辛子,塩", "唐辛子", 3],
    ["山椒チップス", "じゃがいも,山椒,塩", "山椒", 4],
    ["麻辣ピーナッツ", "ピーナッツ,花椒,唐辛子", "花椒,唐辛子", 5]
]

# データフレームに変換
df = pd.DataFrame(data, columns=["商品名", "原材料", "スパイス成分", "推定辛さレベル"])

# CSVとして保存
csv_filename = "./spicy_snacks.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8-sig")

# CSVファイルのパスを返す
csv_filename
