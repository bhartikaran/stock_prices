from datetime import datetime, timedelta
# Function to get today's date in the required format
def get_today_date():
    return datetime.today().strftime('%d-%m-%Y')

# Function to get the date three months ago
def three_days_ago():
    three_days_ago = datetime.today() - timedelta(days=3)
    return three_days_ago.strftime('%d-%m-%Y')