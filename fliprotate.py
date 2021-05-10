from PIL import Image
import glob
image_list=[]
hori_image=[]
verti_image=[]
rotate_image=[]
for filename in glob.glob('C:\\Users\\Somnath Deb\Desktop\\birds\\*.jpg'):
    print(filename)
    img=Image.open(filename)
    image_list.append(img)
for image in image_list:
    image=image_list.transpose(Image.FLIP_LEFT_RIGHT)
    hori_image.append(image)
for image in image_list:   
    image=image_list.transpose(Image.FLIP_TOP_BOTTOM)
    verti_image.append(image)
for image in image_list: 
    image=image_list.rotate(90)
    rotate_image.append(image)
for (i,new) in enumerate(hori_image):
    new.save('{}{}{}'.format('C:\\Users\\Somnath Deb\Desktop\\birds_1\\img',i+1,'.jpg'))    
for (i,new) in enumerate(verti_image):
    new.save('{}{}{}'.format('C:\\Users\\Somnath Deb\Desktop\\birds_2\\img',i+1,'.jpg'))
for (i,new) in enumerate(rotate_image):
    new.save('{}{}{}'.format('C:\\Users\\Somnath Deb\Desktop\\birds_3\\img',i+1,'.jpg'))    