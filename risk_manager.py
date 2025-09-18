def check_risk(config, trades_today, pnl):
    """
    Simple risk check.
    Returns True if allowed to trade, False if limits are hit.
    """
    if pnl <= -config["risk"]["daily_stop"]:
        return False
    if trades_today >= config.get("max_trades_per_day", 5):
        return False
    return True
