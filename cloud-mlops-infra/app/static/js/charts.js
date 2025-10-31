const gpuCtx = document.getElementById("gpuChart");
const cpuCtx = document.getElementById("cpuChart");

let gpuData = [];
let cpuData = [];
let labels = [];

const gpuChart = new Chart(gpuCtx, {
  type: "line",
  data: { labels: labels, datasets: [{ label: "GPU Usage (%)", data: gpuData, borderColor: "red" }] },
});

const cpuChart = new Chart(cpuCtx, {
  type: "line",
  data: { labels: labels, datasets: [{ label: "CPU Usage (%)", data: cpuData, borderColor: "blue" }] },
});

async function updateMetrics() {
  const res = await fetch("/metrics");
  const data = await res.json();
  if (labels.length > 15) { labels.shift(); gpuData.shift(); cpuData.shift(); }
  labels.push(data.timestamp);
  gpuData.push(data.gpu_usage);
  cpuData.push(data.cpu_usage);
  gpuChart.update();
  cpuChart.update();
}
setInterval(updateMetrics, 2000);
