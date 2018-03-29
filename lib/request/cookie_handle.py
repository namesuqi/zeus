import pickle
import os


def save_cookies(response, filename):
    requests_cookiejar = response.cookies
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../../misc/data/cookie/" + filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def load_cookies(filename):
    with open(os.path.abspath(os.path.dirname(__file__)) + "/../../misc/data/cookie/" + filename, 'rb') as f:
        return pickle.load(f)
