def apply_strategy(data):
    """
    Apply consolidation/retest strategy.
    Right now: just returns dummy 'signal'.
    """
    if len(data) > 0:
        return "BUY"
    return "HOLD"
