######
## MidTerm Instagram Filters
######

######
## Warmup
######


######
## CSUMBify Filter
## Description - Create a yellow and blue image to match school colors!
######
"""function csumbIFY"""
def csumbIFY():
  pic = makePicture(pickAFile())
  tmp = pic
  show(pic) ## should still be colored
  
  #make a BnW copy of the image
  bnw = betterBnW(pic)
  explore(pic) ## should still be colored
  show(tmp) ## should be black and white
  
  #return blue pixels within threshhold
  bData = getPxBlue(tmp)
  #return yellow pixels within threshhold
  #yellow is blue + green data
  yData = getPxYellow(pic)
  #insert yellow and blue pixels into BnW image
  #add frame
  return pic

#black and white pic
def betterBnW(image):
  pixels = getPixels(imag) 
  for pixel in pixels :
    #get the color data in the pixel
    red = getRed(pixel)
    green = getGreen(pixel)
    blue = getBlue(pixel)
    luminance = red*0.299 + green*0.587 + blue*0.114
    setRed(pixel, luminance )
    #set the green pixel value
    setGreen(pixel, luminance)
    #set blue pixel
    setBlue(pixel, luminance)
    #repaint the image with the updated red
  return pic64 
  
#Get blue pixels  
def getPxBlue(pic): 
  pixels = getPixels(pic)
  for pixel in pixels :
    if(getGreen(pixel) >= 190):
      if(getBlue(pixel) >= 190):
        setRed(pixel, 0)
        setGreen(pixel, getGreen(pixel))
        setBlue(pixel, getBlue(pixel))
  return pic