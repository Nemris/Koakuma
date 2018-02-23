"""Module for downloading titlekeys.json from that key site."""

__author__ = "Death Mask Salesman"

import hashlib as _hashlib
import urllib.request as _urllib_request

def check_url(url):
    """
    Checks if the URL's SHA-256 matches that of that key site.

    :param url: the URL submitted by the user
    :type url:  str
    :returns:   True if the checksums match, False otherwise
    :rtype:     bool
    """

    keysite_sha256 = "c7c6e54cb2daf90953954392edda8bf82f46fe6d7b262e026f9b788e\
c449f52f"
    user_url_sha256 = _hashlib.sha256(url.encode("utf-8")).hexdigest()

    return user_url_sha256 == keysite_sha256

def get_database(url, path, official):
    """
    Downloads titlekeys.json from the submitted URL.

    :param url:      the URL to download from
    :param path:     the location where to place the downloaded file
    :param official: whether the URL is that key site's official one
    :type url:       str
    :type path:      str
    :type official:  bool
    :returns:        the amount of data saved
    :rtype:          int
    """

    url_suffix = "/json" if official else ""
    path_suffix = "/titlekeys.json"

    try:
      with _urllib_request.urlopen("{0}{1}".format(url, url_suffix)) as request:
           with open("{0}{1}".format(path, path_suffix), "wb") as f:
               saved_data = f.write(request.read())
    except:
        saved_data = 0
    
    return saved_data
