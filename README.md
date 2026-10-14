# Rego Cloud Intern Backend - Systemd Deployment

## Prerequisites
* Ubuntu Server 24.04 LTS
* Python 3, `python3-venv`, and `python3-pip`
* A dedicated `fastapi` system user without an interactive login

## Installation Steps
1. Update system packages and install Python tools.
2. Create a dedicated non-root system user: `sudo useradd -r -s /usr/sbin/nologin fastapi`
3. Create the application directory `/opt/rego-fastapi` and set suitable ownership and permissions.
4. Place `main.py` and `requirements.txt` into the directory.
5. Create a virtual environment and install the dependencies:
   ```bash
   sudo -u fastapi python3 -m venv .venv
   sudo -u fastapi .venv/bin/pip install -r requirements.txt
