import pandas as pd

# 读取数据
df = pd.read_csv("data/loan_portfolio.csv")

# 1. 按行业汇总
industry_summary = df.groupby("industry").agg(
    贷款余额=("loan_amount", "sum"),
    贷款笔数=("loan_id", "count"),
    不良余额=("loan_amount", lambda x: x[df.loc[x.index, "risk_class"].isin(["次级", "可疑", "损失"])].sum())
).reset_index()

industry_summary["不良率"] = (industry_summary["不良余额"] / industry_summary["贷款余额"] * 100).round(2)

# 2. 不良率最高的3个行业
top3 = industry_summary.nlargest(3, "不良率")

# 3. 重点风险客户
high_risk = df[(df["overdue_days"] > 90) & (df["loan_amount"] > 1000)]

# 4. 输出Excel
with pd.ExcelWriter("output/risk_report.xlsx") as writer:
    industry_summary.to_excel(writer, sheet_name="行业汇总", index=False)
    top3.to_excel(writer, sheet_name="高风险行业", index=False)
    high_risk.to_excel(writer, sheet_name="重点风险客户", index=False)

# 5. 自动生成文字总结
summary_text = f"""
【风险简报】
截至报告日，组合总贷款余额 {df['loan_amount'].sum():,.2f} 万元，
整体不良率 {industry_summary['不良余额'].sum() / industry_summary['贷款余额'].sum() * 100:.2f}%。

不良率最高的三个行业为：
"""
for _, row in top3.iterrows():
    summary_text += f"  - {row['industry']}：不良率 {row['不良率']}%，不良余额 {row['不良余额']:,.2f} 万元\n"

summary_text += f"\n重点风险客户（逾期>90天且金额>1000万）共 {len(high_risk)} 户，合计金额 {high_risk['loan_amount'].sum():,.2f} 万元。\n"
summary_text += "建议对上述行业和客户进行专项排查，关注抵质押物价值和还款来源变化。"

with open("output/risk_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print(summary_text)