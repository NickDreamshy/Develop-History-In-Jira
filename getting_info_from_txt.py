import os

path = r"sources1.txt"


# add searching by build number
def getting_date_deep(path: str, build: str = None) -> dict:
    url_hash = dict()
    val = ''
    key = ''
    with open(path) as docs:
        for line in docs:
            if 'VCS URL' in line:
                key = line.rstrip().split()[2]
            if 'Commit hash' in line:
                val = line.rstrip().split(':')[1]
            if key != "" and val != "":
                url_hash[key] = val

    return url_hash


print(getting_date_deep(path))
