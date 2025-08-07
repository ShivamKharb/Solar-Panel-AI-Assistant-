# ☀️ Solar AI Assistant

The **Solar AI Assistant** is a smart web application that analyzes rooftop images to:

- ✅ Classify whether the image is a rooftop or not.
- 📏 Estimate the usable rooftop area for solar panel installation.
- 💰 Calculate installation cost, energy output, savings, and payback period (for Indian users).

---

## 🚀 Features

- 🧠 Deep Learning-based classification using a trained ResNet18 model.
- 🖼️ ROI (Region of Interest) detection from rooftop images using OpenCV.
- 📊 Smart calculator for:
  - Total and usable rooftop area (in m²)
  - Number of panels
  - Estimated cost and energy output
  - Payback time and savings

---

---

## 🛠️ Setup Instructions

1. **Clone the repository**
# STep 1
```bash
git clone https://github.com/your-username/solar-ai-assistant.git
cd solar-ai-assistant

# STep 2 
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
# STep 3 
pip install -r requirements.txt
# Step 4 
streamlit run app.py


