def printimage(img, name):
    print("\n" + name)
    for row in img:
        print(row)

def invert_image(img):
    output = []
    for row in img:
        newrow=[]
        for pixel in row:
            newpixel=255-pixel
            newrow.append(newpixel)
        output.append(newrow)
    return output

            
def adjust_brightness(img,amt):
    output=[]
    for row in img:
        newrow=[]
        for pixel in row:
            newpixel=min(255,max(0,(pixel+amt)))
            newrow.append(newpixel)
        output.append(newrow)
    return output

def threshold(img,limit):
    output=[]
    for row in img:
        newrow=[]
        for pixel in row:
            if pixel>=limit:
                newrow.append(255)
            else:
                newrow.append(0)
        output.append(newrow)
    return output

def horizontalflip(img):
    output=[]
    for row in img:
        newrow=row[::-1]
        output.append(newrow)
    return output

def verticalflip(img):
    output=img[::-1]
    return output

def rotate(img):
    output=[]
    for col in range(0, len(img[0])):
        newrow=[]
        for row in range(len(img)-1,-1,-1):
            newrow.append(img[row][col])
        output.append(newrow)
    return output

def cropimage(img, rstart, rend, cstart, cend):
    output = []
    for row in range(rstart, rend):
        newrow = img[row][cstart:cend]
        output.append(newrow)
    return output

def blurimage(img):
    output = []
    for row in range(len(img)):
        newrow = []
        for col in range(len(img[0])):
            total = 0
            count = 0 
            for r in range(max(0, row - 1), min(len(img), row + 2)):
                for c in range(max(0, col - 1), min(len(img[0]), col + 2)):
                    total += img[r][c]
                    count += 1

            newpixel = total // count
            newrow.append(newpixel)
        output.append(newrow)
    return output
image = [[10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200],
    [210, 220, 230, 240, 250]]

printimage(image, "Original Image")

inverted = invert_image(image)
printimage(inverted, "Inverted Image")

bright = adjust_brightness(image, 30)
printimage(bright, "Brightness Increased")

binary = threshold(image, 128)
printimage(binary, "Thresholded Image")

horizontal = horizontalflip(image)
printimage(horizontal, "Horizontal Flip")

vertical = verticalflip(image)
printimage(vertical, "Vertical Flip")

rotated = rotate(image)
printimage(rotated, "Rotated Image")

cropped = cropimage(image, 0, 2, 0, 2)
printimage(cropped, "Cropped Image")

blurred = blurimage(image)
printimage(blurred, "Blurred Image")



            
        
    
    

