# 🎯 xssniper

![xssniper](/logo.png "xssniper v1.0 - ATHEX!")

[![Version](https://img.shields.io/badge/version-1.0-red)](https://github.com/yourusername/xssniper)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-GPLv3-green)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)](https://github.com/yourusername/xssniper)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/xssniper)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/yourusername/xssniper/pulls)

> **"One Shot. One Inject."** — Silent but Lethal XSS Detection Framework

---

## 📖 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [WAF Bypass Support](#waf-bypass-support)
- [Reporting](#reporting)
- [Screenshots](#screenshots)
- [License](#license)
- [Contributing](#contributing)
- [Credits](#credits)

---

## 🔍 Overview

**xssniper** is an enterprise-grade, automated penetration testing framework designed to **detect**, **exploit**, and **report** Cross-Site Scripting (XSS) vulnerabilities in web applications. With over **1500+ pre-installed payloads**, context-aware validation, and advanced WAF bypass techniques, xssniper is the ultimate weapon for security professionals and bug bounty hunters.

Unlike traditional XSS scanners that generate false positives, xssniper uses a **headless browser reverse connection** (`--reverse-check`) to verify every finding in real-time, ensuring that only **executable** vulnerabilities are reported.

---

## ⚡ Key Features

### 🎯 Detection & Targeting
- **1500+ Pre-installed Payloads**: Automatic fuzzing with constantly updated vectors
- **Context-Aware Validation**: Distinguishes between executable contexts (HTML, JS, event handlers, javascript:/data: URIs) from harmless reflections
- **Headless Browser Verification**: Optional `--reverse-check` confirms findings and eliminates false positives
- **Multiple Targeting Options**:
  - Single URL
  - File (bulk scanning)
  - stdin/pipe input
  - Raw HTTP request (`-r`)
  - Dorking (multiple search engines)
  - Built-in crawler for deep scanning

### 💉 Injection Vectors
- GET/POST parameters
- HTTP Headers (Cookie, User-Agent, Referer)
- DOM-based injection
- HTTP Response Splitting
- JSON/XML payloads

### 🛡️ Evasion & Bypass
- **Per-WAF Bypassers** for 10+ major WAFs
- **Character Encoding Bypassers** (URL, Hex, Unicode, Double-encode, etc.)
- **Proxy & Tor Support** for anonymous scanning
- **Client-Certificate Authentication** for protected endpoints

### 📊 Reporting
- **PDF Reports**: Professional, detailed reports with vulnerability evidence
- **XML/JSON Export**: Perfect for CI/CD pipelines and automation
- **GeoIP Mapping**: Visual representation of target servers worldwide

---

## 🚀 Installation

### 📦 System Requirements
- **Python**: 3.7 or higher
- **OS**: Linux (preferred), Windows, macOS
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk**: 500MB free space

### 🔧 Dependencies
xssniper requires the following Python libraries:

| Library | Purpose |
|---------|---------|
| `python3-pycurl` | Python bindings to libcurl (HTTP requests) |
| `python3-bs4` | Error-tolerant HTML parsing |
| `python3-geoip` | IP-to-country resolution |
| `python3-gi` | GObject introspection for GTK GUI |
| `python3-selenium` | Headless browser automation |
| `firefoxdriver` | Firefox WebDriver for Selenium |
| `ddgs` | DuckDuckGo search API for dorking |
| `fpdf2` | PDF report generation |

### 🐧 Linux (Debian/Ubuntu/Kali/Parrot)
```
sudo apt update
sudo apt install -y python3 python3-pip python3-pycurl python3-bs4 python3-geoip python3-gi python3-selenium firefoxdriver python3-fpdf2
pip3 install ddgs
```

### 🐧 Linux (Arch/Manjaro)
```
sudo pacman -S python python-pip python-pycurl python-beautifulsoup4 python-geoip python-gobject python-selenium firefox-driver python-fpdf2
pip3 install ddgs
```
### 🍎 macOS
```
brew install python3 pycurl beautifulsoup4 geoip pygobject3 selenium geckodriver fpdf2
pip3 install ddgs
```
### Windows
```
pip install pycurl beautifulsoup4 pygeoip PyGObject selenium ddgs fpdf2

# Download Firefox and GeckoDriver manually from:
# https://github.com/mozilla/geckodriver/releases
```

## 🎬 Quick Start

***Basic Scan***
```
python3 xssniper.py -u "http://target.com/page?param=value"
```
***Advanced Scan with Verification***
```
python3 xssniper.py -u "http://target.com/search?q=test" --reverse-check --threads=10
```
***Bulk Scan from File***
```
python3 xssniper.py -l targets.txt --output=results.json
```
***Dorking Mode***
```
python3 xssniper.py -d "inurl:search?q=" --engine=google --pages=5
```

## 📖 Usage Guide
*🎯 Target Options*
- Flag	     Description
- -u,   --url	Single target URL
- -l,   --list	File containing list of targets
- -r,   --request	Raw HTTP request file
- -c,   --crawl	Crawl and scan all pages
- -d,   --dork	Dorking mode with search engines

*💉 Injection Options*
- Flag	         Description
- --data	       POST data (e.g., param1=value1&param2=value2)
- --cookie	     Custom cookie header
- --user-agent	 Custom User-Agent
- --referer      Custom Referer header
- --headers	     Additional custom headers (JSON format)

*🛡️ Evasion Options*
- Flag             	Description
- --waf-bypass    	Enable WAF bypass techniques
- --waf-list	      List all supported WAFs
- --encode	        Encoding type (url, hex, unicode, base64, etc.)
- -proxy	          Proxy URL (e.g., socks5://127.0.0.1:9050)
- --tor	            Enable Tor routing
*🔍 Scanning Options*
- Flag	            Description
- --threads   	    Number of concurrent threads (default: 5)
- --timeout	        Request timeout in seconds (default: 10)
- --delay	          Delay between requests in milliseconds
- --reverse-check	  Enable headless browser verification
- --verbose	        Verbose output mode

*📊 Output Options*
- Flag	       Description
- --output	   Output file (JSON/XML format)
- --pdf	       Generate PDF report
- --html	     Generate HTML report
- --log	       Log file location


## 🛡️ WAF Bypass Support

xssniper includes specialized bypassers for the following WAFs:

| WAF | Vendor | Bypass Vectors | Status |
|-----|--------|---------------|--------|
| Cloudflare | Cloudflare | 15+ | ✅ Supported |
| Akamai | Akamai (Kona) | 12+ | ✅ Supported |
| AWS WAF | Amazon Web Services | 10+ | ✅ Supported |
| Azure WAF | Microsoft | 10+ | ✅ Supported |
| Imperva | Imperva (Incapsula) | 14+ | ✅ Supported |
| F5 ASM | F5 Networks | 11+ | ✅ Supported |
| Barracuda | Barracuda Networks | 8+ | ✅ Supported |
| ModSecurity | Trustwave (OWASP CRS) | 18+ | ✅ Supported |
| Wordfence | Wordfence (WordPress) | 7+ | ✅ Supported |
| Sucuri | Sucuri (CloudProxy) | 9+ | ✅ Supported |
| FortiWeb | Fortinet | 8+ | ✅ Supported |
| WebKnight | AQTRONIX | 6+ | ✅ Supported |

---

## 🎯 Advanced Bypass Techniques

| Technique | Description | Example |
|-----------|-------------|---------|
| Case Mutation | Mix uppercase/lowercase | `<ScRiPt>alert(1)</sCrIpT>` |
| Double Encoding | URL encode twice | `%253Cscript%253E` |
| Hex Encoding | Hexadecimal representation | `\x3cscript\x3e` |
| Unicode Escaping | Unicode character codes | `\u003cscript\u003e` |
| Null Byte Injection | Break WAF parsing | `%00<script>alert(1)</script>` |
| Comment Injection | Break WAF signatures | `<script>/*comment*/alert(1)</script>` |
| Event Handler Abuse | Use alternative triggers | `<body onload=alert(1)>` |
| Data URI Exploitation | Use data: URI scheme | `data:text/html,<script>alert(1)</script>` |
| JavaScript URI | Use javascript: protocol | `<a href="javascript:alert(1)">click</a>` |
| HTML Entity Encoding | Encode special characters | `&lt;script&gt;alert(1)&lt;/script&gt;` |

---

## 🧪 WAF Fingerprinting

| Detection Method | Description |
|------------------|-------------|
| Response Headers | Server, X-Powered-By, Set-Cookie patterns |
| Error Messages | Custom error pages and codes |
| Challenge Pages | Captcha, browser verification |
| Response Time | Delay patterns and rate limiting |
| Cookie Analysis | WAF-specific cookies (e.g., `__cfduid` for Cloudflare) |
| Block Page Signatures | HTML/CSS patterns in block pages |

## 🚀 WAF Bypass Examples
```
# Auto-detect and bypass WAF
python3 xssniper.py -u "http://target.com/page?param=value" --waf-bypass
```
```
# List all supported WAFs
python3 xssniper.py --waf-list
```
```
# Target specific WAF
python3 xssniper.py -u "http://target.com/page?param=value" --waf-bypass --target-waf=cloudflare
```
```
# Custom encoding chain
python3 xssniper.py -u "http://target.com/page?param=value" --encode=url,hex,unicode --waf-bypass
```
```
# Aggressive bypass mode
python3 xssniper.py -u "http://target.com/page?param=value" --waf-bypass --aggressive --threads=20
```

### 📊 Reporting
*📄 PDF Reports*

Generate professional security assessment reports with:

```
python3 xssniper.py -u "http://target.com" --pdf=report.pdf
```
### 💻 CI/CD Integration
*Export results in JSON/XML format for integration with:*

```
python3 xssniper.py -u "http://target.com" --output=results.json
```

## 🙏 Credits
Developer: [Athexblackhat]!
Framework: Built with Python, PyCurl, Selenium, BeautifulSoup, and other open-source libraries.
Special Thanks: The security research community for payload contributions and WAF bypass techniques.