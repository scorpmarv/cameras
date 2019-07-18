import roman
import re
import json
from collections import OrderedDict


def standardize_mark(name):
    """
    As the Canon Mark models are not standardized we change the values
    to follow a pattern, ie: MK2, MKII, MK 2, MK II, mark 2, mark II to Mark II
    """
    mk_regex = re.compile("(m(?:ar)?k\s*)([ivx\d]*)", flags=re.IGNORECASE)
    search = mk_regex.search(name)
    if search:
        replacement = 'Mark'
        version = search.group(2)
        if version:
            if version.isdigit():
                try:
                    version = roman.toRoman(int(version))
                except ValueError:
                    pass
            else:
                version = version.upper()
            replacement += ' ' + version
        return name.replace(search.group(0), replacement)
    return name


def standardize_name(name):
    """
    Remove spaces and make whole name lowercase for comparison
    """
    name = name.strip()
    name = name.lower().replace(" ", "")
    return name


def main():
    # Load file with duplicate cameras
    cameras = open('duplicates.txt', 'r')
    camera_dict = dict()

    for camera in cameras:
        name = standardize_mark(camera)
        standardized_name = standardize_name(name)

        # We use the standardize name to check for duplicates
        if standardized_name not in camera_dict.keys():
            camera_dict.update({standardized_name: name})

    data_sorted = OrderedDict(sorted(camera_dict.items(),  key=lambda x: x[0]))

    f = open("dict.json", "w")
    f.write(json.dumps(data_sorted))
    f.close()


main()
