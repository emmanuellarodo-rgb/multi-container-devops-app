async function fetchData() {
  try {
    const metrics = await fetch('http://backend:5000/metrics');
    const metricsData = await metrics.json();

    const scale = await fetch('http://backend:5000/scale');
    const scaleData = await scale.json();

    const health = await fetch('http://backend:5000/health');
    const healthData = await health.json();

    document.getElementById('cpu').innerText = metricsData.cpu + "%";

    const scaleText = scaleData.decision;
    const scaleEl = document.getElementById('scale');
    scaleEl.innerText = scaleText;

    if (scaleText.includes("UP")) scaleEl.className = "red";
    else if (scaleText.includes("DOWN")) scaleEl.className = "yellow";
    else scaleEl.className = "green";

    document.getElementById('health').innerText = healthData.status;

  } catch (err) {
    console.log(err);
  }
}

setInterval(fetchData, 3000);
fetchData();
