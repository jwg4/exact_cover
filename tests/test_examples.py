from exact_cover import get_all_solutions
from exact_cover.error import NoSolution

from pytest import mark

try:
    from exact_cover_samples import problems, canonical
    RUN_SAMPLES = True
except ImportError:
    problems = []
    RUN_SAMPLES = False


SAMPLE_PROBLEMS = [problems[name]() for name in problems]

@mark.parametrize("problem", SAMPLE_PROBLEMS,)
@mark.skipif(not RUN_SAMPLES, reason="Not running exact-cover-samples")
def test_exact_cover_solve(problem):
    data = problem["data"]

    try:
        result = get_all_solutions(data)
    except NoSolution:
        result = []
    
    expected = problem["solutions"]

    assert canonical(result) == canonical(expected)
