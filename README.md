
<h1 align="center">🛡️ Web Vulnerability Scanner</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web_Framework-ff69b4?logo=flask">
  <img src="https://img.shields.io/badge/Security-Vulnerability_Scanner-red">
  <img src="https://img.shields.io/badge/Author-Rittik_Gourav_Raul-brightgreen">
</p>

<p align="center">
  <b>A Python-based tool to detect XSS and SQL Injection vulnerabilities in web applications</b><br>
  Complete with a web crawler, form parser, automated payload injection, and a Flask UI.
</p>

---

## 🚀 Project Overview

The **Web Vulnerability Scanner** is a lightweight tool designed to help ethical hackers, security researchers, and developers detect common web vulnerabilities like:

- 🧨 Cross-Site Scripting (XSS)
- 🛠️ SQL Injection (SQLi)

It automates the process of crawling, analyzing forms, injecting malicious payloads, and identifying unsafe input fields — all accessible through a simple Flask-based web interface.

---

## 🧠 Key Features

- 🌐 Crawls an entire website for internal links
- 📑 Parses HTML forms using BeautifulSoup
- 🧪 Injects test payloads to detect vulnerabilities
- 📋 Displays results live on a Flask interface
- 📄 Generates a `report.md` file for future reference
- 🧰 Built 100% with Python for easy extensibility

---

## 🏗️ Project Structure

```
web-vuln-scanner/
├── scanner.py         # Core logic: crawling, forms, payloads
├── web_app.py         # Flask UI logic
├── main.py            # For GitHub language detection
├── report.md          # Scan results
├── requirements.txt   # Python dependencies
├── README.md          # You are here
└── templates/
    └── index.html     # Flask frontend
```

---

## 📦 Requirements

Install these Python libraries:

```bash
pip install flask requests beautifulsoup4
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

---

## 🔧 How to Run (Linux or Windows)

```bash
python3 web_app.py
```

📍 Open in your browser:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

1. Enter a URL (like: http://testphp.vulnweb.com)
2. Click **Scan**
3. View vulnerabilities in the browser and `report.md`

---

## 🔍 Sample Report Output

```markdown
### XSS Vulnerability Found
- URL: http://target.com/contact
- Payload: <script>alert('XSS')</script>

### SQL Injection Vulnerability Found
- URL: http://target.com/login
- Payload: ' OR '1'='1
```

---

## 📸 Interface Screenshot

> _UI Screenshot (replace with actual)_

![Web Scanner UI](https://raw.githubusercontent.com/username/repo/main/demo-screenshot.png)

---

## 🧪 Safe Test Targets

Use these **intentionally vulnerable test sites**:

- http://testphp.vulnweb.com
- http://xss-game.appspot.com
- http://demo.testfire.net

⚠️ **Do NOT use this tool on websites without permission.**

---

## 🎓 Learning Outcomes

- How scanners crawl and test web forms
- Writing secure input-handling in Flask
- Testing for XSS & SQLi vulnerabilities
- Ethical hacking workflows

---

## 👤 Author

**Rittik Gourav Raul**  
_BTech Cybersecurity | Internship Project | GitHub: [rgr-001](https://github.com/rgr-001)_

---

## 📜 License

This project is for **educational and ethical use only**. Unauthorized scanning of live websites without permission is illegal and unethical.

---

## ⭐ Feedback or Improvements?

Feel free to fork, raise issues, or contribute if you find bugs or want to enhance this project!

---

## 📌 Tags (Topics)

```
python, flask, web-scanner, xss, sqli, security, vulnerability, ethical-hacking, internship
```

---

```
🛡️ Built with 💻 by Rittik Gourav Raul for Cybersecurity Internship Task
```
