import src.dates as dates
import requests
import src.send_email as send_email
import sys
import src.cookie_manager as cookie_manager
import src.locate_files as locate_files
def query_stock_data(symbol):
    today = dates.get_today_date()
    from_date = dates.three_days_ago()
    params = {
        'from': from_date,
        'to': today,
        'symbol': symbol,
        'dataType': 'deliverable',
        'series': 'EQ'
    }
    url = 'https://www.nseindia.com/api/historical/securityArchives'

    nse_cookie_manager = cookie_manager.NSECookieManager()
    cookies = nse_cookie_manager.get_nse_cookies()
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
    timeout = 15
    try:
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        # Print the content encoding to understand how the data is compressed
        content_encoding = response.headers.get('Content-Encoding', '')
        # If the response is successful
        if response.status_code == 200:
            data = response.json()
            # Extract 'DELIV_PERC' and 'mTIMESTAMP' from the data
            for record in data['data']:
                deliv = record.get('COP_DELIV_PERC', 'N/A')
                print(f"Symbol: {symbol}")
                print(f"DELIV_PERC: {deliv}")
                print(f"Date: {record.get('mTIMESTAMP', 'N/A')}")
                print('-' * 30)

                if deliv > 85:
                    service = send_email.get_gmail_service(locate_files.pickle_file())
                    send_email.send_email(
                    service,
                    'bhartikaran1192@gmail.com',
                    'Stock alert',
                    f'The DELIV_PERC of {symbol} is {deliv}.')

        else:
            print(f"Failed to retrieve data for {symbol}. Status code: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"Request timed out after {timeout} seconds")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        # Catch other types of request errors (e.g., connection errors)
        print(f"Error occurred: {e}")
        sys.exit(1)