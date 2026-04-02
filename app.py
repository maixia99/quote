import streamlit as st

# ==========================================
# 1. 常量配置 (根据你的 Excel 提取)
# ==========================================
DENSITY = 2.71          # 铝密度
FLATTENING_FEE = 1500.0 # 开平费用 (元/吨)
COLORING_FEE = 5000.0   # 上色费用 (元/吨)
LOSS_RATE = 1.15        # 损耗系数
AL_PROCESSING_FEE = 15.0# 铝板加工费 (元/m²)

# 保温材料物料库
MATERIAL_DB = {
    "热固": {"price": 4.4, "backboard": 0.0, "composite_times": 1.0, "glue": 2.0, "labor": 8.0},
    "120容重岩棉（打孔背板）": {"price": 3.3, "backboard": 8.5, "composite_times": 2.0, "glue": 2.0, "labor": 8.0},
    "130容重岩棉（打孔背板）": {"price": 3.52, "backboard": 8.5, "composite_times": 2.0, "glue": 2.0, "labor": 8.0},
    "130容重岩棉（不打孔背板）": {"price": 3.52, "backboard": 0.0, "composite_times": 2.0, "glue": 2.0, "labor": 8.0}
}

# ==========================================
# 2. 页面与UI配置
# ==========================================
st.set_page_config(page_title="铝板保温装饰一体板报价系统", layout="centered")

st.title("🏗️ 铝板保温装饰一体板报价系统")
st.markdown("调整下方参数，系统将自动生成最新的控制价。")

# ==========================================
# 3. 交互输入区
# ==========================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 基础参数")
    al_price = st.number_input("今日铝锭价格 (元/吨)", value=20000.0, step=100.0)
    al_thickness = st.number_input("铝板厚度 (mm)", value=1.5, step=0.1)
    if al_thickness < 1.5:
        st.warning("⚠️ 提示：标准工艺厚度建议≥1.5mm")
    margin = st.number_input("毛利系数 (默认10个点填0.9)", value=0.9, step=0.01)

with col2:
    st.subheader("🧱 材料配置")
    material_name = st.selectbox("选择保温材料类型", options=list(MATERIAL_DB.keys()), index=2)
    insulation_thickness = st.number_input("保温层厚度 (cm)", value=4.0, step=0.5)

st.divider() 

# ==========================================
# 4. 核心计算逻辑
# ==========================================
mat = MATERIAL_DB[material_name]

# 1. 铝基材成本 = (厚度 * 密度 * (铝锭价 + 开平 + 上色) / 1000) * 损耗
al_ton_cost = al_price + FLATTENING_FEE + COLORING_FEE
al_base_cost = (al_thickness * DENSITY * al_ton_cost / 1000) * LOSS_RATE

# 2. 保温材料成本 = 厚度 * 单价
insulation_cost = insulation_thickness * mat["price"]

# 3. 复合成本 = (胶水费 + 复合人工) * 复合次数
composite_cost = (mat["glue"] + mat["labor"]) * mat["composite_times"]

# 4. 总成本
total_cost = al_base_cost + AL_PROCESSING_FEE + insulation_cost + mat["backboard"] + composite_cost

# 5. 最终报价
if margin > 0:
    final_price = total_cost / margin
else:
    final_price = 0.0

# ==========================================
# 5. 结果展示
# ==========================================
st.metric(label=f"📝 【{material_name}】最终建议系统报价", value=f"¥ {final_price:.2f} / m²")

with st.expander("📄 查看成本核算明细"):
    st.markdown(f"""
    * **铝板含损耗成本:** ¥ {al_base_cost:.2f} / m²
    * **铝板加工费:** ¥ {AL_PROCESSING_FEE:.2f} / m²
    * **保温材料纯成本:** ¥ {insulation_cost:.2f} / m²
    * **背板费用:** ¥ {mat['backboard']:.2f} / m²
    * **胶水与复合人工:** ¥ {composite_cost:.2f} / m²
    """)
