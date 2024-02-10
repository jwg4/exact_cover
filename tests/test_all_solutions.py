from exact_cover import get_all_solutions

from . import problems


def normalize(solution):
    """
    transform the output of get_all_solutions
    or the all_solutions key in a problem dict
    into a frozenset of frozensets, so that we can
    compare solutions for equality.
    """
    return frozenset(frozenset(row) for row in solution)

def test_from_problem(problem):
    """
    generate a test function for a problem dict
    """
    def test():
        # xxx not yet available
        result = normalize(get_all_solutions(problem["data"]))
        expected = normalize(problem["all_solutions"])
        assert result == expected
    return test


# define in the current module a test function
# for each problem in problems
# not all symbols in the problems module are considered:
# - need to contain '_problem'
# - and not be a private symbol (start with '_')

for problem_name in dir(problems):
    if ('_problem' not in problem_name
        or problem_name.startswith('_')):
        continue
    test_name = 'test_' + problem_name
    problem_function = getattr(problems, problem_name)
    globals()[test_name] = test_from_problem(problem_function())
