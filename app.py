import streamlit as st
import pandas as pd
import random
from collections import Counter

# 模拟用户评论数据
comments = [
    "推荐的内容重复度太高了，希望能看到更多新东西",
    "广告太多了，刷几条就有一条广告，体验很差",
    "笔记质量参差不齐，很多都是搬运和低质内容",
    "希望增加笔记收藏分类功能，找起来太麻烦了",
    "评论区有时候会有很多杠精，希望加强治理",
    "本地生活的笔记太少了，想找附近的店很不方便",
    "希望推荐算法能更懂我，别一直推我看过的内容"
]

# 简单情绪分析模拟
def analyze_comment(comment):
    if "重复" in comment or "广告" in comment or "差" in comment or "麻烦" in comment:
        return "负面"
    elif "希望" in comment or "建议" in comment or "增加" in comment:
        return "中性-建议"
    else:
        return "正面"

# 痛点分类模拟
def classify_painpoint(comment):
    if "推荐" in comment or "算法" in comment:
        return "推荐算法"
    elif "广告" in comment:
        return "商业化体验"
    elif "收藏" in comment or "分类" in comment:
        return "工具功能"
    elif "评论区" in comment or "杠精" in comment:
        return "社区氛围"
    elif "笔记" in comment or "内容" in comment:
        return "内容质量"
    else:
        return "其他"

# Streamlit界面
st.title("AI用户反馈分析助手")
st.subheader("内容社区用户评论分析Demo")

if st.button("一键分析模拟数据"):
    results = []
    for c in comments:
        results.append({
            "评论": c,
            "情绪": analyze_comment(c),
            "痛点分类": classify_painpoint(c)
        })
    df = pd.DataFrame(results)
    st.dataframe(df)

    # 统计结果
    st.subheader("痛点优先级分析")
    pain_counts = Counter(df["痛点分类"])
    st.bar_chart(pain_counts)