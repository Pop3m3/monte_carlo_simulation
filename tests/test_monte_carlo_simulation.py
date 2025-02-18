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


def test_failing_case_negative_balance():
    """Test a failing case where the initial balance is negative."""
    params = {
        "initial_balance": -1000,
        "risk_percentage": 1,
        "win_rate": 0.5,
        "reward_to_risk_ratio": 2,
        "num_trades": 10,
        "strategy": "fixed",
    }
    try:
        balance, balances, results = monte_carlo_simulation(params)
        assert False, "Simulation should have failed with negative initial balance"
    except ValueError as e:
        assert str(e) == "Initial balance must be positive"


def test_failing_case_high_risk():
    """Test a failing case where the risk percentage is too high."""
    params = {
        "initial_balance": 1000,
        "risk_percentage": 100,
        "win_rate": 0.5,
        "reward_to_risk_ratio": 2,
        "num_trades": 10,
        "strategy": "fixed",
    }
    try:
        balance, balances, results = monte_carlo_simulation(params)
        assert False, "Simulation should have failed with high risk percentage"
    except ValueError as e:
        assert str(e) == "Risk percentage must be less than 100"
