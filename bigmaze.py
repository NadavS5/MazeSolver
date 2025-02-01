import os, time, queue, sys
from PIL import Image
import colorsys

startTime = time.time()
with Image.open(sys.argv[1]) as im:
    width, height = im.size
    px = im.load()


PIXEL_SIZE = 1


start = (width-1,0)
end = (1,height-1)


queue = queue.Queue()
counter = 0

done = set()




directions = {(PIXEL_SIZE,0),(0,PIXEL_SIZE),(0,-PIXEL_SIZE),(-PIXEL_SIZE,0)}

def isValid(current):

    y = current[0]
    x = current[1] 
    
    if(y>= height):
        return False
    
    if(x>= width):
        return False
    
    if(x <0 or y <0) :
        return False


    

    # in yossi's orginal picture the touple length for the colors is 4 and phtoshop' s is 3 
    #so i re-exported it in photoshop 
    #return px[current] != (0,0,0,0)
    return px[current] != (0,0,0)
    
    
    return False

def getNext(current , dirr):
    
    return (current[0] + dirr[0], current[1] + dirr[1])

win = False


def isWin(current):
    
    #return px[current] == (0,255,0)

    return current == end









queue.put(start) #starting point for the bfs
current = start

bfsPaths = {}  #this is for backtracking the solution


print("starting now")
while (not queue.empty()and not win):
    current = queue.get(0)
    counter +=1

    if(isWin(current)):
        total = round(time.time() - startTime, 3)
       
        print("solved in: " + str(total) + " seconds")
        end = current
        win = True
        break
   

    for dirr in directions: 
        next = getNext(current, dirr)
        if isValid(next) and next not in done:
            done.add(next)
            queue.put(next)
            bfsPaths[next] = current 
 
solution = im.copy()




cell = end
def rgb_to_int_tuple(rgb):
    """Convert RGB values from floats (0-1) to integers (0-255)."""
    return tuple(int(x * 255) for x in rgb)



green = 0

hue = 0

if(win):
    
    while cell != start:
        
        
        #print(cell)
        #img1 = ImageDraw.Draw(solution)   
        
        hue += 0.0005
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        

        solution.putpixel(cell, rgb_to_int_tuple(rgb)) 
        cell = bfsPaths[cell]

print(str(len(done)) + " : pixels explored")
print(str(counter) + " / " + str(width*height)+" squared discovered")
solution.save("mazesolution.png")
solution.show()
