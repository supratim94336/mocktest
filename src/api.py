import requests


class Employee:
    """A sample Employee class"""
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


class GoGetter:
    """
    The thing I am testing, this is usually imported into the test file, but
    defined here for simplicity.
    """
    def get(self):
        """
        Get the content of `https://waylonwalker.com` and return it as a string
        if successfull, or False if it's not found.
        """
        r = requests.get("https://waylonwalker.com")
        if r.status_code == 200:
            return r.content
        if r.status_code == 404:
            return False


class DummyRequester:
    def __init__(self, content, status_code):
        """
        mock out content and status_code
        """

        self.content = content
        self.status_code = status_code

    def __call__(self, url):
        """
        The way I set this up GoGetter is going to call an instance of this
        class, so the easiest way to make it work was to implement __call__.
        """
        self.url = url
        return self
