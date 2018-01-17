
import httplib
import cStringIO
import re
import urllib
import urllib2
import requests
import mp4file
import os
import math


def main():
    response = requests.get("https://storage.googleapis.com/vimeo-test/work-at-vimeo-2.mp4", stream=True)
    # Check if byte range is accepted
    if response.headers['accept-ranges'] == "bytes":
        print "Downloading file in bytes..."
        baseFile = os.path.basename(url)
        os.umask(0002)
        try:
            req = urllib2.urlopen(url)
            total_size = int(req.info().getheader('Content-Length').strip())
            downloaded = 0
            CHUNK = 256 * 10240
            with open(baseFile, 'wb') as fp:
                while True:
                    chunk = req.read(CHUNK)
                    downloaded += float(len(chunk))
                    print math.floor( (downloaded / total_size) * 100 )
                    if not chunk: break
                    fp.write(chunk)
        except urllib2.HTTPError, e:
            print "HTTP Error:",e.code , url
            return False
        except urllib2.URLError, e:
            print "URL Error:",e.reason , url
            return False

    return baseFile
        file = downloadChunks("https://storage.googleapis.com/vimeo-test/work-at-vimeo-2.mp4")
        os.system("l".format(file))
        print "Done."

    # If not download the file in full
    else:
        print "Downloading file in full..."
        # downloads the file and checks its integrity with mp4file
        urllib.urlretrieve ("https://storage.googleapis.com/vimeo-test/work-at-vimeo-2.mp4", "work-at-vimeo-2.mp4")
        os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format("work-at-vimeo-2.mp4"))
        print "Done."

if __name__ == "__main__":
    main()
