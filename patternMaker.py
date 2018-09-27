import sys
import os
from PIL import Image

print('Pattern Maker v1.0')
if len (sys.argv)==1:
    print('To use this program, drag and drop an image onto the executable')
    input('Press return to exit...')
    sys.exit(0)
debug=False

#Flags
if '-d' in sys.argv:
    debug=True
#Get Filename
fileName=""
for arg in sys.argv[1:]:
    if arg.strip()[0]!='-':
        fileName=arg
        break
#Get Image
origImage=None
try:
    origImage=Image.open(fileName)
except FileNotFoundError:
    print('Could not open file "'+fileName+'". Please make sure the name is correct and the file exists.')
    input('Press return to exit...')
    sys.exit(0)
except OSError:
    print('The file "'+fileName+'" is either corrupted or not an image, and could not be opened.')
    input('Press return to exit...')
    sys.exit(0)
print('Opened "'+fileName+'"...')


#Get Arguments
temp=""

xCount=10
temp=input('How many columns of the pattern? ['+"{:,}".format(xCount)+']: ')
xCount=(int(temp.replace(',','')) if temp.replace(',','').isdigit() else xCount)

yCount=xCount
temp=input('How many rows of the pattern? ['+"{:,}".format(yCount)+']: ')
yCount=(int(temp.replace(',','')) if temp.replace(',','').isdigit() else yCount)

xSpacing=20
temp=input('# of pixels between each column? ['+"{:,}".format(xSpacing)+']: ')
xSpacing=(int(temp.replace(',','')) if temp.replace(',','').isdigit() else xSpacing)

ySpacing=xSpacing
temp=input('# of pixels between each row? ['+"{:,}".format(ySpacing)+']: ')
ySpacing=(int(temp.replace(',','')) if temp.replace(',','').isdigit() else ySpacing)

#Get size and such
hSize=origImage.width*xCount+(xCount-1)*xSpacing
vSize=origImage.height*yCount+(yCount-1)*ySpacing
totalPixels=hSize*vSize
if debug: print('New Image Size: '+"{:,}".format(hSize)+'x'+"{:,}".format(vSize)+', Total Pixels: '+"{:,}".format(totalPixels))

#Make Image
print('Generating '+"{:,}".format(xCount)+'x'+"{:,}".format(yCount)+' pattern with '+"{:,}".format(xSpacing)+'x'+"{:,}".format(ySpacing)+' spacing...')
if totalPixels>=64000000:
    print('(You are generating a large image. If there is no output for a while, don\'t worry, this hasn\'t frozen, it\'s just working!)')
newImage=Image.new('RGBA',(hSize,vSize),)

#Generate Pattern
for y in range(0,yCount):
    for x in range (0,xCount):
        newImage.paste(origImage,(x*origImage.width+xSpacing,y*origImage.height+ySpacing))


#Save
f, e = os.path.splitext(fileName)
newImage.save(f+'_pattern.png')
print('Done! Saved to "'+f+'_pattern.png"')
input('Press return to exit...')
