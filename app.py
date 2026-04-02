import streamlit as st
import streamlit.components.v1 as components

# 1. 设置网页布局为宽屏
st.set_page_config(page_title="铝板保温装饰一体板报价系统", layout="wide")

# 2. 把完整的 HTML+CSS+JS 代码作为一个超大字符串存起来
# 注意开头的三个引号
html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>铝板保温装饰一体板报价系统</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 24px 16px;
            color: #1a2c3e;
        }
        .container { max-width: 1300px; margin: 0 auto; }
        .header {
            background: linear-gradient(135deg, #1e3c5c 0%, #2b4c6e 100%);
            color: white; padding: 24px 32px; border-radius: 28px;
            margin-bottom: 28px; box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        .header h1 { margin: 0 0 8px 0; font-weight: 700; font-size: 1.8rem; }
        .header p { margin: 0; opacity: 0.9; font-size: 0.95rem; }
        .dashboard { display: flex; flex-wrap: wrap; gap: 28px; }
        .control-panel {
            flex: 1; min-width: 300px; background: white; border-radius: 28px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.05); padding: 28px; height: fit-content;
        }
        .result-panel { display: none !important; }
        .param-group { margin-bottom: 28px; border-bottom: 1px solid #e9eef3; padding-bottom: 20px; }
        .param-group h3 { font-size: 1.1rem; margin: 0 0 18px 0; color: #1e4663; font-weight: 600; }
        .param-row { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; margin-bottom: 16px; justify-content: space-between; }
        .param-label { font-weight: 500; width: 115px; font-size: 0.88rem; color: #2c4b6e; }
        .param-input { flex: 1; min-width: 150px; }
        select, input {
            width: 100%; padding: 10px 12px; border-radius: 14px;
            border: 1px solid #cbd5e1; background: #ffffff; font-size: 0.9rem;
            font-family: inherit; transition: 0.2s;
        }
        select:focus, input:focus { outline: none; border-color: #2b6e9e; box-shadow: 0 0 0 3px rgba(43,110,158,0.15); }
        .input-error { border-color: #e53e3e !important; box-shadow: 0 0 0 3px rgba(229, 62, 62, 0.15) !important; }
        .error-tip { font-size: 0.75rem; color: #e53e3e; margin-top: 4px; display: none; }
        .error-tip.show { display: block; }
        .price-highlight {
            background: linear-gradient(135deg, #f0f7fc 0%, #e8f0f7 100%);
            border-radius: 24px; padding: 24px 20px; margin-top: 20px;
            text-align: center; border: 1px solid #cde0ef;
        }
        .total-price { font-size: 3rem; font-weight: 800; color: #1a6b4a; margin: 12px 0; letter-spacing: -0.5px; }
        .total-label { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1.5px; color: #5d7f9e; font-weight: 500; }
        .unit { font-size: 1rem; font-weight: normal; }
        .freight-tip { text-align: center; margin-top: 12px; font-size: 0.9rem; color: #d93025; font-weight: 500; }
        .footer-note { font-size: 0.7rem; text-align: center; margin-top: 28px; color: #8ba0b5; background: white; border-radius: 20px; padding: 10px; }
        @media (max-width: 700px) { .param-label { width: 100%; } .total-price { font-size: 2.2rem; } }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>📊 铝板保温装饰一体板 · 报价系统</h1>
        <p>铝锭价格 + 毛利系数 可自由调整 | 实时计算报价</p >
    </div>

    <div class="dashboard">
        <div class="control-panel">
            <div class="param-group">
                <h3>产品配置</h3>
                <div class="param-row">
                    <span class="param-label">保温芯材</span>
                    <div class="param-input">
                        <select id="coreType">
                            <option value="thermal">热固改性保温板</option>
                            <option value="rock120">120容重岩棉</option>
                            <option value="rock130">130容重岩棉</option>
                            <option value="rock140">140容重岩棉</option>
                        </select>
                    </div>
                </div>
                <div class="param-row">
                    <span class="param-label">背板类型</span>
                    <div class="param-input">
                        <select id="backType">
                            <option value="perforated">打孔背板</option>
                            <option value="nonPerforated">不打孔背板</option>
                            <option value="cementCloth">水泥基布</option>
                        </select>
                    </div>
                </div>
                <div class="param-row">
                    <span class="param-label">铝板饰面工艺</span>
                    <div class="param-input">
                        <select id="surfaceProcess">
                            <option value="roller">辊涂</option>
                            <option value="spray">喷涂</option>
                        </select>
                    </div>
                </div>
                <div class="param-row">
                    <span class="param-label">铝板厚度 (mm)</span>
                    <div class="param-input">
                        <input type="number" id="thickness" step="0.1" value="1.5" min="0.1">
                        <div class="error-tip" id="thicknessError">喷涂工艺铝板厚度不能小于1.5mm</div>
                    </div>
                </div>
                <div class="param-row">
                    <span class="param-label">保温厚度 (cm)</span>
                    <div class="param-input">
                        <input type="number" id="insulThick" step="0.5" value="4.0" min="0.5">
                    </div>
                </div>
            </div>

            <div class="param-group">
                <h3>价格参数</h3>
                <div class="param-row">
                    <span class="param-label">铝锭价格 (元/吨)</span>
                    <div class="param-input">
                        <input type="number" id="aluminumPrice" step="500" value="20000" min="10000">
                    </div>
                </div>
                <div class="param-row">
                    <span class="param-label">毛利系数</span>
                    <div class="param-input">
                        <input type="number" id="profitFactor" step="0.01" value="0.9" min="0.1">
                    </div>
                </div>
            </div>

            <div class="price-highlight">
                <div class="total-label">当前配置 报价</div>
                <div class="total-price" id="liveQuote">--.-- <span class="unit">元/㎡</span></div>
                <div class="freight-tip">此报价不含运费</div>
            </div>
        </div>
    </div>
    <div class="footer-note">铝板保温装饰一体板报价系统 | 参数可调，实时计算</div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const AL_DENSITY = 2.71;             
        const COMPOSITE_LABOR = 10;          
        const COMPOSITE_GLUE = 3;            
        const SPRAY_ADD_PRICE = 15;          
        
        const FEES = { flattening: 1500, coloring: 5000, processing: 15, lossRate: 1.15 };

        const CORE_MATERIALS = {
            thermal: { name: "热固改性保温板", price: 4.4, compTimes: 1, noBackboard: true },
            rock120: { name: "120容重岩棉", price: 3.3, compTimes: 2, noBackboard: false },
            rock130: { name: "130容重岩棉", price: 3.52, compTimes: 2, noBackboard: false },
            rock140: { name: "140容重岩棉", price: 3.85, compTimes: 2, noBackboard: false }
        };

        const BACKBOARDS = {
            perforated: { name: "打孔背板", price: 8.5 },
            nonPerforated: { name: "不打孔背板", price: 7.5 },
            cementCloth: { name: "水泥基布", price: 4.0 }
        };

        const elCoreType = document.getElementById('coreType');
        const elBackType = document.getElementById('backType');
        const elSurfaceProcess = document.getElementById('surfaceProcess');
        const elThickness = document.getElementById('thickness');
        const elThicknessError = document.getElementById('thicknessError');
        const elInsulThick = document.getElementById('insulThick');
        const elAlPrice = document.getElementById('aluminumPrice');
        const elProfit = document.getElementById('profitFactor');
        const elLiveQuote = document.getElementById('liveQuote');

        function validateThickness() {
            const thickness = parseFloat(elThickness.value) || 1.5;
            const isSpray = elSurfaceProcess.value === 'spray';
            if (isSpray && thickness < 1.5) {
                elThickness.classList.add('input-error');
                elThicknessError.classList.add('show');
                return false;
            } else {
                elThickness.classList.remove('input-error');
                elThicknessError.classList.remove('show');
                return true;
            }
        }

        function getSafeInputs() {
            const thickness = parseFloat(elThickness.value) || 1.5;
            const alPrice = parseFloat(elAlPrice.value) || 20000;
            const insulThick = parseFloat(elInsulThick.value) || 4.0;
            const margin = parseFloat(elProfit.value) || 0.9;
            const isSpray = elSurfaceProcess.value === 'spray';
            return {
                thickness: isSpray ? Math.max(thickness, 1.5) : Math.max(thickness, 0.1),
                alPrice: Math.max(alPrice, 10000),
                insulThick: Math.max(insulThick, 0.5),
                margin: Math.max(margin, 0.1),
                isSpray: isSpray
            };
        }

        function calculatePrice(coreKey, backKey) {
            const material = CORE_MATERIALS[coreKey];
            if (!material) return null;
            const inputs = getSafeInputs();

            const processAddCost = inputs.isSpray ? SPRAY_ADD_PRICE : 0;
            const backboardCost = material.noBackboard ? 0 : (BACK
