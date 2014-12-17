import re
import urllib

## Using CNN.COM

def makePage():
  file = open("/home/babak/superweb.html", "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>""")


  url = "http://www.cnn.com"
  response = urllib.urlopen(url)
  data = response.read()
  slice = data.find('<div data-vr-zone="THE LATEST">')
  headlineLatest = data[slice:]
  substring = '<a href'
  headlines = []


  begin = "(?=(<a href))"
  end =  "(?=(</a>))"
  start_index =  [match.start() for match in re.finditer(begin, headlineLatest)]
  end_index =  [match.start() for match in re.finditer(end, headlineLatest)]

  for i in range( 0, 10) :
    headline = headlineLatest[start_index[i]:end_index[i]]
    index = headline.find('\"')
    if headline[index+1]== 'h':  
      headline = headline + '</a>'
      headlines.append(headline)
    else:
      img = "(?=(img))"
      img = [match.start() for match in re.finditer(img, headline)]
      if( len(img) >=1 ):    
        nHeadline = '<a href="' + url + '/' + headline[index2:] + '</a>'
      else:
        nHeadline = '</br>' + headline[:index2] + url + headline[index2:] + '</a>'
      headlines.append(nHeadline)

  for item in headlines:
    file.write("%s" % item)
  
  file.write("""</body>
  </html>""")
  
  file.close()
  
