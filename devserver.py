import os
import sys
import glob

import http.server
import socketserver

try:
    PORT = int(sys.argv[1])
except:
    PORT = 8000

class DevServerRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def check_nav(self, html, current_page):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        if soup:
            for li in soup.find_all('li'):
                for href in li.find_all('a'):
                    if href.attrs.get('href') == current_page:
                        li_class = li.attrs.get('class', [])
                        li.attrs['class'] = li_class + ["current", ]

        return str(soup) if soup else html
        # return soup.html()

    def build_page(self, path, tmp_path='build/_devserver.temp.html'):
        
        page_source = "src/pages/{}".format(path)
        if not path.endswith(".html"):
            page_source += ".html"

        outfile = open(tmp_path, "w")

        for pagelet in sorted(glob.glob("src/pagelets/*.html")):
            subcontent_file = page_source if pagelet.endswith(".CONTENT.html") else pagelet
            print(" | -- -- Pagelet {}".format(subcontent_file))
            try:
                with open(subcontent_file) as somefile:
                    somehtml = somefile.read()
                    if subcontent_file.endswith("nav.html"):
                        somenav = self.check_nav(somehtml, current_page=path)
                        outfile.write(somenav)
                    else:
                        outfile.write(somehtml)
            except IOError:
                outfile.close()
                return None

        outfile.close()
        return True    

    def do_GET(self):
        relative_path = self.path[1:]
        if not relative_path:
            relative_path = "index"

        if not os.path.exists(relative_path):
            tmp_path = 'build/_devserver.temp.html'
            if self.build_page(relative_path, tmp_path) is True:
                print(" \ -- Serving {} from {}".format(relative_path, tmp_path))
                self.path = tmp_path
            else:
                self.send_error(404)
                return

        return super().do_GET()


if __name__ == "__main__":
    httpd = socketserver.TCPServer(("", PORT), DevServerRequestHandler)
    print ("-- serving at port", PORT)
    httpd.serve_forever()
