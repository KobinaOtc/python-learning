# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print("Encounted coomment: ", data)
    pos = self.getpos()
    print("\tAt line: ", pos[0], " position ", pos[1])

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("sample.html")
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)

if __name__ == "__main__":
  main()
  