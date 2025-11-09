import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for post length and language
LENGTH_OPTIONS = ["Short", "Medium", "Long"]
LANGUAGE_OPTIONS = ["English", "Hinglish"]


def show_home():
    st.title("💼 PostForge: LinkedIn Post Generator")
    st.markdown(
        """
        ### ✨ Welcome to PostForge
        **PostForge** helps you craft engaging, professional, and personalized LinkedIn posts in seconds.  
        Whether you're sharing career insights, data learnings, or personal growth stories —  
        PostForge combines **AI creativity** with your **unique voice**.

        **What you can do:**
        - 🧠 Choose a topic like *Career*, *Data Science*, *AI*, etc.  
        - ✍️ Pick your preferred **length** and **language** (English or Hinglish).  
        - 🚀 Instantly generate a post ready to share on LinkedIn.  
        - 💾 Download or copy it directly.

        ---
        """
    )


def show_generator():
    st.header("🧩 Generate a LinkedIn Post")

    # Create three columns for dropdowns
    col1, col2, col3 = st.columns(3)

    # Initialize FewShotPosts safely
    try:
        fs = FewShotPosts()
        tags = fs.get_tags()
    except Exception as e:
        st.error(f"Error loading topics: {e}")
        return

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=LENGTH_OPTIONS)

    with col3:
        selected_language = st.selectbox("Language", options=LANGUAGE_OPTIONS)

    # Generate post on button click
    if st.button("🚀 Generate Post"):
        with st.spinner("Crafting your LinkedIn post..."):
            try:
                post = generate_post(selected_length, selected_language, selected_tag)
                st.success("✅ Post generated successfully!")
                st.text_area("Your LinkedIn Post:", value=post, height=250)
                st.download_button("⬇️ Download Post", post, file_name="linkedin_post.txt")
            except Exception as e:
                st.error(f"Error generating post: {e}")


def show_about():
    st.title("ℹ️ About PostForge")
    st.markdown(
        """
        **PostForge** is an AI-powered tool developed to simplify content creation for professionals on LinkedIn.  
        It draws inspiration from real, high-performing LinkedIn posts and helps users:

        - Generate well-structured, engaging content ideas  
        - Maintain a natural, human tone (not robotic)  
        - Save time while keeping creativity intact  

        **Built with:**  
        🐍 Python · ⚡ Streamlit · 🤖 OpenAI / Few-shot prompting  

        **Creators:**  
        👩‍💻 [Devanshi Pandey](https://www.linkedin.com/in/devanshi-pandey-0a64a4280/)  
        👨‍💻 [Gaurav Pandey](https://www.linkedin.com/in/gaurav-pandey-094724283/)

        ---
        """
    )


def main():
    # Sidebar navigation
    st.sidebar.title("🔍 Navigation")
    page = st.sidebar.radio("Go to", ["🏠 Home", "✍️ Generate Post", "ℹ️ About"])

    if page == "🏠 Home":
        show_home()
    elif page == "✍️ Generate Post":
        show_generator()
    elif page == "ℹ️ About":
        show_about()


if __name__ == "__main__":
    main()
