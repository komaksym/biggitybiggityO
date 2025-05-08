# Time:  O(|V| + |E|)

# 
class HtmlParser(object):
   def getUrls(self, url):
       
       pass


class Solution(object):
    def crawl(self, startUrl, htmlParser):
        
        SCHEME = "http://"
        def hostname(url):
            pos = url.find('/', len(SCHEME))
            if pos == -1:
                return url
            return url[:pos]

        result = [startUrl]
        lookup = set(result)
        for from_url in result:
            name = hostname(from_url)
            for to_url in htmlParser.getUrls(from_url):
                if to_url not in lookup and name == hostname(to_url):
                    result.append(to_url)
                    lookup.add(to_url)
        return result
