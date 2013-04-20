import urllib2
from cgi import escape

url = "http://www.google.com/search?q={query}"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}


def correct(word):
    result = word
    try:
        req = urllib2.Request(
            url.format(query=escape(word)),
            headers=hdr
        )
        html = urllib2.urlopen(req).read()
        result = html.split('<a class="spell"')[1].split("<i>")[1].split("</i>")[0]
    except:
        pass
    return result

if __name__ == "__main__":
    import sys
    import subprocess
    c = correct(" ".join(sys.argv[1:])).strip()
    sys.stdout.write(c)
    subprocess.call("""echo "{0}" | tr -d '\n' | pbcopy""".format(c), shell=True)
