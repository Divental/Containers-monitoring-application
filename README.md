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

## Set up

1. Clone the repository:
```
git clone git@github.com:YuriiBalandyuk/container-monitoring.git
cd container-monitoring
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Setup telegram bot:
   * Step 1: In the search bar
     ```
     BotFather
     ```
   * Step 2: In the text line
     ```
     /start
     /newbot
     ```
   * Step 3: Create an individual bot name, and your username must end with 'bot'
     ```
     Example: yourcoolbot
     ```
   * Step 4: Save your personal Telegram API key
     ```
     Example: 1234567890:ABCDEF...
     ```
   * Step 5: Create .env file in the 'container-monitoring' directory and put the key there
     ```
     Example: API_TOKEN=1234567890:ABCDEF...
     ```
4. Start the monitoring service:
```
cd .\container-monitoring\
python main.py
```

## License
This project is licensed under the Apache License Version 2.0. See LICENSE for details.

## Contact
For questions, contact yuriibalandyuk@gmail.com or open an issue in the repository.


