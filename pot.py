import streamlit as st
from PIL import Image
import numpy as np
import pickle
import keras 
import dill
from keras.models import model_from_json
import cv2
import os
import PIL

st.set_page_config(page_title='SMART POT SYSTEM')

st.title("SMART POT SYSTEM")

img_file_buffer = st.file_uploader("Upload your plant image", type="jpg")



if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    filename = img_file_buffer.name
else :
    image = Image.open('12.jpg')
    





st.image(
    image, caption=f"Your plant", use_column_width=True,
)



# Load our model
with st.spinner('Model loading please wait ...'):
   
    # load and evaluate a saved model
    from numpy import loadtxt
    from keras.models import load_model
    
    # load model
    model = load_model('modell.h5')
    st.write("Model Loaded")



#add you own path here !!!!
train_path = '----------------'


dico = {
    "Daisy Plant":["* Pour a lightweight seed-starting mix into trays or pots","* Keep the mixture moist and above 70° F (21° C) with at least 8 hours of bright light every day, using a grow light or window.","* Daisies love full sun, but partial sun will also work. Pick a planting area with moist, well-drained soil. ","* Work a moderate amount of organic compost and/or aged manure into the soil for better blooms. "],
    "Cactus":["* Give your cacti enough light but not toooooo much","* Bring them outside when nighttime lows are above 50°F","* Cacti are known for surviving without much watering but if the first 2-3 inches of soil are dry, it’s time to give the plant a drink","* Cacti prefer soil that includes more sand and rocks, in order to drain water and keep the plant dry between drinks and prevent root rot"],
    "Sunflower":["* Support tall sunflowers with stakes as they grow.","* Once the flowers appear, feed sunflowers weekly with a high potassium feed (tomato feed is ideal).","* Water regularly during dry periods, especially the tall varieties, as it’s difficult for them to recover if they are allowed to dry out and wilt.","* In late autumn, pull up the plants and compost them."],
    "Tea Plant":["* Spread a 2-inch layer of mulch over the soil around the plant. Mulch retains soil moisture and prevents weed growth.", "* Water the tea plant about once weekly. Supply approximately 2 inches of water ","* Fertilize tea plants every two months when they are actively growing in spring and summer."]
    }



# if "Analyser Maintenant" is clicked
if st.button("Analyze my plant", key="analyse"):
    if img_file_buffer is None:
        
        st.write("Please upload a plant image to analyze ! ")
    else :
        st.subheader("Plant analysis :")
        
        frame = np.array(image)
        test_images = []
        shape = (200,200)
        img = cv2.imread(os.path.join(train_path,filename))
        # Resize all images to a specific shape
        img = cv2.resize(img,shape)      
        test_images.append(img)      
        # Converting test_images to array
        test_images = np.array(test_images)
        

        # Make predictions
        with st.spinner('Prediction ...'):
            checkImage = test_images[0:1]
            predict = model.predict(np.array(checkImage))

            output = { 0:'Daisy Plant',1:'Cactus',2:'Sunflower',3:'Tea Plant'}

            i = np.argmax(predict)
            st.write("You have a beautiful ", output[i],' !')

            D = dico[output[i]]

            st.write('Here is some tips to take care of your plant : ')
            l = len(D)
            for j in range(l) :
                st.write(D[j])

            if output[i] =='Daisy Plant' :
                st.write("Need more informations check out this : [link](https://en.wikipedia.org/wiki/Bellis_perennis)")
            elif output[i] =='Cactus' :
                st.write("Need more informations check out this : [link](https://en.wikipedia.org/wiki/Cactus)")
            elif output[i] =='Sunflower' :
                st.write("Need more informations check out this : [link](https://en.wikipedia.org/wiki/Helianthus_annuus)")
            else :
                st.write("Need more informations check out this : [link](https://en.wikipedia.org/wiki/Camellia_sinensis)")




