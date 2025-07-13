import os
import datetime
import subprocess

# 自動產生分析資料（你可換成真實分析）
today = datetime.datetime.now().strftime("%Y-%m-%d")
analysis_html = f"""
<div style='background:#f9f9f9;padding:10px;border:1px solid #ccc'>
  <h2>📊 {today} 台股每日 AI 分析</h2>
  <ul>
    <li>00940 ➤ 投資信心比：78%，建議買進比例：65%</li>
    <li>台積電 ➤ 投資信心比：84%，建議買進比例：70%</li>
    <li>雍智科技 ➤ 投資信心比：69%，建議買進比例：55%</li>
    <li>日月光 ➤ 投資信心比：73%，建議買進比例：60%</li>
  </ul>
</div>
"""

# 寫入 index.html（放在最上方）
with open("index.html", "w", encoding="utf-8") as f:
    f.write(f"""
<html>
  <body>
    {analysis_html}
    <p style='color:gray'>更新時間：{datetime.datetime.now()}</p>
  </body>
</html>
""")

print("✅ 已更新 index.html")

# 自動 Git 提交與推送
os.system('git config user.name "DeanBot"')
os.system('git config user.email "dean@example.com"')
os.system("git add index.html")
os.system('git commit -m "每日自動更新 index.html" || echo "No changes to commit"')
os.system('git push https://x-access-token:${{GH_TOKEN}}@github.com/Dean-boot/TWStock-Dashboard.git HEAD:main')import datetime

stock_data = [
    {
        "name": "00940",
        "confidence": 72,
        "buy_ratio": 65,
        "suggestion": "持續觀察，低接可考慮",
    },
    {
        "name": "台積電",
        "confidence": 88,
        "buy_ratio": 80,
        "suggestion": "強烈買進",
    },
    {
        "name": "雍智科技",
        "confidence": 59,
        "buy_ratio": 50,
        "suggestion": "中性，觀望為宜",
    },
    {
        "name": "日月光",
        "confidence": 76,
        "buy_ratio": 68,
        "suggestion": "可分批佈局",
    }
]

def generate_html_block(data):
    block = "<div class='ai-analysis'>\n"
    block += f"<p><strong>更新時間：</strong>{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</p>\n"
    block += "<table>\n<tr><th>股票</th><th>信心比 (%)</th><th>建議買進比 (%)</th><th>操作建議</th></tr>\n"
    for stock in data:
        block += f"<tr><td>{stock['name']}</td><td>{stock['confidence']}%</td><td>{stock['buy_ratio']}%</td><td>{stock['suggestion']}</td></tr>\n"
    block += "</table>\n</div>\n"
    return block

html_content = f"""
<html>
<head>
  <meta charset="UTF-8">
  <title>TWStock Dashboard</title>
  <style>
    body {{ font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px; }}
    .ai-analysis {{ background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 5px rgba(0,0,0,0.1); }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ padding: 10px; text-align: center; border-bottom: 1px solid #ddd; }}
    th {{ background-color: #f0f0f0; }}
  </style>
</head>
<body>
  <h1>TWStock AI 投資分析 Dashboard</h1>
  {generate_html_block(stock_data)}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ 已自動產生 index.html 完成更新")
