def allow_group(allowed_ids: list):
    """

    :param allowed_ids: list - allowed to current handler ids of groups
    :return:
    """
    def decorator(func):
        setattr(func, 'allowed_ids', allowed_ids)
        return func

    return decorator
