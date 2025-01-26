import urllib.request
import re


def _get_charset_from_header(response):
    content_type = response.headers.get('Content-Type', '')
    match = re.search(r'charset=([\w-]+)', content_type)
    return match.group(1) if match else None


def memoizze(fn):
    ## takes a function and return memoized version of it
    cache = {}

    def inner(url):
        if url in cache:
            return cache[url]
        
        result = fn(url)
        cache[url] = result
        return result
    return inner
   
def fetch(url):
    with urllib.request.urlopen(url) as response:
        raw_content = response.read()
        charset = _get_charset_from_header(response)
        
        if charset:
            try:
                return raw_content.decode(charset)
            except (UnicodeDecodeError, LookupError):
                pass
                
        try:
            content = raw_content.decode('utf-8', errors='replace')
            return content
        except UnicodeDecodeError:
            return raw_content.decode('iso-8859-1')


@memoizze
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':

    cache_fetch = memoizze(fetch)
    print(fib(35))

