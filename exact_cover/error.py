class ExactCoverError(Exception):
    pass


class NoSolution(ExactCoverError):
    pass


class CannotSplitFurther(ExactCoverError):
    pass
