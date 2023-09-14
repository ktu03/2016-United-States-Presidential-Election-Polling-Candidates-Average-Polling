from cs103 import *
import requests

@typecheck
def get_date_fact(month: int, day: int) -> str:
    """Fetches a fact about the given day of the year from http://numbersapi.com/
    month is in the range [1,12], where 1 is Jan, 2 is Feb, etc.
    
    day is a legitimate day for the given month (and so in the range [1,31] at most).
    Returns a sentence fragment that can end a fact about the date with no verb or closing punctuation."""
    result = requests.get(f"http://numbersapi.com/{month}/{day}/date?fragment")
    result.raise_for_status()
    return result.text

@typecheck
def get_number_fact(number: int) -> str:
    """Fetches a fact about the given number from http://numbersapi.com/

    Returns a sentence fragment that can end a fact about the date with no verb or closing punctuation."""
    result = requests.get(f"http://numbersapi.com/{number}/math?fragment")
    result.raise_for_status()
    return result.text

@typecheck
def get_year_fact(year: int) -> str:
    """Fetches a fact about the given year from http://numbersapi.com/
    
    Returns a sentence fragment that can end a fact about the date with no verb or closing punctuation."""
    result = requests.get(f"http://numbersapi.com/{year}/year?fragment")
    result.raise_for_status()
    return result.text
