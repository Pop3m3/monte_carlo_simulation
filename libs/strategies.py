"""Module for defining trading strategies."""

import random


def monte_carlo_simulation(params):
    """Simulate a series of trades using the Monte Carlo method.

    Args:
        params (dict): A dictionary containing the simulation parameters.

    Returns:
        list: A list of balances after each trade.
    """
    initial_balance = params["initial_balance"]
    risk_percentage = params["risk_percentage"]
    win_rate = params["win_rate"]
    reward_to_risk_ratio = params["reward_to_risk_ratio"]
    num_trades = params["num_trades"]
    strategy = params.get("strategy", "fixed")

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

        results.append(
            {
                "Trade Number": trade,
                "Result": result,
                "Change in Balance": amount,
                "New Balance": balance,
            }
        )
        balances.append(balance)

    return balance, balances, results
