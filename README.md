# http-status-probe

[![MIT License](https://img.shields.io/github/license/fonseb25/http-status-probe)](LICENSE)  
[![Docker Image Size](https://img.shields.io/docker/image-size/mfonseca21/http-status-probe)](https://hub.docker.com/r/mfonseca21/http-status-probe)  
[![Build Status](https://github.com/fonseb25/http-status-probe/actions/workflows/pylint.yml/badge.svg)](https://github.com/fonseb25/http-status-probe/actions)

## Overview

`http-status-probe` is a lightweight HTTP health-checker service designed for SRE and monitoring workflows. It’s built to integrate seamlessly with Prometheus, Grafana, Kubernetes, and Ansible-based deployments.

This project was developed as a final project for an SRE Academy course.

### Key Features

- Exposes an HTTP endpoint that probes configured URLs and returns status codes.  
- Designed to run in a Docker container, making it easy to deploy.  
- Deployable on Kubernetes, with infrastructure-as-code using Ansible.  
- Metrics exposed for Prometheus consumption to enable alerting and dashboards in Grafana.  
- Simple, minimal footprint.

## Architecture

Here’s a high-level view of `http-status-probe`:
```
.
├── app.py
├── CONTRIBUTING.md
├── deploy
│   ├── deployment.yaml
│   ├── grafana.yaml
│   ├── infra.yaml
│   ├── inventory.ini
│   └── prometheus.yaml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Docker  
- Kubernetes cluster (or `kubectl`)  
- Ansible  
- Prometheus & Grafana (or another monitoring stack)  

### Installation & Deployment

1. **Pull the container from Docker Hub**  
   ```bash
   docker pull fonseb25/http-status-probe:latest
2. **Deploy to Kubernetes using Ansible**

    You can use the provided Ansible playbooks to deploy the necessary YAML manifests.
    ```bash
    ansible-playbook -i deploy/inventory.ini deploy/infra.yaml
    ```