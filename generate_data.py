import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

industries = ["制造业", "批发零售", "房地产", "建筑业", "交通运输", "餐饮住宿"]
risk_classes = ["正常", "关注", "次级", "可疑", "损失"]

rows = []
for i in range(500):
    industry = np.random.choice(industries)
    overdue = np.random.choice([0, 0, 0, 5, 15, 45, 90, 180], p=[0.5, 0.15, 0.1, 0.08, 0.07, 0.05, 0.03, 0.02])
    
    if overdue == 0:
        risk = "正常"
    elif overdue <= 30:
        risk = "关注"
    elif overdue <= 90:
        risk = "次级"
    elif overdue <= 180:
        risk = "可疑"
    else:
        risk = "损失"
    
    rows.append({
        "loan_id": f"LN{i:05d}",
        "customer_id": f"C{np.random.randint(1000, 9999)}",
        "industry": industry,
        "loan_amount": round(np.random.uniform(50, 5000), 2),
        "overdue_days": overdue,
        "risk_class": risk,
        "report_date": (datetime(2025, 8, 31) - timedelta(days=np.random.randint(0, 30))).strftime("%Y-%m-%d")
    })

df = pd.DataFrame(rows)
df.to_csv("data/loan_portfolio.csv", index=False, encoding="utf-8-sig")
print(f"已生成 {len(df)} 条模拟贷款数据")
print(df.head())