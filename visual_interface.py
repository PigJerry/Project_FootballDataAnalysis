from data_fetcher import get_pl_standings
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 页面配置
st.set_page_config(
    page_title="足球数据分析",
    page_icon="⚽",
    layout="wide"
)

# 标题
st.title("足球数据分析平台")
st.markdown("---")

# 侧边栏
with st.sidebar:
    st.header("筛选条件")
    league = st.selectbox(
        "选择联赛",
        ["英格兰足球超级联赛", "西班牙足球甲级联赛", "德国足球甲级联赛", "意大利足球甲级联赛", "法国足球甲级联赛"]
    )
    st.write(f"当前选择：{league}")

# 主区域
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 球队积分榜")
    df_real = get_pl_standings()
    st.dataframe(df_real)

with col2:
    st.subheader("📈 进球趋势")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [2, 4, 3])
    ax.set_title("模拟进球趋势")
    st.pyplot(fig)

# 图表区
st.markdown("---")
col3, col4 = st.columns(2)

with col3:
    st.subheader("📈 球队得分点状离散图")
    st.scatter_chart(
        data=df_real,
        x="进球",
        y="积分",
        color="球队",
        size="净胜球"
    )

with col4:
    st.subheader("⚽ 各球员进球排名")
    player_df = pd.DataFrame({
        "球员": ["哈兰德", "萨拉赫", "凯恩", "孙兴慜", "萨卡"],
        "进球数": [25, 20, 18, 15, 14]
    })
    st.bar_chart(data=player_df, x="球员", y="进球数")

# 图表区
st.subheader("🛡️ 球队成功防守排名（按失球升序）")
st.bar_chart(
    data=df_real.sort_values("失球"),
    x="球队",
    y="失球",
    horizontal=True
)

# 底部指标卡片
st.markdown("---")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric(label="🏆 总场次", value=380)
with col_b:
    st.metric(label="⚽ 总进球", value=1064)
with col_c:
    st.metric(label="📅 赛季", value="2024/25")