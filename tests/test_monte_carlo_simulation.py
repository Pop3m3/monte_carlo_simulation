"""Tests for the Monte Carlo simulation."""

import json
import pytest
from libs.strategies import monte_carlo_simulation


def load_test_parameters():
    """Load test parameters from a JSON file."""
    with open("tests/test_parameters.json", encoding="utf-8") as file:
        return json.load(file)


@pytest.mark.parametrize("test_case", load_test_parameters()["test_cases"])
def test_monte_carlo_simulation(test_case):
    """Test the Monte Carlo simulation with various test cases."""
    params = {
        "initial_balance": test_case["initial_balance"],
        "risk_percentage": test_case["risk_percentage"],
        "win_rate": test_case["win_rate"],
        "reward_to_risk_ratio": test_case["reward_to_risk_ratio"],
        "num_trades": test_case["num_trades"],
        "strategy": test_case["strategy"],
    }
    balance, balances, results = monte_carlo_simulation(params)
    assert (
        len(balances) == test_case["num_trades"] + 1
    )  # initial balance + number of trades
