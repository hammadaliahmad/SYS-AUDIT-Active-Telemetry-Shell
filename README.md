# Endpoint Activity Logging & Telemetry Auditor

A lightweight, event-driven administrative shell simulation built in Python using Tkinter. This project demonstrates how automated security auditing agents monitor terminal interactions, enforce input integrity controls, and compile structured telemetry data for incident response analysis.

## 🚀 Key Features

* **Event-Driven Telemetry Capture:** Intercepts whole-line user interactions dynamically using cursor index evaluation the exact millisecond the user presses `Enter`.
* **Signature-Based Alerting:** Scans active inputs against an enterprise-style keyword array (`sudo`, `nmap`, `rm -rf`, `id_rsa`) using case-insensitive string matching to simulate threat detection.
* **Input Integrity & Validation Controls:** Implements real-time keypress interception (`return "break"`) to prevent users from backspacing into or arrow-keying past the active terminal prompt.
* **SIEM-Ready Structured Logging:** Automatically serializes captured command data, identity metadata, and ISO-formatted timestamps directly into a flat JSON ledger ready for ingestion by platforms like Splunk or Elastic.

## 🛠️ Built With

* **Python 3**
* **Tkinter** (Graphical User Interface Framework)
* **JSON & DateTime Libraries** (Structured Data Parsing)

## 📊 Sample Log Output

The tool completely isolates the user's raw input payload from the interface aesthetics, outputting perfectly formatted JSON blocks inside `activity_log.json`:

```json
{
  "timestamp": "2026-06-03 14:45:12",
  "identity": "root@security-audit",
  "raw_input": "sudo nmap -sV 192.168.1.1"
}
