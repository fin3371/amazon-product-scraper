![Proxio Banner](https://raw.githubusercontent.com/proxio-net/amazon-product-scraper/refs/heads/main/PROXIO%20BANNER.png)

# 🛒 Amazon Product Scraper

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4.14.3-green.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A lightweight, efficient Python scraper for extracting product data from Amazon. Perfect for price monitoring, competitor research, and product analysis.

## 🚀 Powered by Proxio

Scrape Amazon at scale without getting blocked! Use **[Proxio's Residential Proxies](https://proxio.net)** for reliable, CAPTCHA-free scraping.

### 🎁 Special Offer
Use code **`GIT30`** for **30% OFF** your first month!
[**Get Started →**](https://proxio.net/pricing)

---

## 📑 Table of Contents

- [Powered by Proxio](#-powered-by-proxio)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Using Proxio Proxies](#-using-proxio-proxies)
- [Output Example](#-output-example)
- [Anti-Detection Tips](#-anti-detection-tips)
- [Legal Disclaimer](#-legal-disclaimer)
- [Use Cases](#-use-cases)
- [Support](#-support)
- [License](#-license)

---

## ✨ Features

- 🔍 **Keyword search** - Search for products by keyword
- 📦 **ASIN scraping** - Scrape specific products by ASIN
- 🌍 **Multi-domain support** - Works with amazon.com, .co.uk, .de, etc.
- 🔒 **Proxy integration** - Built-in proxy support
- 💾 **Export formats** - CSV and JSON output
- ⚡ **Lightweight** - Uses requests & BeautifulSoup (no heavy browsers)
- 🔄 **Smart delays** - Random delays to mimic human behavior

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/proxio-net/amazon-product-scraper.git
cd amazon-product-scraper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Search by Keyword
```bash
python scraper.py --keyword "wireless headphones" --pages 3
```

### Scrape Specific ASINs
```bash
python scraper.py --asins "B08N5WRWNW,B0BSHF7LKM,B09JQL3NWT"
```

### With Proxy (Recommended)
```bash
python scraper.py --keyword "laptop" --pages 2 --proxy "http://username:password@geo.proxio.cc:16666"
```

### Different Amazon Domain
```bash
python scraper.py --keyword "books" --domain "co.uk" --pages 1
```

### Export to JSON
```bash
python scraper.py --keyword "shoes" --output json
```

### Command-line Arguments
| Argument | Description | Example |
|----------|-------------|---------|
| `--keyword` | Search keyword | `"laptop"` |
| `--asins` | Comma-separated ASINs | `"B0B9WTP5HR,B0CS8B2N24"` |
| `--pages` | Number of pages (default: 1) | `3` |
| `--domain` | Amazon domain (default: com) | `co.uk`, `de`, `fr`, `com.tr` etc. |
| `--proxy` | Proxy URL | `http://user:pass@host:port` |
| `--output` | Format: `csv` or `json` (default: csv) | `json` |

## 🔌 Using Proxio Proxies

Amazon has **aggressive anti-bot detection**. To scrape reliably:

1. **Sign up at [Proxio.net](https://proxio.net)**
2. **Use coupon `GIT30` for 30% off**
3. Get credentials from dashboard
4. Use format: `http://username:password@geo.proxio.cc:16666`

### Why Proxio for Amazon Scraping?
- ✅ **10M+ residential IPs** - Real device IPs, not datacenter
- ✅ **99.9% success rate** - Bypass CAPTCHAs and blocks
- ✅ **Rotating IPs** - Fresh IP for each request
- ✅ **Geo-targeting** - Target specific countries/cities
- ✅ **Unlimited bandwidth** - No caps or throttling

## 📊 Output Example

### CSV Output
```csv
asin,title,price,rating,reviews,url
B0DW238TXK,"ASUS ROG Flow Z13 (2025) Gaming Laptop, 13” ROG Nebula 16:10 2.5K 180Hz/3ms, AMD Ryzen AI MAX+ 395, RDNA 3.5 Graphics, 128GB LPDDR5X 8000MHz, 1TB PCIe Gen 4 SSD, Wi-Fi 7, Win 11 Pro, GZ302EA-XS99","2,364.68",4.0,50,https://www.amazon.com/ASUS-Flow-Gaming-Laptop-Nebula/dp/B0DW238TXK/ref=sr_1_25?dib=eyJ2IjoiMSJ9.K5oS4Vlruu5bAy0m8t8mXIhscDv3Ad2qMAw-S1N98iWzA-yi5ggrghdn4nkQ7s09TJb8hJxux512bkGgUg0nYDpJ6MBaILP60j4CmDKW5vYT-1YNq32emCj-muRP0EPtdUDA8XpxHlzY7LQ4J7S9kzNqUTSsSXQMtSAmZP2alz3CfDa59xR43kf0aumSnoqY4Ofd1-5OyjJUe7Fg99z6Td2mgUHhKEWQ4gnamGKkVRs.H_SjVFvI5YJFspwbe_pd2_C2NChovG1UCpTl6y5iKnc&dib_tag=se&keywords=laptop&qid=1765821577&sr=8-25
B0FN5VQS3Y,"Dell Inspiron 16"" Touchscreen Laptop Computer, Windows 11 Pro 32GB RAM 1TB SSD, Intel Core 7 150U Processor, FHD+ 1920 x 1200 Display, Microsoft Office Lifetime Suite, Backlit Keyboard, Ice Blue",N/A,5.0,2,https://www.amazon.com/Dell-Inspiron-Touchscreen-Processor-Microsoft/dp/B0FN5VQS3Y/ref=sr_1_26?dib=eyJ2IjoiMSJ9.K5oS4Vlruu5bAy0m8t8mXIhscDv3Ad2qMAw-S1N98iWzA-yi5ggrghdn4nkQ7s09TJb8hJxux512bkGgUg0nYDpJ6MBaILP60j4CmDKW5vYT-1YNq32emCj-muRP0EPtdUDA8XpxHlzY7LQ4J7S9kzNqUTSsSXQMtSAmZP2alz3CfDa59xR43kf0aumSnoqY4Ofd1-5OyjJUe7Fg99z6Td2mgUHhKEWQ4gnamGKkVRs.H_SjVFvI5YJFspwbe_pd2_C2NChovG1UCpTl6y5iKnc&dib_tag=se&keywords=laptop&qid=1765821577&sr=8-26
```

### JSON Output
```json
[
  {
    "asin": "B0FTZL5RBT",
    "title": "HP 17.3 inch Laptop, Touchscreen HD+ Display, Intel 12-Core Ultra 7 255U, 16 GB RAM, 1TB SSD, Intel Graphics, Windows 11 Pro, Backlit Keyboard, Natural Silver",
    "price": "N/A",
    "rating": "5.0",
    "reviews": "1",
    "url": "https://www.amazon.com/HP-Touchscreen-Display-Graphics-Keyboard/dp/B0FTZL5RBT/ref=sr_1_31?dib=eyJ2IjoiMSJ9.K5oS4Vlruu5bAy0m8t8mXIhscDv3Ad2qMAw-S1N98iWzA-yi5ggrghdn4nkQ7s09TJb8hJxux512bkGgUg0nYDpJ6MBaILP60j4CmDKW5vYT-1YNq32emCj-muRP0EPtdUDA8XpxHlzY7LQ4J7S9kzNqUTSsSXQMtSAmZP2alz3CfDa59xR43kf0aumSnoqY4Ofd1-5OyjJUe7Fg99z6Td2mgUHhKEWQ4gnamGKkVRs.H_SjVFvI5YJFspwbe_pd2_C2NChovG1UCpTl6y5iKnc&dib_tag=se&keywords=laptop&qid=1765821577&sr=8-31"
  },
  {
    "asin": "B0DW238TXK",
    "title": "ASUS ROG Flow Z13 (2025) Gaming Laptop, 13” ROG Nebula 16:10 2.5K 180Hz/3ms, AMD Ryzen AI MAX+ 395, RDNA 3.5 Graphics, 128GB LPDDR5X 8000MHz, 1TB PCIe Gen 4 SSD, Wi-Fi 7, Win 11 Pro, GZ302EA-XS99",
    "price": "2,364.68",
    "rating": "4.0",
    "reviews": "50",
    "url": "https://www.amazon.com/ASUS-Flow-Gaming-Laptop-Nebula/dp/B0DW238TXK/ref=sr_1_25?dib=eyJ2IjoiMSJ9.K5oS4Vlruu5bAy0m8t8mXIhscDv3Ad2qMAw-S1N98iWzA-yi5ggrghdn4nkQ7s09TJb8hJxux512bkGgUg0nYDpJ6MBaILP60j4CmDKW5vYT-1YNq32emCj-muRP0EPtdUDA8XpxHlzY7LQ4J7S9kzNqUTSsSXQMtSAmZP2alz3CfDa59xR43kf0aumSnoqY4Ofd1-5OyjJUe7Fg99z6Td2mgUHhKEWQ4gnamGKkVRs.H_SjVFvI5YJFspwbe_pd2_C2NChovG1UCpTl6y5iKnc&dib_tag=se&keywords=laptop&qid=1765821577&sr=8-25"
  }
]
```

## 🛡️ Anti-Detection Tips

1. **Always use proxies** - Residential proxies are essential
2. **Respect rate limits** - The scraper has built-in delays
3. **Rotate user agents** - Use different UAs for different sessions
4. **Monitor success rate** - If blocked, switch to better proxies

## ⚠️ Legal Disclaimer

**The legality of web scraping depends on various factors** including Amazon's Terms of Service, the nature of the data (public vs. private), your use case, and local regulations (e.g., GDPR, CCPA).

This tool is provided for data extraction purposes. **You are solely responsible** for ensuring your scraping activities comply with:
- Amazon's Terms of Service and Robot Exclusion Standards
- Applicable laws and regulations in your jurisdiction
- Data protection and privacy laws (GDPR, CCPA, etc.)

**Proxio recommends consulting with legal counsel** before engaging in large-scale data collection activities.

## 💡 Use Cases

- 📊 **Price monitoring** - Track competitor pricing
- 🔍 **Market research** - Analyze product trends
- 📈 **Product analysis** - Study ratings and reviews
- 🏷️ **Deal hunting** - Find the best deals automatically

## 📞 Support

If you encounter any issues or have questions, please reach out to us at **support@proxio.net**. We are committed to maintaining this tool and ensuring it works seamlessly with Proxio proxies.

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

---

## 🔗 Links

- [Proxio Website](https://proxio.net)
- [Proxio Blog - Amazon Scraping Guide](https://proxio.net/blog)
- [Get 30% OFF with code GIT30](https://proxio.net/pricing)

**Maintained by the [Proxio](https://proxio.net) Team**