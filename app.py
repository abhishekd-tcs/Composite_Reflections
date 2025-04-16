import streamlit as st
import numpy as np
from PIL import Image


artwork_path='./artworks/'
# Set up page configuration
st.set_page_config(page_title="Composite Reflection", layout="wide")
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 10% !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)
# Sidebar: Cluster type selection
st.sidebar.title("Theme Selection")
theme_type = st.sidebar.radio("Choose the theme:", ["Artist", "Art Movement", "Thematic"])

# Load corresponding data based on cluster type
if theme_type == "Artist":
    art_list={'Van_Gogh':'Self-Portrait of Vincent Van Gogh, 1887',
            'Pablo_Picasso':'Self-Portrait of Pablo Picasso, 1907',
            'Munch':'Self-Portrait of Edvard Munch, 1911',
            'Salvador_Dali':'Self-Portrait of Salvador Dali, 1941',
            'Brueghel':'Portrait of Jan Brueghel the Elder by Peter Paul Rubens, 1613'
              }
    arts=list(art_list.keys())
    input_images=[]
    collage_images=[]
    videos=['https://youtu.be/BBl4y_a14WY','https://youtu.be/6Ab4fZKKXkk','https://youtu.be/w_0SUU6m01M','https://youtu.be/e2YMe9CIG68','https://youtu.be/VPGoR0c7i7U']
    metadata=[]
    for i in range(len(arts)):
        input_images.append(artwork_path+'Artists/'+arts[i]+'/Input.jpg')
        collage_images.append(artwork_path+'Artists/'+arts[i]+'/Collage.jpg')
        # videos.append(artwork_path+'Artists/'+arts[i]+'/Video.mp4')
        metadata.append(artwork_path+'Artists/'+arts[i]+'/metadata.txt')
elif theme_type == "Art Movement":
    art_list={'Impressionism':'Impressionism: Bal du moulin de la Galette by Pierre-Auguste Renoir, 1876',
            'Early_Renaissance':'Early Renaissance: The Birth of Venus by Sandro Botticelli, 1484',
            'Post_Impressionism':'Post Impressionism: A Sunday Afternoon on the Island of La Grande Jatte by Georges Seurat, 1884 ',
            'Complete_Dataset':'Complete Dataset: A Sunday Afternoon on the Island of La Grande Jatte by Georges Seurat, 1884'
              }
    arts=list(art_list.keys())
    input_images=[]
    collage_images=[]
    videos=['https://youtu.be/QAqCZoiNTuE','https://youtu.be/gGOGeICfDt8','https://youtu.be/Z27m-v-RmNE','https://youtu.be/EXGN9i1Mbsc']
    metadata=[]
    for i in range(len(arts)):
        input_images.append(artwork_path+'Art_Movement/'+arts[i]+'/Input.jpg')
        collage_images.append(artwork_path+'Art_Movement/'+arts[i]+'/Collage.jpg')
        # videos.append(artwork_path+'Art_Movement/'+arts[i]+'/Video.mp4')
        metadata.append(artwork_path+'Art_Movement/'+arts[i]+'/metadata.txt')
elif theme_type == "Thematic":
    art_list={'Apple':'Food: Apples by Vincent Van Gogh, 1887',
              'Russel_Kirsch':'Photograph: Russel Kirsch, the Inventor of the First Digital Photograph, 2007'}
    arts=list(art_list.keys())
    input_images=[]
    collage_images=[]
    videos=['https://youtu.be/5thuwhsD81o','https://youtu.be/gyIyukLYqAs']
    metadata=[]
    for i in range(len(arts)):
        input_images.append(artwork_path+'Thematic/'+arts[i]+'/Input.jpg')
        collage_images.append(artwork_path+'Thematic/'+arts[i]+'/Collage.jpg')
        # videos.append(artwork_path+'Thematic/'+arts[i]+'/Video.mp4')
        metadata.append(artwork_path+'Thematic/'+arts[i]+'/metadata.txt')
# elif theme_type == "Real Life Photograph":
#     art_list={}
#     arts=list(art_list.keys())
#     input_images=[]
#     collage_images=[]
#     videos=[]
#     metadata=[]
#     for i in range(len(arts)):
#         input_images.append(artwork_path+'Photograph/'+arts[i]+'/Input.jpg')
#         collage_images.append(artwork_path+'Photograph/'+arts[i]+'/Collage.jpg')
#         videos.append(artwork_path+'Photograph/'+arts[i]+'/Video.mp4')
#         metadata.append(artwork_path+'Photograph/'+arts[i]+'/metadata.txt')
st.title("Composite Reflections")
st.subheader("Composite Reflections is a method of artwork creation wherein we reimagine an artwork as composed from other constituent artworks. The constituents bear an intimate relation with the main subject.")
st.markdown("### [← Different themes can be seen by expanding the sidebar on the left. (If the sidebar is not visible, please click the arrow in the top left corner.]")
st.header(theme_type+" based Composite Reflections")


if theme_type=='Real Life Photograph':
    css = '''
<style>
section.main > div:has(~ footer ) {
    padding-bottom: 5px;
}
</style>
'''
    st.markdown(css, unsafe_allow_html=True)
for i in range(len(arts)):
    st.header(art_list[arts[i]],divider=True)
    with st.container():
        cols = st.columns([0.2,0.8])
        for j in range (2):
            if j==0:
                image=Image.open(input_images[i])
                with cols[j]:
                    st.image(image, use_container_width=True)
                    st.html("<p style='font-size:200%' align='center'><b>Initial Artwork</b></p>")
                    st.divider()
                    # video=open(videos[i],"rb").read()
                    video=videos[i]
                with cols[j]:
                    st.video(video)
                    st.html("<p align='center'><b style='font-size:150%'>Video Showcase of Composite Reflection</b><br> Please view the video in fullscreen &#40;with the highest quality settings&#41;, for a deeper look at the constituents of the Composite Reflections.</p>")
                    # if theme_type!="Art Movement" and theme_type!="Food":
                    st.divider()
                    meta_info=open(metadata[i],"r").read()
                    st.html(meta_info)
            elif j==1:
                image=Image.open(collage_images[i])
                with cols[j]:
                    st.image(image, use_container_width=True)
                    st.html("<p style='font-size:200%' align='center'><b>Composite Reflection</b></p>")
                
        # if theme_type=="Art Movement" or theme_type=="Food":
        #     meta_info=open(metadata[i],"r").read()
        #     st.html(meta_info)

