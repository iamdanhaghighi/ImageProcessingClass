import cv2

img = cv2.imread('/home/greyhat/Desktop/nmap.png')

def color_to_grey(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def save_image(file_path, mat):
    return cv2.imwrite(file_path, mat)
    

def nearest_interpolation(img, scale):
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_NEAREST)


def bilinear_interpolation(img, scale):
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_LINEAR)


def cubic_interpolation(img, scale):
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)



grayImg = color_to_grey(img)

#save_image('/home/greyhat/Desktop/greyNmap.png', grayImg) 

near_img = nearest_interpolation(grayImg, 5)

#save_image('/home/greyhat/Desktop/nearestInterNmapX5.jpg', near_img)

bilinear_img = bilinear_interpolation(grayImg, 5)

#save_image('/home/greyhat/Desktop/bilinearInterNmapX5.jpg', bilinear_img)

cubic_img = cubic_interpolation(grayImg, 5)

save_image('/home/greyhat/Desktop/cubicInterNmapX5.jpg', cubic_img)

