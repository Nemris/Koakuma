## Purpose

Koakuma is a Python 3 tool to analyze a Wii U `titlekeys.json` file grabbed from that key site or elsewhere, and output any info belonging to a title that matches the user-submitted criteria im a human-friendly format; said output can also be parsed with shell commands to extract only the required info.

As for the accepted criteria, titleIDs, game names and regions are currently recognized. Furthermore, Koakuma is able to discern whether a title is a game, demo, DLC or update.

-----

## Requirements

* Python 3 or greater;
* a working internet connection, in case you choose to let Koakuma connect to that key site and retrieve `titlekeys.json`.

-----

## Installation

No installation needed; download the repository's .zip, unpack it and you're good to go. Avoid moving the `modules` directory, or Koakuma won't work.

-----

## Usage

A brief usage summary can be seen by issuing:

    python koakuma.py -h

Which will result in:

    usage: koakuma.py [-h] [-k KEYSITE] [-i] [-d DATABASE]
                      [-t TITLEID [TITLEID ...]] [-n NAME [NAME ...]]
                      [-r {EUR,USA,JPN} [{EUR,USA,JPN} ...]] [-e]
    
    titlekeys.json info extractor.
    
    optional arguments:
      -h, --help            show this help message and exit
      -k KEYSITE, --keysite KEYSITE
                            download the title database by inserting that key
                            site's URL in the format "http://example.com"
      -i, --ignore-sha256   ignore the SHA-256 check on that key site's URL
      -d DATABASE, --database DATABASE
                            path to the titlekeys.json file
      -t TITLEID [TITLEID ...], --titleid TITLEID [TITLEID ...]
                            filter by titleID
      -n NAME [NAME ...], --name NAME [NAME ...]
                            filter by game name
      -r {EUR,USA,JPN} [{EUR,USA,JPN} ...], --region {EUR,USA,JPN} [{EUR,USA,JPN} ...]
                            filter by region
      -e, --exact-match     ignore mixed case matches

-----

## Command-line arguments

### Related to the keysite and `titlekeys.json`

`-k/--keysite`: the URL to that key site, to be supplied each time you wish to download `titlekeys.json`. If `-i/--ignore-sha256` is supplied, you'll have to specify the full URL;;

`-i/--ignore-sha256`: by default, a SHA-256 of that key site's URL is compared to the SHA-256 of the URL submitted by you: if they differ, then the download is skipped; specify this argument to force the download;

`-d/--database`: manually specify the path to the `titlekeys.json` file; the default path is the same as `koakuma.py`.

### Criteria to match

`-t/--titleid`: the full titleID to be matched; separate them with a blankspace in case you wish to search for more than one;

`-n/--name`: part of a game name to be matched. If the game name contains spaces, surround it with quotes. Specifying "Demo", "DLC" or "Update" will yield the corresponding title types; separate them with a blankspace if you wish to search for more than one;

`-r/--region`: the region to be matched. Must be uppercase; only "EUR", "USA" and "JPN" are recognized; separate them with a blankspace if you wish to search for more than one.

### Related to searches

`-e/--exact-match`: by default, Koakuma ignores your criteria's case: specify this argument to respect your criteria's case.
