from cricket_score import run_rate, strike_rate, required_run_rate, match_status


def test_run_rate_standard():
    assert run_rate(120, 20) == 6.0


def test_run_rate_zero_overs():
    assert run_rate(50, 0) == 0.0


def test_run_rate_partial_over():
    assert run_rate(160, 17.5) == 8.97


def test_strike_rate_standard():
    assert strike_rate(72, 44) == 163.64


def test_strike_rate_zero_balls():
    assert strike_rate(10, 0) == 0.0


def test_required_run_rate_standard():
    assert required_run_rate(195, 160, 5) == 7.0


def test_required_run_rate_target_achieved():
    assert required_run_rate(150, 160, 3) == 0.0


def test_match_status():
    assert match_status(195, 160) == "Need 35 more runs to win"
    assert match_status(150, 160).startswith("Target achieved")
