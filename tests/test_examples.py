from exact_cover import get_all_solutions
from exact_cover.error import NoSolution

from exact_cover_samples import problems
from pytest import mark


SAMPLE_PROBLEMS = [problems[name]() for name in problems]

@mark.parametrize("problem",  
    SAMPLE_PROBLEMS,)  
def test_exact_cover_solve(problem):

    data = problem["data"]
    try:
        set_result = get_all_solutions(data)
        result = [tuple(sorted(int(x) for x in a)) for a in set_result]
    except NoSolution:
        result = []
    
    expected = problem["solutions"]
    try:
        expected = expected.tolist()
        expected = [tuple(sorted(int(x) for x in a)) for a in expected]
    except AttributeError:
        pass

    assert sorted(result) == sorted(expected)
