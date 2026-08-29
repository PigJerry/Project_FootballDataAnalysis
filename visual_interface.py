import streamlit as st

#页面配置
st.set_page_config(
    page_title = "足球数据分析",
    page_icon = "⚽",
    layout = "wide"
)

#标题
st.title("足球数据分析平台")
st.markdown("---")

#侧边栏
with st.sidebar:
    st.header("筛选条件")
    league = st.selectbox(
        "选择联赛",
        ["英格兰足球超级联赛", "西班牙足球甲级联赛", "德国足球甲级联赛", "意大利足球甲级联赛", "法国足球甲级联赛"]
    )
    st.write(f"当前选择：{league}")

#主区域
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 球队积分榜")
    import pandas as pd
    dummy_data = pd.DataFrame({
        "球队": ["阿森纳", "利物浦", "切尔西"],
        "积分": [85, 62, 58]
    })
    st.dataframe(dummy_data)

with col2:
    st.subheader("📈 进球趋势")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [2, 4, 3])
    ax.set_title("模拟进球趋势")
    st.pyplot(fig)

# 5. 底部指标卡片
st.markdown("---")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric(label="🏆 总场次", value=380)
with col_b:
    st.metric(label="⚽ 总进球", value=1064)
with col_c:
    st.metric(label="📅 赛季", value="2024/25")
