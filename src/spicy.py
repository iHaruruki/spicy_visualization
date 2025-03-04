import pytesseract
import cv2
from PIL import Image
import csv
import os

# Tesseract のパスを手動指定
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 画像ファイルのパス
image_path = "image/sample1.jpg"
if image_path is None:
    print("Error: Could not load image. Check the file path.")

# OCRで成分表のテキストを抽出
def extract_ingredients(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='jpn')
    return text

# CSVのデータを読み込む
def load_spicy_data(csv_file):
    spicy_data = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            spicy_data.append(row)
    return spicy_data

#OCR結果とデータセットを比較し、辛さレベルを判定
def determine_spiciness(ingredients, spicy_data):
    max_spice_level = 0
    for snack in spicy_data:
        spices = snack["スパイス成分"].split(',')
        for spice in spices:
            if spice in ingredients:
                max_spice_level = max(max_spice_level, int(snack["推定辛さレベル"]))
    return max_spice_level

# テスト実行
if __name__ == "__main__":
    #image_path = "src/sample_ingredients2.jpg"  # 成分表の画像
    # 画像を読み込む

    image = cv2.imread(image_path)
    csv_file = "src/spicy_snacks.csv"
    # 画像を表示する
    cv2.imshow("Image", image)
    # キーが押されるまで待機
    cv2.waitKey(0)
    # ウィンドウを閉じる
    cv2.destroyAllWindows()
    """
    extracted_text = extract_ingredients(image_path)
    print("OCR抽出結果:", extracted_text)

    """
    extracted_text = "唐辛子"
    spicy_data = load_spicy_data(csv_file)
    spiciness_level = determine_spiciness(extracted_text, spicy_data)
    print("推定辛さレベル:", spiciness_level)
