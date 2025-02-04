from exact_cover import get_all_solutions
from exact_cover.error import NoSolution

from exact_cover_samples import problems
from pytest import mark


SAMPLE_PROBLEMS = [problems[name]() for name in problems]

@mark.parametrize( "problem",  
    SAMPLE_PROBLEMS,)  
def test_exact_cover_solve(problem):
    data = problem["data"]
    try:
        result = get_all_solutions(data)
    except NoSolution:
        result = []
    assert result == problem["solutions"]  
