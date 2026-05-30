import streamlit as st
from graph.builder import build_roadmap_graph
from graph.state import RoadmapState
from utils.pdf_generator import generate_pdf
from dotenv import load_dotenv
import os

load_dotenv()

# ─────────────────────────────────────────
# Page Configuration
# ─────────────────────────────────────────
st.set_page_config(
    page_title="AI Career Mentor Agent",
    page_icon="🤖",
    layout="wide"
)

# ─────────────────────────────────────────
# Custom CSS Styling
# ─────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #ffffff;
    }
    
    /* Header */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #e94560, #0f3460);
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(233, 69, 96, 0.3);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0;
    }
    
    .main-header p {
        font-size: 1rem;
        color: #cccccc;
        margin: 0.5rem 0 0 0;
    }
    
    /* Search box */
    .stTextInput input {
        background-color: #16213e !important;
        color: #ffffff !important;
        border: 2px solid #e94560 !important;
        border-radius: 10px !important;
        font-size: 1.1rem !important;
        padding: 0.75rem !important;
    }
    
    /* Button */
    .stButton button {
        background: linear-gradient(90deg, #e94560, #c23152) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4) !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.6) !important;
    }
    
    /* Roadmap container */
    .roadmap-container {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(233, 69, 96, 0.3);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        backdrop-filter: blur(10px);
    }
    
    /* Download button */
    .stDownloadButton button {
        background: linear-gradient(90deg, #00b4d8, #0077b6) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
        margin-top: 1rem !important;
    }
    
    /* Info cards */
    .info-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(233, 69, 96, 0.2);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    /* Skills tags */
    .skill-tag {
        display: inline-block;
        background: rgba(233, 69, 96, 0.2);
        border: 1px solid #e94560;
        border-radius: 20px;
        padding: 0.3rem 0.8rem;
        margin: 0.3rem;
        font-size: 0.9rem;
        color: #ffffff;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #888888;
        font-size: 0.85rem;
        border-top: 1px solid rgba(233, 69, 96, 0.2);
        margin-top: 3rem;
    }
    
    /* Headings color fix */
    h1, h2, h3, h4 {
        color: #ffffff !important;
    }
    
    /* Text color */
    p, li {
        color: #cccccc !important;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# Header
# ─────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Career Mentor Agent</h1>
    <p>By Kumar Basu Singh | Your Personal AI Career Guide</p>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# Info Cards
# ─────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🎯</h3>
        <p>Role Analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🛠️</h3>
        <p>Skills Mapping</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🗺️</h3>
        <p>Step-by-Step Roadmap</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card">
        <h3>📄</h3>
        <p>PDF Download</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ─────────────────────────────────────────
# Search Section
# ─────────────────────────────────────────
st.markdown("### 🔍 Enter Your Dream Role")

col_input, col_btn = st.columns([3, 1])

with col_input:
    role = st.text_input(
        label="Role",
        placeholder="e.g. Data Scientist, Full Stack Developer, AI Engineer...",
        label_visibility="collapsed"
    )

with col_btn:
    generate_btn = st.button("🚀 Generate Roadmap")


# ─────────────────────────────────────────
# Generate Roadmap
# ─────────────────────────────────────────
if generate_btn:
    if not role.strip():
        st.warning("⚠️ Please enter a role first!")
    else:
        with st.status("🤖 AI Career Mentor is working...", expanded=True) as status:
            st.write("🔍 Analyzing role:", role)
            st.write("⚙️ Extracting required skills...")
            st.write("🌐 Searching documentation links...")
            st.write("📝 Generating your personalized roadmap...")

            try:
                # Build and run the graph
                graph = build_roadmap_graph()

                initial_state = RoadmapState(
                    role=role,
                    skills=[],
                    documentation_links={},
                    roadmap="",
                    pdf_path=None,
                    error=None,
                    is_complete=False
                )

                result = graph.invoke(initial_state)

                status.update(
                    label="✅ Roadmap Generated Successfully!",
                    state="complete"
                )

                # ─────────────────────────────────────────
                # Display Skills
                # ─────────────────────────────────────────
                st.markdown("---")
                st.markdown("### 🛠️ Skills Required")

                skills_html = ""
                for skill in result['skills']:
                    skills_html += f'<span class="skill-tag">✅ {skill}</span>'

                st.markdown(
                    f'<div style="margin: 1rem 0;">{skills_html}</div>',
                    unsafe_allow_html=True
                )

                # ─────────────────────────────────────────
                # Display Roadmap
                # ─────────────────────────────────────────
                st.markdown("---")
                st.markdown("### 🗺️ Your Complete Roadmap")

                st.markdown(
                    f'<div class="roadmap-container">{result["roadmap"]}</div>',
                    unsafe_allow_html=True
                )

                # ─────────────────────────────────────────
                # Generate and Download PDF
                # ─────────────────────────────────────────
                st.markdown("---")
                st.markdown("### 📄 Download Your Roadmap")

                pdf_path = generate_pdf(role, result['roadmap'])

                with open(pdf_path, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()

                st.download_button(
                    label="📥 Download PDF Roadmap",
                    data=pdf_bytes,
                    file_name=f"Career_Roadmap_{role.replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )

                # Clean up PDF file
                if os.path.exists(pdf_path):
                    os.remove(pdf_path)

            except Exception as e:
                status.update(label="❌ Error occurred!", state="error")
                st.error(f"Something went wrong: {str(e)}")
                st.info("Please check your API keys in .env file and try again.")


# ─────────────────────────────────────────
# How It Works Section
# ─────────────────────────────────────────
st.markdown("---")
st.markdown("### ℹ️ How It Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>1️⃣</h3>
        <p><b>Enter Role</b><br>Type your dream job role in the search bar</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>2️⃣</h3>
        <p><b>AI Analyzes</b><br>Our AI identifies all required skills</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>3️⃣</h3>
        <p><b>Roadmap Generated</b><br>Get a detailed step-by-step learning path</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card">
        <h3>4️⃣</h3>
        <p><b>Download PDF</b><br>Save your roadmap as a PDF file</p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────
# Footer
# ─────────────────────────────────────────
st.markdown("""
<div class="footer">
    <p>🤖 AI Career Mentor Agent | By Kumar Basu Singh</p>
    <p>Built with LangGraph • Groq • Tavily • Streamlit</p>
</div>
""", unsafe_allow_html=True)