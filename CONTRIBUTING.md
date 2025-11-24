# Contributing to http-status-probe

First off — thank you for considering contributing! 🙏 We welcome contributions from everyone, whether it's bug reports, features, documentation, or helping with testing.

## Table of Contents

1. [How Can I Contribute?](#how-can-i-contribute)  
2. [Development Setup](#development-setup)  
3. [Submitting a Pull Request](#submitting-a-pull-request)  
4. [Reporting Issues](#reporting-issues)

---

## How Can I Contribute?

You can contribute in various ways:

- Reporting bugs or suggesting enhancements via GitHub Issues  
- Writing or improving documentation  
- Adding new probe types or enhancing probe logic  
- Improving Docker or Kubernetes/Ansible deployment scripts  
- Improving test coverage, adding unit or integration tests  
- Optimizing performance / resource usage  

---

## Development Setup

Here’s how to set up a development environment:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/fonseb25/http-status-probe.git
   cd http-status-probe
2. **Install dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
3. **Run Locally**
    ```bash
    docker build -t http-status-probe-dev .
    docker run -p 8080:8080 http-status-probe-dev

---

## Submitting a Pull Request

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-new-feature`)
3. Make your changes, and commit them with a clear message
4. Run tests locally
5. Push to your fork (`git push origin feature/my-new-feature`)
6. Open a Pull Request against `main` in the upstream repo
7. Fill in the PR template (if you have one) — describe what change you made, why, and any related issue

---

## Reporting Issues

If you find a bug or want to suggest a feature:
1. Search existing issues to see if it has already been reported
2. If not, open a new issue
3. Provide as much detail as possible: steps to reproduce, expected vs actual behavior, logs, environment, versions, etc.