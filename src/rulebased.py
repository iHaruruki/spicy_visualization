import json
import os
import csv
import pytesseract
from PIL import Image

def calculate_tolerance(answers: dict) -> float:
    """
    各レベル（1～5）で2問のうち大きいほうの値を採用し、平均値を算出する。
    """
    total = 0
    for level in range(1, 6):
        pair = answers.get(f'level{level}', [0, 0])
        total += max(pair)
    return total / 5

def apply_user_correction(base_tolerance: float, user_preference: str) -> float:
    """
    ユーザの生活状況に応じた補正を加える。
    "辛いの行ける" → +1, "全く食べない" → -1, "少し辛いものならok" → 0
    """
    correction = 0
    if user_preference == "辛いの行ける":
        correction = 1
    elif user_preference == "全く食べない":
        correction = -1
    return base_tolerance + correction

def process_ocr(image_path: str) -> str:
    """
    指定された画像ファイルに対してOCR処理を行い、抽出したテキストを返す。
    Tesseract OCRの日本語データ（lang='jpn'）を使用する例。
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='jpn')
        return text
    except Exception as e:
        return f"画像処理エラー: {e}"

def load_snack_db(csv_filename: str) -> dict:
    """
    CSV ファイルからスナック情報を読み込み、
    スナック名をキー、辛さレベル（整数）を値とする辞書を返す。
    """
    snack_db = {}
    if os.path.exists(csv_filename):
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    snack_db[row["name"]] = int(row["spiciness"])
                except (KeyError, ValueError):
                    continue
    else:
        print(f"CSVファイル {csv_filename} が存在しません。")
    return snack_db

def main():
    print("=== 辛さ許容量計算プログラム ===")
    user_id = input("ユーザIDを入力してください: ")

    # アンケートの回答入力
    print("\n【アンケート入力】")
    print("各レベルごとの質問2問の回答（数値）を入力してください。")
    answers = {}
    for level in range(1, 6):
        print(f"\n＜レベル {level} の質問＞")
        try:
            ans1 = float(input(f" レベル {level} 質問1の回答: "))
        except ValueError:
            print("数値を入力してください。")
            return
        answers[f'level{level}'] = [ans1]

    # 生活状況に関する補正入力
    print("\n【生活状況の入力】")
    print("普段の生活での辛さの許容度を選択してください:")
    print(" 1: 全く食べない")
    print(" 2: 少し辛いものならok")
    print(" 3: 辛いの行ける")
    pref_input = input("選択肢 (1/2/3): ")
    if pref_input == "1":
        user_preference = "全く食べない"
    elif pref_input == "2":
        user_preference = "少し辛いものならok"
    elif pref_input == "3":
        user_preference = "辛いの行ける"
    else:
        print("無効な入力です。")
        return

    # 許容量の計算
    base_tolerance = calculate_tolerance(answers)
    final_tolerance = apply_user_correction(base_tolerance, user_preference)
    print(f"\nユーザ {user_id} の基本許容量: {base_tolerance:.2f}")
    print(f"補正後の最終許容量: {final_tolerance:.2f}")

    # CSV ファイルからスナック情報を読み込む
    csv_filename = "snacks.csv"
    snack_db = load_snack_db(csv_filename)
    if not snack_db:
        print("スナック情報が読み込めませんでした。CSVファイルを確認してください。")
        return

    # スナックの評価方法の選択
    print("\n【スナック評価】")
    print("スナックの評価を行います。")
    print("スナック名を直接入力する場合は '1' を、画像ファイルからOCRで抽出する場合は '2' を入力してください。")
    method = input("選択 (1/2): ")

    if method == "1":
        snack_name = input("スナック名を入力してください: ")
    elif method == "2":
        image_path = input("画像ファイルのパスを入力してください: ")
        if not os.path.exists(image_path):
            print("指定された画像ファイルが存在しません。")
            return
        ocr_text = process_ocr(image_path)
        print("\n【OCR結果】")
        print(ocr_text)
        # OCR結果をもとにスナック名を入力（OCRの精度によっては修正が必要）
        snack_name = input("\nOCR結果から評価するスナック名を入力してください: ")
    else:
        print("無効な選択肢です。")
        return

    # スナックの辛さレベル取得と評価
    spiciness = snack_db.get(snack_name)
    if spiciness is None:
        print("該当するスナックが見つかりません。")
        return

    print(f"\n{snack_name} の辛さレベルは {spiciness} です。")
    evaluation = "食べられる" if final_tolerance >= spiciness else "辛すぎる"
    print(f"評価結果: {evaluation}")

if __name__ == '__main__':
    main()
