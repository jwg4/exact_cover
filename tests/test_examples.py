from exact_cover import get_all_solutions
from exact_cover.error import NoSolution

from pytest import mark

from tests.config import GLOBAL_CONFIG

try:
    from exact_cover_samples import problems, canonical

    RUN_SAMPLES = True
except ImportError:
    problems = []
    RUN_SAMPLES = False


SAMPLE_PROBLEMS = [problems[name]() for name in problems]
PROBLEM_IDS = [p["shortname"] for p in SAMPLE_PROBLEMS]


@mark.parametrize("problem", SAMPLE_PROBLEMS, ids=PROBLEM_IDS)
@mark.skipif(not RUN_SAMPLES, reason="Not running exact-cover-samples")
@mark.skipif(GLOBAL_CONFIG["SKIP_SLOW"], reason="Skipping slow tests")
def test_exact_cover_solve(problem):
    data = problem["data"]

    try:
        result = get_all_solutions(data)
    except NoSolution:
        result = []

    expected = problem["solutions"]

    assert canonical(result) == canonical(expected)
