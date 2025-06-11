# 🛡️ SimpleWAF: A Web Application Firewall Simulator

A simplified, interactive Web Application Firewall (WAF) simulator built with **Python** and **Streamlit**. This project demonstrates core WAF principles by inspecting simulated HTTP requests against a configurable set of security rules to detect common web vulnerabilities like **SQL Injection**, **Cross-Site Scripting (XSS)**, and **Path Traversal**.

---

## 🚀 Introduction

In today's digital landscape, web applications are constant targets for malicious attacks. A **Web Application Firewall (WAF)** acts as a crucial defensive layer, protecting applications by filtering and monitoring HTTP traffic.

**SimpleWAF** provides a hands-on platform to understand how WAFs function. It allows you to:

- Simulate various HTTP requests, including both clean and malicious payloads.
- Observe how pre-defined WAF rules (based on common attack signatures) are applied.
- Manage rules dynamically and see their immediate effect on detection capabilities.

This project highlights practical skills in **defensive cybersecurity**, **threat detection**, and **application security**.

---

## ✨ Features

- **Request Simulation:** Simulate GET and POST HTTP requests with custom URLs and request bodies.
- **Rule-Based Detection:** Inspects requests using regex-based rules to catch:
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - Path Traversal / Directory Traversal
  - Command Injection
- **Dynamic Rule Management:** Add new custom rules or remove existing ones via the UI.
- **Interactive UI:** Built with Streamlit for a clean and intuitive web interface.
- **Clear Feedback:** Visual feedback shows whether a request is clean or a threat, with rule details.

---

## 📸 Preview

![Preview Screenshot](public/1.png) 
![Preview Screenshot](public/2.png) 

---

## 🛠️ Tech Stack

- **Python** – Core programming language
- **Streamlit** – For building the interactive frontend
- **re** – Python's regular expression module

---

## 📦 Getting Started

### Prerequisites

- Python 3.8+
- `pip` (usually included with Python)

### Installation

```bash
git clone https://github.com/shivangi1612/simplewaf.git
cd SimpleWAF
