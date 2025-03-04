def evaluate_spiciness(ingredients: str) -> int:
    # 辛味成分とそのスコアの例（実際の値は調整が必要）
    spicy_dict = {
        '唐辛子': 3,
        'チリペッパー': 4,
        'ハバネロ': 5,
        'カプサイシン': 5
    }

    total_score = 0
    for spicy_item, score in spicy_dict.items():
        if spicy_item in ingredients:
            total_score += score

    # スコアを10段階に正規化（例として単純にクリッピング）
    normalized_score = min(total_score, 10)
    return normalized_score

# 例：成分表のテキスト
sample_ingredients = "トマト、玉ねぎ、唐辛子、オリーブオイル"
print("評価された辛さ（10段階）:", evaluate_spiciness(sample_ingredients))
