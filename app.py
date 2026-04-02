<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>铝板保温装饰一体板报价系统</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 24px 16px;
            color: #1a2c3e;
        }

        .container {
            max-width: 1300px;
            margin: 0 auto;
        }

        .header {
            background: linear-gradient(135deg, #1e3c5c 0%, #2b4c6e 100%);
            color: white;
            padding: 24px 32px;
            border-radius: 28px;
            margin-bottom: 28px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }

        .header h1 {
            margin: 0 0 8px 0;
            font-weight: 700;
            font-size: 1.8rem;
        }

        .header p {
            margin: 0;
            opacity: 0.9;
            font-size: 0.95rem;
        }

        .dashboard {
            display: flex;
            flex-wrap: wrap;
            gap: 28px;
        }

        .control-panel {
            flex: 1;
            min-width: 300px;
            background: white;
            border-radius: 28px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.05);
            padding: 28px;
            height: fit-content;
        }

        .result-panel {
            display: none !important;
        }

        .param-group {
            margin-bottom: 28px;
            border-bottom: 1px solid #e9eef3;
            padding-bottom: 20px;
        }

        .param-group h3 {
            font-size: 1.1rem;
            margin: 0 0 18px 0;
            color: #1e4663;
            font-weight: 600;
        }

        .param-row {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            justify-content: space-between;
        }

        .param-label {
            font-weight: 500;
            width: 115px;
            font-size: 0.88rem;
            color: #2c4b6e;
        }

        .param-input {
            flex: 1;
            min-width: 150px;
        }

        select, input {
            width: 100%;
            padding: 10px 12px;
            border-radius: 14px;
            border: 1px solid #cbd5e1;
            background: #ffffff;
            font-size: 0.9rem;
            font-family: inherit;
            transition: 0.2s;
        }

        select:focus, input:focus {
            outline: none;
            border-color: #2b6e9e;
            box-shadow: 0 0 0 3px rgba(43,110,158,0.15);
        }

        .input-error {
            border-color: #e53e3e !important;
            box-shadow: 0 0 0 3px rgba(229, 62, 62, 0.15) !important;
        }

        .error-tip {
            font-size: 0.75rem;
            color: #e53e3e;
            margin-top: 4px;
            display: none;
        }

        .error-tip.show {
            display: block;
        }

        .price-highlight {
            background: linear-gradient(135deg, #f0f7fc 0%, #e8f0f7 100%);
            border-radius: 24px;
            padding: 24px 20px;
            margin-top: 20px;
            text-align: center;
            border: 1px solid #cde0ef;
        }

        .total-price {
            font-size: 3rem;
            font-weight: 800;
            color: #1a6b4a;
            margin: 12px 0;
            letter-spacing: -0.5px;
        }

        .total-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: #5d7f9e;
            font-weight: 500;
        }

        .unit {
            font-size: 1rem;
            font-weight: normal;
        }

        /* 新增不含运费提示样式 */
        .freight-tip {
            text-align: center;
            margin-top: 12px;
            font-size: 0.9rem;
            color: #d93025;
            font-weight: 500;
        }

        .footer-note {
            font-size: 0.7rem;
            text-align: center;
            margin-top: 28px;
            color: #8ba0b5;
            background: white;
            border-radius: 20px;
            padding: 10px;
        }

        @media (max-width: 700px) {
            .param-label {
                width: 100%;
            }
            .total-price {
                font-size: 2.2rem;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>📊 铝板保温装饰一体板 · 报价系统</h1>
        <p>铝锭价格 + 毛利系数 可自由调整 | 实时计算报价</p>
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
                <div class="total-price" id="liveQuote">¥ 188.31 <span class="unit">元/㎡</span></div>
                <!-- 这里添加不含运费提示 -->
                <div class="freight-tip">此报价不含运费</div>
            </div>
        </div>

        <div class="result-panel">
            <div class="detail-table">
                <table>
                    <thead>
                        <tr>
                            <th style="width: 20%;">产品系列</th>
                            <th style="width: 20%;">背板类型</th>
                            <th style="width: 35%;">保温规格</th>
                            <th style="width: 25%;">报价 (元/㎡)</th>
                        </tr>
                    </thead>
                    <tbody id="priceTableBody"></tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="footer-note">
        铝板保温装饰一体板报价系统 | 参数可调，实时计算
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const a = 2.71, b = 10, c = 3;
        const sprayAddPrice = 15;
        const d = {
            e: 1500,
            f: 5000,
            g: 15,
            h: 1.15
        };

        const i = {
            thermal: { j: "热固改性保温板", k: 4.4, l: 1, m: true },
            rock120: { j: "120容重岩棉", k: 3.3, l: 2, m: false },
            rock130: { j: "130容重岩棉", k: 3.52, l: 2, m: false },
            rock140: { j: "140容重岩棉", k: 3.85, l: 2, m: false }
        };

        const n = {
            perforated: 8.5,
            nonPerforated: 7.5,
            cementCloth: 4.0
        };

        const o = {
            perforated: "打孔背板",
            nonPerforated: "不打孔背板",
            cementCloth: "水泥基布"
        };

        const p = document.getElementById('coreType');
        const q = document.getElementById('backType');
        const processSelect = document.getElementById('surfaceProcess');
        const r = document.getElementById('thickness');
        const thicknessError = document.getElementById('thicknessError');
        const s = document.getElementById('insulThick');
        const t = document.getElementById('aluminumPrice');
        const u = document.getElementById('profitFactor');
        const v = document.getElementById('liveQuote');

        if (!p || !q || !v || !processSelect || !thicknessError) {
            v.textContent = '加载失败，请刷新页面';
            return;
        }

        let w = p.value;

        function validateThickness() {
            const thicknessVal = parseFloat(r.value) || 1.5;
            const isSpray = processSelect.value === 'spray';
            
            if (isSpray && thicknessVal < 1.5) {
                r.classList.add('input-error');
                thicknessError.classList.add('show');
                return false;
            } else {
                r.classList.remove('input-error');
                thicknessError.classList.remove('show');
                return true;
            }
        }

        function x() {
            const y = parseFloat(r.value) || 1.5;
            const z = parseFloat(t.value) || 20000;
            const A = parseFloat(s.value) || 4.0;
            const B = parseFloat(u.value) || 0.9;
            
            return {
                D: processSelect.value === 'spray' ? Math.max(y, 1.5) : Math.max(y, 0.1),
                E: Math.max(z, 10000),
                F: d.e,
                G: d.f,
                H: d.g,
                I: d.h,
                J: Math.max(A, 0.5),
                K: Math.max(B, 0.1)
            };
        }

        function L(M, N) {
            const O = i[M];
            if (!O) return null;
            const P = x();
            const isSpray = processSelect.value === 'spray';
            const processAdd = isSpray ? sprayAddPrice : 0;

            let Q = O.m ? 0 : (n[N] || 0);
            const R = P.D * a;
            const S = P.E + P.F + P.G;
            const T = R * S / 1000;
            const U = T * P.I;
            const V = U + P.H;
            const W = P.J * O.k;
            const X = O.l * (c + b);
            const Y = V + W + Q + X + processAdd;
            const Z = Y / P.K;

            return {
                aa: Math.max(Z, 0),
                ab: O.j,
                ac: O.m ? "无背板" : (o[N] || "未知"),
                ad: O.m
            };
        }

        function ba(bb) {
            return bb.toFixed(2);
        }

        function bc() {
            if (!validateThickness()) {
                v.innerHTML = `<span style="color: #e53e3e;">✘ 喷涂工艺厚度需≥1.5mm</span>`;
                return;
            }
            
            const bd = w === 'thermal' ? 'perforated' : q.value;
            const be = L(w, bd);
            if (be) {
                v.innerHTML = `¥ ${ba(be.aa)} <span class="unit">元/㎡</span>`;
            } else {
                v.textContent = '--.-- 元/㎡';
            }
        }

        function bf() {
            const bg = i[w];
            if (bg && bg.m) {
                q.disabled = true;
            } else {
                q.disabled = false;
            }
        }

        function bh() {
            bf();
            bc();
        }

        function bi() {
            [r, t, u, s].forEach(el => {
                el.addEventListener('input', bh);
                el.addEventListener('change', bh);
            });

            processSelect.addEventListener('change', bh);
            r.addEventListener('input', validateThickness);

            p.addEventListener('change', e => {
                w = e.target.value;
                bh();
            });

            q.addEventListener('change', bh);
            window.addEventListener('resize', bh);
        }

        function bj() {
            w = p.value;
            bi();
            setTimeout(() => {
                bh();
            }, 100);
        }

        (function bk() {
            bj();
        })();
    });
</script>
</body>
</html>