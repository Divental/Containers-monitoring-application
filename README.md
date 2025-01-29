# Container monitoring application

## Overview

Container Monitoring is an automated system for tracking resource usage in containerized environments. It collects real-time metrics, analyzes resource consumption, and sends notifications to designated channels when thresholds are exceeded.

## Features

* Metrics Collection: Gathers CPU, RAM, disk, and network usage from running containers;
* Alerts & Notifications: Sends alerts via Telegram when resources exceed predefined limits;
* Visualization: Uses Grafana and Prometheus for real-time monitoring and dashboarding;
* Automation & Integration:
    * Uses systemd for automatic startup;
    * Logs data with the Elastic Stack;
    * Implements CI/CD workflows with GitHub Actions.

## Tech Stack

* Programming Language: Python (psutil, docker-py);
* Containerization: Docker;
* Monitoring & Logging: Prometheus, Grafana, Elastic Stack;
* Automation & CI/CD: systemd, GitHub Actions;
* Messaging: Telegram API.

## Installation

### Prerequisites: 

* Docker installed on your system;
* Python 3.7 with pip;
* Prometheus and Grafana set up.

## Setup

1. Clone the repository:
```
git clone git@github.com:YuriiBalandyuk/container-monitoring.git
cd container-monitoring
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Start the monitoring service:
```
python main.py
```
