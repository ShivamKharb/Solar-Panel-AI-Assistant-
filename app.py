# app.py

import streamlit as st
from PIL import Image
from utils.image_utils import classify_image, load_model
from image_analysis import analyze_rooftop, generate_roi_mask
from utils.roi_calculator import calculate_area, calculate_roi

st.set_page_config(page_title="Solar AI Assistant", layout="centered")
st.title("Solar AI Assistant ")
st.markdown("""
Upload a rooftop image and let the AI:
- Detect if it's a rooftop
- Estimate usable area
- Calculate cost, output & payback period for solar panels
""")

@st.cache_resource
def get_model():
    model_path = "models/rooftop_classifier.pth"
    return load_model(model_path)

model = get_model()

uploaded_file = st.file_uploader("Upload rooftop image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze Image"):
        with st.spinner("Classifying..."):
            prediction = classify_image(image, model)

        if prediction == "rooftop":
            st.success(" Rooftop detected and suitable for solar installation.")

            with st.spinner("Generating mask..."):
                mask = generate_roi_mask(image)
                st.image(mask, caption="ROI Mask", use_container_width=True)

            with st.spinner("Calculating mask area..."):
                mask_area = calculate_area(mask)
                st.markdown(f"**Estimated Rooftop Area (from mask):** `{mask_area:.2f} m²`")

            with st.spinner("Heuristic image analysis..."):
                analysis = analyze_rooftop(image)
                st.json(analysis)

            with st.spinner("Estimating solar potential..."):
                roi_info = calculate_roi(analysis)
                if "error" in roi_info:
                    st.error(roi_info["error"])
                else:
                    st.markdown("### Solar Installation Summary")
                    st.json(roi_info)

        elif prediction == "non-rooftop":
            st.error(" This image is not a suitable rooftop.")
        else:
            st.warning(f"Unclear prediction: `{prediction}`")
