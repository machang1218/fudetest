import streamlit as st
import numpy as np

# 初始化session_state
if 'selected_result' not in st.session_state:
    st.session_state.selected_result = ""

# 人名映射字典
name_mapping = {
    1: "藏其旺",
    2: "王晓会",
    3: "王淑萍",
    4: "王立英",
    5: "王笑丽",
    6: "李孝梅",
    7: "林春华",
    8: "孙桂荣",
    9: "王一婷"
}

# 页面标题
st.title("红红火火")

# 添加垂直间距
st.write("\n\n")

def random_selection():
    """执行随机选择"""
    total_names = len(name_mapping)
    random_num = np.random.randint(1, total_names + 1)  # 生成1到总人数的随机整数
    st.session_state.selected_result = name_mapping[random_num]

# 创建按钮列布局
col1, col2, col3 = st.columns([1,2,1])
with col2:
    # 随机选择按钮
    if st.button("🎉 随机挑选幸运宝宝 🎉", 
                key="random_btn",
                use_container_width=True,
                type="primary"):
        random_selection()

# 添加垂直间距
st.write("\n\n")

# 显示结果
if st.session_state.selected_result:
    st.markdown(f"<h2 style='text-align: center;'>{st.session_state.selected_result}</h2>", 
                unsafe_allow_html=True)

# 添加页脚说明
st.write("\n\n")
st.markdown("---")
st.caption("每次点击按钮会随机选择一位幸运儿")
