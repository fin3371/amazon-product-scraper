"""
Amazon Product Scraper
Extracts product information from Amazon search results
Supports proxy rotation for reliable scraping
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import argparse
import time
import random
from typing import List, Dict
from urllib.parse import urlencode


class AmazonScraper:
    def __init__(self, proxy: str = None, domain: str = "com"):
        """
        Initialize Amazon Scraper
        
        Args:
            proxy: Proxy URL in format "http://username:password@host:port"
            domain: Amazon domain (com, co.uk, de, etc.)
        """
        self.proxy = {"http": proxy, "https": proxy} if proxy else None
        self.domain = domain
        self.base_url = f"https://www.amazon.{domain}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Referer": f"{self.base_url}/",
            "Host": f"www.amazon.{domain}",
            "TE": "Trailers",
        }
        self.results = []
        self.session = requests.Session()
    
    def scrape_search(self, keyword: str, pages: int = 1):
        """
        Scrape Amazon search results
        
        Args:
            keyword: Search keyword
            pages: Number of pages to scrape (default: 1)
        """
        base_url = f"{self.base_url}/s"
        
        for page in range(1, pages + 1):
            params = {
                "k": keyword,
                "page": page
            }
            
            url = f"{base_url}?{urlencode(params)}"
            print(f"🔍 Scraping page {page}/{pages}: {keyword}")
            
            try:
                response = self.session.get(
                    url, 
                    headers=self.headers, 
                    proxies=self.proxy,
                    timeout=15
                )
                response.raise_for_status()
                
                # Random delay to mimic human behavior
                time.sleep(random.uniform(2, 4))
                
                self._parse_search_page(response.text)
                
            except requests.RequestException as e:
                print(f"❌ Error scraping page {page}: {e}")
                continue
    
    def scrape_asins(self, asin_list: List[str]):
        """
        Scrape specific products by ASIN
        
        Args:
            asin_list: List of ASINs to scrape
        """
        for asin in asin_list:
            url = f"{self.base_url}/dp/{asin}"
            print(f"🔍 Scraping ASIN: {asin}")
            
            try:
                response = self.session.get(
                    url,
                    headers=self.headers,
                    proxies=self.proxy,
                    timeout=15
                )
                response.raise_for_status()
                
                time.sleep(random.uniform(2, 4))
                
                self._parse_product_page(response.text, asin)
                
            except requests.RequestException as e:
                print(f"❌ Error scraping ASIN {asin}: {e}")
                continue
    
    def _parse_search_page(self, html: str):
        """Parse Amazon search results page"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find all product cards
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        for product in products:
            try:
                # Extract ASIN
                asin = product.get('data-asin', 'N/A')
                
                # Extract title
                title_el = product.find('h2')
                title = title_el.get_text(strip=True) if title_el else "N/A"
                
                # Extract price
                price_whole = product.find('span', class_='a-price-whole')
                price_fraction = product.find('span', class_='a-price-fraction')
                
                if price_whole and price_fraction:
                    price = f"{price_whole.get_text(strip=True)}{price_fraction.get_text(strip=True)}"
                elif price_whole:
                    price = price_whole.get_text(strip=True)
                else:
                    price = "N/A"
                
                # Extract rating
                rating_el = product.find('span', class_='a-icon-alt')
                rating = rating_el.get_text(strip=True).split()[0] if rating_el else "N/A"
                
                # Extract review count
                # Look for the span with underline text associated with reviews (often in parentheses)
                reviews_el = product.find('span', class_='s-underline-text')
                reviews = reviews_el.get_text(strip=True).replace('(', '').replace(')', '').replace(',', '') if reviews_el else "0"
                
                # Extract product URL
                link_el = product.find('a', class_='a-link-normal s-no-outline')
                product_url = f"{self.base_url}{link_el['href']}" if link_el else "N/A"
                
                product_data = {
                    "asin": asin,
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "reviews": reviews,
                    "url": product_url
                }
                
                self.results.append(product_data)
                print(f"✓ Scraped: {title[:50]}...")
                
            except Exception as e:
                print(f"Error parsing product: {e}")
                continue
    
    def _parse_product_page(self, html: str, asin: str):
        """Parse individual Amazon product page"""
        soup = BeautifulSoup(html, 'html.parser')
        
        try:
            # Extract title
            title_el = soup.find('span', {'id': 'productTitle'})
            title = title_el.get_text(strip=True) if title_el else "N/A"
            
            # Extract price
            price_el = soup.find('span', {'class': 'a-price-whole'})
            price = price_el.get_text(strip=True) if price_el else "N/A"
            
            # Extract rating
            rating_el = soup.find('span', {'class': 'a-icon-alt'})
            rating = rating_el.get_text(strip=True).split()[0] if rating_el else "N/A"
            
            # Extract review count
            reviews_el = soup.find('span', {'id': 'acrCustomerReviewText'})
            reviews = reviews_el.get_text(strip=True).split()[0].replace(',', '') if reviews_el else "0"
            
            product_data = {
                "asin": asin,
                "title": title,
                "price": price,
                "rating": rating,
                "reviews": reviews,
                "url": f"{self.base_url}/dp/{asin}"
            }
            
            self.results.append(product_data)
            print(f"✓ Scraped: {title[:50]}...")
            
        except Exception as e:
            print(f"Error parsing product page: {e}")
    
    def save_to_csv(self, filename: str = "amazon_results.csv"):
        """Save results to CSV"""
        if not self.results:
            print("No results to save")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)
        
        print(f"✓ Saved {len(self.results)} products to {filename}")
    
    def save_to_json(self, filename: str = "amazon_results.json"):
        """Save results to JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Saved {len(self.results)} products to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Amazon Product Scraper")
    parser.add_argument("--keyword", help="Search keyword")
    parser.add_argument("--asins", help="Comma-separated list of ASINs")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--domain", default="com", help="Amazon domain (com, co.uk, de, etc.)")
    parser.add_argument("--proxy", help="Proxy URL")
    parser.add_argument("--output", default="csv", choices=["csv", "json"], help="Output format")
    
    args = parser.parse_args()
    
    if not args.keyword and not args.asins:
        print("❌ Error: Please provide either --keyword or --asins")
        return
    
    scraper = AmazonScraper(proxy=args.proxy, domain=args.domain)
    
    if args.keyword:
        print(f"🔍 Scraping Amazon for: {args.keyword}")
        scraper.scrape_search(args.keyword, args.pages)
    
    if args.asins:
        asin_list = [a.strip() for a in args.asins.split(',')]
        print(f"🔍 Scraping {len(asin_list)} ASINs")
        scraper.scrape_asins(asin_list)
    
    if args.output == "csv":
        filename = f"amazon_results_{args.domain}.csv"
        scraper.save_to_csv(filename)
    else:
        filename = f"amazon_results_{args.domain}.json"
        scraper.save_to_json(filename)
    
    print(f"✅ Scraping complete! Found {len(scraper.results)} products")


if __name__ == "__main__":
    main()
