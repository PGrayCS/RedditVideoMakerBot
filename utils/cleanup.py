import os
import shutil
from os.path import exists


def _listdir(d):  # listdir with full path
    return [os.path.join(d, f) for f in os.listdir(d)]


def cleanup(reddit_id) -> int:
    """Deletes temporary assets for a given Reddit post.

    Returns:
        int: ``1`` if the folder existed and was removed, otherwise ``0``.
    """
    directory = f"../assets/temp/{reddit_id}/"
    if exists(directory):
        shutil.rmtree(directory)
        return 1
    return 0
