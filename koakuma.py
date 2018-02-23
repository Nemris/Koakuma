"""Core of Koakuma."""

__author__ = "Death Mask Salesman"
__copyright__ = "Copyright 2018, Death Mask Salesman"
__license__ = "BSD-3-Clause"
__version__ = "0.1"

import argparse
import os

# Custom modules
from modules import dbfetcher
from modules import dbparser
from modules import utils

ap = argparse.ArgumentParser(description = "titlekeys.json info extractor.")

ap.add_argument(
        "-k",
        "--keysite",
        type = str,
        nargs = 1,
        help = "download the title database by inserting that key site's URL \
in the format \"http://example.com\""
)
ap.add_argument(
        "-i",
        "--ignore-sha256",
        action = "store_true",
        default = False,
        help = "ignore the SHA-256 check on that key site's URL"
        )
ap.add_argument(
        "-d",
        "--database",
        type = str,
        nargs = 1,
        default = ["{0}/titlekeys.json".format(os.path.dirname(
            os.path.abspath(
                __file__)))],
        help = "path to the titlekeys.json file"
)
ap.add_argument(
        "-t",
        "--titleid",
        type = str,
        nargs = "+",
        default = [],
        help = "filter by titleID"
)
ap.add_argument(
        "-n",
        "--name",
        type = str,
        nargs = "+",
        default = [],
        help = "filter by game name"
)
ap.add_argument(
        "-r",
        "--region",
        type = str,
        nargs = "+",
        choices = ["EUR", "USA", "JPN"],
        default = [],
        help = "filter by region"
)
ap.add_argument(
        "-e",
        "--exact-match",
        action = "store_true",
        default = False,
        help = "ignore mixed case matches"
)

def main(keysite,
         skip_sha,
         database,
         titleids,
         names,
         regions,
         exact):
    """
    Core of Koakuma.

    :param keysite:  that key site's URL
    :param skip_sha: whether to skip that key site URL's SHA-256 check
    :param database: the path to titlekeys.json
    :param titleids: the titleIDs to search for
    :param names:    the game names to search for
    :param regions:  the regions to search for
    :param exact:    whether to ignore mixed case matches
    :type keysite:   str
    :type skip_sha:  bool
    :type database:  str
    :type titleids:  list
    :type names:     list
    :type regions:   list
    :type exact:     bool
    """

    database = database.pop()

    if keysite:
        keysite = keysite.pop()

        if skip_sha:
            official = False
            valid_url = True
        else:
            valid_url = dbfetcher.check_url(keysite)

            if valid_url:
                official = True

        if valid_url:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            saved_data = dbfetcher.get_database(keysite, current_dir, official)

            if not saved_data:
                utils.print_warn("database download failed.")
        else:
            utils.print_warn("SHA-256 mismatch. Skipping database download.")

    data = dbparser.load(database)

    if not data:
        utils.exit_fatal("{0}: file does not exist or invalid format.".format(database))

    data = dbparser.purge(data)

    results = dbparser.search(data, titleids, names, regions, exact)

    for d in results:
        print("--------------------")
        print("titleID: {0}".format(d.get("titleID")))
        print("Name: {0}".format(d.get("name")))
        print("Region: {0}".format(d.get("region")))

if __name__ == "__main__":
    args = ap.parse_args()

    main(args.keysite,
         args.ignore_sha256,
         args.database,
         args.titleid,
         args.name,
         args.region,
         args.exact_match)
