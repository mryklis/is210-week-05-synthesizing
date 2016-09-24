#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module gets the current date"""


import datetime

CURDATE = None


def get_current_date():
    """sets the date to the current date.

    Args:
      None

    Returns:
      date (date) : as the current date from datetime module.

    Example:
      >>>get_current_date():
      datetime.date(2015, 1, 1)
    """

    date = datetime.date.today()
    return date

if __name__ == "__main__":
    CURDATE = get_current_date()
