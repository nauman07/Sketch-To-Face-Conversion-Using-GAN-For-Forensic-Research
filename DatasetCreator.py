from PIL import Image
for i in range(1,20001):
    try:
        #Read the two images
        image1 = Image.open('C:/Users/User/AppData/Local/Programs/Python/Python37/sketch_to_image-/Sketch-Photo-Conversion-using-Deep-CNN-master/Sketch-Photo-Conversion-using-Deep-CNN-master/crop_sketches/'+str(i)+'.jpg')
        #image1.show()
        image2 = Image.open('C:/Users/User/AppData/Local/Programs/Python/Python37/sketch_to_image-/Sketch-Photo-Conversion-using-Deep-CNN-master/Sketch-Photo-Conversion-using-Deep-CNN-master/crop/'+str(i)+'.jpg')
        #image2.show()
        #resize, first image
        #image1 = image1.resize((426, 240))
        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
        new_image.paste(image1,(0,0))
        new_image.paste(image2,(image1_size[0],0))
        new_image=new_image.resize((512,256))
        new_image.save("dataset/"+str(i)+".jpg","JPEG")
        #new_image.show()
        print(i)
    except:
        print("number is not present")
