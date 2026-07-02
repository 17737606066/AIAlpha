<script setup>
import { Activity, AlertTriangle, BarChart3, FileText, Radar } from "lucide-vue-next";

const modules = [
  { icon: BarChart3, label: "Portfolio", value: "88", note: "medium risk" },
  { icon: Radar, label: "Stock Radar", value: "12", note: "candidates" },
  { icon: Activity, label: "Signal Engine", value: "7", note: "active signals" },
  { icon: AlertTriangle, label: "Risk Watch", value: "3", note: "alerts" },
];

const factors = [
  ["Fundamental", 78],
  ["Capital Flow", 72],
  ["Industry", 86],
  ["Technical", 68],
  ["Valuation", 61],
  ["News", 74],
  ["Risk Control", 70],
];
</script>

<template>
  <main class="shell">
    <section class="topbar">
      <div>
        <p class="eyebrow">AI Alpha Ultimate</p>
        <h1>Investment Decision Dashboard</h1>
      </div>
      <button class="icon-button" aria-label="Open reports">
        <FileText :size="20" />
      </button>
    </section>

    <section class="grid metrics">
      <article v-for="item in modules" :key="item.label" class="metric">
        <component :is="item.icon" :size="20" />
        <span>{{ item.label }}</span>
        <strong>{{ item.value }}</strong>
        <small>{{ item.note }}</small>
      </article>
    </section>

    <section class="workspace">
      <div class="panel">
        <h2>Multi-Factor Signal</h2>
        <div v-for="[name, score] in factors" :key="name" class="factor">
          <span>{{ name }}</span>
          <div class="bar"><i :style="{ width: `${score}%` }"></i></div>
          <b>{{ score }}</b>
        </div>
      </div>

      <div class="panel">
        <h2>Morning Brief</h2>
        <p>Global tone is neutral. AI infrastructure, PCB, and advanced packaging remain the main watchlist themes.</p>
        <p>Risk budget should be checked before adding exposure. Avoid chasing crowded breakouts without confirmation.</p>
      </div>
    </section>
  </main>
</template>
