# 信贷组合风险监控工具

## 业务背景

信贷业务中，风险经理需要定期监控贷款组合的行业集中度和不良率变化。
传统方式依赖手工Excel透视表，耗时长、容易遗漏，且简报撰写占用大量时间。

## 解决方案

本工具用 Python + AI 实现端到端风险监控：

1. 自动读取贷款组合数据
2. 按行业计算不良率，识别高风险行业
3. 筛选重点风险客户（逾期>90天且金额>1000万）
4. 自动生成风险简报初稿，人工润色后可直接上报

## 效果

- 原本需要2小时的手工分析，压缩到10分钟
- 风险信号识别更全面，避免人工遗漏
- 简报初稿由AI生成，风险经理只需审核和补充业务判断

## 技术栈

- Python (pandas)
- Cursor / GitHub Copilot 辅助开发
- Claude / ChatGPT 生成简报初稿

## 项目结构
risk-monitor-ai/
├── data/ # 模拟数据
├── output/ # 分析结果
├── generate_data.py # 生成模拟数据
├── analyze_loans.py # 核心分析脚本
├── sample_report.md # AI辅助生成的周报样例
└── README.md

text

## 如何使用

1. 安装依赖：`pip install pandas openpyxl`
2. 生成模拟数据：`python generate_data.py`
3. 运行分析：`python analyze_loans.py`
4. 查看结果：`output/` 文件夹
5. 查看周报样例：`sample_report.md`

## 后续升级方向

- [1] 引入多月数据，计算不良率环比、同比
- [2] 增加预警规则引擎，实现事前预警
- [3] 生成HTML可视化看板
- [4] 接入外部行业数据，做交叉分析

## 关于作者

Alana Zhang, 金融从业者，AI爱好者，擅长用AI和Python解决业务落地问题。
邮箱：alana0503@hotmail.com
