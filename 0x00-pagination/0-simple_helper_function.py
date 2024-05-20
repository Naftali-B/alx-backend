#!/usr/bin/env python3
""" helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for the given page and page size.
    
    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.
    
    Returns:
    tuple: A tuple containing the start index and the end index.
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
