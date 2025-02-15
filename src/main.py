"""Main module for running the Monte Carlo simulation."""

import argparse
import time
import matplotlib.pyplot as plt
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display
from libs.strategies import monte_carlo_simulation


def reshape_text(text):
    """Reshape Arabic text for proper display.

    Args:
        text (str): The text to reshape.

    Returns:
        str: The reshaped text.
    """
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text


def plot_results(all_balances, initial_balance, prompts):
    """Plot the results of the Monte Carlo simulation.

    Args:
        all_balances (list): List of balances after each trade.
        initial_balance (float): The initial trading balance.
        prompts (dict): Dictionary of prompts for user input.
    """
    plt.figure(figsize=(10, 5))
    for balances in all_balances:
        plt.plot(balances, marker="o", alpha=0.5)
    plt.title(prompts["plot_title"])
    plt.xlabel("Number of Trades")
    plt.ylabel("Balance")
    plt.grid(True)
    plt.axhline(
        initial_balance,
        color="red",
        linestyle="--",
        label=prompts["initial_balance_label"],
    )
    plt.legend()
    plt.show(block=False)  # Non-blocking show
    time.sleep(1)  # Small delay to ensure the plot window renders


def main():
    """Main function to run the Monte Carlo simulation.

    Parses command-line arguments, collects user inputs, runs simulations,
    and optionally shows the plot of balance changes.

    Returns:
        tuple: A tuple containing all balances, initial balance, prompts, and show_plot flag.
    """
    parser = argparse.ArgumentParser(description="Monte Carlo Simulation")
    parser.add_argument(
        "--lang",
        choices=["en", "fa"],
        default="en",
        help="Language for the application (en or fa)",
    )
    parser.add_argument(
        "--show-plot", action="store_true", help="Show the plot after simulation"
    )
    parser.add_argument(
        "--strategy",
        choices=["fixed", "variable"],
        default="fixed",
        help="Trading strategy to use",
    )
    args = parser.parse_args()

    if args.lang == "fa":
        prompts = {
            "initial_balance": reshape_text("مقدار اولیه بالانس تجاری را وارد کنید: "),
            "risk_percentage": reshape_text(
                "مقدار ریسک در هر معامله (درصدی از بالانس اولیه) را وارد کنید: "
            ),
            "win_rate": reshape_text("نرخ برد را وارد کنید (مثلاً 0.6 برای 60%): "),
            "reward_to_risk_ratio": reshape_text("نسبت سود به ریسک را وارد کنید: "),
            "num_trades": reshape_text("تعداد معاملات را وارد کنید: "),
            "num_simulations": reshape_text("تعداد شبیه‌سازی‌ها را وارد کنید: "),
            "plot_title": reshape_text(
                "تغییرات بالانس در طول معاملات (تمام شبیه‌سازی‌ها)"
            ),
            "initial_balance_label": reshape_text("بالانس اولیه"),
        }
    else:
        prompts = {
            "initial_balance": "Enter the initial trading balance: ",
            "risk_percentage": "Enter the risk percentage per trade (as a percentage of the initial balance): ",
            "win_rate": "Enter the win rate (e.g., 0.6 for 60%): ",
            "reward_to_risk_ratio": "Enter the reward-to-risk ratio: ",
            "num_trades": "Enter the number of trades: ",
            "num_simulations": "Enter the number of simulations: ",
            "plot_title": "Balance Changes Over Trades (All Simulations)",
            "initial_balance_label": "Initial Balance",
        }

    initial_balance = float(input(prompts["initial_balance"]))
    risk_percentage = float(input(prompts["risk_percentage"]))
    win_rate = float(input(prompts["win_rate"]))
    reward_to_risk_ratio = float(input(prompts["reward_to_risk_ratio"]))
    num_trades = int(input(prompts["num_trades"]))
    num_simulations = int(input(prompts["num_simulations"]))

    all_balances_list = []
    sample_results = []

    params = {
        "initial_balance": initial_balance,
        "risk_percentage": risk_percentage,
        "win_rate": win_rate,
        "reward_to_risk_ratio": reward_to_risk_ratio,
        "num_trades": num_trades,
        "strategy": args.strategy,
    }

    for simulation in range(num_simulations):
        final_balance, balances, results = monte_carlo_simulation(params)
        all_balances_list.append(balances)
        if simulation == 0:
            sample_results = results

    df_sample_results = pd.DataFrame(sample_results)
    df_sample_results.to_excel("monte_carlo_sample_results.xlsx", index=False)

    return all_balances_list, initial_balance, prompts, args.show_plot


if __name__ == "__main__":
    all_balances_list, initial_balance, prompts, show_plot = main()
    if show_plot:
        plot_results(all_balances_list, initial_balance, prompts)
