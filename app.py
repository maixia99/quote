import streamlit as st
import streamlit.components.v1 as components

# 设置网页布局
st.set_page_config(page_title="铝板保温装饰一体板报价系统", layout="wide")

# 完整的 HTML+CSS+JS 代码
html_code = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>铝板保温装饰一体板报价系统</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #f1f5f9;
            margin: 0;
            padding: 20px;
            color: #1e293b;
        }
        .container { 
            max-width: 800px; 
            margin: 0 auto; 
        }
        .header {
            background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
            color: white; 
            padding: 28px 32px; 
            border-radius: 20px;
            margin-bottom: 24px; 
            box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15);
            text-align: center;
        }
        .header h1 { margin: 0 0 10px 0; font-weight: 700; font-size: 1.6rem; letter-spacing: 1px;}
        .header p { margin: 0; opacity: 0.8; font-size: 0.95rem; }
        
        .control-panel {
            background: white; 
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03); 
            padding: 32px; 
        }
        .param-group { margin-bottom: 32px; }
        .param-group h3 { 
            font-size: 1.1rem; 
            margin: 0 0 20px 0; 
            color: #0f172a; 
            font-weight: 700; 
            display: flex;
            align-items: center;
        }
        .param-group h3::before {
            content: '';
            display: inline-block;
            width: 4px;
            height: 18px;
            background: #3b82f6;
            margin-right: 10px;
            border-radius: 2px;
        }
        .param-row { 
            display: grid; 
            grid-template-columns: 130px 1fr; 
            align-items: center; 
            gap: 16px; 
            margin-bottom: 16px; 
        }
        .param-label { font-weight: 600; font-size: 0.95rem; color: #475569; }
        
        select {
            width: 100%; 
            padding: 12px 16px; 
            border-radius: 12px;
            border: 1px solid #cbd5e1; 
            background: #f8fafc; 
            font-size: 0.95rem;
            font-weight: 500;
            color: #1e293b;
            font-family: inherit; 
            transition: 0.2s;
            cursor: pointer;
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23475569' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: right 12px center;
            background-size: 16px;
        }
        select:focus { outline: none; border-color: #3b82f6; background: #ffffff; box-shadow: 0 0 0 3px rgba(59,130,246,0.1); }

        .number-control {
            display: flex;
            align-items: center;
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.2s;
        }
        .number-control:focus-within {
            border-color: #3b82f6;
            background: #ffffff;
            box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
        }
        .stepper-btn {
            background: transparent;
            border: none;
            color: #64748b;
            font-size: 1.4rem;
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            user-select: none;
        }
        .stepper-btn:hover { background: #e2e8f0; color: #0f172a; }
        .stepper-btn:active { background: #cbd5e1; }
        
        .number-control input {
            flex: 1;
            text-align: center;
            border: none;
            background: transparent;
            font-size: 1.05rem;
            font-weight: 600;
            color: #0f172a;
            padding: 10px 0;
            outline: none;
            box-shadow: none;
            width: 100%;
        }
        input[type=number]::-webkit-inner-spin-button, 
        input[type=number]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
        input[type=number] { -moz-appearance: textfield; }

        .input-error { border-color: #ef4444 !important; box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1) !important; }
        .error-tip { font-size: 0.8rem; color: #ef4444; margin-top: 6px; display: none; font-weight: 500;}
        .error-tip.show { display: block; }

        .price-highlight {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border-radius: 20px; 
            padding: 28px 20px; 
            margin-top: 32px;
            text-align: center; 
            border: 1px solid #bbf7d0;
            position: relative;
            overflow: hidden;
        }
        .total-label { font-size: 0.9rem; color: #166534; font-weight: 700; opacity: 0.8;}
        .total-price { font-size: 3.5rem; font-weight: 800; color: #15803d; margin: 8px 0 4px 0; font-variant-numeric: tabular-nums;}
        .unit { font-size: 1.1rem; font-weight: 600; color: #166534; }
        .freight-tip { display: inline-block; margin-top: 8px; font-size: 0.85rem; color: #991b1b; font-weight: 600; background: #fee2e2; padding: 4px 12px; border-radius: 20px; }

        .footer-note { font-size: 0.75rem; text-align: center; margin-top: 24px; color: #94a3b8; font-weight: 500; }

        @media (max-width: 600px) { 
            .param-row { grid-template-columns: 1fr; gap: 8px; margin-bottom: 20px;} 
            .param-label { width: 100%; margin-bottom: 4px;} 
            .total-price { font-size: 2.8rem; } 
            .header { padding: 24px 20px; }
            .control-panel { padding: 24px 20px; }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>📊 铝板保温装饰一体板报价系统</h1>
        <p>参数自由调整 · 实时精准核算</p>
    </div>

    <div class="control-panel">
        <div class="param-group">
            <h3>产品规格配置</h3>
            <div class="param-row">
                <span class="param-label">保温芯材</span>
                <select id="coreType">
                    <option value="thermal">热固改性保温板</option>
                    <option value="rock120">120容重岩棉</option>
                    <option value="rock130" selected>130容重岩棉</option>
                    <option value="rock140">140容重岩棉</option>
                </select>
            </div>
            <div class="param-row">
                <span class="param-label">背板类型</span>
                <select id="backType">
                    <option value="perforated">打孔背板</option>
                    <option value="nonPerforated">不打孔背板</option>
                    <option value="cementCloth">水泥基布</option>
                </select>
            </div>
            <div class="param-row">
                <span class="param-label">铝板饰面工艺</span>
                <select id="surfaceProcess">
                    <option value="roller">辊涂</option>
                    <option value="spray">喷涂</option>
                </select>
            </div>
            <div class="param-row">
                <span class="param-label">铝板厚度 (mm)</span>
                <div>
                    <div class="number-control" id="thickControl">
                        <button class="stepper-btn minus">-</button>
                        <input type="number" id="thickness" step="0.1" value="1.5" min="0.1">
                        <button class="stepper-btn plus">+</button>
                    </div>
                    <div class="error-tip" id="thicknessError">⚠️ 喷涂工艺铝板厚度不能小于1.5mm</div>
                </div>
            </div>
            <div class="param-row">
                <span class="param-label">保温厚度 (cm)</span>
                <div class="number-control">
                    <button class="stepper-btn minus">-</button>
                    <input type="number" id="insulThick" step="0.5" value="4.0" min="0.5">
                    <button class="stepper-btn plus">+</button>
                </div>
            </div>
        </div>

        <div class="param-group" style="margin-bottom: 0;">
            <h3>实时市场参数</h3>
            <div class="param-row">
                <span class="param-label">今日铝锭 (元/吨)</span>
                <div class="number-control">
                    <button class="stepper-btn minus">-</button>
                    <input type="number" id="aluminumPrice" step="100" value="20000" min="10000">
                    <button class="stepper-btn plus">+</button>
                </div>
            </div>
            <div class="param-row">
                <span class="param-label">公司毛利 (%)</span>
                <div class="number-control">
                    <button class="stepper-btn minus">-</button>
                    <input type="number" id="profitPercentage" step="0.1" value="10.0" min="0" max="99">
                    <button class="stepper-btn plus">+</button>
                </div>
            </div>
        </div>

        <div class="price-highlight">
            <div class="total-label">系统建议底价</div>
            <div class="total-price" id="liveQuote">--.-- <span class="unit">元/㎡</span></div>
            <div class="freight-tip">⚠️ 此报价暂不含运费</div>
        </div>
    </div>
    
    <div class="footer-note">Powered by 铝板保温装饰一体板智能核算模型</div>
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
        const elThickControl = document.getElementById('thickControl');
        const elThicknessError = document.getElementById('thicknessError');
        const elInsulThick = document.getElementById('insulThick');
        const elAlPrice = document.getElementById('aluminumPrice');
        const elProfitPercent = document.getElementById('profitPercentage');
        const elLiveQuote = document.getElementById('liveQuote');

        function validateThickness() {
            const thickness = parseFloat(elThickness.value) || 1.5;
            const isSpray = elSurfaceProcess.value === 'spray';
            if (isSpray && thickness < 1.5) {
                elThickControl.classList.add('input-error');
                elThicknessError.classList.add('show');
                return false;
            } else {
                elThickControl.classList.remove('input-error');
                elThicknessError.classList.remove('show');
                return true;
            }
        }

        function calculatePrice(coreKey, backKey) {
            const material = CORE_MATERIALS[coreKey];
            if (!material) return null;
            
            const thickness = parseFloat(elThickness.value) || 1.5;
            const alPrice = parseFloat(elAlPrice.value) || 20000;
            const insulThick = parseFloat(elInsulThick.value) || 4.0;
            const profitPercent = parseFloat(elProfitPercent.value) || 10;
            const isSpray = elSurfaceProcess.value === 'spray';
            
            const marginFactor = 1 - (profitPercent / 100);
            const safeMarginFactor = Math.max(marginFactor, 0.01); 

            const safeThickness = isSpray ? Math.max(thickness, 1.5) : Math.max(thickness, 0.1);

            const processAddCost = isSpray ? SPRAY_ADD_PRICE : 0;
            const backboardCost = material.noBackboard ? 0 : (BACKBOARDS[backKey]?.price || 0);

            const alWeightSqm = safeThickness * AL_DENSITY;
            const alTonCost = Math.max(alPrice, 10000) + FEES.flattening + FEES.coloring;
            const alBaseCostWithLoss = (alWeightSqm * alTonCost / 1000) * FEES.lossRate;
            const totalAlCost = alBaseCostWithLoss + FEES.processing;

            const insulationCost = Math.max(insulThick, 0.5) * material.price;
            const compositeCost = material.compTimes * (COMPOSITE_GLUE + COMPOSITE_LABOR);

            const totalCost = totalAlCost + insulationCost + backboardCost + compositeCost + processAddCost;
            return Math.max(totalCost / safeMarginFactor, 0);
        }

        function updateUI() {
            const coreKey = elCoreType.value;
            const material = CORE_MATERIALS[coreKey];
            elBackType.disabled = !!material.noBackboard;
            elBackType.style.opacity = material.noBackboard ? "0.5" : "1";

            if (!validateThickness()) {
                elLiveQuote.innerHTML = `<span style="color: #dc2626; font-size: 2rem;">不可用此规格</span>`;
                return;
            }
            
            const backKey = material.noBackboard ? 'perforated' : elBackType.value;
            const quoteResult = calculatePrice(coreKey, backKey);
            
            if (quoteResult !== null) {
                elLiveQuote.innerHTML = `¥ ${quoteResult.toFixed(2)}`;
            } else {
                elLiveQuote.textContent = '--.--';
            }
        }

        document.querySelectorAll('.stepper-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                const isPlus = this.classList.contains('plus');
                const input = this.parentElement.querySelector('input');
                const step = parseFloat(input.getAttribute('step')) || 1;
                const min = parseFloat(input.getAttribute('min')) || 0;
                const max = input.hasAttribute('max') ? parseFloat(input.getAttribute('max')) : Infinity;
                
                let val = parseFloat(input.value) || 0;
                
                const getDecimals = (num) => (num.toString().split('.')[1] || '').length;
                const maxDecimals = Math.max(getDecimals(val), getDecimals(step));
                
                if (isPlus) {
                    val += step;
                    if (val > max) val = max;
                } else {
                    val -= step;
                    if (val < min) val = min;
                }
                
                input.value = val.toFixed(maxDecimals);
                updateUI();
            });
        });

        [elThickness, elAlPrice, elProfitPercent, elInsulThick].forEach(el => {
            el.addEventListener('input', updateUI);
            el.addEventListener('blur', updateUI); 
        });
        elSurfaceProcess.addEventListener('change', updateUI);
        elCoreType.addEventListener('change', updateUI);
        elBackType.addEventListener('change', updateUI);

        updateUI(); 
    });
</script>
</body>
</html>
"""

components.html(html_code, height=880, scrolling=True)
