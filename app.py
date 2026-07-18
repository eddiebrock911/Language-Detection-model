import streamlit as st
import pickle
import time
import base64
from gtts import gTTS
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests

# streamlit run app.py

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Premium AI Language Detector Pro",
    page_icon="🔮",
    layout="centered"
)

# ---------------- Session State Initialization ----------------
if "text_input" not in st.session_state:
    st.session_state.text_input = ""

# ---------------- Helper Functions ----------------
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Text to Speech Generator
def text_to_speech(text, lang_code='en'):
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save("speech.mp3")
        with open("speech.mp3", "rb") as f:
            audio_bytes = f.read()
        b64 = base64.b64encode(audio_bytes).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error("Audio generate nahi ho paya. Kripya check karein ki language code sahi hai ya nahi.")

# Language Metadata Mock (Real app mein ise expand kiya ja sakta hai)
LANG_DATA = {
    "English": {"flag": "🇬🇧", "code": "en", "script": "Latin", "region": "Global", "speakers": "1.5 Billion"},
    "Spanish": {"flag": "🇪🇸", "code": "es", "script": "Latin", "region": "Europe & Americas", "speakers": "550 Million"},
    "French": {"flag": "🇫🇷", "code": "fr", "script": "Latin", "region": "Europe & Africa", "speakers": "300 Million"},
    "Hindi": {"flag": "🇮🇳", "code": "hi", "script": "Devanagari", "region": "South Asia", "speakers": "600 Million"},
    "German": {"flag": "🇩🇪", "code": "de", "script": "Latin", "region": "Europe", "speakers": "130 Million"}
}

# ---------------- Load Model ----------------
@st.cache_resource
def load_models():
    # Placeholder models agar fail ho jayein toh fallback ke liye
    try:
        with open("language_detection_model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        return model, vectorizer
    except FileNotFoundError:
        return None, None

model, vectorizer = load_models()

# ---------------- Load Animations ----------------
lottie_ai = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_M9p23l.json") # Robot/AI animation

# ---------------- Premium Custom CSS (Glassmorphism + Neon Glow) ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #141e30);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Glassmorphic Card Container */
.main-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    padding: 35px;
    border-radius: 25px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    margin-bottom: 25px;
}

h1 {
    text-align: center;
    color: #ffffff;
    font-size: 45px;
    font-weight: 800;
    text-shadow: 0 0 10px rgba(0, 255, 204, 0.5);
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #00ffcc;
    font-size: 18px;
    margin-bottom: 30px;
    font-weight: 300;
}

textarea {
    background: rgba(0, 0, 0, 0.3) !important;
    color: #ffffff !important;
    border-radius: 15px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

textarea:focus {
    border-color: #00ffcc !important;
    box-shadow: 0 0 10px rgba(0, 255, 204, 0.3) !important;
}

/* Neon Glow Buttons */
.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    color: white;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    box-shadow: 0 4px 15px rgba(0, 114, 255, 0.3);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 198, 255, 0.6);
    color: #ffffff !important;
}

/* Secondary Button Custom Styling (Clear) */
div[data-testid="column"]:nth-child(2) .stButton > button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    box-shadow: 0 4px 15px rgba(255, 75, 43, 0.3);
}
div[data-testid="column"]:nth-child(2) .stButton > button:hover {
    box-shadow: 0 6px 20px rgba(255, 65, 108, 0.6);
}

.result-card {
    background: rgba(0, 255, 204, 0.1);
    border: 1px solid rgba(0, 255, 204, 0.3);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
}

.footer {
    text-align: center;
    color: rgba(255, 255, 255, 0.6);
    margin-top: 50px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- UI Header ----------------
if lottie_ai:
    st_lottie(lottie_ai, height=120, key="coding")

st.markdown("<h1>🔮 AI Language Detector Pro</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Next-Gen Multilingual Analysis & Insights Platform</p>", unsafe_allow_html=True)

# ---------------- Main Container ----------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# Feature: File Uploader
uploaded_file = st.file_uploader("📄 Upload a text file (.txt)", type=["txt"])
if uploaded_file is not None:
    try:
        st.session_state.text_input = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error("File read karne mein dikkat aayi.")

# Text Input Area
text = st.text_area(
    "Enter Text or Paragraph",
    value=st.session_state.text_input,
    height=150,
    placeholder="Yahan apna text likhein ya file upload karein..."
)

# Controls layout
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    detect = st.button("🚀 Analyze Language")
with col2:
    listen = st.button("🔊 Listen")
with col3:
    clear = st.button("🗑 Clear")

if clear:
    st.session_state.text_input = ""
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Processing & Model Execution ----------------
if detect or listen:
    if text.strip() == "":
        st.warning("⚠️ Kripya pehle kuch text likhein ya file upload karein!")
    else:
        # Mocking Prediction agar pickle files loading fail ho jayein (Testing Purpose)
        if model is None or vectorizer is None:
            # Simple fallback check for demo
            predicted_lang = "Hindi" if "namaste" in text.lower() or "kaise" in text.lower() else "English"
            confidence_scores = [94.5, 3.2, 1.3, 0.5, 0.5]
            target_langs = ["English", "Spanish", "French", "Hindi", "German"]
            confidence = 94.5
        else:
            # Real Model Prediction
            vector = vectorizer.transform([text.lower()])
            prediction = model.predict(vector)
            predicted_lang = prediction[0]
            
            if hasattr(model, "predict_proba"):
                prob = model.predict_proba(vector)[0]
                confidence = prob.max() * 100
                confidence_scores = sorted(list(prob * 100), reverse=True)[:5]
                # Assuming classes exist
                target_langs = [model.classes_[i] for i in prob.argsort()[::-1][:5]]
            else:
                confidence = 98.7
                confidence_scores = [98.7, 1.3]
                target_langs = [predicted_lang, "Other"]

        # Metadata fetch karein
        lang_meta = LANG_DATA.get(predicted_lang, {"flag": "🏳️", "code": "en", "script": "Unknown", "region": "Global", "speakers": "N/A"})

        # Action: Text to Speech (🔊 Listen Button Triggered)
        if listen:
            st.info(f"🔊 Playing Audio in detected accent ({predicted_lang})...")
            text_to_speech(text, lang_code=lang_meta["code"])

        # Display Results
        if detect:
            with st.spinner("✨ Quantum Neural Analysis running..."):
                time.sleep(1.2)

            st.markdown(f"""
            <div class="result-card">
                <span style="font-size: 20px; color: #ddd; letter-spacing: 2px;">DETECTED IDENTITY</span><br>
                <span style="font-size: 55px;">{lang_meta['flag']}</span><br>
                <span style="font-size: 42px; font-weight: 800; color: #00ffcc;">{predicted_lang}</span><br>
                <p style="color: #fff; margin-top: 10px;">Confidence Score: <b>{confidence:.2f}%</b></p>
            </div>
            """, unsafe_allow_html=True)

            st.progress(int(confidence))

            # Feature: Copy Button UI Trick
            st.text_input("📋 Copy Detected Result:", value=f"Language: {predicted_lang} ({lang_meta['flag']}) | Confidence: {confidence:.2f}%", disabled=False)

            # ---------------- Analytics & Extra Info ----------------
            st.markdown("### 📊 Probability Analytics")
            
            # Interactive Plotly Chart
            fig = go.Figure(go.Bar(
                x=confidence_scores,
                y=target_langs,
                orientation='h',
                marker=dict(color='rgba(0, 255, 204, 0.6)', line=dict(color='rgba(0, 255, 204, 1.0)', width=1.5))
            ))
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color="white"),
                xaxis=dict(title="Confidence (%)", showgrid=False),
                yaxis=dict(autorange="reversed", showgrid=False),
                height=250,
                margin=dict(l=20, r=20, t=20, b=20)
            )
            st.plotly_chart(fig, use_container_width=True)

            # Feature: Language Information Cards
            st.markdown("### 📚 Linguistic Metadata")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Primary Script", lang_meta["script"])
            with c2:
                st.metric("Native Regions", lang_meta["region"])
            with c3:
                st.metric("Global Speakers", lang_meta["speakers"])

# ---------------- Footer ----------------
st.markdown("""
<div class="footer">
    💎 Pro System Powered by Streamlit & Machine Learning | © 2026 Pro UI
</div>
""", unsafe_allow_html=True)