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
        .container { 
            max-width: 900px; 
            margin: 0 auto; 
            background: white; 
            border-radius: 12px; 
            box-shadow: 0 8px 20px rgba(0,0,0,0.1); 
            overflow: hidden; 
        }
        .header { 
            background: linear-gradient(135deg, #1e3c5c 0%, #2b4c6e 100%); 
            color: white; 
            padding: 24px 32px; 
            text-align: center; 
        }
        .header h1 { margin: 0; font-size: 26px; font-weight: 700; }
        .content { 
            padding: 32px; 
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 32px; 
        }
        .section-title {
            font-size: 18px;
            border-bottom: 2px solid #eef2f7;
            padding-bottom: 8px;
            margin-bottom: 20px;
            color: #1e3c5c;
        }
        .form-group { margin-bottom: 20px; }
        .form-group label { 
            display: block; 
            margin-bottom: 8px; 
            font-weight: 600; 
            color: #4a5568; 
            font-size: 14px;
        }
        .form-group input, .form-group select { 
            width: 100%; 
            padding: 12px; 
            border: 1px solid #cbd5e1; 
            border-radius: 8px; 
            font-size: 16px; 
            transition: all 0.3s;
        }
        .form-group input:focus, .form-group select:focus {
            outline: none;
            border-color: #1e3c5c;
            box-shadow: 0 0 0 3px rgba(30, 60, 92, 0.1);
        }
        .result-panel { 
            grid-column: span 2; 
            background: #f8fafc; 
            padding: 24px; 
            border-radius: 12px; 
            text-align: center; 
            border: 2px dashed #94a3b8; 
        }
        .result-price { 
            font-size: 38px; 
            color: #e53e3e; 
            font-weight: bold; 
            margin: 16px 0; 
        }
        .error-msg {
            color: #e53e3e;
            font-size: 14px;
            margin-top: 8px;
            display: none;
        }
        .details { 
            text-align: left; 
            margin-top: 20px; 
            font-size: 15px; 
            color: #64748b; 
            line-height: 1.6;
            background: white;
            padding: 16px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }
        @media(max-width: 768px) { 
            .content { grid-template-columns: 1fr; padding: 20px; } 
            .result-panel { grid-column: span 1; } 
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>铝板保温装饰一体板报价系统</h1>
        </div>
        <div class="content">
            <div>
                <div class="section-title">📊 基础参数</div>
                <div class="form-group">
                    <label>今日铝锭价格 (元/吨)</label>
                    <input type="number" id="alPrice" value="20000" step="100">
                </div>
                <div class="form-group">
                    <label>铝板厚度 (mm)</label>
                    <input type="number" id="alThickness" value="1.5" step="0.1">
                    <div id="thicknessError" class="error-msg">⚠️ 提示：标准工艺厚度建议≥1.5mm</div>
                </div>
                <div class="form-group">
                    <label>毛利系数 (如0.9代表10个点)</label>
                    <input type="number" id="margin" value="0.9" step="0.01">
                </div>
            </div>

            <div>
                <div class="section-title">🧱 材料配置</div>
                <div class="form-group">
                    <label>选择保温材料类型</label>
                    <select id="materialType">
                        <option value="热固">热固</option>
                        <option value="120容重岩棉(打孔背板)">120容重岩棉(打孔背板)</option>
                        <option value="130容重岩棉(打孔背板)" selected>130容重岩棉(打孔背板)</option>
                        <option value="130容重岩棉(不打孔)">130容重岩棉(不打孔背板)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>保温层厚度 (cm)</label>
                    <input type="number" id="insulationThickness" value="4.0" step="0.1">
                </div>
            </div>

            <div class="result-panel">
                <div style="color: #475569; font-weight: bold; font-size: 18px;">最终建议系统报价</div>
                <div class="result-price" id="finalPrice">¥ 0.00 / ㎡</div>
                
                <div class="details" id="costDetails">
                    </div>
            </div>
        </div>
    </div>

    <script>
        // 1. 全局配置常量 (保持与 Excel 数据严格一致)
        const DENSITY = 2.71;          // 铝密度
        const FLATTENING_FEE = 1500.0; // 开平费用
        const COLORING_FEE = 5000.0;   // 上色费用
        const LOSS_RATE = 1.15;        // 损耗率
        const AL_PROCESSING_FEE = 15.0;// 铝板加工费

        // 保温材料物料库
        const MATERIAL_DB = {
            "热固": { price: 4.4, backboard: 0.0, composite_times: 1.0, glue: 2.0, labor: 8.0 },
            "120容重岩棉(打孔背板)": { price: 3.3, backboard: 8.5, composite_times: 2.0, glue: 2.0, labor: 8.0 },
            "130容重岩棉(打孔背板)": { price: 3.52, backboard: 8.5, composite_times: 2.0, glue: 2.0, labor: 8.0 },
            "130容重岩棉(不打孔)": { price: 3.52, backboard: 0.0, composite_times: 2.0, glue: 2.0, labor: 8.0 }
        };

        // 2. 核心计算函数
        function calculateQuote() {
            try {
                // 获取输入值
                const alPrice = parseFloat(document.getElementById('alPrice').value) || 0;
                const alThickness = parseFloat(document.getElementById('alThickness').value) || 0;
                const margin = parseFloat(document.getElementById('margin').value) || 1;
                const materialName = document.getElementById('materialType').value;
                const insThickness = parseFloat(document.getElementById('insulationThickness').value) || 0;

                // 厚度校验提示
                const errorMsg = document.getElementById('thicknessError');
                errorMsg.style.display = alThickness < 1.5 ? 'block' : 'none';

                // 获取对应材料的固定属性
                const mat = MATERIAL_DB[materialName];

                // 核心计算公式 (还原 Excel 表格逻辑)
                // 1. 铝板含损耗成本 = (厚度 * 密度 * (铝锭价 + 开平 + 上色) / 1000) * 损耗
                const alTonCost = alPrice + FLATTENING_FEE + COLORING_FEE;
                const alBaseCost = (alThickness * DENSITY * alTonCost / 1000) * LOSS_RATE;

                // 2. 保温材料纯成本 = 保温厚度 * 单价
                const insulationCost = insThickness * mat.price;

                // 3. 复合总成本 = (胶水 + 人工) * 复合次数
                const compositeCost = (mat.glue + mat.labor) * mat.composite_times;

                // 4. 合计总成本
                const totalCost = alBaseCost + AL_PROCESSING_FEE + insulationCost + mat.backboard + compositeCost;

                // 5. 最终报价 = 总成本 / 毛利系数
                const finalPrice = totalCost / margin;

                // 渲染最终结果
                document.getElementById('finalPrice').innerText = `¥ ${finalPrice.toFixed(2)}`;
                
                // 渲染核算明细
                document.getElementById('costDetails').innerHTML = `
                    <strong>📄 成本核算明细：</strong><br>
                    • 铝板基材成本（含损耗）: <span style="float:right">¥ ${alBaseCost.toFixed(2)} / ㎡</span><br>
                    • 铝板加工费: <span style="float:right">¥ ${AL_PROCESSING_FEE.toFixed(2)} / ㎡</span><br>
                    • 保温层纯成本: <span style="float:right">¥ ${insulationCost.toFixed(2)} / ㎡</span><br>
                    • 背板加工费: <span style="float:right">¥ ${mat.backboard.toFixed(2)} / ㎡</span><br>
                    • 胶水与复合人工: <span style="float:right">¥ ${compositeCost.toFixed(2)} / ㎡</span>
                `;
            } catch (error) {
                console.error("计算出错:", error);
                document.getElementById('finalPrice').innerText = '--.-- 元/㎡';
            }
        }

        // 3. 初始化与事件监听 (确保 DOM 加载完成后绑定)
        document.addEventListener('DOMContentLoaded', () => {
            const inputElements = ['alPrice', 'alThickness', 'margin', 'materialType', 'insulationThickness'];
            
            inputElements.forEach(id => {
                const el = document.getElementById(id);
                // 监听输入和选择变化，实时触发计算
                el.addEventListener('input', calculateQuote);
                el.addEventListener('change', calculateQuote);
            });

            // 页面加载完毕后立刻执行一次默认计算
            calculateQuote();
        });
    </script>
</body>
</html>
