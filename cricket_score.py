import sys


def overs_to_balls(overs):
    """Convert cricket overs (e.g. 17.5) to balls (107)."""
    whole = int(overs)
    balls = round((overs - whole) * 10)
    return whole * 6 + balls


def run_rate(runs, overs):
    balls = overs_to_balls(overs)
    if balls <= 0:
        return 0.0
    return round(runs * 6 / balls, 2)


def strike_rate(runs, balls):
    if balls <= 0:
        return 0.0
    return round(runs * 100 / balls, 2)


def required_run_rate(target, current_runs, overs_left):
    needed = target - current_runs
    if needed <= 0:
        return 0.0
    balls_left = overs_to_balls(overs_left)
    if balls_left <= 0:
        return float("inf")
    return round(needed * 6 / balls_left, 2)


def main(argv):
    if len(argv) != 7:
        print("Usage: python cricket_score.py runs overs bat_runs balls target overs_left")
        return 1
    runs, overs, bat_runs, balls, target, overs_left = (float(a) for a in argv[1:])
    print("===== Cricket Score Calculator =====")
    print(f"Team score        : {int(runs)} runs in {overs} overs")
    print(f"Run rate          : {run_rate(runs, overs)}")
    print(f"Batsman           : {int(bat_runs)} off {int(balls)} balls")
    print(f"Strike rate       : {strike_rate(bat_runs, int(balls))}")
    print(f"Target            : {int(target)} ({overs_left} overs left)")
    print(f"Required run rate : {required_run_rate(target, runs, overs_left)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
