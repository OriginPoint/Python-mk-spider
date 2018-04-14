from urllib import request
import ssl

class DownLoader(object):

    def download(self, url):
        if url is None:
            return None
        ssl.create_default_context=ssl._create_unverified_context
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
