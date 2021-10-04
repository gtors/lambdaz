from .base import Lambda


def unwrap_partial(args, kwargs):
    def inner(maybe_lambda):
        return unwrap(maybe_lambda, args, kwargs)

    return inner


def unwrap(maybe_lambda, args, kwargs):
    if isinstance(maybe_lambda, Lambda):
        maybe_lambda = maybe_lambda._terminated_()
        return maybe_lambda(*args, **kwargs)
    else:
        return maybe_lambda
