# SYS-AUDIT: Active Telemetry Shell

A Python-based endpoint simulation tool featuring a custom graphical facade built with Tkinter. This project is designed to simulate an interactive terminal environment to demonstrate real-time, rule-based signature detection and structured security telemetry logging.

Instead of executing live commands on the host operating system, the utility isolates and evaluates inputs within a controlled interface, mimicking how defensive detection agents and high-interaction honeypots intercept Indicators of Compromise (IoCs).

## 🚀 Features

- **Graphical Terminal Facade:** Implements an interactive terminal environment mimicking a root-level Linux prompt (`[ root@security-audit:~ ]# `).
- **Rule-Based Detection Engine:** Intercepts real-time string inputs to match against pre-configured signature strings and high-risk administrative commands (e.g., `sudo`, `rm -rf`, `nmap`, `id_rsa`).
- **Structured Telemetry Logging:** Captures rich session metadata—including precise timestamps and user identity—and serializes data into SIEM-ready JSON formatting.
- **GUI Event-Handling Overrides:** Overrides default Tkinter text widgets and key bindings to prevent terminal prompt manipulation and maintain console integrity.

## 🛠️ Tech Stack & Key Concepts

- **Language:** Python
- **GUI Framework:** Tkinter
- **Data Interchange:** JSON
- **Concepts:** Event-Driven Programming, Host-Based Auditing, Signature Matching, Data Serialization, Input Validation

## 📂 Architecture & Code Overview

The system processes terminal inputs through a specialized execution pipeline:

1. **Input Interception:** The UI binds the `<Return>` key to capture line-by-line user entries.
2. **Signature Evaluation:** The raw string is cross-referenced with a list of security alert triggers. If matched, an immediate operational alert (`[ALERT]: SUSPICIOUS ACTIVITY DETECTED`) is appended directly into the terminal stream.
3. **Log Flushing:** Session metadata is structured into an append-only transaction file (`activity_log.json`).

### Sample Log Output
```json
{
  "timestamp": "2026-06-03 18:15:00",
  "identity": "root@security-audit",
  "raw_input": "nmap -sV 192.168.1.1"
}
