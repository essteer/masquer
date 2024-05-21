import random


def select_data(sample_space: list[str], weights: list[float]) -> str:
    """
    Makes a weighted random selection from a given sample space

    Parameters
    ----------
    sample_space: list[str]
        options to randomly select from

    weights: list[float]
        weight per sample in sample_space

    Returns
    -------
    selection: str
        selection from sample_space
    """
    selection = random.choices(sample_space, weights=weights, k=1)

    return selection[0]
