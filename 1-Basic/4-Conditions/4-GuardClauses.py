def process_payment(amount, is_premium_user):
    # Guard clauses
    if amount <= 0:
        return "Invalid amount"
    
    if not is_premium_user and amount > 1000:
        return "Amount exceeds non-premium limit"
    
    # Main functionality
    return f"Processing payment of ${amount}"