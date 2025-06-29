# 🚨 InfraWatch — Real-Time Infrastructure Monitoring Platform

InfraWatch is a full-stack, cloud-native infrastructure monitoring system inspired by the high-reliability requirements of telecom companies like **Nokia**. It provides **real-time server health metrics**, **automated alerting**, and a **modern React dashboard**, all built with production-grade technologies.

> ✅ Designed to impress hiring managers at **Nokia Canada**  
> ✅ Engineered with Spring Boot, React, MySQL, Python, and Docker  
> ✅ Built with reliability, modularity, and observability in mind

---

## 📡 Live Demo Overview

- 🧠 Real-time system metric ingestion via Python-based agents
- 📦 Spring Boot backend for API, alert engine, and data persistence
- 📈 React frontend dashboard for live metric visualization and alerts
- 📊 Auto-refresh every 10s for real-time updates
- 🔔 Auto-generated alerts when thresholds are breached (e.g., CPU > 70%)

---

## 🧠 Architecture

[ Python Agent ] ---> [ Spring Boot Backend ] ---> [ MySQL DB ]
|
[ React UI ]


Each layer is modular and pluggable, making InfraWatch highly extensible.

---

## ⚙️ Tech Stack

| Layer        | Tech Used                          |
|--------------|------------------------------------|
| Agent        | Python, psutil, argparse, requests |
| Backend API  | Java 17, Spring Boot, JPA, MySQL   |
| Frontend UI  | React (CRA), Axios, Recharts       |
| Data Storage | MySQL (local / cloud)              |
| Deployment   | Docker (WIP), GCP-ready setup      |

---

## 🚀 Local Setup

### 1. 🖥 Backend (Spring Boot)

```bash
cd infrawatch-backend
./mvnw spring-boot:run

Ensure MySQL is running and accessible (set credentials in application.properties).
```
---
### 2. 🌐 Frontend (React)
```bash
cd infrawatch-frontend
npm install
npm start
```
---
### 3. 🐍 Agent (Python)
```bash
cd infrawatch-agent
python agent.py --serverId=1 --source=agent-01
```
---
### 📊 Key Features
✅ Real-Time Metrics: Collected every 10s and visualized live

✅ Alerts System: Auto-detects threshold violations (e.g., CPU > 70%)

✅ Modern Dashboard: Built with Recharts, tables, and a clean layout

✅ Agent Customization: Run agents on multiple servers with unique IDs

✅ Resilient Backend: Spring Boot + MySQL + JPA
---
### 📈 Sample Metric Payload
```json
{
  "metricType": "CPU",
  "value": 85.2,
  "unit": "%",
  "timestamp": "2025-06-17T18:25:43",
  "serverId": 1,
  "source": "agent-01"
}
```
---
###📌 Coming Soon
📦 Docker + GCP Deployment

📧 Email/Webhook alerts (via AWS SES or SendGrid)

📉 Historical data analytics with filterable views

👤 User authentication + role-based dashboard access

🌍 Agent CLI installer (Linux/Windows)
---
🧑‍💼 About the Developer
Hi, I’m a Software Engineer Intern at Cognizant in Canada, building InfraWatch as a flagship project to showcase my real-world skills in full-stack systems, cloud architecture, and observability tools. I’m passionate about joining Nokia Canada in 2026 as a full-time engineer.

📨 parmarrex114@gmail.com
🔗 https://www.linkedin.com/in/rex-parmar/
---
📄 License
MIT License — use freely for learning, building, and improving observability tools!

---
🔥 If you’re hiring or mentoring — I’d love to connect and showcase InfraWatch live!

