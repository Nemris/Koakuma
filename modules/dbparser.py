"""Module to extract info from titlekeys.json."""

__author__ = "Death Mask Salesman"

import json as _json

import utils as _utils

def _check_info(info, criteria, exact):
    """
    Checks if a string matches at least a criteria.

    :param info:     a piece of info pertaining to a game
    :param criteria: a series of criteria to check for
    :param exact:    whether to ignore mixed case matches
    :type info:      str
    :type criteria:  list
    :type exact:     bool
    :returns:        True if a criteria matches, False otherwise
    :rtype:          bool
    """

    if not exact:
        info = info.lower()
        criteria = [s.lower() for s in criteria]
        criteria = _utils.deduplicate_list(criteria)

    match_found = False

    for c in criteria:
        if c in info:
            match_found = True
            break

    return match_found

def _check_title_type(titleid):
    """
    Checks if the game is a demo, DLC or update.

    :param titlekey: the titleID to examine
    :type titlekey:  str
    :returns:        0 if game, 1 if demo, 2 if DLC, 3 if update
    :rtype:          int
    """

    demo_id = "0002"
    dlc_id = "000c"
    update_id = "000e"

    type_id = titleid[4:8]

    if type_id == demo_id:
        title_type = 1
    elif type_id == dlc_id:
        title_type = 2
    elif type_id == update_id:
        title_type = 3
    else:
        title_type = 0

    return title_type

def _purge_names(game_name):
    """
    Replaces newlines with a blankspace.

    :param game_name: the game name to work on
    :type game_name:  str
    :returns:         the game name with newlines replaced by blanks
    :rtype:           str
    """

    return game_name.replace("\n", " ").replace("  ", " ")

def load(titlekeys):
    """
    Reads all data from titlekeys.json.

    :param titlekeys: the path to the titlekeys.json file
    :type titlekeys:  str
    :returns:         the data read from titlekeys.json
    :rtype:           list
    """

    try:
        with open(titlekeys, "r") as f:
            data = _json.load(f)
    except:
        data = []

    return data

def purge(data):
    """
    Removes all data entries with a blank game name.

    :param data: the data read from titlekeys.json
    :type data:  list
    :returns:    the data devoid of entries having blank game names
    :rtype:      list
    """

    return [d for d in data if d.get("name")]

def search(data, titleids, names, regions, exact):
    """
    Searches data to check for any entry matching a series of criteria.

    :param data:     the data read from titlekeys.json
    :param titleids: the titleIDs specified by the user
    :param names:    the game names specified by the user
    :param regions:  the regions specified by the user
    :param exact:    whether to ignore mixed case matches
    :type data:      list
    :type titleids:  list
    :type names:     list
    :type regions:   list
    :type exact:     bool
    :returns:        the entries which match the user's criteria
    :rtype:          list
    """

    title_types = ["", " (Demo)", " (DLC)", " (Update)"]

    matching_items = []

    for d in data:
        title_type = _check_title_type(d.get("titleID"))
        d["name"] = "{0}{1}".format(
                _purge_names(d.get("name")),
                title_types[title_type])

        if titleids:
            if not _check_info(d.get("titleID"), titleids, exact):
                continue

        if names:
            if not _check_info(d.get("name"), names, exact):
                continue

        if regions:
            if not _check_info(d.get("region"), regions, exact):
                continue

        matching_items.append(d)

    return matching_items
