import datetime
import os
import random

QUESTION_BANK = [
    "今天在上課或學習過程中有什麼新發現或有趣的收穫？",
    "今天在運動或身體狀態上有沒有什麼突破或特別的感受？",
    "最近讀的文章、書籍或影片，有哪一句話或觀點觸動了你？",
    "今天遇到了什麼小挫折或挑戰？你嘗試怎麼處理它？",
    "今天最讓你感到放鬆或開心的瞬間是什麼時候？",
    "如果用一個關鍵詞形容今天，會是什麼？為什麼？",
    "今天社團或與朋友互動時，有沒有發生令人印象深刻的事？",
    "有沒有哪件計畫中的事情是你今天跨出了一小步的？",
]


def generate_daily_draft():
    selected_questions = random.sample(
        QUESTION_BANK, k=min(3, len(QUESTION_BANK))
    )

    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    datetime_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")

    filename = f"{date_str}-daily-reflection.md"
    output_dir = os.path.join(
        os.path.dirname(__file__), "..", "content", "posts"
    )
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    content = f"""---
title: "{date_str} 生活隨筆與記錄"
date: {datetime_str}
draft: false
tags: ["生活紀錄", "靈感隨筆"]
---

### 💡 今日靈感引導

"""
    for i, q in enumerate(selected_questions, 1):
        content += f"#### Q{i}: {q}\n> *(在這裡寫下你的回答...)*\n\n"

    content += "---\n\n### 📝 自由紀錄與隨筆\n*(自由補充今天的其他細節或圖片)*\n"

    if os.path.exists(file_path):
        print(f"⚠️ 檔案 {filename} 已存在！")
        return

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 已成功建立今日草稿：content/posts/{filename}")


if __name__ == "__main__":
    generate_daily_draft()
    