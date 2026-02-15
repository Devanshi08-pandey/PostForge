import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="PostForge",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- FUTURISTIC RGB UI ---------------- #
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 20% 30%,
        rgb(30,41,59) 0%,
        rgb(15,23,42) 40%,
        rgb(2,6,23) 100%);
    color: rgb(226,232,240);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgb(11,18,32);
}

/* Glow Effects */
body::before {
    content: "";
    position: fixed;
    width: 450px;
    height: 450px;
    background: rgb(37,99,235);
    filter: blur(180px);
    top: -120px;
    left: -120px;
    opacity: 0.25;
    z-index: -1;
}

body::after {
    content: "";
    position: fixed;
    width: 450px;
    height: 450px;
    background: rgb(124,58,237);
    filter: blur(200px);
    bottom: -140px;
    right: -140px;
    opacity: 0.25;
    z-index: -1;
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0 0 40px rgba(99,102,241,0.2);
}

/* Feature Cards */
.feature-card {
    min-height: 280px;
}

/* Gradient Text */
.gradient-text {
    font-size: 48px;
    font-weight: 700;
    background: linear-gradient(
        90deg,
        rgb(56,189,248),
        rgb(129,140,248),
        rgb(192,132,252)
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        rgb(37,99,235),
        rgb(124,58,237)
    );
    color: white;
    border-radius: 12px;
    padding: 10px 22px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    box-shadow: 0 0 20px rgba(124,58,237,0.6);
}

/* Text Area */
textarea {
    background-color: rgba(255,255,255,0.05) !important;
    color: rgb(241,245,249) !important;
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- OPTIONS ---------------- #
LENGTH_OPTIONS = ["Short", "Medium", "Long"]
LANGUAGE_OPTIONS = ["English", "Hinglish"]

# ---------------- HOME ---------------- #
def show_home():
    st.markdown("""
    <div class="card">
        <div class="gradient-text">PostForge</div>
        <p style="margin-top:15px; font-size:18px; color:rgb(203,213,225);">
        AI-powered LinkedIn content generation platform for modern professionals.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card feature-card">
            <h3>Intelligent Generation</h3>
            <p>Advanced few-shot prompting ensures natural and engaging posts.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card feature-card">
            <h3>Professional Formatting</h3>
            <p>Optimized for LinkedIn readability and engagement.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card feature-card">
            <h3>Fast & Reliable</h3>
            <p>Generate polished posts in seconds.</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- GENERATOR ---------------- #
def show_generator():

    st.markdown("""
    <div class="card">
        <h2>Generate LinkedIn Post</h2>
    </div>
    """, unsafe_allow_html=True)

    fs = FewShotPosts()
    tags = fs.get_tags()

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("Topic", tags)

    with col2:
        selected_length = st.selectbox("Length", LENGTH_OPTIONS)

    with col3:
        selected_language = st.selectbox("Language", LANGUAGE_OPTIONS)

    if st.button("Generate Post"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.success("Post generated successfully.")
        st.text_area("Generated Post", post, height=250)
        st.download_button("Download Post", post, file_name="linkedin_post.txt")

# ---------------- ABOUT ---------------- #
def show_about():

    st.markdown("""
    <div class="card">
        <h2>About PostForge</h2>
        <p style="margin-top:15px;">
        PostForge is a modern AI-driven platform built to simplify professional LinkedIn publishing.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Developers")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <strong>Devanshi Pandey</strong><br>
            <span style="color:rgb(148,163,184); font-size:14px;">
            AI & Full Stack Developer
            </span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <strong>Gaurav Pandey</strong><br>
            <span style="color:rgb(148,163,184); font-size:14px;">
            Software Developer
            </span>
        </div>
        """, unsafe_allow_html=True)

# ---------------- MAIN ---------------- #
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("", ["Home", "Generate Post", "About"])

    if page == "Home":
        show_home()
    elif page == "Generate Post":
        show_generator()
    elif page == "About":
        show_about()

    st.markdown(
        "<hr style='border:0.5px solid rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; color:rgb(148,163,184); font-size:13px;'>© 2026 PostForge. Built for modern professionals.</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
