import urllib2
from urllib import urlencode
import json


url = "http://www.google.com/search?q={query}"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
query = """https://www.googleapis.com/customsearch/v1?num=1&"""

keys = [
    # provide at least one google api key from https://code.google.com/apis/console/
]

'key={key}&cx={cx}&num=1&q={q}'

pl_cse = '009341357436794688484:bi6ngbl4mvk'
en_cse = '009341357436794688484:rvhujssywbq'


def correct(word):
    result = word
    for key in keys:
        try:
            full_query = query + (
                urlencode({'key': key, 'cx': pl_cse, 'q': word})
            )

            search_result = json.loads(
                urllib2.urlopen(full_query).read()
            )
            if 'spelling' in search_result:
                return search_result['spelling']['correctedQuery']
            else:
                return result
        except urllib2.HTTPError:
            continue
    else:
        return result + '.no_key'


if __name__ == "__main__":
    import sys
    import subprocess
    c = correct(" ".join(sys.argv[1:])).strip().encode('utf-8')
    sys.stdout.write(c)
    subprocess.call("""echo "{0}" | tr -d '\n' | pbcopy""".format(c), shell=True)
