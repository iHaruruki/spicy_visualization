#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# 鬟溷刀繝��繧ｿ繧ｻ繝�ヨ縺ｮ菴懈�
data = [
    ["繧ｿ繧､繝√ャ繝励せ", "縺倥ｃ縺後＞繧�,蜚占ｾ帛ｭ�,蝪ｩ", "蜚占ｾ帛ｭ�", 3],
    ["繧上＆縺ｳ縺帙ｓ縺ｹ縺�", "邀ｳ,繧上＆縺ｳ,驢､豐ｹ", "繧上＆縺ｳ", 4],
    ["繝医Β繝､繝�繧ｯ繝ｳ蜻ｳ繧ｹ繝翫ャ繧ｯ", "蟆城ｺｦ邊�,蜚占ｾ帛ｭ�,繝ｬ繝｢繝ｳ繧ｰ繝ｩ繧ｹ", "蜚占ｾ帛ｭ�,繝ｬ繝｢繝ｳ繧ｰ繝ｩ繧ｹ", 4],
    ["繧ｫ繝ｩ繝�繝ｼ繝√Ι", "縺倥ｃ縺後＞繧�,蜚占ｾ帛ｭ�,蝪ｩ", "蜚占ｾ帛ｭ�", 5],
    ["繝励Μ繝�ヤ�医ヨ繝�繝､繝�蜻ｳ��", "蟆城ｺｦ邊�,蜚占ｾ帛ｭ�,蝪ｩ", "蜚占ｾ帛ｭ�", 3],
    ["繧ｳ繧､繧ｱ繝､繧ｹ繧ｳ繝ｼ繝ｳ�域ｿ霎帙メ繝ｪ蜻ｳ��", "縺ｨ縺�ｂ繧阪％縺�,蜚占ｾ帛ｭ�,蝪ｩ", "蜚占ｾ帛ｭ�", 5],
    ["豼霎帙Λ繝ｼ繝｡繝ｳ繧ｹ繝翫ャ繧ｯ", "蟆城ｺｦ邊�,蜚占ｾ帛ｭ�,閭｡讀�", "蜚占ｾ帛ｭ�,閭｡讀�", 5],
    ["繧上＆縺ｳ繝昴ユ繝医メ繝��繧ｹ", "縺倥ｃ縺後＞繧�,繧上＆縺ｳ,蝪ｩ", "繧上＆縺ｳ", 4],
    ["繧ｵ繝�袖繧ｹ繝翫ャ繧ｯ", "蟆城ｺｦ邊�,蜚占ｾ帛ｭ�,繝斐�繝翫ャ繝�", "蜚占ｾ帛ｭ�", 3],
    ["繝√Μ繝壹ャ繝代�繝昴ユ繝�", "縺倥ｃ縺後＞繧�,蜚占ｾ帛ｭ�,蝪ｩ", "蜚占ｾ帛ｭ�", 4],
    ["蝗帛ｷ晞｢ｨ鮗ｻ霎｣繧ｹ繝翫ャ繧ｯ", "蟆城ｺｦ邊�,闃ｱ讀�,蜚占ｾ帛ｭ�", "闃ｱ讀�,蜚占ｾ帛ｭ�", 5],
    ["繝上ヰ繝阪Ο繝√ャ繝励せ", "縺倥ｃ縺後＞繧�,繝上ヰ繝阪Ο,蝪ｩ", "繝上ヰ繝阪Ο", 5],
    ["繝医ャ繝昴ぐ繧ｹ繝翫ャ繧ｯ", "蟆城ｺｦ邊�,蜚占ｾ帛ｭ�,遐らｳ�", "蜚占ｾ帛ｭ�", 3],
    ["繧ｿ繧ｳ繧ｹ繝√ャ繝励せ�医せ繝代う繧ｷ繝ｼ��", "縺ｨ縺�ｂ繧阪％縺�,蜚占ｾ帛ｭ�,繝√Μ繝代え繝繝ｼ", "蜚占ｾ帛ｭ�,繝√Μ繝代え繝繝ｼ", 4],
    ["髻灘嵜繝ｩ繝ｼ繝｡繝ｳ繧ｹ繝翫ャ繧ｯ", "蟆城ｺｦ邊�,蜚占ｾ帛ｭ�,縺ｫ繧薙↓縺�", "蜚占ｾ帛ｭ�", 4],
    ["繧ｫ繝ｬ繝ｼ繧ｹ繝翫ャ繧ｯ", "蟆城ｺｦ邊�,繧ｫ繝ｬ繝ｼ邊�,蜚占ｾ帛ｭ�", "繧ｫ繝ｬ繝ｼ邊�,蜚占ｾ帛ｭ�", 3],
    ["繧ｿ繧､繧ｹ繝代う繧ｷ繝ｼ繧ｯ繝ｩ繝�き繝ｼ", "邀ｳ,蜚占ｾ帛ｭ�,縺ｫ繧薙↓縺�", "蜚占ｾ帛ｭ�", 4],
    ["繧ｹ繝代う繧ｷ繝ｼ繝輔ぅ繝�す繝･繧ｹ繝翫ャ繧ｯ", "鬲�,蜚占ｾ帛ｭ�,蝪ｩ", "蜚占ｾ帛ｭ�", 3],
    ["螻ｱ讀偵メ繝��繧ｹ", "縺倥ｃ縺後＞繧�,螻ｱ讀�,蝪ｩ", "螻ｱ讀�", 4],
    ["鮗ｻ霎｣繝斐�繝翫ャ繝�", "繝斐�繝翫ャ繝�,闃ｱ讀�,蜚占ｾ帛ｭ�", "闃ｱ讀�,蜚占ｾ帛ｭ�", 5]
]

# 繝��繧ｿ繝輔Ξ繝ｼ繝�縺ｫ螟画鋤
df = pd.DataFrame(data, columns=["蝠�刀蜷�", "蜴滓攝譁�", "繧ｹ繝代う繧ｹ謌仙�", "謗ｨ螳夊ｾ帙＆繝ｬ繝吶Ν"])

# CSV縺ｨ縺励※菫晏ｭ�
csv_filename = "./spicy_snacks.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8-sig")

# CSV繝輔ぃ繧､繝ｫ縺ｮ繝代せ繧定ｿ斐☆
csv_filename


# In[1]:


get_ipython().system('pip install pandas')


# In[8]:


pip install pytesseract pillow pandas easyocr


# In[29]:


get_ipython().system('pip install opencv-python')





# In[9]:


get_ipython().system('pip install Image')

get_ipython().system('pip install csv')


# In[8]:


import pytesseract
import cv2
from PIL import Image
import csv

# OCR縺ｧ謌仙�陦ｨ縺ｮ繝�く繧ｹ繝医ｒ謚ｽ蜃ｺ
def extract_ingredients(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='jpn')
    return text

# CSV縺ｮ繝��繧ｿ繧定ｪｭ縺ｿ霎ｼ繧
def load_spicy_data(csv_file):
    spicy_data = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            spicy_data.append(row)
    return spicy_data

# OCR邨先棡縺ｨ繝��繧ｿ繧ｻ繝�ヨ繧呈ｯ碑ｼ�＠縲∬ｾ帙＆繝ｬ繝吶Ν繧貞愛螳�
def determine_spiciness(ingredients, spicy_data):
    max_spice_level = 0
    for snack in spicy_data:
        spices = snack["繧ｹ繝代う繧ｹ謌仙�"].split(',')
        for spice in spices:
            if spice in ingredients:
                max_spice_level = max(max_spice_level, int(snack["謗ｨ螳夊ｾ帙＆繝ｬ繝吶Ν"]))
    return max_spice_level

# 繝�せ繝亥ｮ溯｡�
if __name__ == "__main__":
    image_path = "./sample_ingredients2.jpg"  # 謌仙�陦ｨ縺ｮ逕ｻ蜒�
    csv_file = "./spicy_snacks.csv"



    """
     # 逕ｻ蜒上ｒ隱ｭ縺ｿ霎ｼ繧
    image = cv2.imread(image_path)


    # 逕ｻ蜒上ｒ陦ｨ遉ｺ縺吶ｋ
    cv2.imshow("Image", image)

    # 繧ｭ繝ｼ縺梧款縺輔ｌ繧九∪縺ｧ蠕�ｩ�
    cv2.waitKey(0)

    # 繧ｦ繧｣繝ｳ繝峨え繧帝哩縺倥ｋ
    cv2.destroyAllWindows()
    """


    extracted_text = extract_ingredients(image_path)
    print("OCR謚ｽ蜃ｺ邨先棡:", extracted_text)

    spicy_data = load_spicy_data(csv_file)
    spiciness_level = determine_spiciness(extracted_text, spicy_data)
    print("謗ｨ螳夊ｾ帙＆繝ｬ繝吶Ν:", spiciness_level)




# In[ ]:
