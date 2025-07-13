import datetime

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
