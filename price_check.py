import requests

# ====== CONFIG ======
ITEM_THRESHOLDS = {
    "Tuna": 980,
    "Raw Tuna": 280,
    "Carp": 200,
    "Raw Carp": 39
}
DISCORD_WEBHOOK = "YOUR_DISCORD_WEBHOOK_URL"
# Official Idle Clans public API base
API_BASE = "https://query.idleclans.com/api"
# ===================

def send_discord(message):
    requests.post(DISCORD_WEBHOOK, json={"content": message})

def get_lowest_price(item_name):
    # ==== IMPORTANT: You must replace the API path below with the correct Idle Clans price endpoint ====
    response = requests.get(f"{API_BASE}/market?item={item_name}")
    data = response.json()

    # This assumes API returns a list of offers with "sell_price"
    prices = [offer["sell_price"] for offer in data.get("offers", [])]
    return min(prices) if prices else 0

def check_prices():
    for item, threshold in ITEM_THRESHOLDS.items():
        price = get_lowest_price(item)
        if price > threshold:
            send_discord(f"Price Alert! {item}: lowest sell price is {price}")

if __name__ == "__main__":
    check_prices()
