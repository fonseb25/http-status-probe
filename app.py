"""
Application for probing http codes returned on requests
"""

import random
import asyncio
import httpx
from fastapi import FastAPI
from prometheus_client import Counter, Histogram, Gauge, make_asgi_app
import uvicorn

app = FastAPI()

# Metrics
PROBES = Counter("probes_total", "Total probes", ["code"])
LATENCY = Histogram("probe_latency_seconds", "Probe latency", ["code"])
IN_FLIGHT = Gauge("probes_in_flight", "Probes in flight")
FAILURES = Counter("probe_failures_total", "Failures", ["code", "error"])

prometheus_app = make_asgi_app()
app.mount("/metrics", prometheus_app)

CODES = [200, 300, 400, 500]
URL = "https://httpbin.org/status/{}"

async def probe():
    """
    probe function to loop through the codes array
    """
    async with httpx.AsyncClient() as client:
        while True:
            code = random.choice(CODES)
            IN_FLIGHT.inc()
            PROBES.labels(code=code).inc()
            start = asyncio.get_event_loop().time()
            try:
                await client.get(URL.format(code), timeout=10)
                LATENCY.labels(code=code).observe(asyncio.get_event_loop().time() - start)
            except httpx.HTTPError as e:
                FAILURES.labels(code=code, error=type(e).__name__).inc()
            finally:
                IN_FLIGHT.dec()
            await asyncio.sleep(3)

@app.on_event("startup")
async def startup():
    """
    startup function that creates the probe task
    """
    # start_http_server(8000)  # Prometheus metrics
    asyncio.create_task(probe())

@app.get("/")
def home():
    """
    home function to return status
    """
    return {"status": "probing httpbin.org"}

@app.get("/health")
def health():
    """
    health function to return status
    """
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
