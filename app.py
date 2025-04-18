import streamlit as st
from utils.vision import analyze_image
from utils.captions import generate_caption_pack
from dotenv import load_dotenv
import os
import uuid 

load_dotenv()
st.set_page_config(page_title="Audi Caption Generator", page_icon="🚘")

st.title("🚘 Car Content Caption Generator")
st.write("Upload a photo of your car and get captions, hashtags, and TikTok sound ideas instantly.")

uploaded_file = st.file_uploader("Upload your car photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    file_name = f"uploads/{uuid.uuid4().hex}_{uploaded_file.name}"
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="Uploaded Car", use_column_width=True)
    with st.spinner("Analyzing your car photo..."):
        description = analyze_image(file_name)
        caption_pack = generate_caption_pack(description)

    st.subheader("📸 Caption")
    st.write(caption_pack["caption"])

    st.subheader("🏷️ Hashtags")
    st.write(" ".join(caption_pack["hashtags"]))

    st.subheader("🎵 TikTok Sound Ideas")
    for sound in caption_pack["sounds"]:
        st.markdown(f"- **{sound['title']}** – _{sound['vibe']}_")

    st.success("Done! You can copy and paste directly to your post.")
