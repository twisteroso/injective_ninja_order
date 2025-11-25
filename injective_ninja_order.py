import requests, time

def ninja_order():
    print("Injective — Ninja Order Assassin (stealth $10M+ limit orders)")
    seen = set()
    while True:
        r = requests.get("https://api.injective.network/api/exchange/v1beta1/exchange/orders")
        for order in r.json().get("orders", []):
            oid = order["order_hash"]
            if oid in seen: continue
            seen.add(oid)
            
            # Catch massive hidden limit orders (not market)
            if order.get("order_type") != "limit": continue
            qty = float(order["quantity"])
            price = float(order["price"])
            value = qty * price
            
            if value > 10_000_000:  # >$10M resting on the book
                side = "BUY" if "buy" in order["order_info"]["side"] else "SELL"
                market = order["market_id"][:20]
                print(f"NINJA ORDER PLACED\n"
                      f"{side} ${value:,.0f} resting silently\n"
                      f"Price level: ${price:,.4f}\n"
                      f"Market: ...{market}\n"
                      f"Order hash: {oid[:16]}...\n"
                      f"https://hub.injective.network/markets/{order['market_id']}\n"
                      f"→ This is not aggression. This is ambush.\n"
                      f"→ When price touches this level — someone dies instantly.\n"
                      f"→ The blade is already drawn. You just can't see it.\n"
                      f"{'⚔️  ︎'*30}\n")
        time.sleep(1.5)

if __name__ == "__main__":
    ninja_order()
