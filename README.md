# 🔌 USB Sentinel

A lightweight Python security tool for monitoring USB drive activity and identifying unusual connection patterns.

## 🛡️ Overview

USB Sentinel monitors drive connections on a Windows system and records USB connection and disconnection events.

The tool maintains a local activity log and assigns a basic risk level based on the number of currently connected drives.

## ✨ Features

- 🔌 USB drive connection monitoring
- 🔄 USB connection and disconnection detection
- 📝 Local security event logging
- 📊 Basic activity-based risk classification
- 🕒 Timestamped security events
- 💻 Lightweight command-line interface
- ⚡ Real-time monitoring with periodic checks

## 🔍 How It Works

USB Sentinel continuously checks the available drives on the system.

When a new drive appears, the tool:

1. Detects the new drive
2. Records the connection event
3. Captures the timestamp
4. Calculates a basic risk level
5. Displays the security event## 🗂️ Activity Logging

Security events are stored locally in:

```text
usb_activity.log
```

Each event contains:

### 🕒 Timestamp

Records the exact date and time when the USB event occurred.

### 🔄 Event Type

Identifies whether the USB device was connected or disconnected.

### 💾 Drive Identifier

Records the detected drive associated with the security event.

## 🧰 Technologies Used

### 🐍 Python

Core programming language used to build the monitoring tool.

### 💻 Operating System Interface (`os`)

Used to detect available drives on the Windows system.

### 📦 JSON (`json`)

Used to structure security event data before storing it in the log.

### 🕒 Date and Time (`datetime`)

Used to generate timestamps for security events.

### ⏱️ Time-based Monitoring (`time`)

Used to periodically check for changes in connected drives.

## 🎯 Project Objective

The objective of USB Sentinel is to demonstrate a simple endpoint-security monitoring concept using Python.

The project focuses on detecting removable-drive activity, recording security events, and presenting basic risk indicators that can be extended into a more advanced endpoint monitoring system.

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/nithyashree-24/USB-Sentinel.git
```

### 2. Open the Project Folder

```bash
cd USB-Sentinel
```

### 3. Run the Program

```bash
python usb_sentinel.py
```

When a drive is removed, the disconnection is also recorded.

## 🚦 Risk Classification

| Risk Level | Condition |
|---|---|
| 🟢 LOW | Fewer than 3 connected drives |
| 🟡 MEDIUM | 3–4 connected drives |
| 🔴 HIGH | 5 or more connected drives |

> The risk level is a simple activity-based indicator and does not determine whether a USB device is malicious.

## 🔮 Future Enhancements

### 🔹 Device Identification

Capture additional USB device information such as device name, vendor, and serial number.

### 🔹 Trusted Device Management

Maintain a list of approved USB devices and flag unknown devices.

### 🔹 File Activity Monitoring

Monitor file creation, modification, and deletion activity on connected removable drives.

### 🔹 Advanced Risk Scoring

Combine device identity, connection frequency, activity patterns, and file behaviour into a more detailed risk score.

### 🔹 Security Dashboard

Build a graphical dashboard for viewing USB events, risk levels, and historical activity.
