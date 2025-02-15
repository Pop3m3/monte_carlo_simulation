import random

def monte_carlo_simulation(initial_balance, risk_percentage, win_rate, reward_to_risk_ratio, num_trades, strategy="fixed"):
    balance = initial_balance
    balances = [balance]
    results = []

    for trade in range(1, num_trades + 1):
        if strategy == "fixed":
            risk_amount = risk_percentage / 100 * initial_balance
        elif strategy == "variable":
            risk_amount = risk_percentage / 100 * balance
        else:
            raise ValueError("Unknown strategy")

        reward_amount = reward_to_risk_ratio * risk_amount

        if random.random() < win_rate:
            balance += reward_amount
            result = "Win"
            amount = reward_amount
        else:
            balance -= risk_amount
            result = "Loss"
            amount = -risk_amount

        results.append({
            'Trade Number': trade,
            'Result': result,
            'Change in Balance': amount,
            'New Balance': balance
        })
        balances.append(balance)

    return balance, balances, results