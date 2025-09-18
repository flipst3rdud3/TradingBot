import yaml
from data_loader import get_price_data
from strategy import apply_strategy
from risk_manager import check_risk
from order_executor import place_order

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    print("✅ TradingBot started with config:", config)

    # Example workflow
    data = get_price_data()
    signal = apply_strategy(data)

    trades_today = 0
    pnl = 0

    if check_risk(config, trades_today, pnl):
        place_order(signal)
    else:
        print("❌ Risk limits hit — no trades allowed.")

if __name__ == "__main__":
    main()
