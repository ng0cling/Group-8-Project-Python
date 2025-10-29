#app
import streamlit as st
import pandas as pd
#from io import StringIO
import requests

# HOME PAGE (chưa ghép được với Menu)
# st.set_page_config(page_title="Movie Review & Suggestion", page_icon="🎬", layout="centered")
# st.markdown("""
#     <style>
#         .main-title {
#             font-size: 30px;
#             font-weight: 700;
#             color: #B40404;
#             text-align: center;
#         }
#         .sub-title {
#             font-size: 22px;
#             font-weight: 600;
#             margin-top: 10px;
#         }
#         .description {
#             font-size: 16px;
#             margin-bottom: 30px;
#         }
#         .button-style > button {
#             width: 300px !important;
#             background-color: #C50000 !important;
#             color: white !important;
#             font-size: 20px !important;
#             font-weight: 700 !important;
#             border-radius: 10px !important;
#             padding-top: 10px !important;
#             padding-bottom: 10px !important;
#         }
#     </style>
# """, unsafe_allow_html=True)
# st.markdown('<p class="main-title">Movie Review & Suggestion</p>', unsafe_allow_html=True)

# st.markdown('<p class="sub-title">Welcome to Movie Review & Suggestion 🎬</p>', unsafe_allow_html=True)
# st.markdown('<p class="description">Here you can share your thoughts on movies or find new movie suggestions</p>', unsafe_allow_html=True)
# col1, col2, col3 = st.columns([1,2,1])

# with col2:
#     st.markdown('<div class="button-style">', unsafe_allow_html=True)
#     analysis = st.button("Analysis your file 🔍")
#     suggestion = st.button("Movie suggestions 🎬")
#     st.markdown('</div>', unsafe_allow_html=True)

# if analysis:
#     st.markdown('<meta http-equiv="refresh" content="0; url=https://google.com" />', unsafe_allow_html=True)

# if suggestion:
#     st.markdown('<meta http-equiv="refresh" content="0; url=https://google.com" />', unsafe_allow_html=True)

#Giao diện tiêu đề và menu:
st.set_page_config(page_title="Movie Review & Suggestion", page_icon="🎬", layout="centered")

st.title("🎬 Movie Review & Suggestion")
st.markdown("---")
menu = ["Home", "Movie suggestions"]
choice = st.sidebar.selectbox("Navigation", menu)

#Nhập raw text & upload file
st.subheader("Movie Review & Suggestion")
st.write("### Nhập review trực tiếp")
raw_text = st.text_area("Nhập bình luận phim của bạn tại đây:", placeholder="Nhập review...")
st.write("### Hoặc tải lên file CSV")
uploaded_file = st.file_uploader("Drag and drop file here", type=["csv"])

#Xử lý dữ liệu, hiển thị preview
df = pd.DataFrame()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("#### Data preview")
    st.dataframe(df.head())

elif raw_text:
    df = pd.DataFrame({"Review": [raw_text]})
    st.write("#### Your review:")
    st.dataframe(df)

#URL:
analyse = st.button(label = "Analyse")
if analyse:
    url = "https://review-sentiment-app.onrender.com/predict"

    if raw_text:
        payload = {"review": raw_text}
        try:
                with st.spinner("Analysing... Please wait ⏳"):
                    response = requests.post(url, json=payload)
                    if response.status_code == 200:
                        result = response.json()
                        st.success(f"✅ Sentiment: **{result['sentiment']}**")
                    else:
                        st.error(f"Server error: {response.status_code}")
        except Exception as e:
                st.error(f"Connection failed: {e}")
