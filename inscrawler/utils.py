import random
from functools import wraps
from time import sleep

from .exceptions import RetryException


def instagram_int(string):
    return int(string.replace(",", ""))


def retry(attempt=10, wait=0.3):
    def wrap(func):
        @wraps(func)
        def wrapped_f(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except RetryException:
                if attempt > 1:
                    sleep(wait)
                    return retry(attempt - 1, wait)(func)(*args, **kwargs)
                else:
                    exc = RetryException()
                    exc.__cause__ = None
                    raise exc

        return wrapped_f

    return wrap


def randmized_sleep(average=1):
    _min, _max = average * 1 / 2, average * 3 / 2
    sleep(random.uniform(_min, _max))


def validate_posts(dict_posts):
    """
        The validator is to verify if the posts are fetched wrong.
        Ex. the content got messed up or duplicated.
    """
    posts = dict_posts.values()
    contents = [post["datetime"] for post in posts]
    # assert len(set(contents)) == len(contents)
    if len(set(contents)) == len(contents):
        print("These post data should be correct.")

def get_num_followers(browser):
    div = browser.find(".k9GMp .Y8-fY .-nal3")
    for candidate in div:
        if candidate.get_attribute("href") and candidate.get_attribute("href").endswith("followers/"):
            return int(candidate.find_element_by_class_name("g47SY").text.replace(",", "").replace("k", "000").replace("m", "000000").replace(".", ""))

def get_num_following(browser):
    div = browser.find(".k9GMp .Y8-fY .-nal3")
    for candidate in div:
        if candidate.get_attribute("href") and candidate.get_attribute("href").endswith("following/"):
            return int(candidate.find_element_by_class_name("g47SY").text.replace(",", "").replace("k", "000").replace(".", ""))

def contain_zh(text):
    """
        Check if string contains chinese char
    """
    for c in text:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False