import requests

# ====== CONFIG ======
MIN_PRICE = {
    "ItemA": 5000,
    "ItemB": 10000,
    "ItemC": 7500
}  # Set minimum price per item
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1474898358928801854/UQIpsQx4qiJCvZMDqjDnam9sZVEEgzGs5EjzaE_dw4zv7qEqIl6cX66x-ZbTByCBTkLm"
PRICE_API_URL = "https://example.com/idle-clans-prices"  # Replace with actual API
# ===================

def send_discord(message):
    requests.post(DISCORD_WEBHOOK, json={"content": message})

def check_prices():
    data = requests.get(PRICE_API_URL).json()
    for item in data['items']:
        name = item['name']
        lowest = item['sell_price']
        if name in MIN_PRICE and lowest > MIN_PRICE[name]:
            send_discord(f"Price Alert! {name} lowest sell price is {lowest}")

if __name__ == "__main__":
    check_prices()
