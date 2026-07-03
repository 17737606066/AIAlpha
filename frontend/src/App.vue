<script setup>
import { computed, onMounted, ref } from "vue";
import { Activity, AlertTriangle, BarChart3, FileText, Map, Radar, RefreshCw, Shield, WalletCards } from "lucide-vue-next";

const activeView = ref("dashboard");
const query = ref("");
const selectedHolding = ref(null);
const reportExpanded = ref(false);
const lastRefresh = ref("09:30:00");
const dataSource = ref("演示数据");
const marketTone = ref("中性偏强，AI硬件主线仍在，但分歧扩大。");
const discipline = ref("只有资金与评分同时确认才加仓，避免情绪追涨。");
const morningBrief = ref({
  global: "美元、美债与科技股风险偏好共同影响 A股 AI主线。",
  opportunities: ["PCB", "AI服务器", "先进封装", "HBM"],
  account_action: "核心持仓继续观察，题材高位降低暴露。",
});

const factors = ref([
  ["基本面", 78],
  ["资金面", 72],
  ["行业景气", 86],
  ["技术结构", 68],
  ["估值", 61],
  ["消息面", 74],
  ["风险控制", 70],
]);

const stocks = ref([
  { name: "AI服务器链", theme: "AI服务器 PCB", score: 88, risk: "中", action: "持有，等确认加仓", detail: "产业趋势强，资金承接较好，短线不追高。" },
  { name: "PCB核心", theme: "PCB CCL", score: 85, risk: "中", action: "分批跟踪", detail: "景气度高，观察换手与量能是否健康。" },
  { name: "先进封装", theme: "封装 HBM", score: 80, risk: "中低", action: "回踩关注", detail: "订单逻辑清晰，适合右侧确认。" },
  { name: "存储/HBM", theme: "HBM 存储", score: 76, risk: "中", action: "观察订单", detail: "关注价格周期与海外需求。" },
  { name: "半导体设备", theme: "设备 国产替代", score: 72, risk: "中", action: "低吸研究", detail: "长期逻辑好，短期看催化。" },
  { name: "高位题材股", theme: "短线 情绪 风险", score: 57, risk: "高", action: "控仓止损", detail: "情绪驱动更强，资金退潮时回撤会放大。" },
]);

const funds = ref([
  ["AI服务器", 82],
  ["PCB/CCL", 79],
  ["先进封装", 72],
  ["HBM存储", 66],
  ["半导体设备", 58],
  ["消费电子", 44],
]);

const risks = ref([
  ["追高风险", 76],
  ["汇率扰动", 54],
  ["政策扰动", 48],
  ["流动性回撤", 63],
  ["单一主题集中", 71],
]);

const logs = ref([
  "09:30 启动全模块：宏观、资金、产业、技术、风险。",
  "09:32 资金地图显示 AI硬件链流入占优。",
  "09:35 风险雷达提示高位题材股不宜加仓。",
]);

const tabs = [
  ["dashboard", "总览", BarChart3],
  ["radar", "股票雷达", Radar],
  ["funds", "资金地图", Map],
  ["risk", "风险雷达", Shield],
  ["portfolio", "持仓", WalletCards],
  ["reports", "晨报", FileText],
  ["logs", "日志", Activity],
];

const accountScore = computed(() => Math.min(96, Math.round(factors.value.reduce((sum, item) => sum + item[1], 0) / factors.value.length) + 12));
const filteredStocks = computed(() => {
  const keyword = query.value.trim().toLowerCase();
  return stocks.value.filter((stock) => !keyword || `${stock.name}${stock.theme}${stock.action}${stock.risk}`.toLowerCase().includes(keyword));
});
const strongSignals = computed(() => stocks.value.filter((stock) => stock.score >= 78).length);
const activeRisks = computed(() => risks.value.filter((risk) => risk[1] > 60).length);

onMounted(loadDashboardOverview);

async function loadDashboardOverview() {
  try {
    const response = await fetch("/api/dashboard/overview");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    applyOverview(await response.json());
    dataSource.value = "后端 API";
    const time = new Date().toLocaleTimeString("zh-CN", { hour12: false });
    lastRefresh.value = time;
    logs.value.unshift(`${time} 已从后端 API 加载驾驶舱数据。`);
  } catch {
    dataSource.value = "演示数据";
  }
}

function applyOverview(payload) {
  if (Array.isArray(payload.factors)) factors.value = payload.factors.map((item) => [item.name, item.score]);
  if (Array.isArray(payload.stocks)) stocks.value = payload.stocks.map((stock) => ({ detail: "来自后端驾驶舱接口，等待接入实时行情与公告数据。", ...stock }));
  if (Array.isArray(payload.funds)) funds.value = payload.funds.map((item) => [item.name, item.heat]);
  if (Array.isArray(payload.risks)) risks.value = payload.risks.map((item) => [item.name, item.score]);
  if (payload.market_tone) marketTone.value = payload.market_tone;
  if (payload.discipline) discipline.value = payload.discipline;
  if (payload.morning_brief) morningBrief.value = payload.morning_brief;
}

function scoreClass(score) {
  if (score >= 78) return "positive";
  if (score < 65) return "risk";
  return "warning";
}

function switchView(view) {
  activeView.value = view;
}

function selectHolding(stock) {
  selectedHolding.value = stock;
  activeView.value = "portfolio";
}

function rescore() {
  factors.value = factors.value.map(([name, score]) => [name, clamp(score + randomStep(4), 45, 96)]);
  stocks.value = stocks.value.map((stock) => ({ ...stock, score: clamp(stock.score + randomStep(3), 48, 94) }));
  funds.value = funds.value.map(([name, score]) => [name, clamp(score + randomStep(5), 35, 95)]);
  const time = new Date().toLocaleTimeString("zh-CN", { hour12: false });
  lastRefresh.value = time;
  logs.value.unshift(`${time} 重新评分：资金地图、风险雷达、持仓评分已刷新。`);
}

function randomStep(range) {
  return Math.round(Math.random() * range * 2 - range);
}

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}
</script>

<template>
  <main class="shell">
    <section class="topbar">
      <div>
        <p class="eyebrow">AI Alpha Ultimate 2.1 · {{ dataSource }}</p>
        <h1>投资决策驾驶舱</h1>
      </div>
      <button class="primary-button" @click="rescore">
        <RefreshCw :size="18" />
        重新评分
      </button>
    </section>

    <section class="toolbar">
      <div class="tabs">
        <button v-for="[key, label, Icon] in tabs" :key="key" class="tab" :class="{ active: activeView === key }" @click="switchView(key)">
          <component :is="Icon" :size="16" />
          {{ label }}
        </button>
      </div>
      <input v-model="query" class="search" placeholder="搜索 PCB / HBM / 封装 / 风险" @input="activeView = 'radar'" />
    </section>

    <section class="metrics">
      <article class="metric"><span>账户评分</span><strong>{{ accountScore }}</strong><small>可持有，严控追高</small></article>
      <article class="metric"><span>雷达候选</span><strong>{{ filteredStocks.length }}</strong><small>{{ strongSignals }} 个强信号</small></article>
      <article class="metric"><span>资金热度</span><strong>{{ funds[0][1] }}</strong><small>流入 AI 硬件</small></article>
      <article class="metric"><span>风险预警</span><strong>{{ activeRisks }}</strong><small class="risk">需复核</small></article>
      <article class="metric"><span>最近刷新</span><strong class="time-text">{{ lastRefresh }}</strong><small>评分日志已记录</small></article>
    </section>

    <section v-if="activeView === 'dashboard'" class="workspace">
      <div class="panel">
        <h2>多因子评分</h2>
        <div v-for="[name, score] in factors" :key="name" class="factor">
          <span>{{ name }}</span>
          <div class="bar"><i :style="{ width: `${score}%` }"></i></div>
          <b>{{ score }}</b>
        </div>
      </div>
      <div class="panel">
        <h2>今日总控</h2>
        <p>{{ marketTone }}</p>
        <p><span v-for="item in morningBrief.opportunities" :key="item" class="tag">{{ item }}</span></p>
        <p>{{ discipline }}</p>
        <p>{{ morningBrief.account_action }}</p>
      </div>
    </section>

    <section v-if="activeView === 'radar'" class="panel">
      <h2>AI 股票雷达</h2>
      <div class="card-grid">
        <article v-for="stock in filteredStocks" :key="stock.name" class="stock-card" @click="selectHolding(stock)">
          <div><h3>{{ stock.name }}</h3><p>{{ stock.theme }}</p></div>
          <strong :class="scoreClass(stock.score)">{{ stock.score }}</strong>
          <small>风险：{{ stock.risk }}</small>
          <b>{{ stock.action }}</b>
        </article>
      </div>
    </section>

    <section v-if="activeView === 'funds'" class="workspace">
      <div class="panel">
        <h2>AI 资金地图</h2>
        <div v-for="[name, score] in funds" :key="name" class="factor">
          <span>{{ name }}</span>
          <div class="bar fund"><i :style="{ width: `${score}%` }"></i></div>
          <b>{{ score }}</b>
        </div>
      </div>
      <div class="panel heat-grid">
        <h2>板块热力</h2>
        <button v-for="[name, score] in funds" :key="name" class="heat-tile" :class="{ hot: score > 75, cold: score < 55 }" @click="query = name; activeView = 'radar'">
          <b>{{ name }}</b>
          <span>资金热度 {{ score }}</span>
        </button>
      </div>
    </section>

    <section v-if="activeView === 'risk'" class="workspace">
      <div class="panel">
        <h2>风险雷达</h2>
        <div v-for="[name, score] in risks" :key="name" class="factor">
          <span>{{ name }}</span>
          <div class="bar danger"><i :style="{ width: `${score}%` }"></i></div>
          <b :class="score > 70 ? 'risk' : 'warning'">{{ score }}</b>
        </div>
      </div>
      <div class="panel">
        <h2>风控动作</h2>
        <p>高位题材股跌破短线结构时减仓。</p>
        <p>单一主题不要超过 45%，保留现金做纠错。</p>
        <p>每次重新评分自动写入交易日志。</p>
      </div>
    </section>

    <section v-if="activeView === 'portfolio'" class="panel">
      <h2>持仓观察</h2>
      <table class="table">
        <thead><tr><th>标的</th><th>主题</th><th>评分</th><th>动作</th></tr></thead>
        <tbody>
          <tr v-for="stock in stocks" :key="stock.name" @click="selectedHolding = stock">
            <td>{{ stock.name }}</td><td>{{ stock.theme }}</td><td :class="scoreClass(stock.score)">{{ stock.score }}</td><td>{{ stock.action }}</td>
          </tr>
        </tbody>
      </table>
      <div class="detail" v-if="selectedHolding">
        <h3>{{ selectedHolding.name }}</h3>
        <p>{{ selectedHolding.detail }}</p>
        <p><b>AI建议：</b>{{ selectedHolding.action }}</p>
        <p><b>风险等级：</b>{{ selectedHolding.risk }}</p>
      </div>
    </section>

    <section v-if="activeView === 'reports'" class="workspace">
      <div class="panel">
        <h2>今日投资晨报</h2>
        <p>全球：{{ morningBrief.global }}</p>
        <p>A股：{{ marketTone }}</p>
        <p>机会：{{ morningBrief.opportunities.join('、') }}</p>
        <p v-if="reportExpanded">完整：若指数放量上行，优先看资金地图热度前三；若缩量震荡，控制仓位并等待回踩确认。</p>
      </div>
      <div class="panel">
        <h2>账户总控</h2>
        <p>今日最强：PCB核心、AI服务器链</p>
        <p>今日最危险：高位题材股</p>
        <button class="primary-button" @click="reportExpanded = !reportExpanded">{{ reportExpanded ? '收起晨报' : '展开完整晨报' }}</button>
      </div>
    </section>

    <section v-if="activeView === 'logs'" class="panel">
      <h2>AI 交易日志</h2>
      <div class="log"><p v-for="item in logs" :key="item">{{ item }}</p></div>
    </section>
  </main>
</template>
