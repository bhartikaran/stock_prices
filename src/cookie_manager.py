import requests
from datetime import datetime, timedelta
import random


class NSECookieManager:
    def __init__(self, base_url="https://www.nseindia.com"):
        self.base_url = base_url
        self.cookies = ''
        self.cookie_used_count = 0
        self.cookie_max_age = 5400  # 1.5 hours (in seconds)
        self.cookie_expiry = datetime.now()
        self.required_cookies = ['nsit', 'nseappid', 'ak_bmsc', 'AKA_A2', 'bm_mi', 'bm_sv', 'bm_sz', 'RT', '_abck',
                                 '_ga', '_ga_87M7PJ3R97']
        self.user_agent = self._generate_user_agent()

    def _generate_user_agent(self):
        # Simulate generating a random user-agent string for each request
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        ]
        return random.choice(user_agents)

    def _fetch_new_cookies(self):
        headers = {
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = requests.get(self.base_url, headers=headers)

        if response.status_code == 200:
            set_cookies = response.headers.get('set-cookie', '').split(',')
            cookies = []

            # Extract only the required cookies
            for cookie in set_cookies:
                cookie_key_value = cookie.split(';')[0].strip()
                cookie_name = cookie_key_value.split('=')[0]
                if cookie_name in self.required_cookies:
                    cookies.append(cookie_key_value)

            self.cookies = '; '.join(cookies)
            self.cookie_used_count = 0
            self.cookie_expiry = datetime.now() + timedelta(seconds=self.cookie_max_age)
        else:
            raise Exception(f"Failed to fetch cookies, status code: {response.status_code}")

    def get_nse_cookies(self):
        # Check if cookies are empty, used too many times, or expired
        if not self.cookies or self.cookie_used_count > 10 or datetime.now() >= self.cookie_expiry:
            self.user_agent = self._generate_user_agent()  # Generate a new user-agent for each request
            self._fetch_new_cookies()

        # Increment the usage count
        self.cookie_used_count += 1

        return self.cookies


if __name__ == "__main__":
    # Example usage:
    nse_cookie_manager = NSECookieManager(base_url="https://www.nseindia.com")
    cookies = nse_cookie_manager.get_nse_cookies()

    # Now you can use the `cookies` in a request to the NSE API
    headers = {
        'authority': 'www.nseindia.com',
        'method': 'GET',
        'scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookies,
        'User-Agent': nse_cookie_manager.user_agent,
        'Referer': 'https://www.nseindia.com/',
        'Connection': 'keep-alive'
    }


    # Function to get today's date in the required format
    def get_today_date():
        return datetime.today().strftime('%d-%m-%Y')


    today = get_today_date()
    params = {
        'from': '17-09-2024',
        'to': today,
        'symbol': 'IREDA',
        'dataType': 'deliverable',
        'series': 'EQ'
    }
    response = requests.get("https://www.nseindia.com/api/historical/securityArchives", headers=headers, params=params)

    print(response.json())
