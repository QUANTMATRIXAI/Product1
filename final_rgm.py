import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# --- Streamlit config ---
st.set_page_config(page_title="RGM App", layout="wide")

# --- Custom CSS Based on Style Guide (Quant Matrix AI) ---
st.markdown("""
<!-- Same snippet, just added references to #41C185 (Secondary) and #458EE2 (Tertiary) -->

<style>
/* Import Inter from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Overall body styling */
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    background-color: #F5F5F5; /* Light background */
    color: #333333;            /* Dark text */
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #FFFFFF; /* White sidebar */
    border-right: 1px solid #999999;
}

/* Title / Headings */
h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    margin-bottom: 0.5em;
}

/* Button Overrides (Primary Buttons) */
.stButton > button {
    background-color: transparent;  /* Transparent fill */
    color: #333333;                 /* Dark text */
    border: 3px solid #FFBD59;      /* Yellow border */
    padding: 0.6em 1.2em;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
}

/* Hover + Active states for Primary Buttons */
.stButton > button:hover {
    background-color: #FFCF87;
}
.stButton > button:active {
    background-color: #FFE7C2;
    transform: scale(0.98);
}

/* Focused Button Outline (use Tertiary color) */
.stButton > button:focus {
    outline: 2px solid #458EE2; /* Tertiary Blue */
    outline-offset: 2px;
}

/* Disabled Button */
.stButton > button:disabled {
    background-color: #999999;
    color: #FFFFFF;
    cursor: not-allowed;
}

/* Additional Classes for Secondary/Tertiary Buttons if needed */
/* (Used if you do custom HTML or a small hack with st.markdown/HTML) */
.btn-secondary {
    background-color: #41C185 !important; /* Secondary Green */
    color: #FFFFFF !important;
}
.btn-tertiary {
    background-color: #458EE2 !important; /* Tertiary Blue */
    color: #FFFFFF !important;
}

/* Card-like blocks for sections */
.block-container {
    background-color: #FFFFFF; 
    border-radius: 8px;
    padding: 2rem;
    margin-top: 1rem;
    /* etc... */
}
/* Limit container width */
main .block-container {
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
}
/* Adjust main page padding */
.css-1lcbmhc.e1fqkh3o6 {
    padding: 1rem 2rem;
}
/* Additional card styling for custom usage */
.custom-card {
    background-color: #FFFFFF;
    border: 1px solid #999999;
    border-radius: 8px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.5rem;
}
</style>

""", unsafe_allow_html=True)

st.sidebar.title("RGM App Sidebar")

# -----------------------------
#   Session State & Navigation
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "history" not in st.session_state:
    st.session_state.history = []

def go_to(page_name):
    st.session_state.history.append(st.session_state.page)
    st.session_state.page = page_name
    st.rerun()

def go_back():
    if st.session_state.history:
        st.session_state.page = st.session_state.history.pop()
    else:
        st.session_state.page = "home"
    st.rerun()

def go_home():
    st.session_state.page = "home"
    st.session_state.history = []
    st.rerun()
    
section_names = { 
    "1": "Pre-Process",
    "2": "Explore",
    "3": "Engineer",
    "4": "Build",
    "5": "Evaluate",
    "6": "Plan",
    "7": "Report"
}

def home_page():
    import streamlit as st
    
    st.title("Welcome to RGM App")
    
    # Updated custom CSS to match your style guide and accent colors
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: #F5F5F5;
        }}
        .workflow-header {{
            background-color: #FFBD59; 
            border-left: 5px solid #FFC87A;
            padding: 10px 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .workflow-title {{
            font-size: 1.2rem;
            margin: 0;
            color: #333333;
        }}
        .custom-card {{
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
            height: 100%;
            position: relative;
            transition: transform 0.2s;
            border: 1px solid #E0E0E0;
        }}
        .custom-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 5px 10px rgba(0,0,0,0.15);
        }}
        .step-number {{
            display: inline-block;
            width: 25px;
            height: 25px;
            background-color: #FFBD59; 
            color: white;
            border-radius: 50%;
            text-align: center;
            line-height: 25px;
            font-weight: bold;
            margin-right: 10px;
        }}
        .last-step {{
            background-color: #FFC87A; 
        }}
        .section-title {{
            margin-top: 0;
            font-size: 1.1rem;
            color: #333333;
            display: flex;
            align-items: center;
        }}
        .section-desc {{
            color: #666666;
            font-size: 0.9rem;
            margin-bottom: 0;
            padding-left: 35px;
        }}
        .workflow-timeline {{
            position: relative;
            margin-bottom: 30px;
            padding: 15px;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            background-color: #FAFAFA;
        }}
        .timeline-title {{
            font-size: 1rem;
            color: #666666;
            margin-bottom: 15px;
        }}
        .timeline-steps {{
            display: flex;
            justify-content: space-between;
        }}
        .timeline-step {{
            text-align: center;
            position: relative;
            flex: 1;
        }}
        .timeline-step:not(:last-child):after {{
            content: "";
            position: absolute;
            top: 12px;
            right: 0;
            width: 80%;
            height: 2px;
            background-color: #FFBD59; 
        }}
        .step-dot {{
            display: inline-block;
            width: 25px;
            height: 25px;
            background-color: #FFBD59; 
            color: white;
            border-radius: 50%;
            text-align: center;
            line-height: 25px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .step-dot-7 {{
            background-color: #FFC87A;
        }}
        .step-name {{
            font-size: 0.8rem;
            color: #333333;
        }}
    </style>
    """, unsafe_allow_html=True)
    
    # Workflow header
    st.markdown("""
    <div class="workflow-header">
        <h2 class="workflow-title">📋 RGM Workflow: Follow the 7-step process</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline visualization
    timeline_html = f"""
    <div class="workflow-timeline">
        <h3 class="timeline-title">Workflow Steps:</h3>
        <div class="timeline-steps">
            <div class="timeline-step">
                <div class="step-dot">1</div>
                <div class="step-name">{section_names['1']}</div>
            </div>
            <div class="timeline-step">
                <div class="step-dot">2</div>
                <div class="step-name">{section_names['2']}</div>
            </div>
            <div class="timeline-step">
                <div class="step-dot">3</div>
                <div class="step-name">{section_names['3']}</div>
            </div>
            <div class="timeline-step">
                <div class="step-dot">4</div>
                <div class="step-name">{section_names['4']}</div>
            </div>
            <div class="timeline-step">
                <div class="step-dot">5</div>
                <div class="step-name">{section_names['5']}</div>
            </div>
            <div class="timeline-step">
                <div class="step-dot">6</div>
                <div class="step-name">{section_names['6']}</div>
            </div>
            <div class="timeline-step">
                <div class="step-dot step-dot-7">7</div>
                <div class="step-name">{section_names['7']}</div>
            </div>
        </div>
    </div>
    """
    st.markdown(timeline_html, unsafe_allow_html=True)

    # Row 1: Sections 1, 2, 3
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="custom-card">
            <h3 class="section-title">
                <span class="step-number">1</span>
                <span>🔬 {section_names['1']}</span>
            </h3>
            <p class="section-desc">Analyze, detect, and manage base/promo scenarios with advanced logic.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Pre-Process", use_container_width=True):
            go_to("section1")

    with col2:
        st.markdown(f"""
        <div class="custom-card">
            <h3 class="section-title">
                <span class="step-number">2</span>
                <span>🔎 {section_names['2']}</span>
            </h3>
            <p class="section-desc">Additional functionalities, data processing, or analytics for Section 2.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Explore", use_container_width=True):
            go_to("section2")

    with col3:
        st.markdown(f"""
        <div class="custom-card">
            <h3 class="section-title">
                <span class="step-number">3</span>
                <span>⚙️ {section_names['3']}</span>
            </h3>
            <p class="section-desc">Expand or explore tasks, visualizations, or reports for Section 3.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Engineer", use_container_width=True):
            go_to("section3")

    # Row 2: Sections 4, 5, 6
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(f"""
        <div class="custom-card">
            <h3 class="section-title">
                <span class="step-number">4</span>
                <span>🏗️ {section_names['4']}</span>
            </h3>
            <p class="section-desc">Manage engineering tasks, processes, or workflows.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Build", use_container_width=True):
            go_to("Build_1")

    with col5:
        st.markdown(f"""
        <div class="custom-card">
            <h3 class="section-title">
                <span class="step-number">5</span>
                <span>📝 {section_names['5']}</span>
            </h3>
            <p class="section-desc">Evaluate models, results, or processes with rigorous checks.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Evaluate", use_container_width=True):
            go_to("section5")

    with col6:
        st.markdown(f"""
        <div class="custom-card">
            <h3 class="section-title">
                <span class="step-number">6</span>
                <span>📅 {section_names['6']}</span>
            </h3>
            <p class="section-desc">Plan upcoming tasks, iterations, or strategies for your workflow.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Plan", use_container_width=True):
            go_to("section6")

    # Row 3: Section 7
    col7 = st.columns(1)[0]
    with col7:
        st.markdown(f"""
        <div class="custom-card">
            <h3 class="section-title">
                <span class="step-number last-step">7</span>
                <span>📑 {section_names['7']}</span>
            </h3>
            <p class="section-desc">Generate, organize, and view final reports or summaries.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Report", use_container_width=True):
            go_to("report_1")

    # Footer
    st.markdown("""
    ---
    <div style='text-align:center; color:#666666; font-size:0.9rem;'>
    © 2025 RGM Tool &nbsp;|&nbsp; Powered by Quant Matrix AI &nbsp;–&nbsp; All Rights Reserved
    </div>
    """, unsafe_allow_html=True)

def go_to(section_key: str):
    import streamlit as st
    st.session_state["page"] = section_key
    st.rerun()



        
# ------------------------------
#  SECTION PAGE (Multi-Purpose)
# ------------------------------
def section_page(section_number):
    displayed_name = section_names.get(section_number, f"Section {section_number}")
    st.header(displayed_name)

    # Only do special layout for section 1
    if section_number == "1":
            st.write("Below are the **three modules** for Base/Promo Detection.")

            # Add module flow CSS
            st.markdown("""
            <style>
                .module-container {
                    position: relative;
                    padding: 10px 0 20px 0;
                }
                
                .module-card {
                    background-color: white;
                    border-radius: 8px;
                    padding: 15px;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
                    height: 100%;
                    position: relative;
                    transition: transform 0.2s;
                    border: 1px solid #E0E0E0;
                    z-index: 2;
                }
                
                .module-card:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 5px 10px rgba(0,0,0,0.15);
                }
                
                .step-badge {
                    display: inline-block;
                    width: 22px;
                    height: 22px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 22px;
                    font-weight: bold;
                    margin-right: 8px;
                    font-size: 0.8rem;
                }
                
                .module-title {
                    display: flex;
                    align-items: center;
                    margin-top: 0;
                    margin-bottom: 10px;
                    font-size: 1.1rem;
                }
                
                .module-desc {
                    color: #666;
                    font-size: 0.9rem;
                    margin-bottom: 0;
                    padding-left: 30px;
                }
                
                .flow-indicator {
                    position: absolute;
                    top: 40%;
                    right: -17px;
                    width: 35px;
                    height: 12px;
                    z-index: 1;
                    overflow: hidden;
                }
                
                .flow-indicator svg {
                    fill: #4CAF50;
                }
                
                .flow-header {
                    background-color: #F5F5F5;
                    border-left: 4px solid #4CAF50;
                    padding: 8px 12px;
                    margin-bottom: 15px;
                    border-radius: 4px;
                    font-size: 0.95rem;
                    color: #333;
                }
            </style>
            """, unsafe_allow_html=True)

            # Flow header
            st.markdown(
                """
                <div class="flow-header">
                    <strong>Sequential Process:</strong> Follow the steps in order (1-2-3) for optimal results
                </div>
                """, 
                unsafe_allow_html=True
            )

            # Create columns for the three modules
            col1, col2, col3 = st.columns(3)

            # 1) Validate
            with col1:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">1</span>
                                Validate
                            </h4>
                            <p class="module-desc">Check data consistency, completeness, and accuracy.</p>
                        </div>
                        <div class="flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Validate", use_container_width=True):
                    go_to("preprocess_validate")

            # 2) Feature Overview
            with col2:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">2</span>
                                Feature Overview
                            </h4>
                            <p class="module-desc">Review data attributes, distributions, and potential transformations.</p>
                        </div>
                        <div class="flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Feature Overview", use_container_width=True):
                    go_to("preprocess_feature_overview")

            # 3) Prepare
            with col3:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">3</span>
                                Prepare
                            </h4>
                            <p class="module-desc">Clean, transform, and finalize data for subsequent steps.</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Prepare", use_container_width=True):
                    go_to("preprocess_prepare")

            
                        # Divider + Navigation
            st.markdown("---")
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("Back"):
                    go_back()
            with col_b:
                if st.button("Home"):
                    go_home()
                    

                

                
    elif section_number == "2":
            st.write("Below are the **five modules** for Price/Promo Elasticity.")

            # Add module flow CSS with adjustments for 5 columns
            st.markdown("""
            <style>
                .module-container {
                    position: relative;
                    padding: 10px 0 20px 0;
                }
                
                .module-card {
                    background-color: white;
                    border-radius: 8px;
                    padding: 12px;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
                    height: 100%;
                    position: relative;
                    transition: transform 0.2s;
                    border: 1px solid #E0E0E0;
                    z-index: 2;
                }
                
                .module-card:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 5px 10px rgba(0,0,0,0.15);
                }
                
                .step-badge {
                    display: inline-block;
                    width: 20px;
                    height: 20px;
                    background-color: #2196F3;
                    color: white;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 20px;
                    font-weight: bold;
                    margin-right: 6px;
                    font-size: 0.75rem;
                }
                
                .module-title {
                    display: flex;
                    align-items: center;
                    margin-top: 0;
                    margin-bottom: 8px;
                    font-size: 0.95rem;
                }
                
                .module-desc {
                    color: #666;
                    font-size: 0.75rem;
                    margin-bottom: 0;
                    padding-left: 26px;
                }
                
                .flow-indicator {
                    position: absolute;
                    top: 40%;
                    right: -13px;
                    width: 26px;
                    height: 10px;
                    z-index: 3;
                }
                
                .flow-indicator svg {
                    fill: #2196F3;
                }
                
                .flow-header {
                    background-color: #E3F2FD;
                    border-left: 4px solid #2196F3;
                    padding: 8px 12px;
                    margin-bottom: 15px;
                    border-radius: 4px;
                    font-size: 0.95rem;
                    color: #333;
                }
            </style>
            """, unsafe_allow_html=True)

            # Flow header
            st.markdown(
                """
                <div class="flow-header">
                    <strong>Sequential Process:</strong> Follow the steps in order (1-2-3-4-5) for comprehensive analysis
                </div>
                """, 
                unsafe_allow_html=True
            )

            # Create columns for the five modules
            col1, col2, col3, col4, col5 = st.columns(5)

            # ============= MODULE 1 =============
            with col1:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">1</span>
                                Market Construct
                            </h4>
                            <p class="module-desc">Define and analyze market structure, segments, and key factors.</p>
                        </div>
                        <div class="flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Market Construct", use_container_width=True):
                    go_to("market_construct")

            # ============= MODULE 2 =============
            with col2:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">2</span>
                                Price Ladder
                            </h4>
                            <p class="module-desc">Visualize and evaluate price points, thresholds, and positioning.</p>
                        </div>
                        <div class="flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Price Ladder", use_container_width=True):
                    go_to("price_ladder")

            # ============= MODULE 3 =============
            with col3:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">3</span>
                                Promo Intensity
                            </h4>
                            <p class="module-desc">Assess promotion frequency, depth, and impacts on volume.</p>
                        </div>
                        <div class="flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Promo Intensity", use_container_width=True):
                    go_to("promo_intensity")

            # ============= MODULE 4 =============
            with col4:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">4</span>
                                Promo Comparison
                            </h4>
                            <p class="module-desc">Compare different promotional strategies side by side.</p>
                        </div>
                        <div class="flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Promo Comparison", use_container_width=True):
                    go_to("promocomparison")

            # ============= MODULE 5 =============
            with col5:
                st.markdown(
                    """
                    <div class="module-container">
                        <div class="module-card">
                            <h4 class="module-title">
                                <span class="step-badge">5</span>
                                Correlations
                            </h4>
                            <p class="module-desc">Analyze relationships between price, promo, and other variables.</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Correlations", use_container_width=True):
                    go_to("correlations")


            # Divider + Navigation
            st.markdown("---")
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("Back"):
                    go_back()
            with col_b:
                if st.button("Home"):
                    go_home()

                
                
    elif section_number == "3":
            st.write("Below are the **advanced modules** for RGM analysis.")

            # Add module flow CSS with adjustments for 4 columns (advanced modules)
            st.markdown("""
            <style>
                .advanced-module-container {
                    position: relative;
                    padding: 10px 0 20px 0;
                }
                
                .advanced-module-card {
                    background-color: white;
                    border-radius: 8px;
                    padding: 15px;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
                    height: 100%;
                    position: relative;
                    transition: transform 0.2s;
                    border: 1px solid #E0E0E0;
                    z-index: 2;
                }
                
                .advanced-module-card:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 5px 10px rgba(0,0,0,0.15);
                }
                
                .advanced-step-badge {
                    display: inline-block;
                    width: 22px;
                    height: 22px;
                    background-color: #673AB7;
                    color: white;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 22px;
                    font-weight: bold;
                    margin-right: 8px;
                    font-size: 0.8rem;
                }
                
                .advanced-module-title {
                    display: flex;
                    align-items: center;
                    margin-top: 0;
                    margin-bottom: 10px;
                    font-size: 1.05rem;
                }
                
                .advanced-module-desc {
                    color: #666;
                    font-size: 0.85rem;
                    margin-bottom: 0;
                    padding-left: 30px;
                }
                
                .advanced-flow-indicator {
                    position: absolute;
                    top: 40%;
                    right: -15px;
                    width: 30px;
                    height: 10px;
                    z-index: 3;
                }
                
                .advanced-flow-indicator svg {
                    fill: #673AB7;
                }
                
                .advanced-flow-header {
                    background-color: #EDE7F6;
                    border-left: 4px solid #673AB7;
                    padding: 8px 12px;
                    margin-bottom: 15px;
                    border-radius: 4px;
                    font-size: 0.95rem;
                    color: #333;
                }
            </style>
            """, unsafe_allow_html=True)

            # Flow header for advanced modules
            st.markdown(
                """
                <div class="advanced-flow-header">
                    <strong>Advanced Workflow:</strong> These modules offer sophisticated analysis capabilities (follow steps 1-4)
                </div>
                """, 
                unsafe_allow_html=True
            )

            # Create columns for the four advanced modules
            col1, col2, col3, col4 = st.columns(4)

            # ============= MODULE 1 =============
            with col1:
                st.markdown(
                    """
                    <div class="advanced-module-container">
                        <div class="advanced-module-card">
                            <h4 class="advanced-module-title">
                                <span class="advanced-step-badge">1</span>
                                Feature Overview
                            </h4>
                            <p class="advanced-module-desc">Gain a quick insight into available features, metrics, and data structures.</p>
                        </div>
                        <div class="advanced-flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Feature Overview", key="adv_feature_overview", use_container_width=True):
                    go_to("feature_overview_2")

            # ============= MODULE 2 =============
            with col2:
                st.markdown(
                    """
                    <div class="advanced-module-container">
                        <div class="advanced-module-card">
                            <h4 class="advanced-module-title">
                                <span class="advanced-step-badge">2</span>
                                Create
                            </h4>
                            <p class="advanced-module-desc">Generate new features or datasets to enhance model performance.</p>
                        </div>
                        <div class="advanced-flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Create", key="adv_create", use_container_width=True):
                    go_to("create_section3")

            # ============= MODULE 3 =============
            with col3:
                st.markdown(
                    """
                    <div class="advanced-module-container">
                        <div class="advanced-module-card">
                            <h4 class="advanced-module-title">
                                <span class="advanced-step-badge">3</span>
                                Transform
                            </h4>
                            <p class="advanced-module-desc">Apply transformations, aggregations, or scaling techniques to your data.</p>
                        </div>
                        <div class="advanced-flow-indicator">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                            </svg>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Transform", key="adv_transform", use_container_width=True):
                    go_to("transform_section3")

            # ============= MODULE 4 =============
            with col4:
                st.markdown(
                    """
                    <div class="advanced-module-container">
                        <div class="advanced-module-card">
                            <h4 class="advanced-module-title">
                                <span class="advanced-step-badge">4</span>
                                Select
                            </h4>
                            <p class="advanced-module-desc">Choose or filter the most relevant features or data subsets for analysis.</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Select", key="adv_select", use_container_width=True):
                    go_to("select_section3")

    elif section_number == "5":
        st.write("Evaluate.")

        # ---------- shared CSS (same tokens as section‑3) ----------
        st.markdown(
            """
            <style>
                .advanced-module-container {
                    position: relative;
                    padding: 10px 0 20px 0;
                }
                .advanced-module-card {
                    background-color: white;
                    border-radius: 8px;
                    padding: 15px;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
                    height: 100%;
                    position: relative;
                    transition: transform 0.2s;
                    border: 1px solid #E0E0E0;
                    z-index: 2;
                }
                .advanced-module-card:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 5px 10px rgba(0,0,0,0.15);
                }
                .advanced-step-badge {
                    display: inline-block;
                    width: 22px;
                    height: 22px;
                    background-color: #673AB7;
                    color: white;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 22px;
                    font-weight: bold;
                    margin-right: 8px;
                    font-size: 0.8rem;
                }
                .advanced-module-title {
                    display: flex;
                    align-items: center;
                    margin-top: 0;
                    margin-bottom: 10px;
                    font-size: 1.05rem;
                }
                .advanced-module-desc {
                    color: #666;
                    font-size: 0.85rem;
                    margin-bottom: 0;
                    padding-left: 30px;
                }
                .advanced-flow-indicator {
                    position: absolute;
                    top: 40%;
                    right: -15px;
                    width: 30px;
                    height: 10px;
                    z-index: 3;
                }
                .advanced-flow-indicator svg { fill: #673AB7; }
                .advanced-flow-header {
                    background-color: #EDE7F6;
                    border-left: 4px solid #673AB7;
                    padding: 8px 12px;
                    margin-bottom: 15px;
                    border-radius: 4px;
                    font-size: 0.95rem;
                    color: #333;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # ---------- header ----------
        st.markdown(
            """
            <div class="advanced-flow-header">
                <strong>Evaluation Workflow:</strong> Follow steps 1‑2 to review and finalise models
            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------- exactly two columns ----------
        col1, col2 = st.columns(2)

        # ───────── MODULE 1 – Model Selection ─────────
        with col1:
            st.markdown(
                """
                <div class="advanced-module-container">
                    <div class="advanced-module-card">
                        <h4 class="advanced-module-title">
                            <span class="advanced-step-badge">1</span>
                            Statistical check(Model Selector)
                        </h4>
                        <p class="advanced-module-desc">
                            Filter, compare, and choose candidate models for evaluation.
                        </p>
                    </div>
                    <div class="advanced-flow-indicator">
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
                        </svg>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Model Selection", key="eval_model_sel", use_container_width=True):
                go_to("model_selection")

        # ───────── MODULE 2 – Post‑Modelling / Final Save ─────────
        with col2:
            st.markdown(
                """
                <div class="advanced-module-container">
                    <div class="advanced-module-card">
                        <h4 class="advanced-module-title">
                            <span class="advanced-step-badge">2</span>
                            Business Logic Check
                        </h4>
                        <p class="advanced-module-desc">
                            Inspect contribution charts, compare metrics, and lock‑in the winning model(s).
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Post‑Modelling", key="eval_post_mod", use_container_width=True):
                go_to("post_modelling")

        # ---------- divider & nav ----------
        st.markdown("---")
        nav_a, nav_b = st.columns(2)
        with nav_a:
            if st.button("Back"):
                go_back()
        with nav_b:
            if st.button("Home"):
                go_home()




#####################timeline

# ==========================================================
#  Re‑usable 7‑step timeline
# ==========================================================
# =============================================================================
#  Gorgeous 7‑Step Timeline  ➜  call show_timeline("1") … "7"
# =============================================================================
# ==============================================================
#  BLUE 7‑STEP TIMELINE  ➜  call show_timeline("3"), etc.
# ==============================================================
# ============================================================
#  Yellow dots + Blue progress   →  show_timeline("3")
# ============================================================
import streamlit as st

STEP_LABELS = {
    "1": "Pre‑Process", "2": "Explore",  "3": "Engineer",
    "4": "Build",       "5": "Evaluate", "6": "Plan", "7": "Report"
}

def show_timeline(active: str):
    total   = 7
    current = int(active)

    # ❶ ALWAYS push the style (no session‑state check)
    st.markdown(
        """
        <style>
        .tl-wrap   {margin:0 0 18px 0;}
        .tl-steps  {display:flex; justify-content:space-between;}
        .tl-step   {flex:1; text-align:center; position:relative; font-size:0.8rem;}
        .tl-dot    {width:28px; height:28px; line-height:28px; border-radius:50%;
                    display:inline-block; color:#fff; font-weight:700;}
        .done-dot     {background:#FFBD59;}
        .current-dot  {background:#FFC87A;}
        .upcoming-dot {background:#CCCCCC;}
        .tl-step:not(:last-child)::after{
            content:''; position:absolute; top:14px; right:-50%;
            width:100%; height:4px; background:#CCCCCC; z-index:-1;
        }
        .done:not(:last-child)::after, .current:not(:last-child)::after{
            background:#458EE2;  /* blue progress */
        }
        .tl-progress{height:6px; background:#E5E5E5; border-radius:3px; margin-top:10px;}
        .tl-fill    {height:100%; background:#458EE2;}
        </style>
        """,
        unsafe_allow_html=True
    )

    pct = (current - 1) / (total - 1) * 100
    html = ["<div class='tl-wrap'><div class='tl-steps'>"]
    for n in range(1, total + 1):
        cls_step = "done" if n < current else "current" if n == current else "upcoming"
        dot_cls  = {"done":"done-dot","current":"current-dot","upcoming":"upcoming-dot"}[cls_step]
        html.append(
            f"<div class='tl-step {cls_step}'>"
            f"<span class='tl-dot {dot_cls}'>{n}</span><br>{STEP_LABELS[str(n)]}"
            "</div>"
        )
    html.append("</div>")
    html.append(f"<div class='tl-progress'><div class='tl-fill' style='width:{pct}%;'></div></div></div>")
    st.markdown("".join(html), unsafe_allow_html=True)



#########################################def Engineer
###############inter page navigation

####################section1

def validate_page():

    import streamlit as st
    import pandas as pd
    show_timeline("1")          # highlight step 1

    # 0) Helpers ----------------------------------------------------------------
    def go_back():
        st.session_state.page = st.session_state.history.pop() if st.session_state.history else "home"
        st.rerun()

    def go_home():
        st.session_state.page = "home"
        st.session_state.history = []
        st.rerun()

    def go_to(page_name: str):
        st.session_state.history.append(st.session_state.page)
        st.session_state.page = page_name
        st.rerun()

    # 1) Header -----------------------------------------------------------------
    st.header("Validate")
    st.markdown("<hr class='accent-hr'>", unsafe_allow_html=True)
    st.write(
        "Data must be **daily** (`Date`) or **weekly** (`Year` + `Week`). "
        "Monthly files (`Year` + `Month` without `Week`) are not allowed."
    )

    # 2) Load DataFrame ----------------------------------------------------------
    df = st.session_state.get("D0", None)
    if df is None or df.empty:
        st.error("⚠️ No dataset found. Upload & select a file in the sidebar.")
        return  # stop without crashing

    # 3) Column‑name cleanup -----------------------------------------------------
    expected = [
        "Channel", "Brand", "PPG", "SalesValue", "Volume",
        "Variant", "PackType", "PackSize",
        "Date", "Year", "Month", "Week",
        "Price", "BasePrice"
    ]
    rename_map = {}
    for col in df.columns:
        stripped = col.strip()
        match = next((e for e in expected if e.lower() == stripped.lower()), None)
        new_name = match if match else stripped
        if new_name != col:
            rename_map[col] = new_name
    if rename_map:
        df = df.rename(columns=rename_map)
        st.info(
            "🧹 **Auto‑renamed columns:**\n"
            + "\n".join(f"• `{o}` → `{n}`" for o, n in rename_map.items())
        )

    # 4) Frequency check ---------------------------------------------------------
    time_cols = {k: k in df.columns for k in ("Date", "Year", "Week", "Month")}
    if time_cols["Year"] and time_cols["Month"] and not time_cols["Week"] and not time_cols["Date"]:
        st.error("❌ Monthly data detected (`Year` + `Month` only). Supply `Date` or `Year` + `Week`.")
        return
    elif time_cols["Year"] and time_cols["Week"]:
        st.success("✅ **Weekly** data detected (`Year` + `Week`).")
    elif time_cols["Date"]:
        st.success("✅ **Daily** data detected (`Date`).")
    else:
        st.error("❌ Cannot detect valid time columns. Need `Date` or both `Year` & `Week`.")
        return

    # 5) Overview ----------------------------------------------------------------
    st.subheader("Data Overview")
    st.write(f"**Rows:** {df.shape[0]:,}  **Columns:** {df.shape[1]}")
    st.dataframe(df.head(5), use_container_width=True)

    # 6) Missing‑value panel -----------------------------------------------------
    miss_counts = df.isna().sum().loc[lambda s: s > 0]
    left, right = st.columns([1, 2])

    with left:
        st.subheader("Missing‑value counts")
        if miss_counts.empty:
            st.success("✅ No missing values.")
        else:
            st.table(miss_counts.rename("Missing"))
            st.markdown("*Columns:* " + ", ".join(f"`{c}`" for c in miss_counts.index))

    with right:
        st.subheader("Sample rows with missing values")
        if miss_counts.empty:
            st.write("—")
        else:
            bad_rows = df[df.isna().any(axis=1)]
            st.dataframe(bad_rows.head(5), use_container_width=True)
            if len(bad_rows) > 5:
                st.write(f"...and **{len(bad_rows) - 5}** more rows.")

    # 7) Validation checks -------------------------------------------------------
    required     = ["Channel", "Brand", "PPG", "SalesValue", "Volume"]
    agg_dims     = ["Variant", "PackType", "PackSize"]
    checks: list[dict] = []

    # Required
    missing_req = [c for c in required if c not in df.columns]
    checks.append({
        "name": "Required columns",
        "status": "fail" if missing_req else "pass",
        "msg": f"Missing: {', '.join(missing_req)}" if missing_req else "All present."
    })
    # Aggregator
    found_aggs = [c for c in agg_dims if c in df.columns]
    checks.append({
        "name": "Aggregator dims",
        "status": "warn" if not found_aggs else "pass",
        "msg": "None found." if not found_aggs else f"Found: {', '.join(found_aggs)}"
    })
    # Numeric checks
    for col in ("Volume", "SalesValue"):
        ok = col in df.columns and pd.api.types.is_numeric_dtype(df[col])
        checks.append({
            "name": f"{col} numeric",
            "status": "pass" if ok else "fail",
            "msg": "" if ok else f"`{col}` missing or non‑numeric."
        })
    # Price
    if "Price" in df.columns:
        ok = pd.api.types.is_numeric_dtype(df["Price"])
        checks.append({"name": "Price numeric", "status": "pass" if ok else "warn",
                       "msg": "" if ok else "Exists but not numeric."})
    else:
        checks.append({"name": "Price column", "status": "warn",
                       "msg": "Will compute from `SalesValue / Volume`."})
    # BasePrice
    bp_ok = "BasePrice" in df.columns
    checks.append({"name": "BasePrice column",
                   "status": "pass" if bp_ok else "warn",
                   "msg": "Already present." if bp_ok else "Will be computed in Base‑Price Estimator."})

    # Overall validity flag
    valid = all(c["status"] != "fail" for c in checks)

    # 8) Validation report cards ----------------------------------------------
    st.subheader("Validation Report")
    colours = {"pass": "#2E7D32", "warn": "#FFB300", "fail": "#C62828"}
    icons   = {"pass": "✅",       "warn": "⚠️",       "fail": "❌"}
    cards   = st.columns(len(checks))

    for col_box, chk in zip(cards, checks):
        with col_box:
            html = (
                f"<div style='border-left:5px solid {colours[chk['status']]};"
                "padding:0.75em 1em; background:#FFF; border-radius:4px;'>"
                f"<strong>{icons[chk['status']]} {chk['name']}</strong>"
                + (f"<br><small>{chk['msg']}</small>" if chk['msg'] else "")
                + "</div>"
            )
            st.markdown(html, unsafe_allow_html=True)

    # Overall validity flag
    valid = all(c["status"] != "fail" for c in checks)

    # If everything passed, show a green banner + short guide
    if valid:
        st.success("🎉 **All critical checks passed.**")
        st.markdown(
            "##### Next step\n"
            "Click **Proceed to Feature Overview ➜** to explore and review your data’s feature columns."
        )

    # 9) Persist cleaned DF + rename map ---------------------------------------
    st.session_state['D0'] = df
    st.session_state['validator_renamed'] = rename_map

    # ─ Navigation buttons ──────────────────────────────────
    st.markdown("---")
    col_back, col_next = st.columns(2)

    with col_back:
        if st.button("Back"):
            go_back()

    with col_next:
        if valid:
            if st.button("Proceed to Feature Overview ➜"):
                go_to("preprocess_feature_overview")
        else:
            st.button("Proceed to Feature Overview ➜", disabled=True)
            st.warning("Fix the issues above, then re‑run **Validate** to continue.")
                
                
################################################

def feature_overview_page():

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

    # timeline first  (highlight main step 1)
    show_timeline("1")

    # ───────── constants ─────────
    TIME_KEYS = {"Year", "Month", "Week"}    # treat as non‑numeric

    # ───────── header & css  ─────
    st.header("Feature Overview")
    st.markdown(
        "<p class='subheader'>Interactive filters and at‑a‑glance statistics "
        "to understand your dataset before engineering.</p>"
        "<hr class='accent-hr'>",
        unsafe_allow_html=True
    )

    # ───────── data retrieval ─────
    df = st.session_state.get("D0", None)
    if df is None or df.empty:
        st.warning("No data found – run **Validate** first.")
        return

    # ───────── sidebar aggregator filters ─────
    with st.sidebar:
        st.subheader("Aggregator Filters")
        cat_cols_all = df.select_dtypes(include=["object", "category"]).columns.tolist()

        if cat_cols_all:
            default_sel = st.session_state.get("fo_saved_aggs", [])
            agg_cols_sel = st.multiselect("Choose columns:", cat_cols_all, default=default_sel)

            for col in agg_cols_sel:
                options = ["All"] + sorted(df[col].dropna().unique().tolist())
                sel = st.radio(col, options, horizontal=True, key=f"fo_{col}")
                if sel != "All":
                    df = df[df[col] == sel]

            st.session_state["fo_saved_aggs"] = agg_cols_sel
            st.markdown("---")
            st.write(f"**Rows after filter:** {len(df):,}")
            st.download_button("⬇ Download filtered CSV", df.to_csv(index=False), "filtered_data.csv")
        else:
            st.info("No categorical columns to filter.")

    if df.empty:
        st.error("All rows filtered out – relax your filters.")
        return

    # ───────── TABS layout ───────
    tabs = st.tabs(["Overview", "Columns", "Numeric", "Categorical",
                    "Distributions", "Correlation", "Samples"])

    # ======= TAB 0: Overview =======
    with tabs[0]:
        n_rows, n_cols = df.shape
        mem_mb = df.memory_usage(deep=True).sum() / 1e6
        missing_cells = df.isna().sum().sum()
        pct_missing = missing_cells / (n_rows * n_cols) * 100 if n_rows and n_cols else 0

        st.metric("Rows", f"{n_rows:,}")
        st.metric("Columns", f"{n_cols}")
        st.metric("Memory", f"{mem_mb:.2f} MB")
        st.metric("Missing cells", f"{missing_cells:,} ({pct_missing:.2f} %)")

    # ======= TAB 1: Columns ========
    with tabs[1]:
        st.subheader("Column Details")
        info = []
        for c in df.columns:
            info.append({
                "Column": c,
                "Type": str(df[c].dtype),
                "Missing": df[c].isna().sum(),
                "Unique": df[c].nunique(dropna=True),
                "Examples": ", ".join(map(str, df[c].dropna().unique()[:3])) or "—"
            })
        st.dataframe(pd.DataFrame(info), use_container_width=True)

    # ======= TAB 2: Numeric =========
    with tabs[2]:
        numeric_cols = [
            c for c in df.select_dtypes(include=[np.number]).columns
            if c not in TIME_KEYS
        ]
        if numeric_cols:
            st.subheader("Descriptive Stats")
            st.dataframe(df[numeric_cols].describe().T, use_container_width=True)

            if st.checkbox("Show potential outliers (1.5×IQR)"):
                out = []
                for col in numeric_cols:
                    q1, q3 = df[col].quantile([.25, .75])
                    iqr = q3 - q1
                    lb, ub = q1 - 1.5 * iqr, q3 + 1.5 * iqr
                    out.append({
                        "Column": col,
                        "Outliers": ((df[col] < lb) | (df[col] > ub)).sum(),
                        "Lower": f"{lb:.2f}", "Upper": f"{ub:.2f}"
                    })
                st.dataframe(pd.DataFrame(out), use_container_width=True)
        else:
            st.info("No numeric columns (excluding Year/Month/Week).")

    # ======= TAB 3: Categorical =====
    with tabs[3]:
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        if cat_cols:
            st.subheader("Frequency Table")
            ccol = st.selectbox("Column", cat_cols)
            topk = st.slider("Top K", 1, 30, 10)
            freq = df[ccol].value_counts(dropna=False).head(topk)
            freq_df = (freq.rename_axis(ccol)
                       .reset_index(name="Count")
                       .assign(Percent=lambda d: d["Count"] / d["Count"].sum() * 100))
            st.dataframe(freq_df, use_container_width=True)

            if len(cat_cols) > 1 and st.checkbox("Enable cross‑tab"):
                c2 = st.selectbox("vs.", [c for c in cat_cols if c != ccol])
                ct = pd.crosstab(df[ccol], df[c2])
                st.write("Cross‑Tab (Counts)")
                st.dataframe(ct, use_container_width=True)
                if st.checkbox("Heatmap"):
                    st.plotly_chart(px.imshow(ct, text_auto=True, aspect="auto"), use_container_width=True)

        else:
            st.info("No categorical columns.")

    # ======= TAB 4: Distributions ===
    with tabs[4]:
        num_cols = [
            c for c in df.select_dtypes(include=[np.number]).columns
            if c not in TIME_KEYS
        ]
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        left, right = st.columns(2)

        with left:
            st.markdown("#### Numeric Histogram")
            ncol = st.selectbox("Numeric column", ["(None)"] + num_cols)
            if ncol != "(None)":
                fig = px.histogram(df, x=ncol, nbins=30, color_discrete_sequence=["#458EE2"])
                if st.checkbox("Log‑scale Y"):
                    fig.update_yaxes(type="log")
                st.plotly_chart(fig, use_container_width=True)

        with right:
            st.markdown("#### Categorical Bar")
            ccol1 = st.selectbox("Categorical column", ["(None)"] + cat_cols)
            if ccol1 != "(None)":
                cnt = df[ccol1].value_counts(dropna=False).reset_index()
                cnt.columns = [ccol1, "Count"]
                cnt["Percent"] = cnt["Count"] / cnt["Count"].sum() * 100
                y_axis = "Percent" if st.radio("Y‑axis", ["Count", "Percent"]) == "Percent" else "Count"
                fig_b = px.bar(cnt, x=ccol1, y=y_axis, color_discrete_sequence=["#41C185"])
                st.plotly_chart(fig_b, use_container_width=True)

    # ======= TAB 5: Correlation =====
    with tabs[5]:
        num_cols_corr = [
            c for c in df.select_dtypes(include=[np.number]).columns
            if c not in TIME_KEYS and df[c].nunique() > 1
        ]
        if len(num_cols_corr) > 1:
            method = st.selectbox("Method", ["pearson", "spearman", "kendall"])
            thresh = st.slider("Mask |ρ| < ", 0.0, 1.0, 0.0, 0.05)
            corr = df[num_cols_corr].corr(method=method)
            if thresh > 0:
                corr = corr.mask(corr.abs() < thresh)
            st.plotly_chart(px.imshow(
                corr, text_auto=True, aspect="auto",
                color_continuous_scale="RdBu",
                title=f"{method.title()} correlation (Year/Month/Week excluded)"
            ), use_container_width=True)
        else:
            st.info("Need ≥ 2 numeric columns (excluding Year/Month/Week).")

    # ======= TAB 6: Samples =========
    with tabs[6]:
        st.subheader("Sample Rows")
        n = st.slider("Rows to preview", 1, 50, 5)
        st.dataframe(df.head(n), use_container_width=True)

    # ───────── navigation buttons ───────────────────────────────
    st.markdown("---")
    col_back, col_home, col_next = st.columns(3)

    with col_back:
        if st.button("Back"):
            go_back()

    with col_home:
        if st.button("Home"):
            go_home()

    with col_next:
        if st.button("Proceed to Prepare ➜"):
            go_to("preprocess_prepare")    # or whatever key you use for the Prepare page


def prepare_page():
    import streamlit as st

    # 1) timeline & header ----------------------------------------------------
    show_timeline("1")                       # still in main step 1 (Pre‑Process)
    st.header("Prepare")
    st.markdown(
        "<p class='subheader'>Compute **Base Price** first, then refine "
        "your **Promo‑Price** clusters.</p><hr class='accent-hr'>",
        unsafe_allow_html=True
    )

    # 2) pull dataset ---------------------------------------------------------
    df = st.session_state.get("D0", None)
    if df is None or df.empty:
        st.error("No data found – run **Validate** and **Feature Overview** first.")
        return

    has_base_price = "BasePrice" in df.columns

    # 3) two expandable sections ---------------------------------------------
    with st.expander("① Base‑Price Preparation", expanded=not has_base_price):
        if has_base_price:
            st.success("`BasePrice` already present – you may skip this step.")
        st.write(
            "The Automated **Base‑Price Estimator** calculates a stable baseline "
            "price by analysing weekly transitions. "
            "If your dataset lacks a `BasePrice` column, run it first."
        )
        if st.button("Open Base‑Price Estimator ➜"):
            go_to("preprocess_base_price")         # adjust key to your estimator page
            
            
    # ------------------------------------------------------------------------
    with st.expander("② Promo‑Price Preparation", expanded=has_base_price):
        if not has_base_price:
            st.warning(
                "Add a `BasePrice` column before estimating promo depth. "
                "Complete step ① first."
            )
            st.button("Open Promo‑Depth Estimator ➜", disabled=True)
        else:
            st.write(
                "With `BasePrice` in place, you can proceed to cluster discounts, "
                "define promo bins, and save your final promo structure."
            )
            if st.button("Open Promo‑Depth Estimator ➜"):
                go_to("preprocess_promo_depth")     # adjust key to your promo page

# ───────────────────────── helper: plot base‑price ─────────────────────────
def _plot_base(week_df, agg_col, ppg_val):
    """Plot weekly price vs. computed BasePrice and highlight transitions."""
    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=week_df["WeekYear"],
        y=week_df["Price"],
        mode="lines+markers",
        name="Weekly Price",
        line=dict(color="blue")
    ))
    fig.add_trace(go.Scatter(
        x=week_df["WeekYear"],
        y=week_df["BasePrice"],
        mode="lines",
        name="Base Price",
        line=dict(color="red", dash="dash")
    ))
    for i in week_df.index[week_df["IsTransition"]]:
        fig.add_trace(go.Scatter(
            x=[week_df.at[i, "WeekYear"]],
            y=[week_df.at[i, "BasePrice"]],
            mode="markers",
            marker=dict(color="orange", size=10, symbol="diamond"),
            name="Transition"
        ))
    fig.update_layout(
        title=f"Base‑Price calculation   |   {agg_col}: {ppg_val}",
        xaxis_title="Week",
        yaxis_title="Price"
    )
    st.plotly_chart(fig, use_container_width=True)





# ══════════════════════════════════════════════════════════════╗
#  BASE‑PRICE  ESTIMATOR  –  Pre‑Process ▸ Prepare (1.1)        ║
# ══════════════════════════════════════════════════════════════╝
def base_price_page():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go

    # ── 0) timeline + header ───────────────────────────────────────────────
    show_timeline("1")                      # still inside main step 1 (Pre‑Process)
    st.subheader("📊 Automated Base‑Price Estimator")
    st.markdown("<hr class='accent-hr'>", unsafe_allow_html=True)

    # ── 1) load data ────────────────────────────────────────────────────────
    df = st.session_state.get("D0", None)
    if df is None or df.empty:
        st.error("No data – upload & validate first."); return

    if "Price" not in df.columns and {"SalesValue", "Volume"} <= set(df.columns):
        df["Price"] = np.where(df["Volume"] != 0, df["SalesValue"] / df["Volume"], np.nan)
    if "BasePrice" not in df.columns:
        df["BasePrice"] = np.nan

    # ── 2) drill‑down selections ───────────────────────────────────────────
    channel = st.selectbox("Channel", sorted(df["Channel"].dropna().unique()))
    sub_ch  = df[df["Channel"] == channel]
    if sub_ch.empty: st.warning("No rows in that channel."); return

    brand   = st.radio("Brand", sorted(sub_ch["Brand"].dropna().unique()), horizontal=True)
    sub_br  = sub_ch[sub_ch["Brand"] == brand]

    agg_cols = ["Variant", "PackType", "PackSize"]
    agg_col  = st.selectbox("Aggregator dimension", agg_cols)
    if agg_col not in sub_br.columns: st.warning(f"`{agg_col}` missing."); return
    agg_val  = st.radio(agg_col, sorted(sub_br[agg_col].dropna().unique()), horizontal=True)
    sub_agg  = sub_br[sub_br[agg_col] == agg_val]
    if sub_agg.empty: st.warning("No rows after aggregator filter."); return

    ppgs = sorted(sub_agg["PPG"].dropna().unique())
    if not ppgs: st.warning("No PPG values."); return

    # ── helper validation checks ───────────────────────────────────────────
    def validate_up(prices, cand, bp, th5, promo):
        above = (prices >= bp * (1 + th5 / 100)).sum()
        within = ((prices >= cand * 0.97) & (prices <= cand * 1.03)).sum()
        return above >= promo // 2 and within >= promo // 2

    def validate_down(prices, cand, promo=12, required=9, tol=0.02):
        if len(prices) < promo: return False
        cnt = ((prices >= cand * (1 - tol)) & (prices <= cand * (1 + tol))).sum()
        return cnt >= required

    # ── 3)  loop over PPGs ─────────────────────────────────────────────────
    for idx, ppg in enumerate(ppgs):
        block = sub_agg[sub_agg["PPG"] == ppg]
        st.markdown(f"### PPG **{ppg}**")

        # advanced parameters
        with st.expander("Advanced settings", expanded=False):
            force  = st.checkbox("Force recalculation", key=f"f{idx}")
            c1,c2,c3,c4,c5 = st.columns(5)
            roll  = c1.number_input("Rolling weeks", 4, 52, 12, 1, key=f"r{idx}")
            up_th = c2.number_input("Up % thr", 1.0, 20.0, 5.0, 0.5, key=f"u{idx}")
            dn_th = c3.number_input("Down % thr", 1.0, 20.0, 5.0, 0.5, key=f"d{idx}")
            val_w = c4.number_input("Validate weeks", 2, 18, 12, 1, key=f"v{idx}")
            perc  = c5.number_input("Percentile", 50.0, 100.0, 75.0, 5.0, key=f"p{idx}")

        # skip heavy calc if already filled
        if block["BasePrice"].notna().all() and not force:
            st.info("BasePrice already filled – skipping recalculation.")
            wk = (block.groupby(["Year","Month","Week"], as_index=False)
                        .agg(SalesValue=('SalesValue','sum'),
                             Volume=('Volume','sum'),
                             BasePrice=('BasePrice','mean')))
            wk["Price"] = wk["SalesValue"]/wk["Volume"]
            wk["WeekYear"] = wk["Year"].astype(str) + "-W" + wk["Week"].astype(str)
            wk["IsTransition"] = False
            _plot_base(wk, agg_col, ppg); continue

        # weekly aggregation for calculation
        wk = (block.groupby(["Year","Month","Week"], as_index=False)
                    .agg(SalesValue=('SalesValue','sum'), Volume=('Volume','sum')))
        wk["Price"] = wk["SalesValue"]/wk["Volume"]
        wk = wk.sort_values(["Year","Week"]).reset_index(drop=True)
        wk["WeekYear"] = wk["Year"].astype(str) + "-W" + wk["Week"].astype(str)
        if len(wk) < roll: st.warning("Not enough weeks."); continue

        price = wk["Price"].to_numpy()
        n = len(price); bp_arr = np.empty(n); trans = []
        cur_bp = np.percentile(price[:roll], perc); last_t = -roll

        for i in range(n):
            cur = price[i]; fut = price[i:i+val_w]
            if len(fut) < val_w: bp_arr[i] = cur_bp; continue
            up = False
            if cur >= cur_bp*(1+up_th/100) and i-last_t >= roll and validate_up(fut, cur, cur_bp, up_th, val_w):
                cur_bp = max(np.percentile(fut, perc), cur); trans.append(i); last_t = i; up = True
            if not up and cur <= cur_bp*(1-dn_th/100) and i-last_t >= roll and validate_down(fut, cur, val_w):
                cur_bp = min(np.percentile(fut, perc), cur); trans.append(i); last_t = i
            bp_arr[i] = cur_bp

        wk["BasePrice"] = bp_arr
        wk["IsTransition"] = wk.index.isin(trans)
        _plot_base(wk, agg_col, ppg)

        # per‑PPG save
        if st.button(f"Save {brand}/{agg_val}/{ppg}", key=f"s{idx}"):
            for _, row in wk.iterrows():
                m = ((df["Channel"] == channel) & (df["Brand"] == brand) &
                     (df[agg_col] == agg_val) & (df["PPG"] == ppg) &
                     (df["Year"] == row["Year"]) & (df["Month"] == row["Month"]) &
                     (df["Week"] == row["Week"]))
                df.loc[m, "BasePrice"] = row["BasePrice"]
            st.success("BasePrice saved.")

    # ── 4)  batch “Save ALL” ───────────────────────────────────────────────
    if st.button("Save ALL Base Prices"):
        updated = df.copy()
        agg_options = ["Variant","PackType","PackSize"]

        for ch in updated["Channel"].dropna().unique():
            ch_df = updated[updated["Channel"] == ch]
            for br in ch_df["Brand"].dropna().unique():
                br_df = ch_df[ch_df["Brand"] == br]
                for ac in agg_options:
                    if ac not in br_df.columns: continue
                    for aval in br_df[ac].dropna().unique():
                        a_df = br_df[br_df[ac] == aval]
                        for ppg in a_df["PPG"].dropna().unique():
                            filt = a_df[a_df["PPG"] == ppg]
                            if filt.empty: continue

                            wk = (filt.groupby(["Year","Month","Week"], as_index=False)
                                        .agg(SalesValue=('SalesValue','sum'),
                                             Volume=('Volume','sum')))
                            wk["Price"] = wk["SalesValue"] / wk["Volume"]
                            wk = wk.sort_values(["Year","Week"]).reset_index(drop=True)
                            if len(wk) < 12: continue

                            pa = wk["Price"].to_numpy()
                            n = len(pa); bp = np.empty(n)
                            cur = np.percentile(pa[:12], 75); last = -12
                            for i in range(n):
                                cu = pa[i]; fut = pa[i:i+12]; up = False
                                if cu >= cur*1.05 and i-last >= 12 and validate_up(fut, cu, cur, 5, 12):
                                    cur = max(np.percentile(fut, 75), cu); last = i; up = True
                                elif not up and cu <= cur*0.95 and i-last >= 12 and validate_down(fut, cu):
                                    cur = min(np.percentile(fut, 75), cu); last = i
                                bp[i] = cur
                            wk["BasePrice"] = bp

                            for _, row in wk.iterrows():
                                m = ((updated["Channel"] == ch) & (updated["Brand"] == br) &
                                     (updated[ac] == aval) & (updated["PPG"] == ppg) &
                                     (updated["Year"] == row["Year"]) & (updated["Month"] == row["Month"]) &
                                     (updated["Week"] == row["Week"]))
                                updated.loc[m & updated["BasePrice"].isna(), "BasePrice"] = row["BasePrice"]

        df = updated
        st.session_state["D0"] = df
        # ── add this line to also persist into dataframe1 ──
        st.session_state["dataframe1"] = df.copy()
        st.success("✅ All missing BasePrices calculated & updated.")
        st.download_button("📥 Download updated CSV",
                           df.to_csv(index=False), "updated_dataset_baseprice.csv")

    # persist current df back
    st.session_state["D0"] = df

    # ── 5) navigation ───────────────────────────────────────────────
    st.markdown("---")
    col_back, col_home = st.columns(2)
    with col_back:
        if st.button("Back"):
            go_back()
    with col_home:
        if st.button("Home"):
            go_home()


# ───────────────────────── helper plot ─────────────────────────
def _plot_base(week_df, agg_col, ppg_val):
    """Plot weekly price vs BasePrice with transition markers."""
    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=week_df["WeekYear"], y=week_df["Price"],
        mode="lines+markers", name="Weekly Price", line=dict(color="blue")
    ))
    fig.add_trace(go.Scatter(
        x=week_df["WeekYear"], y=week_df["BasePrice"],
        mode="lines", name="Base Price", line=dict(color="red", dash="dash")
    ))
    for i in week_df.index[week_df["IsTransition"]]:
        fig.add_trace(go.Scatter(
            x=[week_df.at[i, "WeekYear"]],
            y=[week_df.at[i, "BasePrice"]],
            mode="markers",
            marker=dict(color="orange", size=10, symbol="diamond"),
            name="Transition"
        ))
    fig.update_layout(
        title=f"Base‑Price | {agg_col}: {ppg_val}",
        xaxis_title="Week",
        yaxis_title="Price"
    )
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════╗
#  PROMO‑DEPTH  ESTIMATOR  –  Pre‑Process ▸ Prepare (1.2)       ║
# ══════════════════════════════════════════════════════════════╝
def promo_depth_page():

    # This heading replaces any existing placeholder heading you had before.
    st.subheader("📉 Automatic Promo Depth Estimator")

    # Retrieve the main DataFrame from session state (saved by the File Management section)
    dataframe = st.session_state.get("D0", None)

    # -----------
    #  MAIN LOGIC
    # -----------
    import math
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    # Utility function for elbow detection:
    def find_elbow_k(k_values, inertias):
        x1, y1 = k_values[0], inertias[0]
        x2, y2 = k_values[-1], inertias[-1]
        line_len = math.dist((x1, y1), (x2, y2))
        if line_len == 0:
            return k_values[0]
        distances = []
        for i, k_val in enumerate(k_values):
            x0, y0 = k_val, inertias[i]
            # Perpendicular distance from point (x0,y0) to line (x1,y1)->(x2,y2)
            num = abs((y2 - y1)*x0 - (x2 - x1)*y0 + x2*y1 - y2*x1)
            distances.append(num / line_len)
        return k_values[np.argmax(distances)]

    # Check for mandatory columns in your data: BasePrice and Price
    def has_required_columns(df_check):
        return ("BasePrice" in df_check.columns) and ("Price" in df_check.columns)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    # Choose source: try dataframe1 before D0
    # ---------------------------------------------------------------------
    df1 = st.session_state.get("dataframe1", None)
    df0 = st.session_state.get("D0",      None)

    if df1 is not None and has_required_columns(df1):
        df = df1.copy()
        st.write("Using `dataframe1` for promo_depth (it has BasePrice & Price).")
    elif df0 is not None and has_required_columns(df0):
        df = df0.copy()
        st.write("Using `st.session_state['D0']` for promo_depth.")
    else:
        st.error(
            "Neither `dataframe1` nor `D0` contain both "
            "`BasePrice` and `Price`. Please ensure you ran the Base Price step."
        )
        st.stop()


    # ------------------------------------------------
    # SECTION A: Channel, Brand, Aggregator, PPG, etc.
    # ------------------------------------------------
    col1, col2 = st.columns([1, 2])
    with col1:
        channel_selected = st.selectbox(
            "Select Channel",
            sorted(df["Channel"].dropna().unique()),
            key="depth_channel"
        )
    channel_data = df[df["Channel"] == channel_selected]

    with col2:
        brand_list = sorted(channel_data["Brand"].dropna().unique())
        brand_selected = st.radio(
            "Select Brand",
            options=brand_list,
            horizontal=True,
            key="depth_brand"
        )
    brand_data = channel_data[channel_data["Brand"] == brand_selected]

    aggregator_options = ["Variant", "PackType", "PackSize"]
    aggregator_col = st.selectbox(
        "Select Aggregator Dimension",
        aggregator_options,
        key="depth_aggregator"
    )
    if aggregator_col not in brand_data.columns:
        st.warning(f"Column '{aggregator_col}' not found in the data.")
        st.stop()

    # If you saved an aggregator value from the Base Price page, you could re-use it:
    if "aggregator_selected" in st.session_state:
        aggregator_selected = st.session_state["aggregator_selected"]
        st.write(f"Using aggregator: **{aggregator_selected}** from session state.")
    else:
        aggregator_selected = st.selectbox(
            "Select Aggregator Value",
            sorted(brand_data[aggregator_col].dropna().unique()),
            key="depth_aggregator_value"
        )
    aggregator_data = brand_data[brand_data[aggregator_col] == aggregator_selected]

    # PPG selection
    ppg_choices = sorted(aggregator_data["PPG"].dropna().unique())
    ppg_selected = st.selectbox("Select PPG", ppg_choices, key="depth_ppg")
    subset = aggregator_data[aggregator_data["PPG"] == ppg_selected]
    if subset.empty:
        st.warning("No data found for this combination.")
        st.stop()

    # Frequency (Daily vs. Weekly)
    agg_freq = st.radio(
        "Select Aggregation Frequency for Promo Depth",
        options=["Daily", "Weekly"],
        index=1,
        key="promo_agg_freq"
    )

    # Define grouping columns based on frequency
    if agg_freq == "Daily":
        if "Day" not in subset.columns:
            # If there's a Date column, use that
            if "Date" in subset.columns:
                subset["Day"] = pd.to_datetime(subset["Date"], errors="coerce").dt.date
            else:
                # Fallback: parse from index or show error
                st.warning("No 'Date' column found. Cannot aggregate daily.")
                st.stop()
        grouping_cols = ["Day"]
    else:
        # Weekly => group by Year, Week (and Month if present)
        grouping_cols = ["Year", "Week"]
        if "Month" in subset.columns:
            grouping_cols = ["Year", "Month", "Week"]

    # -------------------------------------
    # 2) Aggregate WITHOUT recomputing Price
    # -------------------------------------
    agg_data = subset.groupby(grouping_cols, as_index=False).agg(
        {
            "SalesValue": "sum",
            "Volume": "sum",
            "Price": "mean",       # Price must already be in your DF
            "BasePrice": "mean"    # BasePrice must already be in your DF
        }
    )

    # Compute PromoDepth
    agg_data["PromoDepth"] = (agg_data["BasePrice"] - agg_data["Price"]) / agg_data["BasePrice"]
    agg_data["PromoDepth"] = agg_data["PromoDepth"].clip(0, 1)

    # Create a time axis label
    if agg_freq == "Weekly":
        if "Month" in agg_data.columns:
            agg_data["WeekStartDate"] = pd.to_datetime(
                agg_data["Year"].astype(str)
                + agg_data["Week"].astype(str).str.zfill(2)
                + "1",
                format="%G%V%u",
                errors="coerce"
            )
        else:
            agg_data["WeekStartDate"] = pd.to_datetime(
                agg_data["Year"].astype(str)
                + agg_data["Week"].astype(str).str.zfill(2)
                + "1",
                format="%G%V%u",
                errors="coerce"
            )
        agg_data.dropna(subset=["WeekStartDate"], inplace=True)
        agg_data.sort_values("WeekStartDate", inplace=True)
        agg_data["TimeLabel"] = agg_data["WeekStartDate"].dt.strftime("%Y-W%V")
    else:
        agg_data["Day"] = pd.to_datetime(agg_data["Day"], errors="coerce")
        agg_data.dropna(subset=["Day"], inplace=True)
        agg_data.sort_values("Day", inplace=True)
        agg_data["TimeLabel"] = agg_data["Day"].dt.strftime("%Y-%m-%d")

    st.write(f"**{len(agg_data)}** rows after aggregation using {agg_freq} frequency.")
    st.markdown("<hr style='border:2px solid black'/>", unsafe_allow_html=True)

    # ------------------------------------------------
    # SECTION B: K-Means & Bin Range Definition
    # ------------------------------------------------
    st.subheader("B) K-Means on Discounted Rows & Bin Range Definition")
    df_discounts = agg_data[agg_data["PromoDepth"] > 0].copy()
    if df_discounts.empty:
        st.info("No discount found (Price >= BasePrice). Nothing to cluster.")
        st.stop()

    # Prepare data for elbow method
    X = df_discounts["PromoDepth"].values.reshape(-1, 1)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    k_candidates = range(1, min(8, len(X_scaled) + 1))
    inertias = []
    for k in k_candidates:
        km_test = KMeans(n_clusters=k, random_state=42)
        km_test.fit(X_scaled)
        inertias.append(km_test.inertia_)

    rec_k = find_elbow_k(list(k_candidates), inertias)

    col_left, col_right = st.columns(2)
    with col_left:
        fig_elbow = go.Figure()
        fig_elbow.add_trace(go.Scatter(x=list(k_candidates), y=inertias, mode="lines+markers"))
        fig_elbow.update_layout(title="Elbow Plot", xaxis_title="k", yaxis_title="Inertia")
        st.plotly_chart(fig_elbow, use_container_width=True)

    with col_right:
        st.info(f"Recommended k = {rec_k}")
        chosen_k = st.number_input(
            "Final # Clusters (k):",
            min_value=1,
            max_value=7,
            value=int(rec_k),
            step=1
        )

        # Run K-Means
        km = KMeans(n_clusters=chosen_k, random_state=42)
        km.fit(X_scaled)
        df_discounts["ClusterID"] = km.labels_

        # Summaries
        count_label = "NumDays" if agg_freq == "Daily" else "NumWeeks"
        summary = df_discounts.groupby("ClusterID", as_index=False).agg(
            **{
                count_label: ("PromoDepth", "count"),
                "AvgDepth": ("PromoDepth", "mean"),
                "MinDepth": ("PromoDepth", "min"),
                "MaxDepth": ("PromoDepth", "max")
            }
        )
        summary[["AvgDepth", "MinDepth", "MaxDepth"]] *= 100
        st.dataframe(summary)

        # Generate auto-bins from cluster centers
        centers_scaled = km.cluster_centers_
        centers_real = scaler.inverse_transform(centers_scaled).flatten()
        centers_real = np.clip(centers_real, 0, 1)

        # Sort cluster centers and build bin boundaries
        sorted_pairs = sorted(dict(enumerate(centers_real)).items(), key=lambda x: x[1])
        def midpoint(a, b):
            return (a + b) / 2

        auto_bins = []
        for i in range(len(sorted_pairs)):
            cid, cval = sorted_pairs[i]
            left = 0.0 if i == 0 else midpoint(sorted_pairs[i-1][1], cval)
            right = 1.0 if i == len(sorted_pairs) - 1 else midpoint(cval, sorted_pairs[i+1][1])
            auto_bins.append({
                "ClusterID": cid,
                "name": f"Promo{i+1}",
                "min": round(left * 100, 2),
                "max": round(right * 100, 2),
                "centroid": round(cval * 100, 2)
            })

        # Key for storing bin definitions
        current_config_key = (channel_selected, brand_selected, aggregator_selected, ppg_selected)

        if "saved_bins_current" not in st.session_state:
            st.session_state["saved_bins_current"] = {}
        if "old_chosen_k" not in st.session_state:
            st.session_state["old_chosen_k"] = {}

        # Retrieve or initialize the bins for this combo
        existing = st.session_state["saved_bins_current"].get(current_config_key, None)
        if existing is None:
            st.session_state["saved_bins_current"][current_config_key] = {"bins": auto_bins}
            existing = st.session_state["saved_bins_current"][current_config_key]
        else:
            # If we have bins already and the user changed k, overwrite with new auto-bins
            old_k = st.session_state["old_chosen_k"].get(current_config_key, None)
            if old_k != chosen_k:
                existing["bins"] = auto_bins

        st.session_state["old_chosen_k"][current_config_key] = chosen_k

        # Let user edit bins
        current_data = existing
        new_defs = []
        with st.expander("Define & Edit Bin Ranges (Min% .. Max%)", expanded=True):
            for cdef in current_data["bins"]:
                cid = cdef["ClusterID"]
                colA, colB, colC, colD = st.columns([1.5, 1, 1, 1])
                name_in = colA.text_input(
                    f"Name (Cluster {cid})",
                    cdef["name"],
                    key=f"cname_{current_config_key}_{cid}"
                )
                min_in = colB.text_input(
                    "Min%",
                    str(cdef["min"]),
                    key=f"cmin_{current_config_key}_{cid}"
                )
                max_in = colC.text_input(
                    "Max%",
                    str(cdef["max"]),
                    key=f"cmax_{current_config_key}_{cid}"
                )
                try:
                    cent_val = round((float(min_in) + float(max_in)) / 2, 2)
                except ValueError:
                    cent_val = cdef["centroid"]
                colD.write(f"Centroid: {cent_val}")

                new_defs.append({
                    "ClusterID": cid,
                    "name": name_in,
                    "min": min_in,
                    "max": max_in,
                    "centroid": cent_val
                })

        def build_final_bins(ch, br, agg_val, pp, bin_list):
            out = []
            for item in bin_list:
                out.append({
                    "ClusterID": item["ClusterID"],
                    "Channel": ch,
                    "Brand": br,
                    "Aggregator": agg_val,  
                    "PPG": pp,
                    "Min": item["min"],
                    "Max": item["max"],
                    "Centroid": item["centroid"],
                    "ClusterName": f"{br}_{agg_val}_{pp}_Promo{item['ClusterID']+1}"
                })
            return out

        if "final_clusters_depth" not in st.session_state:
            st.session_state["final_clusters_depth"] = {}

        if st.button("Save & Update Bin Ranges"):
            try:
                for nd in new_defs:
                    mn = float(nd["min"])
                    mx = float(nd["max"])
                    nd["min"] = round(mn, 2)
                    nd["max"] = round(mx, 2)
                    nd["centroid"] = round((mn + mx) / 2, 2)
                current_data["bins"] = new_defs
                st.success("Manual bins updated.")

                final_bin_defs = build_final_bins(
                    channel_selected,
                    brand_selected,
                    aggregator_selected,
                    ppg_selected,
                    new_defs
                )
                st.session_state["final_clusters_depth"][current_config_key] = final_bin_defs
            except Exception as e:
                st.error(f"Error updating bins: {e}")

        # Assign each discounted row to a bin
        def assign_bin(row):
            discount_pct = row["PromoDepth"] * 100
            for b in current_data["bins"]:
                if b["min"] <= discount_pct <= b["max"]:
                    return b["name"]
            return None

        df_discounts["PromoBin"] = df_discounts.apply(assign_bin, axis=1)
        df_discounts = df_discounts[df_discounts["PromoBin"].notnull()]

        bin_names = [b["name"] for b in current_data["bins"]]
        color_cycle = px.colors.qualitative.Set2
        bin_color_map = {n: color_cycle[i % len(color_cycle)] for i, n in enumerate(bin_names)}

    # ------------------------------------------------
    # SECTION B.2: Raw Cluster Plot (Discount% vs. Time)
    # ------------------------------------------------
    st.subheader("B.2) Raw Cluster Plot (Discount% vs. Time)")

    if "rawcluster_toggle" not in st.session_state:
        st.session_state["rawcluster_toggle"] = False

    if st.button("Toggle Sort (Time vs. Asc. Discount)", key="raw_cluster_button"):
        st.session_state["rawcluster_toggle"] = not st.session_state["rawcluster_toggle"]

    cluster_data = df_discounts.copy()
    if st.session_state["rawcluster_toggle"]:
        cluster_data = cluster_data.sort_values("PromoDepth").reset_index(drop=True)
        cluster_data["Xaxis"] = cluster_data.index + 1
        x_label = "Sorted by Discount"
        tickvals, ticktext = None, None
    else:
        agg_sorted = agg_data.sort_values("TimeLabel").reset_index(drop=True)
        agg_sorted["Xaxis"] = agg_sorted.index + 1
        lab_map = {row["TimeLabel"]: row["Xaxis"] for _, row in agg_sorted.iterrows()}

        cluster_data = cluster_data.sort_values("TimeLabel").reset_index(drop=True)
        cluster_data["Xaxis"] = cluster_data["TimeLabel"].map(lab_map)
        x_label = "Time"
        tickvals = list(lab_map.values())
        ticktext = list(lab_map.keys())

    cluster_data["Discount%"] = cluster_data["PromoDepth"] * 100
    fig_raw = px.scatter(
        cluster_data,
        x="Xaxis",
        y="Discount%",
        color="PromoBin",
        title="Raw Cluster Plot: Discount% vs. Time",
        labels={"Xaxis": x_label, "Discount%": "Discount(%)", "PromoBin": "Bin"},
        hover_data=["Price", "BasePrice"]
    )
    if tickvals and ticktext:
        fig_raw.update_layout(xaxis=dict(tickmode="array", tickvals=tickvals, ticktext=ticktext))

    for b in current_data["bins"]:
        bname = b["name"]
        cent = b["centroid"]
        sub = cluster_data[cluster_data["PromoBin"] == bname]
        if not sub.empty:
            median_x = sub["Xaxis"].median()
            fig_raw.add_trace(go.Scatter(
                x=[median_x],
                y=[cent],
                mode="markers",
                marker=dict(color=bin_color_map.get(bname, "gray"), symbol="diamond", size=12),
                name=f"Centroid {bname} ({cent}%)"
            ))

    st.plotly_chart(fig_raw, use_container_width=True)
    st.markdown("<hr style='border:2px solid black'/>", unsafe_allow_html=True)

    # ------------------------------------------------
    # SECTION C: Final Table, Bar Chart & Final Promo Plot
    # ------------------------------------------------
    st.subheader("C) Final Table, Bar Chart & Final Promo Plot")
    if agg_freq == "Daily":
        count_label = "NumDays"
        vol_label = "VolPerDay"
    else:
        count_label = "NumWeeks"
        vol_label = "VolPerWeek"

    vol_summary = df_discounts.groupby("PromoBin", as_index=False).agg(
        **{
            count_label: ("PromoBin", "count"),
            "TotalVol": ("Volume", "sum")
        }
    )
    vol_summary[vol_label] = vol_summary["TotalVol"] / vol_summary[count_label].replace(0, np.nan)
    totalV = vol_summary["TotalVol"].sum()
    vol_summary["VolShare%"] = (vol_summary["TotalVol"] / totalV * 100) if totalV > 0 else 0
    vol_summary.sort_values(vol_label, ascending=False, inplace=True)
    vol_summary.reset_index(drop=True, inplace=True)

    bins_df = pd.DataFrame(current_data["bins"])
    merged_table = pd.merge(vol_summary, bins_df, left_on="PromoBin", right_on="name", how="left")
    merged_table = merged_table[["PromoBin", count_label, "max", "TotalVol", vol_label, "VolShare%"]]

    def color_promo(val):
        return f"background-color: {bin_color_map.get(val, '#ffffff')}; color: white; font-weight: bold;"

    st.markdown(f"#### Combined Table (Sorted by {vol_label} DESC)")
    st.table(merged_table.style.applymap(color_promo, subset=["PromoBin"]))

    fig_bar = px.bar(
        vol_summary,
        x="PromoBin",
        y=vol_label,
        title=f"Volume per {'Day' if agg_freq == 'Daily' else 'Week'} by Bin (Descending)",
        labels={
            "PromoBin": "Bin",
            vol_label: f"Volume per {'Day' if agg_freq=='Daily' else 'Week'}"
        },
        color="PromoBin",
        color_discrete_map=bin_color_map
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    chosen_bins = st.multiselect(
        "Choose bins to highlight in final chart:",
        sorted(df_discounts["PromoBin"].unique()),
        default=sorted(df_discounts["PromoBin"].unique())
    )
    if "promo_plot_toggle" not in st.session_state:
        st.session_state["promo_plot_toggle"] = False
    if st.button("Toggle X-axis (Time vs. Asc. Discount)", key="promo_plot_button"):
        st.session_state["promo_plot_toggle"] = not st.session_state["promo_plot_toggle"]

    if st.session_state["promo_plot_toggle"]:
        chart_data = agg_data.sort_values("PromoDepth").reset_index(drop=True)
        chart_data["Xaxis"] = chart_data.index + 1
        x_label = "Sorted by Discount"
        tickvals, ticktext = None, None
    else:
        if agg_freq == "Weekly":
            chart_data = agg_data.sort_values("WeekStartDate").reset_index(drop=True)
        else:
            chart_data = agg_data.sort_values("Day").reset_index(drop=True)
        chart_data["Xaxis"] = chart_data.index + 1
        x_label = "Time"
        tickvals = chart_data["Xaxis"].tolist()
        ticktext = chart_data["TimeLabel"].tolist()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=chart_data["Xaxis"],
        y=chart_data["Price"],
        mode="lines+markers",
        name="Price",
        line=dict(color="blue"),
        marker=dict(color="blue", size=4),
        customdata=np.stack([chart_data["BasePrice"], chart_data["PromoDepth"]], axis=-1),
        hovertemplate=(
            "<b>Price:</b> %{y:.2f}<br>"
            "<b>BasePrice:</b> %{customdata[0]:.2f}<br>"
            "<b>Depth:</b> %{customdata[1]:.1%}"
        )
    ))
    fig.add_trace(go.Scatter(
        x=chart_data["Xaxis"],
        y=chart_data["BasePrice"],
        mode="lines",
        name="BasePrice",
        line=dict(color="red", dash="dot"),
        hoverinfo="skip"
    ))

    if tickvals and ticktext:
        fig.update_layout(xaxis=dict(tickmode="array", tickvals=tickvals, ticktext=ticktext))

    disc_plot = df_discounts[df_discounts["PromoBin"].isin(chosen_bins)].copy()
    if st.session_state["promo_plot_toggle"]:
        disc_plot = disc_plot.sort_values("PromoDepth").reset_index(drop=True)
        disc_plot["Xaxis"] = disc_plot.index + 1
    else:
        if agg_freq == "Weekly":
            disc_plot = disc_plot.sort_values("WeekStartDate").reset_index(drop=True)
        else:
            disc_plot = disc_plot.sort_values("Day").reset_index(drop=True)
        disc_plot["Xaxis"] = disc_plot["TimeLabel"].map({row["TimeLabel"]: row["Xaxis"] for _, row in chart_data.iterrows()})

    for bname in chosen_bins:
        sub = disc_plot[disc_plot["PromoBin"] == bname]
        fig.add_trace(go.Scatter(
            x=sub["Xaxis"],
            y=sub["Price"],
            mode="markers",
            name=bname,
            marker=dict(color=bin_color_map.get(bname, "gray"), size=8),
            customdata=np.stack([sub["BasePrice"], sub["PromoDepth"]], axis=-1),
            hovertemplate=(
                f"<b>Bin:</b> {bname}<br><b>Price:</b> %{{y:.2f}}<br>"
                f"<b>BasePrice:</b> %{{customdata[0]:.2f}}<br>"
                f"<b>Depth:</b> %{{customdata[1]:.1%}}"
            )
        ))

    fig.update_layout(
        title="Final Promo Plot: Price vs BasePrice (Markers by Bin)",
        xaxis_title=x_label,
        yaxis_title="Price",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------
    # SECTION D: FINAL SAVE (Auto-Generate Only for Unedited Combos)
    # ------------------------------------------------
    st.markdown("<hr style='border:2px solid black'/>", unsafe_allow_html=True)
    st.subheader("Final Save (Auto-Generate Only for Unedited Combos)")

    if st.button("FINAL SAVE (All Configurations)"):
        final_clusters = st.session_state.get("final_clusters_depth", {})
        for ch in df["Channel"].dropna().unique():
            ch_df = df[df["Channel"] == ch]
            for br in ch_df["Brand"].dropna().unique():
                br_df = ch_df[ch_df["Brand"] == br]
                for agg_col2 in aggregator_options:
                    if agg_col2 not in br_df.columns:
                        continue
                    for agg_val2 in br_df[agg_col2].dropna().unique():
                        agg_df2 = br_df[br_df[agg_col2] == agg_val2]
                        for pp in agg_df2["PPG"].dropna().unique():
                            key = (ch, br, agg_val2, pp)
                            if key in final_clusters:
                                st.info(f"Skipping {key} (already in final clusters).")
                                continue
                            sub_df = agg_df2[agg_df2["PPG"] == pp]
                            if sub_df.empty:
                                continue

                            # Adjust grouping for daily vs. weekly
                            if agg_freq == "Daily":
                                if "Day" not in sub_df.columns:
                                    if "Date" in sub_df.columns:
                                        sub_df["Day"] = pd.to_datetime(sub_df["Date"], errors="coerce").dt.date
                                    else:
                                        st.warning("Daily grouping requires a 'Date' column. Skipping this subset.")
                                        continue
                                grouping_cols2 = ["Day"]
                            else:
                                if "Month" in sub_df.columns:
                                    grouping_cols2 = ["Year", "Month", "Week"]
                                else:
                                    grouping_cols2 = ["Year", "Week"]

                            # Group the same way, but do NOT recompute Price
                            w_agg = sub_df.groupby(grouping_cols2, as_index=False).agg(
                                {
                                    "SalesValue": "sum",
                                    "Volume": "sum",
                                    "Price": "mean",
                                    "BasePrice": "mean"
                                }
                            )
                            w_agg["PromoDepth"] = (w_agg["BasePrice"] - w_agg["Price"]) / w_agg["BasePrice"]
                            w_agg["PromoDepth"] = w_agg["PromoDepth"].clip(0, 1)

                            disc = w_agg[w_agg["PromoDepth"] > 0].copy()
                            if disc.empty:
                                continue

                            X_c = disc["PromoDepth"].values.reshape(-1, 1)
                            sc_c = StandardScaler()
                            X_sc = sc_c.fit_transform(X_c)

                            cands = range(1, min(7, len(X_sc)) + 1)
                            inert_list = []
                            for ck in cands:
                                tmp_km = KMeans(n_clusters=ck, random_state=42)
                                tmp_km.fit(X_sc)
                                inert_list.append(tmp_km.inertia_)
                            best_k2 = find_elbow_k(list(cands), inert_list)

                            auto_km = KMeans(n_clusters=best_k2, random_state=42)
                            auto_km.fit(X_sc)
                            disc["ClusterID"] = auto_km.labels_

                            sc_centers = auto_km.cluster_centers_
                            real_centers = sc_c.inverse_transform(sc_centers).flatten()
                            real_centers = np.clip(real_centers, 0, 1)

                            sorted_enumer = sorted(dict(enumerate(real_centers)).items(), key=lambda x: x[1])
                            def midpoint(a, b):
                                return (a + b) / 2
                            auto_binlist = []
                            for i2 in range(len(sorted_enumer)):
                                cid, cval = sorted_enumer[i2]
                                left = 0.0 if i2 == 0 else midpoint(sorted_enumer[i2-1][1], cval)
                                right = 1.0 if i2 == len(sorted_enumer)-1 else midpoint(cval, sorted_enumer[i2+1][1])
                                auto_binlist.append({
                                    "ClusterID": cid,
                                    "Channel": ch,
                                    "Brand": br,
                                    "PPG": pp,
                                    "Aggregator": agg_val2,
                                    "Min": round(left * 100, 2),
                                    "Max": round(right * 100, 2),
                                    "Centroid": round(cval * 100, 2),
                                    "ClusterName": f"{br}_{agg_val2}_{pp}_Promo{i2+1}"
                                })

                            def build_final_bins(ch2, br2, agg_vv, pp2, bin_list):
                                out2 = []
                                for item in bin_list:
                                    out2.append({
                                        "ClusterID": item["ClusterID"],
                                        "Channel": ch2,
                                        "Brand": br2,
                                        "Aggregator": agg_vv,
                                        "PPG": pp2,
                                        "Min": item["Min"],
                                        "Max": item["Max"],
                                        "Centroid": item["Centroid"],
                                        "ClusterName": item["ClusterName"]
                                    })
                                return out2

                            final_bin_defs = build_final_bins(ch, br, agg_val2, pp, auto_binlist)
                            final_clusters[key] = final_bin_defs

        st.session_state["final_clusters_depth"] = final_clusters
        st.success("✅ Final Save done for all unedited combos. Manual combos remain intact.")

    st.subheader("Download Saved Clusters (All Combos)")
    final_data = st.session_state.get("final_clusters_depth", {})
    if final_data and isinstance(final_data, dict):
        all_c = []
        for combo, bins_list in final_data.items():
            all_c.extend(bins_list)
        if all_c:
            df_clusters = pd.DataFrame(all_c)
            desired_order = [
                "Channel", "Brand", "Aggregator", "PPG",
                "ClusterID", "Min", "Max", "Centroid", "ClusterName"
            ]
            df_clusters = df_clusters.reindex(columns=desired_order)
            st.dataframe(df_clusters)
            csv_data = df_clusters.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Clusters as CSV",
                data=csv_data,
                file_name="promo_clusters.csv",
                mime="text/csv"
            )
        else:
            st.info("No combos have final clusters. Manually edit or do final save.")
    else:
        st.info("No final clusters so far. Manually edit or do final save first.")

    # ------------------------------------------------
    # SECTION E: Download Updated Aggregated Dataset (Current Combo)
    # ------------------------------------------------
    st.markdown("<hr style='border:2px solid black'/>", unsafe_allow_html=True)
    st.subheader("Download Updated Aggregated Dataset (Current Combo)")

    agg_final = agg_data.copy()
    agg_final["PromoName"] = "No Promo"
    agg_final["PromoMin"] = 0
    agg_final["PromoMax"] = 0

    current_data = st.session_state["saved_bins_current"].get(
        (channel_selected, brand_selected, aggregator_selected, ppg_selected), {}
    )
    if not df_discounts.empty and current_data.get("bins"):
        bin_map = {b["name"]: (b["min"], b["max"]) for b in current_data["bins"]}
        agg_final.loc[df_discounts.index, "PromoName"] = df_discounts["PromoBin"]
        for idx in df_discounts.index:
            bin_name = df_discounts.loc[idx, "PromoBin"]
            if bin_name in bin_map:
                agg_final.loc[idx, "PromoMin"] = bin_map[bin_name][0]
                agg_final.loc[idx, "PromoMax"] = bin_map[bin_name][1]

    csv_final = agg_final.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Updated Aggregated Dataset (Current Combo)",
        data=csv_final,
        file_name="updated_aggregated_dataset.csv",
        mime="text/csv"
    )

    if st.button("Clear All Saved Clusters"):
        if "final_clusters_depth" in st.session_state:
            st.session_state["final_clusters_depth"] = {}
            st.success("All saved clusters have been cleared.")
        else:
            st.info("No saved clusters found.")


    # ===== navigation =====
    st.markdown("---")
    col_back,col_home = st.columns(2)
    with col_back:
        if st.button("Back", key="pd_nav_back"):
            go_back()
    with col_home:
        if st.button("Home", key="pd_nav_home"):
            go_home()



#####################################################################Explore1


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------------------------------------------------
# Market Construct Page
# -----------------------------------------------------------------------

def market_construct_page():
    # 1) Retrieve Data
    df = st.session_state.get("D0", None)
    if df is None or df.empty:
        st.warning("No data uploaded yet. Please upload a file in the sidebar.")
        st.stop()

    # 1a) Remove any rows where Brand == "cat1"
    if "Brand" in df.columns:
        df = df[df["Brand"] != "cat1"]

    # 2) Prepare Options
    def sorted_or_all(col):
        return ["All"] + sorted(df[col].unique()) if col in df.columns else ["All"]

    market_options   = sorted_or_all("Market")
    channel_options  = sorted_or_all("Channel")
    metric_options   = ["MS Value", "Volume", "Price", "MS Volume"]
    time_options     = ["Weekly", "Monthly", "Yearly"]
    brand_options    = sorted_or_all("Brand")
    variant_options  = sorted_or_all("Variant")
    packtype_options = sorted_or_all("PackType")
    ppg_options      = sorted_or_all("PPG")

    # Wrap long radio sets
    max_len = max(len(brand_options), len(variant_options), len(packtype_options), len(ppg_options))
    if max_len > 5:
        st.markdown(
            """
            <style>
            div[data-baseweb="radio"] > div { display: flex !important; flex-wrap: wrap !important; }
            div[data-baseweb="radio"] label { margin: .5rem 1rem .5rem 0; }
            </style>
            """, unsafe_allow_html=True)

    # 3) Custom CSS
    st.markdown("""
    <style>
    .stApp { background-color: #F5F5F5; }
    .custom-header { font-family: 'Inter'; font-size:36px; font-weight:600; color:#333; }
    .accent-hr { border:0; height:2px; background:linear-gradient(to right,#FFBD59,#FFC87A); margin:1rem 0; }
    div[data-testid="stHorizontalBlock"] button { background-color:#FFBD59!important; color:#333!important; font-weight:600!important; border:none!important; border-radius:4px!important; margin-bottom:0.5rem; }
    div[data-testid="stHorizontalBlock"] button:hover { background-color:#FFC87A!important; }
    </style>
    """, unsafe_allow_html=True)

    # 4) Header
    st.markdown('<h1 class="custom-header">Market Construct</h1>', unsafe_allow_html=True)

    # 5) Filter UI in two columns
    left_col, right_col = st.columns([2,3])
    with right_col:
        mc1, mc2 = st.columns(2)
        with mc1:
            st.markdown("##### Market")
            chosen_market  = st.selectbox("", market_options)
        with mc2:
            st.markdown("##### Channel")
            chosen_channel = st.selectbox("", channel_options)

        st.markdown("##### Metric & Time")
        mt1, mt2 = st.columns(2)
        with mt1:
            chosen_metric = st.radio("Metric:", metric_options, horizontal=True)
        with mt2:
            chosen_time   = st.radio("Time:", time_options, horizontal=True)

    with left_col:
        st.markdown("##### Product Filters")
        p1, p2, p3, p4 = st.columns(4)
        with p1:
            chosen_brand     = st.radio("Brand:", brand_options, index=0, horizontal=True)
        with p2:
            chosen_variant   = st.radio("Variant:", variant_options, index=0, horizontal=True)
        with p3:
            chosen_packtype  = st.radio("PackType:", packtype_options, index=0, horizontal=True)
        with p4:
            chosen_ppg       = st.radio("PPG:", ppg_options, index=0, horizontal=True)

    st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)

    # 6) Apply filters
    cat_df = df.copy()
    if chosen_market  != "All": cat_df = cat_df[cat_df["Market"]  == chosen_market]
    if chosen_channel != "All": cat_df = cat_df[cat_df["Channel"] == chosen_channel]

    bs = cat_df.copy()
    if chosen_brand    != "All": bs = bs[bs["Brand"]    == chosen_brand]
    if chosen_variant  != "All": bs = bs[bs["Variant"]  == chosen_variant]
    if chosen_packtype != "All": bs = bs[bs["PackType"] == chosen_packtype]
    if chosen_ppg      != "All": bs = bs[bs["PPG"]      == chosen_ppg]

    # 7) Time key
    def set_time(df_, freq):
        df_ = df_.copy()
        df_["Date"] = pd.to_datetime(df_.get("Date",""), errors="coerce")
        df_.dropna(subset=["Date"], inplace=True)
        if freq=="Weekly":  df_["TimeKey"] = df_["Date"].dt.to_period("W").apply(lambda r: r.start_time)
        elif freq=="Monthly":df_["TimeKey"] = df_["Date"].dt.to_period("M").apply(lambda r: r.start_time)
        elif freq=="Yearly": df_["TimeKey"] = df_["Date"].dt.year
        else:                  df_["TimeKey"] = df_["Date"]
        return df_

    cat_df      = set_time(cat_df, chosen_time)
    brand_df    = set_time(bs, chosen_time)

    for c in ["SalesValue","Volume"]:
        if c not in cat_df.columns:   cat_df[c]   = 0
        if c not in brand_df.columns: brand_df[c] = 0

    # 8) Aggregators
    cat_agg = cat_df.groupby("TimeKey", as_index=False).agg(
        CatSalesValue=("SalesValue","sum"), CatVolume=("Volume","sum")
    )

    def agg_dim(d, dim):
        if d.empty: return d.assign(TimeKey=[], **{"Value":[]})
        g = d.groupby(["TimeKey",dim], as_index=False).agg(SalesValue=("SalesValue","sum"), Volume=("Volume","sum"))
        m = g.merge(cat_agg, on="TimeKey", how="left")
        if chosen_metric=="MS Value":    m["Value"] = m["SalesValue"]/m["CatSalesValue"].replace(0,np.nan)
        elif chosen_metric=="Volume":     m["Value"] = m["Volume"]
        elif chosen_metric=="Price":      m["Value"] = m["SalesValue"]/m["Volume"].replace(0,np.nan)
        elif chosen_metric=="MS Volume":  m["Value"] = m["Volume"]/m["CatVolume"].replace(0,np.nan)
        else:                              m["Value"] = 0
        return m.assign(Dimension=lambda df: dim)

    # build chart list
    charts = [("Category", cat_agg.assign(Value=1), "Dimension")]
    for dim, user_choice in [("Brand",chosen_brand),("PackType",chosen_packtype),
                              ("PPG",chosen_ppg),("Variant",chosen_variant)]:
        df_dim = agg_dim(brand_df, dim)
        if not df_dim.empty and not(df_dim[dim].nunique()==1 and user_choice=="All"):
            charts.append((dim, df_dim, dim))

    st.markdown(f"### {chosen_metric} ({chosen_time})")

    def build_chart(df_, col):
        df_ = df_.sort_values("TimeKey")
        if chosen_time=="Weekly": return px.line(df_,x="TimeKey",y="Value",color=col,markers=True)
        else:                      return px.bar(df_, x="TimeKey",y="Value",color=col, barmode="group")

    # display charts in rows
    n = len(charts)
    sizes = [n] if n<=4 else ([3, n-3] if n<=6 else [4, n-4])
    idx = 0
    for sz in sizes:
        row = charts[idx:idx+sz]; idx+=sz
        cols = st.columns(sz)
        for i, (title, dfc, col_name) in enumerate(row):
            with cols[i]:
                st.write(f"#### {title} ({chosen_metric})")
                st.plotly_chart(build_chart(dfc, col_name), use_container_width=True)
                st.text_area(f"Comments ({title})", "")

    st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)

    # Navigation buttons row
    st.markdown('---')
    nav1, nav2, nav3 = st.columns([1,1,1])
    with nav1:
        if st.button("Back", key="mc_back"): go_back()
    with nav2:
        if st.button("Home", key="mc_home"): go_home()
    with nav3:
        if st.button("Go to Price Ladder", key="mc_to_price_ladder"): go_to("price_ladder")


def price_ladder_page():
    
        import streamlit as st
        import pandas as pd
        import numpy as np
        import plotly.graph_objects as go

        # -----------------------------------------------------------------------
        # CUSTOM CSS
        # -----------------------------------------------------------------------
        st.markdown("""
        <style>
        .stApp {
            background-color: #F5F5F5;
        }
        .custom-header {
            font-family: 'Inter', sans-serif;
            font-size: 36px; 
            font-weight: 600;
            color: #333333;
            margin-bottom: 0.2rem;
        }
        .subheader {
            font-family: 'Inter', sans-serif;
            font-size: 18px;
            color: #666666;
            margin-top: 0;
            margin-bottom: 1rem;
        }
        .accent-hr {
            border: 0;
            height: 2px;
            background: linear-gradient(to right, #FFBD59, #FFC87A);
            margin: 0.5rem 0 1.5rem 0;
        }
        .card {
            background-color: #FFFFFF; 
            padding: 1.2rem 1.2rem;
            margin-bottom: 1rem;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
        .card h2 {
            font-family: 'Inter', sans-serif;
            font-size: 24px;
            margin: 0.2rem 0 1rem 0;
            color: #333333;
        }
        div[data-testid="stHorizontalBlock"] button {
            background-color: #FFBD59 !important; 
            color: #333333 !important;
            font-weight: 600 !important;
            border-radius: 4px !important;
            border: none !important;
            margin-bottom: 0.5rem;
        }
        div[data-testid="stHorizontalBlock"] button:hover {
            background-color: #FFC87A !important;
        }
        .dataframe-table {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: #333333;
        }
        </style>
        """, unsafe_allow_html=True)

        # -----------------------------------------------------------------------
        # MAIN HEADER & NAVIGATION
        # -----------------------------------------------------------------------
        st.markdown('<h1 class="custom-header">Brand Ladder with Monthly Selection</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subheader">Pick one or two months in your dataset to see each aggregator\'s last BasePrice (and optional Vol/Week). Multiple own aggregators, no % difference.</p>', unsafe_allow_html=True)
        st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)




        # -----------------------------------------------------------------------
        # RETRIEVE DATA (assuming final BasePrice is in st.session_state["dataframe1"])
        # -----------------------------------------------------------------------
        df_bp = st.session_state.get("dataframe1", None)
        if df_bp is None or df_bp.empty:
            st.warning("No data with final BasePrice found. Please ensure 'dataframe1' is loaded.")
            st.stop()

        # We must have columns: 'Year','Month', or something to define "one-month" subsets
        if not ({"Year","Month"} <= set(df_bp.columns)):
            st.warning("No 'Year'/'Month' columns found; cannot do monthly selection. Please ensure these exist.")
            st.stop()

        # Ensure numeric or integer Year/Month
        df_bp["Year"] = pd.to_numeric(df_bp["Year"], errors="coerce")
        df_bp["Month"] = pd.to_numeric(df_bp["Month"], errors="coerce")
        df_bp.dropna(subset=["Year","Month"], inplace=True)
        df_bp = df_bp.astype({"Year":"int","Month":"int"})

        if df_bp.empty:
            st.warning("After forcing numeric Year/Month, no data remain.")
            st.stop()

        # We'll define a helper "YYYY-MM" aggregator for user picks
        df_bp["YearMonth"] = df_bp["Year"].astype(str).str.zfill(4) + "-" + df_bp["Month"].astype(str).str.zfill(2)

        # Figure out all distinct months, sorted ascending
        all_months = sorted(df_bp["YearMonth"].unique())

        # =============================================================================
        # CARD 1: FILTERS & MONTH PICK
        # =============================================================================
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("## Step 1: Filters & Month Selection")

        # (Optional) Channel filter
        channel_data = df_bp.copy()
        if "Channel" in channel_data.columns:
            colA, colB = st.columns(2)
            with colA:
                selected_channel = st.selectbox("Select Channel:", channel_data["Channel"].dropna().unique())
            channel_data = channel_data[channel_data["Channel"] == selected_channel]
            if channel_data.empty:
                st.warning("No data for that channel.")
                st.markdown('</div>', unsafe_allow_html=True)
                st.stop()
        else:
            st.info("No 'Channel' column – skipping channel filter.")

        # aggregator columns
        possible_agg_cols = ["Brand","Variant","PackType","PPG","PackSize"]
        found_agg_cols = [c for c in possible_agg_cols if c in channel_data.columns]
        if not found_agg_cols:
            st.error("No aggregator columns found.")
            st.stop()

        c1, c2, c3 = st.columns([1.2,1.2,1.2])
        with c1:
            st.markdown("**Select aggregator columns**")
            selected_agg_cols = st.multiselect(
                "Aggregator definition:",
                options=found_agg_cols,
                default=["Brand"]
            )

        if not selected_agg_cols:
            st.warning("No aggregator columns selected.")
            st.stop()

        def combine_cols(row):
            return " - ".join(str(row[c]) for c in selected_agg_cols)

        channel_data["Aggregator"] = channel_data.apply(combine_cols, axis=1)
        all_aggs = sorted(channel_data["Aggregator"].unique())

        # Instead of "Base Aggregator" single pick, let user pick multiple "own brand" aggregator(s).
        with c2:
            st.markdown("**Own Aggregator(s)**")
            own_aggs = st.multiselect("Pick your aggregator(s):", all_aggs)

        with c3:
            st.markdown("**Competitors**")
            comp_aggs = st.multiselect(
                "Competitor(s):",
                [a for a in all_aggs if a not in own_aggs]
            )

        # Merge final aggregator list
        final_aggs = own_aggs + comp_aggs
        if not final_aggs:
            st.warning("No aggregator chosen.")
            st.stop()

        # Compare Mode?
        compare_mode = st.checkbox("Compare Two Different Months?", value=False)

        if compare_mode:
            colM1, colM2 = st.columns(2)
            with colM1:
                month_1 = st.selectbox("Pick Month #1", all_months)
            with colM2:
                month_2 = st.selectbox("Pick Month #2", all_months)
        else:
            month_1 = st.selectbox("Pick Month", all_months)
            month_2 = None

        show_vol_week = st.checkbox("Show Vol/Week on the brand ladder?", value=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # =============================================================================
        # CARD 2: BRAND LADDER (and Market Share if not compare)
        # =============================================================================
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("## Step 2: Brand Ladder")

        data_sub = channel_data[channel_data["Aggregator"].isin(final_aggs)]
        if data_sub.empty:
            st.warning("No data after aggregator picks.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.stop()

        # filter by months
        def data_for_month(df_, yearmonth):
            return df_[df_["YearMonth"] == yearmonth]

        data1 = data_for_month(data_sub, month_1)
        data2 = None
        if compare_mode and month_2:
            data2 = data_for_month(data_sub, month_2)

        if data1.empty and not compare_mode:
            st.warning("No data for selected month.")
            st.stop()

        # define build_ladder_data
        def build_ladder_data(df_, aggregator_list):
            # We'll find "last base price"
            # If multiple rows, we sort by (Year,Week) or by index
            df_ = df_.copy()
            if "Year" in df_.columns and "Week" in df_.columns:
                df_.sort_values(["Year","Week"], inplace=True)
            elif "Date" in df_.columns:
                df_.sort_values("Date", inplace=True)
            else:
                df_.reset_index(drop=True, inplace=True)

            # pick a volume col
            used_vol = None
            if show_vol_week:
                if "VolumeUnits" in df_.columns:
                    used_vol = "VolumeUnits"
                elif "Volume" in df_.columns:
                    used_vol = "Volume"

            rows = []
            for agg in aggregator_list:
                sub = df_[(df_["Aggregator"]==agg) & df_["BasePrice"].notna()]
                if sub.empty:
                    rows.append({"Aggregator": agg, "LastBasePrice": 0, "VolumePerWeek": 0})
                    continue
                last_bp = sub.iloc[-1]["BasePrice"]
                same_bp = sub[sub["BasePrice"]==last_bp]
                volpw = 0
                if used_vol and not same_bp.empty:
                    total_vol = same_bp[used_vol].sum()
                    if {"Year","Week"} <= set(same_bp.columns):
                        wcount = same_bp[["Year","Week"]].drop_duplicates().shape[0]
                    else:
                        wcount = len(same_bp)
                    volpw = total_vol/wcount if wcount else 0

                rows.append({
                    "Aggregator": agg,
                    "LastBasePrice": last_bp,
                    "VolumePerWeek": volpw
                })
            return pd.DataFrame(rows)

        def plot_ladder(ladder_df, own_list, chart_title):
            if ladder_df.empty:
                return None
            # sort by LastBasePrice
            ladder_df.sort_values("LastBasePrice", inplace=True)
            # define color / size
            def color_n_size(agg):
                if agg in own_list:
                    return "#FF7F7F",10
                else:
                    return "#458EE2",7
            cvals, svals = [], []
            for _, row in ladder_df.iterrows():
                c,s = color_n_size(row["Aggregator"])
                cvals.append(c)
                svals.append(s)
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=ladder_df["Aggregator"],
                y=ladder_df["LastBasePrice"],
                mode="lines+markers",
                line=dict(shape="hv", width=2, color="#666666"),
                marker=dict(color=cvals, size=svals, line=dict(width=1, color="#666")),
                name="Last BasePrice"
            ))
            # if show_vol_week
            if show_vol_week and "VolumePerWeek" in ladder_df.columns:
                if ladder_df["VolumePerWeek"].any():
                    fig.add_trace(go.Scatter(
                        x=ladder_df["Aggregator"],
                        y=ladder_df["VolumePerWeek"],
                        mode="lines+markers",
                        line=dict(shape="hv", width=2, color="#41C185"),
                        name="Volume/Week",
                        yaxis="y2"
                    ))
            # annotation => only price
            for i, row in ladder_df.iterrows():
                note_text = f"${row['LastBasePrice']:.2f}"
                fig.add_annotation(
                    x=row["Aggregator"],
                    y=row["LastBasePrice"],
                    text=note_text,
                    showarrow=False,
                    yshift=8
                )
            fig.update_layout(
                title=chart_title,
                xaxis_title="Aggregators",
                yaxis_title="Last BasePrice",
                yaxis2=dict(title="Volume/Week", overlaying="y", side="right"),
                template="plotly_white",
                margin=dict(l=40,r=40,t=60,b=40)
            )
            return fig

        # single or compare
        cLeft, cRight = st.columns(2)
        ladder1 = build_ladder_data(data1, final_aggs)
        fig1 = plot_ladder(ladder1, own_aggs, f"Brand Ladder (Month: {month_1})")

        if fig1:
            cLeft.plotly_chart(fig1, use_container_width=True)
            cLeft.dataframe(ladder1, use_container_width=True)
        else:
            cLeft.warning(f"No data in first month: {month_1}")

        if compare_mode and month_2:
            # second chart, no market share
            ladder2 = build_ladder_data(data2, final_aggs)
            fig2 = plot_ladder(ladder2, own_aggs, f"Brand Ladder (Month: {month_2})")
            if fig2:
                cRight.plotly_chart(fig2, use_container_width=True)
                cRight.dataframe(ladder2, use_container_width=True)
            else:
                cRight.warning(f"No data in second month: {month_2}")
        else:
            # market share
            cRight.write("### Market Share")
            share_colors = ["#FFBD59","#FFC87A","#41C185","#458EE2","#999999"]

            # pick volume or fallback to sales
            def compute_market_share(df_):
                vol_col = None
                if "VolumeUnits" in df_.columns:
                    vol_col = "VolumeUnits"
                elif "Volume" in df_.columns:
                    vol_col = "Volume"
                if vol_col:
                    share_df = df_.groupby("Aggregator", as_index=False).agg(TotalVol=(vol_col,"sum"))
                    tv = share_df["TotalVol"].sum()
                    if tv>0:
                        share_df["Share(%)"] = share_df["TotalVol"]/tv*100
                        fig_pie = go.Figure(data=[go.Pie(
                            labels=share_df["Aggregator"],
                            values=share_df["TotalVol"],
                            hole=0.4
                        )])
                        fig_pie.update_layout(
                            colorway=share_colors,
                            title="Market Share (Volume)",
                            margin=dict(l=10,r=10,t=60,b=10),
                            height=400
                        )
                        return fig_pie, share_df
                    else:
                        return None,None
                elif "SalesValue" in df_.columns:
                    share_df = df_.groupby("Aggregator", as_index=False).agg(TotalSales=("SalesValue","sum"))
                    ts = share_df["TotalSales"].sum()
                    if ts>0:
                        share_df["Share(%)"] = share_df["TotalSales"]/ts*100
                        fig_pie = go.Figure(data=[go.Pie(
                            labels=share_df["Aggregator"],
                            values=share_df["TotalSales"],
                            hole=0.4
                        )])
                        fig_pie.update_layout(
                            colorway=share_colors,
                            title="Market Share (Sales)",
                            margin=dict(l=10,r=10,t=60,b=10),
                            height=400
                        )
                        return fig_pie, share_df
                    else:
                        return None,None
                return None,None

            fig_share, df_share = compute_market_share(data1)
            if fig_share:
                cRight.plotly_chart(fig_share, use_container_width=True)
                cRight.dataframe(df_share, use_container_width=True)
            else:
                cRight.warning("No volume or sales for share calculation or total is 0.")

        st.markdown('</div>', unsafe_allow_html=True)
        # Navigation buttons row
        st.markdown('---')
        nav1, nav2 = st.columns([1,1])
        with nav1:
            if st.button("Back", key="mc_back"): go_back()
        with nav2:
            if st.button("Home", key="mc_home"): go_home()







##########################################################section3

def feature_overview_page_2():
    """
    Feature Overview (Engineer / Pre‑Process) that works off the frame
    created after Base‑Price calculation.
    """
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

    # ──────────────────────────────────────────────
    # 1. progress timeline  (main step 1 in workflow)
    # ──────────────────────────────────────────────
    show_timeline("3")

    # ──────────────────────────────────────────────
    # 2. data retrieval
    #    - prefer dataframe1  (after base price)
    #    - fallback to D0     (raw upload)
    # ──────────────────────────────────────────────
    df = st.session_state.get("dataframe1")

    if df is None or df.empty:
        df = st.session_state.get("D0")

    if (
        df is None
        or df.empty
        or "BasePrice" not in df.columns
        or "Price" not in df.columns
    ):
        st.warning(
            "📌 **Base price not calculated yet.**\n\n"
            "Run **Prepare → Base Price Estimator** first, then return here."
        )
        st.stop()

    # ──────────────────────────────────────────────
    # 3. constants & header
    # ──────────────────────────────────────────────
    TIME_KEYS = {"Year", "Month", "Week"}

    st.header("Feature Overview")
    st.markdown(
        "<p class='subheader'>Interactive filters and at‑a‑glance statistics "
        "to understand your dataset before engineering.</p>"
        "<hr class='accent-hr'>",
        unsafe_allow_html=True
    )

    # ──────────────────────────────────────────────
    # 4. sidebar aggregator filters
    # ──────────────────────────────────────────────
    with st.sidebar:
        st.subheader("Aggregator Filters")
        cat_cols_all = df.select_dtypes(include=["object", "category"]).columns.tolist()

        if cat_cols_all:
            default_sel = st.session_state.get("fo_saved_aggs", [])
            agg_cols_sel = st.multiselect("Choose columns:", cat_cols_all, default=default_sel)

            for col in agg_cols_sel:
                options = ["All"] + sorted(df[col].dropna().unique().tolist())
                sel = st.radio(col, options, horizontal=True, key=f"fo_{col}")
                if sel != "All":
                    df = df[df[col] == sel]

            st.session_state["fo_saved_aggs"] = agg_cols_sel
            st.markdown("---")
            st.write(f"**Rows after filter:** {len(df):,}")
            st.download_button("⬇ Download filtered CSV", df.to_csv(index=False), "filtered_data.csv")
        else:
            st.info("No categorical columns to filter.")

    if df.empty:
        st.error("All rows filtered out – relax your filters.")
        return

    # ──────────────────────────────────────────────
    # 5. TABS layout
    # ──────────────────────────────────────────────
    tabs = st.tabs([
        "Overview", "Columns", "Numeric", "Categorical",
        "Distributions", "Correlation", "Samples"
    ])

    # ===== TAB 0: Overview =====
    with tabs[0]:
        n_rows, n_cols = df.shape
        mem_mb = df.memory_usage(deep=True).sum() / 1e6
        missing_cells = df.isna().sum().sum()
        pct_missing = missing_cells / (n_rows * n_cols) * 100 if n_rows and n_cols else 0

        st.metric("Rows", f"{n_rows:,}")
        st.metric("Columns", f"{n_cols}")
        st.metric("Memory", f"{mem_mb:.2f} MB")
        st.metric("Missing cells", f"{missing_cells:,} ({pct_missing:.2f} %)")

    # ===== TAB 1: Columns =====
    with tabs[1]:
        st.subheader("Column Details")
        info = []
        for c in df.columns:
            info.append({
                "Column": c,
                "Type": str(df[c].dtype),
                "Missing": df[c].isna().sum(),
                "Unique": df[c].nunique(dropna=True),
                "Examples": ", ".join(map(str, df[c].dropna().unique()[:3])) or "—"
            })
        st.dataframe(pd.DataFrame(info), use_container_width=True)

    # ===== TAB 2: Numeric =====
    with tabs[2]:
        numeric_cols = [
            c for c in df.select_dtypes(include=[np.number]).columns
            if c not in TIME_KEYS
        ]
        if numeric_cols:
            st.subheader("Descriptive Stats")
            st.dataframe(df[numeric_cols].describe().T, use_container_width=True)

            if st.checkbox("Show potential outliers (1.5×IQR)"):
                out = []
                for col in numeric_cols:
                    q1, q3 = df[col].quantile([.25, .75])
                    iqr = q3 - q1
                    lb, ub = q1 - 1.5 * iqr, q3 + 1.5 * iqr
                    out.append({
                        "Column": col,
                        "Outliers": ((df[col] < lb) | (df[col] > ub)).sum(),
                        "Lower": f"{lb:.2f}", "Upper": f"{ub:.2f}"
                    })
                st.dataframe(pd.DataFrame(out), use_container_width=True)
        else:
            st.info("No numeric columns (excluding Year/Month/Week).")

    # ===== TAB 3: Categorical =====
    with tabs[3]:
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        if cat_cols:
            st.subheader("Frequency Table")
            ccol = st.selectbox("Column", cat_cols)
            topk = st.slider("Top K", 1, 30, 10)
            freq = df[ccol].value_counts(dropna=False).head(topk)
            freq_df = (freq.rename_axis(ccol)
                       .reset_index(name="Count")
                       .assign(Percent=lambda d: d["Count"] / d["Count"].sum() * 100))
            st.dataframe(freq_df, use_container_width=True)

            if len(cat_cols) > 1 and st.checkbox("Enable cross‑tab"):
                c2 = st.selectbox("vs.", [c for c in cat_cols if c != ccol])
                ct = pd.crosstab(df[ccol], df[c2])
                st.write("Cross‑Tab (Counts)")
                st.dataframe(ct, use_container_width=True)
                if st.checkbox("Heatmap"):
                    st.plotly_chart(px.imshow(ct, text_auto=True, aspect="auto"), use_container_width=True)
        else:
            st.info("No categorical columns.")

    # ===== TAB 4: Distributions =====
    with tabs[4]:
        num_cols = [
            c for c in df.select_dtypes(include=[np.number]).columns
            if c not in TIME_KEYS
        ]
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        left, right = st.columns(2)

        with left:
            st.markdown("#### Numeric Histogram")
            ncol = st.selectbox("Numeric column", ["(None)"] + num_cols)
            if ncol != "(None)":
                fig = px.histogram(df, x=ncol, nbins=30, color_discrete_sequence=["#458EE2"])
                if st.checkbox("Log‑scale Y"):
                    fig.update_yaxes(type="log")
                st.plotly_chart(fig, use_container_width=True)

        with right:
            st.markdown("#### Categorical Bar")
            ccol1 = st.selectbox("Categorical column", ["(None)"] + cat_cols)
            if ccol1 != "(None)":
                cnt = df[ccol1].value_counts(dropna=False).reset_index()
                cnt.columns = [ccol1, "Count"]
                cnt["Percent"] = cnt["Count"] / cnt["Count"].sum() * 100
                y_axis = "Percent" if st.radio("Y‑axis", ["Count", "Percent"]) == "Percent" else "Count"
                fig_b = px.bar(cnt, x=ccol1, y=y_axis, color_discrete_sequence=["#41C185"])
                st.plotly_chart(fig_b, use_container_width=True)

    # ===== TAB 5: Correlation =====
    with tabs[5]:
        num_cols_corr = [
            c for c in df.select_dtypes(include=[np.number]).columns
            if c not in TIME_KEYS and df[c].nunique() > 1
        ]
        if len(num_cols_corr) > 1:
            method = st.selectbox("Method", ["pearson", "spearman", "kendall"])
            thresh = st.slider("Mask |ρ| < ", 0.0, 1.0, 0.0, 0.05)
            corr = df[num_cols_corr].corr(method=method)
            if thresh > 0:
                corr = corr.mask(corr.abs() < thresh)
            st.plotly_chart(px.imshow(
                corr, text_auto=True, aspect="auto",
                color_continuous_scale="RdBu",
                title=f"{method.title()} correlation (Year/Month/Week excluded)"
            ), use_container_width=True)
        else:
            st.info("Need ≥ 2 numeric columns (excluding Year/Month/Week).")

    # ===== TAB 6: Samples =====
    with tabs[6]:
        st.subheader("Sample Rows")
        n = st.slider("Rows to preview", 1, 50, 5)
        st.dataframe(df.head(n), use_container_width=True)

    # ──────────────────────────────────────────────
    # 6. navigation buttons
    # ──────────────────────────────────────────────
    st.markdown("---")
    back, home, create = st.columns(3)

    with back:
        if st.button("Back"):
            go_back()

    with home:
        if st.button("Home"):
            go_home()

    with create:
        if st.button("Go to Create"):
            st.session_state["page"] = "create_section3"
            st.rerun()


# ─────────────────────────────────────────
# Helper • error + navigation
# ─────────────────────────────────────────
def error_with_nav(msg: str):
    import streamlit as st
    st.error(msg)
    col_b, col_h = st.columns(2)
    with col_b:
        if st.button("◀ Back"):
            go_back()
    with col_h:
        if st.button("🏠 Home"):
            go_home()
    st.stop()


# ─────────────────────────────────────────
# Engineer ▸ CREATE  (v5, with dual preview)
# ─────────────────────────────────────────
def create_page():
    import streamlit as st
    import pandas as pd
    import numpy as np

    # ─── Timeline badge ───
    show_timeline("3")

    # ─── Retrieve dataframe ───
    if "create_data" in st.session_state and not st.session_state["create_data"].empty:
        df = st.session_state["create_data"].copy()
    elif "dataframe1" in st.session_state and not st.session_state["dataframe1"].empty:
        df = st.session_state["dataframe1"].copy()
        st.session_state["create_data"] = df.copy()
    elif "D0" in st.session_state and st.session_state["D0"] is not None \
            and not st.session_state["D0"].empty:
        df = st.session_state["D0"].copy()
        st.session_state["create_data"] = df.copy()
    else:
        error_with_nav("🚫 **No data.** Upload in **Validate** and run Base‑Price first.")

    # save baseline column list once
    if "create_base_cols" not in st.session_state:
        st.session_state["create_base_cols"] = df.columns.tolist()

    # ─── Preview helper ───
    def preview_expander(rows: int = 8):
        base = set(st.session_state["create_base_cols"])
        new_cols = [c for c in df.columns if c not in base]
        orig_cols = [c for c in df.columns if c in base]

        with st.expander("Preview data sample", expanded=False):
            if new_cols:
                left, right = st.columns(2)
                with left:
                    st.markdown("##### New columns")
                    st.dataframe(df[new_cols].tail(rows).reset_index(drop=True),
                                 use_container_width=True)
                with right:
                    st.markdown("##### Original columns")
                    show_cols = orig_cols[:10]
                    st.dataframe(df[show_cols].tail(rows).reset_index(drop=True),
                                 use_container_width=True)
                    if len(orig_cols) > 10:
                        st.caption(f"First 10 of {len(orig_cols)} original columns shown.")
            else:
                st.info("No new columns yet – create some!")

    # ─── Sidebar • global filter ───
    with st.sidebar:
        st.subheader("Aggregator filter")
        cat_cols_all = df.select_dtypes(include=["object", "category"]).columns.tolist()
        sel_cols = st.multiselect("Filter columns", cat_cols_all,
                                  default=st.session_state.get("create_saved_aggs", []),
                                  key="flt_cols")
        changed = False
        for c in sel_cols:
            opts = ["All"] + sorted(df[c].dropna().unique())
            val = st.radio(c, opts, horizontal=True, key=f"flt_val_{c}")
            if val != "All":
                df = df[df[c] == val]
                changed = True
        st.session_state["create_saved_aggs"] = sel_cols
        st.write(f"Active rows: **{len(df):,}**")
        if changed and st.button("Apply filter", key="flt_apply"):
            st.session_state["create_data"] = df.copy()
            st.success("Filter applied.")

    # refresh column lists after filter
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    # ─── Header & CSS ───
    st.markdown("""
    <style>
      .ribbon{background:#673AB7;color:#fff;padding:6px 16px;border-radius:6px;
              display:inline-block;margin-bottom:10px;font-weight:600;}
      .floating-save{position:fixed;bottom:18px;right:18px;z-index:9999;
          background:#FFBD59;color:#333;font-weight:600;padding:10px 22px;
          border-radius:30px;box-shadow:0 2px 6px rgba(0,0,0,0.25);}
      .floating-save:hover{background:#FFC87A;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<span class="ribbon">Step 3 – Engineer ▸ Create</span>', unsafe_allow_html=True)
    st.caption("Sidebar filter slices data for every builder. Each tab shows a live sample.")

    # ─── Tab layout ───
    tabs = st.tabs([
        "Numeric", "Interaction", "Group",
        "Date/Time", "Trend", "Residuals", "Preview / Save"
    ])

    # ========== TAB 0 • Numeric ==========
    with tabs[0]:
        st.markdown("### Numeric transforms")
        c1, c2 = st.columns(2)
        with c1:
            new_basic = st.text_input("New column", "NumFeature1", key="num_new")
            mode      = st.radio("Mode", ["Two‑Column Arithmetic", "Single‑Column"],
                                 horizontal=True, key="num_mode")
        with c2:
            if mode == "Two‑Column Arithmetic":
                a = st.selectbox("A", ["(None)"] + num_cols, key="num_two_a")
                b = st.selectbox("B", ["(None)"] + num_cols, key="num_two_b")
                op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"],
                                  key="num_two_op")
                if a not in ("(None)", b) and b != "(None)" and \
                   st.button("Add numeric", key="num_add_two"):
                    df[new_basic] = (
                        df[a] + df[b] if op == "Add" else
                        df[a] - df[b] if op == "Subtract" else
                        df[a] * df[b] if op == "Multiply" else
                        np.where(df[b] != 0, df[a] / df[b], np.nan)
                    )
                    st.session_state["create_data"] = df.copy()
                    st.success(f"{new_basic} added.")
            else:
                c = st.selectbox("Column", ["(None)"] + num_cols, key="num_one_c")
                op = st.selectbox("Transform", ["Log", "Sqrt", "Negate"], key="num_one_op")
                if c != "(None)" and st.button("Add numeric", key="num_add_one"):
                    df[new_basic] = (
                        np.where(df[c] > 0,  np.log(df[c]), np.nan) if op == "Log" else
                        np.where(df[c] >= 0, np.sqrt(df[c]), np.nan) if op == "Sqrt" else
                        -df[c]
                    )
                    st.session_state["create_data"] = df.copy()
                    st.success(f"{new_basic} added.")
        preview_expander()

    # ========== TAB 1 • Interaction ==========
    with tabs[1]:
        st.markdown("### Interaction features")
        int_mode = st.radio("Type", ["Pairwise Numeric", "Cat Cross", "Min/Max"],
                            horizontal=True, key="int_mode")
        out_col  = st.text_input("New column", "Interact1", key="int_new")
        if int_mode == "Pairwise Numeric":
            x = st.selectbox("X", ["(None)"] + num_cols, key="int_pair_x")
            y = st.selectbox("Y", ["(None)"] + num_cols, key="int_pair_y")
            if x not in ("(None)", y) and y != "(None)" and \
               st.button("Create", key="int_make_pair"):
                df[out_col] = df[x] * df[y]
                st.session_state["create_data"] = df.copy()
                st.success(f"{out_col} added.")
        elif int_mode == "Cat Cross":
            a = st.selectbox("Cat A", ["(None)"] + cat_cols, key="int_cat_a")
            b = st.selectbox("Cat B", ["(None)"] + cat_cols, key="int_cat_b")
            if a not in ("(None)", b) and b != "(None)" and \
               st.button("Create", key="int_make_cross"):
                df[out_col] = df[a].astype(str) + "_" + df[b].astype(str)
                st.session_state["create_data"] = df.copy()
                st.success(f"{out_col} added.")
        else:
            sel = st.multiselect("Numeric columns", num_cols, key="int_mm_sel")
            mm  = st.selectbox("Compute", ["Min", "Max"], key="int_mm_op")
            if sel and st.button("Create", key="int_make_mm"):
                df[out_col] = df[sel].min(axis=1) if mm == "Min" else df[sel].max(axis=1)
                st.session_state["create_data"] = df.copy()
                st.success(f"{out_col} added.")
        preview_expander()

    # ========== TAB 2 • Group ==========
    with tabs[2]:
        st.markdown("### Group‑based features")
        g_col  = st.selectbox("Group column", ["(None)"] + cat_cols, key="grp_col")
        g_feat = st.text_input("New column", "GroupFeat1", key="grp_new")
        op     = st.selectbox("Operation", ["Mean", "Count", "Diff‑from‑Mean"], key="grp_op")
        num_sel = st.selectbox("Numeric column", ["(None)"] + num_cols,
                               key="grp_num") if num_cols else "(None)"
        ready = g_col != "(None)" and (op == "Count" or num_sel != "(None)")
        if ready and st.button("Create group feature", key="grp_make"):
            grp = df.groupby(g_col)
            if op == "Mean":
                df[g_feat] = grp[num_sel].transform("mean")
            elif op == "Count":
                df[g_feat] = grp[g_col].transform("count")
            else:
                df[g_feat] = df[num_sel] - grp[num_sel].transform("mean")
            st.session_state["create_data"] = df.copy()
            st.success(f"{g_feat} added.")
        preview_expander()

    # ========== TAB 3 • Date/Time ==========
    with tabs[3]:
        st.markdown("### Date / Time features")
        dt_col = st.selectbox("Date column", ["(None)"] + df.columns.tolist(), key="dt_col")
        new_dt = st.text_input("New base name", "DateFeat1", key="dt_new")
        dt_op  = st.selectbox("Operation", ["Day/Month", "Delta (days)", "Lag"], key="dt_op")
        if dt_col != "(None)":
            if not np.issubdtype(df[dt_col].dtype, np.datetime64):
                df[dt_col] = pd.to_datetime(df[dt_col], errors="coerce")
            if np.issubdtype(df[dt_col].dtype, np.datetime64) and \
               st.button("Create", key="dt_make"):
                if dt_op == "Day/Month":
                    df[new_dt + "_day"]   = df[dt_col].dt.day
                    df[new_dt + "_month"] = df[dt_col].dt.month
                elif dt_op == "Delta (days)":
                    today = pd.Timestamp.today().normalize()
                    df[new_dt] = (today - df[dt_col]).dt.days
                else:
                    df[new_dt] = df[dt_col].shift(1)
                st.session_state["create_data"] = df.copy()
                st.success("Date/time feature(s) added.")
        preview_expander()

    # ========== TAB 4 • Trend ==========
    with tabs[4]:
        st.markdown("### Trend index")
        trend_col = st.text_input("Trend column", "TrendIdx", key="trend_name")
        grp_cols  = st.multiselect("Group by", cat_cols, key="trend_grp")
        if st.button("Create trend", key="trend_make"):
            if grp_cols:
                df[trend_col] = df.groupby(grp_cols).cumcount() + 1
            else:
                df[trend_col] = np.arange(1, len(df) + 1)
            st.session_state["create_data"] = df.copy()
            st.success(f"{trend_col} created.")
        preview_expander()

    # ========== TAB 5 • Residuals ==========
    with tabs[5]:
        st.markdown("### Regression residuals")
        y_var = st.selectbox("Y (dependent)", ["(None)"] + num_cols, key="resid_y")
        x_var = st.selectbox("X (independent)", ["(None)"] + num_cols, key="resid_x")
        resid = st.text_input("Residual column", "Resid_Y_on_X", key="resid_name")
        valid = y_var not in ("(None)", x_var) and x_var != "(None)"
        if valid and st.button("Create residuals", key="resid_make"):
            data = df[[x_var, y_var]].dropna()
            if len(data) < 3:
                st.warning("Need ≥3 rows of data.")
            else:
                β, α = np.polyfit(data[x_var], data[y_var], 1)
                df[resid] = df[y_var] - (α + β * df[x_var])
                st.session_state["create_data"] = df.copy()
                st.success("Residuals added.")
        preview_expander()

    # ========== TAB 6 • Preview / Save ==========
    with tabs[6]:
        st.markdown("### Preview & save")
        st.dataframe(df.head(25), use_container_width=True)
        st.download_button("⬇ Download preview CSV",
                           df.head(1000).to_csv(index=False),
                           "create_preview.csv",
                           key="preview_dl")
        preview_expander(rows=12)

    # ─── Floating save ───
    if st.button("💾 Save all changes", key="save_fab_click"):
        st.session_state["create_data"] = df.copy()
        st.success("Changes saved to session.")


    # ─── Bottom nav ───
    create, home, nxt = st.columns(3)

    with create:
        if st.button("Go to Feature Overview"):
            st.session_state["page"] = "feature_overview_2"
            st.rerun()


    with home:
        if st.button("🏠 Home", key="nav_home"):
            go_home()

    with nxt:
        if st.button("Transform ➜", key="nav_to_transform"):
            go_to("transform_section3")


def transform_page():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    from scipy import stats
    from sklearn.preprocessing import OneHotEncoder, LabelEncoder, QuantileTransformer
    from sklearn.decomposition import PCA
    from sklearn.feature_selection import mutual_info_regression

    # ─── get working DataFrame ───
    if "transform_data" in st.session_state:
        df = st.session_state["transform_data"].copy()
    else:
        if "create_data" not in st.session_state or st.session_state["create_data"].empty:
            error_with_nav("No data found – build something on **Create** first.")
        df = st.session_state["create_data"].copy()

    # ─── remember baseline for new‑col detection ───
    if "transform_base_cols" not in st.session_state:
        st.session_state["transform_base_cols"] = df.columns.tolist()
    
    # ─── initialize transformation history ───
    if "transform_history" not in st.session_state:
        st.session_state["transform_history"] = []
    
    # ─── timeline badge ───
    show_timeline("3")

    # ─── sidebar filter ───
    with st.sidebar:
        st.subheader("Filter slice")
        for c in df.select_dtypes(include=["object","category"]).columns:
            opts = ["All"] + sorted(df[c].dropna().unique().tolist())
            sel = st.radio(c, opts, horizontal=True, key=f"tf_filt_{c}")
            if sel != "All":
                df = df[df[c] == sel]
        st.write(f"Rows: **{len(df):,}**")
        
        # Add undo in sidebar
        st.markdown("---")
        st.subheader("Actions")
        if st.button("⬅️ Undo Last Transformation"):
            if st.session_state["transform_history"]:
                last_state = st.session_state["transform_history"].pop()
                if "transform_history_desc" in st.session_state:
                    st.session_state["transform_history_desc"].pop()
                st.session_state["transform_data"] = last_state
                st.success("Last transformation undone!")
                st.experimental_rerun()

    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    
    # ─── scaling helpers ───
    def scale_series(s: pd.Series, method: str, **kwargs) -> pd.Series:
        v = s.dropna()
        idx = s.index
        if v.empty:
            return pd.Series(np.nan, index=idx)
        
        if method == "Standard":
            std = v.std()
            return (s - v.mean())/std if std else pd.Series(np.nan, index=idx)
        
        if method == "MinMax":
            mn, mx = v.min(), v.max()
            return (s - mn)/(mx - mn) if mx!=mn else pd.Series(np.nan, index=idx)
        
        if method == "Robust":
            q75, q25 = v.quantile(.75), v.quantile(.25)
            iqr = q75-q25
            return (s - v.median())/iqr if iqr else pd.Series(np.nan, index=idx)
        
        if method == "MeanNorm":
            mn, mx = v.min(), v.max()
            span = mx-mn
            return (s - v.mean())/span if span else pd.Series(np.nan, index=idx)
        
        if method == "Log":
            # Add offset if needed to make all values positive
            offset = abs(min(0, v.min())) + 1 if v.min() <= 0 else 0
            return np.log(s + offset)
        
        if method == "Box-Cox":
            # Add offset if needed to make all values positive
            offset = abs(min(0, v.min())) + 1 if v.min() <= 0 else 0
            transformed, _ = stats.boxcox(s + offset)
            return pd.Series(transformed, index=s.index)
        
        if method == "Quantile":
            transformer = QuantileTransformer(output_distribution='normal')
            # Reshape for sklearn
            values = s.values.reshape(-1, 1)
            return pd.Series(transformer.fit_transform(values).flatten(), index=s.index)
        
        if method == "Yeo-Johnson":
            transformed, _ = stats.yeojohnson(s)
            return pd.Series(transformed, index=s.index)
        
        # Default case
        return s

    def handle_outliers(series, method, **kwargs):
        s = series.copy()
        if method == "None":
            return s
        
        if method == "Cap at percentile":
            lower = kwargs.get('lower', 0.05)
            upper = kwargs.get('upper', 0.95)
            low_val = s.quantile(lower)
            high_val = s.quantile(upper)
            s = s.clip(low_val, high_val)
            
        elif method == "Remove":
            # For demonstration - in practice, you might want to handle this differently
            q1, q3 = s.quantile(0.25), s.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            s = s.mask((s < lower_bound) | (s > upper_bound))
            
        elif method == "Replace with mean/median":
            replace_with = kwargs.get('replace_with', 'mean')
            q1, q3 = s.quantile(0.25), s.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            if replace_with == 'mean':
                replace_val = s.mean()
            else:  # median
                replace_val = s.median()
            s = s.mask((s < lower_bound) | (s > upper_bound), replace_val)
            
        return s



    # ─── Main interface with tabs ───
    transform_tabs = st.tabs(["Scaling", "Encoding", "Dimensionality Reduction", "Analytics"])
    
    # ─── TAB 1: SCALING ───
    with transform_tabs[0]:
        st.markdown("### Data Scaling")
        
        left_scale, right_scale = st.columns([1, 1.2])
        
        with left_scale:
            # Column selection
            col_group = st.radio("Column selection", ["Individual", "Batch"], horizontal=True)
            
            if col_group == "Individual":
                x_sel = st.multiselect("Target column(s)", num_cols, key="tf_x_sel")
            else:
                selection_type = st.selectbox("Selection type", ["All Numeric", "Custom Group"])
                if selection_type == "All Numeric":
                    x_sel = num_cols
                else:
                    x_sel = st.multiselect("Select columns", num_cols)
            
            # Scaling method
            x_mtd = st.selectbox("Scaling method", 
                              ["Standard", "MinMax", "Robust", "MeanNorm", "Log", "Box-Cox", "Quantile", "Yeo-Johnson"],
                              key="tf_x_mtd")
            
            # Outlier handling
            outlier_method = st.selectbox("Outlier handling", 
                                       ["None", "Cap at percentile", "Remove", "Replace with mean/median"])
            
            if outlier_method == "Cap at percentile":
                lower, upper = st.slider("Percentile range", 0.0, 1.0, (0.05, 0.95), 0.05)
                outlier_params = {"lower": lower, "upper": upper}
            elif outlier_method == "Replace with mean/median":
                replace_with = st.radio("Replace with", ["mean", "median"], horizontal=True)
                outlier_params = {"replace_with": replace_with}
            else:
                outlier_params = {}
            
            # Suffix for new columns
            x_suf = st.text_input("Suffix for scaled columns", "_scaled", key="tf_x_suf")
            
            # Apply button
            if st.button("Apply scaling", key="tf_apply_scale"):
                # Save current state to history
                st.session_state["transform_history"].append(df.copy())
                if "transform_history_desc" not in st.session_state:
                    st.session_state["transform_history_desc"] = []
                st.session_state["transform_history_desc"].append(f"Applied {x_mtd} scaling to {len(x_sel)} columns")
                
                # Apply transformations
                for col in x_sel:
                    # First handle outliers if needed
                    if outlier_method != "None":
                        df[col] = handle_outliers(df[col], outlier_method, **outlier_params)
                    
                    # Then apply scaling
                    df[col + x_suf] = scale_series(df[col], x_mtd)
                
                # Save
                st.session_state["transform_data"] = df.copy()
                st.success(f"Scaled {len(x_sel)} columns with {x_mtd} method")
        
        with right_scale:
            st.markdown("### Compare before vs after")
            orig = st.selectbox("Original", ["None"] + num_cols, key="tf_cmp_o")
            
            # Get newly created columns for comparison
            base = set(st.session_state["transform_base_cols"])
            new_cols = [c for c in df.columns if c not in base]
            
            trans = st.selectbox("Transformed", ["None"] + new_cols, key="tf_cmp_t")
            
            if orig != "None" and trans != "None":
                viz_type = st.radio("Visualization type", 
                                 ["Distribution", "Line", "Bar", "Scatter", "Box Plot"], 
                                 horizontal=True, key="tf_viz_type")
                
                n = st.slider("Rows to plot", 5, 100, 30, key="tf_cmp_n")
                
                plot_df = df[[orig, trans]].head(n).reset_index()
                
                if viz_type == "Distribution":
                    # Create histogram with both variables
                    fig = px.histogram(pd.melt(df[[orig, trans]].dropna()), 
                                      x="value", color="variable", marginal="rug", 
                                      opacity=0.7, barmode="overlay", histnorm="probability density")
                    fig.update_layout(title="Distribution Comparison", margin=dict(l=20, r=20, t=40, b=20))
                    st.plotly_chart(fig, use_container_width=True)
                    
                elif viz_type == "Line":
                    fig = px.line(plot_df, x="index", y=[orig, trans], markers=True)
                    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
                    st.plotly_chart(fig, use_container_width=True)
                    
                elif viz_type == "Bar":
                    fig = px.bar(plot_df, x="index", y=[orig, trans], barmode="group")
                    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
                    st.plotly_chart(fig, use_container_width=True)
                    
                elif viz_type == "Scatter":
                    fig = px.scatter(df, x=orig, y=trans, trendline="ols", 
                                    title=f"Correlation: {df[[orig, trans]].corr().iloc[0,1]:.4f}")
                    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
                    st.plotly_chart(fig, use_container_width=True)
                    
                else:  # Box Plot
                    fig = go.Figure()
                    fig.add_trace(go.Box(y=df[orig].dropna(), name=orig))
                    fig.add_trace(go.Box(y=df[trans].dropna(), name=trans))
                    fig.update_layout(title="Box Plot Comparison", margin=dict(l=20, r=20, t=40, b=20))
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Select both Original and Transformed columns to compare.")
        
        # Preview new columns
        base = set(st.session_state["transform_base_cols"])
        new = [c for c in df.columns if c not in base]
        if new:
            st.markdown("#### New columns (last 8 rows)")
            st.dataframe(df[new].tail(8).reset_index(drop=True), use_container_width=True)
        else:
            st.info("No new columns yet – hit **Apply scaling**.")
    
    # ─── TAB 2: ENCODING ───
    with transform_tabs[1]:
        st.markdown("### Categorical Encoding")
        
        left_encode, right_encode = st.columns([1, 1.2])
        
        with left_encode:
            if not cat_cols:
                st.warning("No categorical columns found in the dataset.")
            else:
                # Encoding method selection
                encoding_method = st.selectbox("Encoding method", 
                                            ["One-Hot Encoding", "Label Encoding", "Target Encoding", "Binary Encoding"])
                
                # Column selection
                cat_to_encode = st.multiselect("Columns to encode", cat_cols)
                
                if encoding_method == "Target Encoding":
                    target_col = st.selectbox("Target column (for Target Encoding)", num_cols)
                
                # Prefix/suffix for new columns
                prefix = st.text_input("Prefix for encoded columns", "")
                
                if st.button("Apply encoding"):
                    # Save current state to history
                    st.session_state["transform_history"].append(df.copy())
                    if "transform_history_desc" not in st.session_state:
                        st.session_state["transform_history_desc"] = []
                    st.session_state["transform_history_desc"].append(f"Applied {encoding_method} to {len(cat_to_encode)} columns")
                    
                    if encoding_method == "One-Hot Encoding":
                        # Create dummy variables
                        for col in cat_to_encode:
                            # Get dummies and add prefix if specified
                            dummies = pd.get_dummies(df[col], prefix=f"{prefix}{col}" if prefix else None)
                            # Add to dataframe
                            df = pd.concat([df, dummies], axis=1)
                    
                    elif encoding_method == "Label Encoding":
                        # Apply label encoding
                        for col in cat_to_encode:
                            le = LabelEncoder()
                            # Create new column name
                            new_col = f"{prefix}{col}_encoded" if prefix else f"{col}_encoded"
                            # Apply encoding
                            df[new_col] = le.fit_transform(df[col].astype(str))
                    
                    elif encoding_method == "Target Encoding":
                        # Apply target encoding (mean encoding)
                        for col in cat_to_encode:
                            # Group by categorical and calculate mean of target
                            encoding_map = df.groupby(col)[target_col].mean().to_dict()
                            # Create new column name
                            new_col = f"{prefix}{col}_target_encoded" if prefix else f"{col}_target_encoded"
                            # Apply encoding
                            df[new_col] = df[col].map(encoding_map)
                    
                    elif encoding_method == "Binary Encoding":
                        # Binary encoding (requires category_encoders package, using binary representation)
                        for col in cat_to_encode:
                            # Get unique values
                            unique_vals = df[col].dropna().unique()
                            # Create mapping
                            mapping = {val: format(i, 'b').zfill(len(bin(len(unique_vals))[2:])) 
                                      for i, val in enumerate(unique_vals)}
                            # Create new columns for each bit position
                            max_bits = max(len(v) for v in mapping.values())
                            # Map original values to binary representation
                            base_name = f"{prefix}{col}" if prefix else col
                            
                            # Temporary column with binary representation
                            temp_bin = df[col].map(mapping)
                            # Create a column for each bit position
                            for pos in range(max_bits):
                                df[f"{base_name}_bin_{pos}"] = temp_bin.apply(
                                    lambda x: int(x[pos]) if isinstance(x, str) and pos < len(x) else np.nan
                                )
                    
                    # Save updated dataframe
                    st.session_state["transform_data"] = df.copy()
                    st.success(f"Applied {encoding_method} to {len(cat_to_encode)} columns")
        
        with right_encode:
            st.markdown("### Encoded Data Preview")
            
            # Preview new columns
            base = set(st.session_state["transform_base_cols"])
            new_encode_cols = [c for c in df.columns if c not in base]
            
            if new_encode_cols:
                n_preview = min(10, len(new_encode_cols))
                st.write(f"Showing {n_preview} of {len(new_encode_cols)} new columns")
                st.dataframe(df[new_encode_cols[:n_preview]].head(10), use_container_width=True)
                
                # Correlation heatmap for new numerical columns
                new_num_cols = [c for c in new_encode_cols if c in df.select_dtypes(include=[np.number]).columns]
                if len(new_num_cols) > 1:
                    st.markdown("#### Correlation between encoded features")
                    corr = df[new_num_cols].corr()
                    fig = px.imshow(corr, color_continuous_scale='RdBu_r', origin='lower',
                                   title="Correlation Matrix for Encoded Features")
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No newly encoded columns yet – apply encoding first.")
    
    # ─── TAB 3: DIMENSIONALITY REDUCTION ───
    with transform_tabs[2]:
        st.markdown("### Dimensionality Reduction")
        
        dim_method = st.selectbox("Method", ["PCA", "Feature Selection by Correlation", "Feature Selection by Importance"])
        
        if dim_method == "PCA":
            # Get numeric columns for PCA
            pca_cols = st.multiselect("Columns for PCA", num_cols)
            
            if pca_cols:
                n_components = st.slider("Number of components", 1, min(len(pca_cols), 10), 2)
                
                pca_prefix = st.text_input("Prefix for PCA components", "PCA_")
                
                if st.button("Apply PCA"):
                    # Save current state to history
                    st.session_state["transform_history"].append(df.copy())
                    if "transform_history_desc" not in st.session_state:
                        st.session_state["transform_history_desc"] = []
                    st.session_state["transform_history_desc"].append(f"Applied PCA to {len(pca_cols)} columns")
                    
                    try:
                        # Apply PCA
                        pca = PCA(n_components=n_components)
                        pca_result = pca.fit_transform(df[pca_cols].dropna())
                        
                        # Create new dataframe with PCA results
                        pca_df = pd.DataFrame(
                            pca_result, 
                            columns=[f"{pca_prefix}{i+1}" for i in range(n_components)],
                            index=df[pca_cols].dropna().index
                        )
                        
                        # Add PCA components to original dataframe
                        for col in pca_df.columns:
                            df[col] = np.nan  # Initialize with NaN
                            df.loc[pca_df.index, col] = pca_df[col]  # Fill values
                        
                        # Display explained variance
                        explained_var = pca.explained_variance_ratio_
                        st.write("Explained variance by component:")
                        for i, var in enumerate(explained_var):
                            st.write(f"- Component {i+1}: {var:.4f} ({var*100:.2f}%)")
                        
                        # Cumulative explained variance
                        cum_var = np.cumsum(explained_var)
                        st.write(f"Total variance explained: {cum_var[-1]*100:.2f}%")
                        
                        # Plot explained variance
                        fig = go.Figure()
                        fig.add_trace(go.Bar(
                            x=[f"PC{i+1}" for i in range(len(explained_var))],
                            y=explained_var,
                            name="Individual"
                        ))
                        fig.add_trace(go.Scatter(
                            x=[f"PC{i+1}" for i in range(len(cum_var))],
                            y=cum_var,
                            name="Cumulative",
                            line=dict(color='red')
                        ))
                        fig.update_layout(title="Explained Variance by Principal Component",
                                         xaxis_title="Principal Component",
                                         yaxis_title="Explained Variance Ratio",
                                         legend=dict(x=0.02, y=0.98),
                                         margin=dict(l=20, r=20, t=40, b=20))
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Save
                        st.session_state["transform_data"] = df.copy()
                        st.success(f"Added {n_components} PCA components to the dataset")
                        
                    except Exception as e:
                        st.error(f"Error during PCA: {str(e)}")
                        
                    if n_components >= 2:
                        st.markdown("### PCA Visualization (First 2 Components)")
                        plot_df = df.copy()
                        
                        # Select target for coloring if available
                        if len(cat_cols) > 0:
                            color_col = st.selectbox("Color by", ["None"] + cat_cols)
                            
                            if color_col != "None":
                                fig = px.scatter(
                                    plot_df, 
                                    x=f"{pca_prefix}1", 
                                    y=f"{pca_prefix}2",
                                    color=color_col,
                                    hover_data=[c for c in plot_df.columns if c != color_col][:5]
                                )
                            else:
                                fig = px.scatter(
                                    plot_df, 
                                    x=f"{pca_prefix}1", 
                                    y=f"{pca_prefix}2",
                                    hover_data=plot_df.columns[:5]
                                )
                            
                            fig.update_layout(title="PCA Result Visualization",
                                             margin=dict(l=20, r=20, t=40, b=20))
                            st.plotly_chart(fig, use_container_width=True)
        
        elif dim_method == "Feature Selection by Correlation":
            corr_thresh = st.slider("Correlation threshold", 0.0, 1.0, 0.8, 0.05)
            
            if st.button("Identify Correlated Features"):
                # Calculate correlation matrix for numeric features
                corr_matrix = df[num_cols].corr().abs()
                
                # Create upper triangle mask
                upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
                
                # Find features with correlation greater than threshold
                highly_correlated = [column for column in upper.columns if any(upper[column] > corr_thresh)]
                
                if highly_correlated:
                    st.write(f"Found {len(highly_correlated)} features with correlation > {corr_thresh}:")
                    for col in highly_correlated:
                        correlations = upper[col][upper[col] > corr_thresh].sort_values(ascending=False)
                        for idx, val in correlations.items():
                            st.write(f"- {col} & {idx}: correlation = {val:.4f}")
                    
                    # Visualize correlation matrix
                    st.markdown("### Correlation Matrix")
                    fig = px.imshow(
                        corr_matrix,
                        color_continuous_scale='RdBu_r',
                        origin='lower',
                        title="Feature Correlation Matrix"
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Option to remove features
                    to_remove = st.multiselect("Select features to remove", highly_correlated)
                    
                    if to_remove and st.button("Remove Selected Features"):
                        # Save current state to history
                        st.session_state["transform_history"].append(df.copy())
                        if "transform_history_desc" not in st.session_state:
                            st.session_state["transform_history_desc"] = []
                        st.session_state["transform_history_desc"].append(f"Removed {len(to_remove)} correlated features")
                        
                        # Remove selected features
                        df = df.drop(columns=to_remove)
                        
                        # Save
                        st.session_state["transform_data"] = df.copy()
                        st.success(f"Removed {len(to_remove)} correlated features")
                else:
                    st.info(f"No features with correlation > {corr_thresh} found.")
        
        elif dim_method == "Feature Selection by Importance":
            # Choose target variable
            target_col = st.selectbox("Target variable", num_cols)
            
            # Choose features to evaluate
            features = [c for c in num_cols if c != target_col]
            selected_features = st.multiselect("Features to evaluate", features, default=features)
            
            if st.button("Calculate Feature Importance"):
                if not selected_features:
                    st.warning("Please select at least one feature to evaluate.")
                else:
                    try:
                        # Calculate mutual information
                        X = df[selected_features].fillna(df[selected_features].mean())
                        y = df[target_col].fillna(df[target_col].mean())
                        
                        mi_scores = mutual_info_regression(X, y)
                        mi_df = pd.DataFrame({'Feature': selected_features, 'Importance': mi_scores})
                        mi_df = mi_df.sort_values('Importance', ascending=False)
                        
                        # Display feature importance
                        st.markdown("### Feature Importance")
                        st.dataframe(mi_df)
                        
                        # Plot feature importance
                        fig = px.bar(
                            mi_df, 
                            x='Feature', 
                            y='Importance',
                            title=f"Feature Importance (Mutual Information) for predicting {target_col}"
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Option to keep top N features
                        top_n = st.slider("Keep top N features", 1, len(selected_features), len(selected_features))
                        
                        features_to_keep = mi_df['Feature'].iloc[:top_n].tolist()
                        features_to_drop = [f for f in selected_features if f not in features_to_keep]
                        
                        if features_to_drop and st.button("Remove Low Importance Features"):
                            # Save current state to history
                            st.session_state["transform_history"].append(df.copy())
                            if "transform_history_desc" not in st.session_state:
                                st.session_state["transform_history_desc"] = []
                            st.session_state["transform_history_desc"].append(f"Removed {len(features_to_drop)} low importance features")
                            
                            # Remove selected features
                            df = df.drop(columns=features_to_drop)
                            
                            # Save
                            st.session_state["transform_data"] = df.copy()
                            st.success(f"Removed {len(features_to_drop)} low importance features")
                    
                    except Exception as e:
                        st.error(f"Error calculating feature importance: {str(e)}")
    
    # ─── TAB 4: ANALYTICS ───
    with transform_tabs[3]:
        st.markdown("### Data Analysis and Suggestions")
        
        if st.button("Analyze Dataset"):
            # Get quick stats
            numeric_stats = df.describe().T
            numeric_stats['missing'] = df.isnull().sum()
            numeric_stats['missing_pct'] = df.isnull().sum() / len(df) * 100
            numeric_stats['dtype'] = df.dtypes
            
            st.markdown("#### Dataset Overview")
            st.write(f"Rows: {len(df):,} | Columns: {len(df.columns):,}")
            st.write(f"Numeric columns: {len(num_cols):,} | Categorical columns: {len(cat_cols):,}")
            
            # Display statistics
            st.markdown("#### Numeric Column Statistics")
            st.dataframe(numeric_stats, use_container_width=True)
            
            # Skewness analysis
            st.markdown("#### Distribution Analysis")
            skew_df = pd.DataFrame({
                'Column': num_cols,
                'Skewness': [stats.skew(df[col].dropna()) for col in num_cols],
                'Kurtosis': [stats.kurtosis(df[col].dropna()) for col in num_cols]
            })
            
            st.dataframe(skew_df, use_container_width=True)
            
            # Suggestions based on analysis
            st.markdown("#### Transformation Suggestions")
            suggestions = []
            
            # Check for skewness
            for _, row in skew_df.iterrows():
                if abs(row['Skewness']) > 1:
                    suggestions.append(f"Column '{row['Column']}' is {'positively' if row['Skewness'] > 0 else 'negatively'} skewed (skew={row['Skewness']:.2f}). Consider a log or Box-Cox transformation.")
            
            # Check for high correlation
            if len(num_cols) > 1:
                corr_matrix = df[num_cols].corr().abs()
                upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
                highly_correlated = [(column, idx, val) for column in upper.columns for idx, val in upper[column].items() if val > 0.8]
                
                if highly_correlated:
                    suggestions.append(f"Found {len(highly_correlated)} highly correlated pairs (>0.8). Consider dimensionality reduction.")
                    for col1, col2, val in highly_correlated[:5]:  # Show top 5
                        suggestions.append(f"- {col1} & {col2}: correlation = {val:.4f}")
                    if len(highly_correlated) > 5:
                        suggestions.append(f"- ... and {len(highly_correlated) - 5} more")
            
            # Check for categorical columns with high cardinality
            high_cardinality = []
            for col in cat_cols:
                if df[col].nunique() > 10:
                    high_cardinality.append((col, df[col].nunique()))
            
            if high_cardinality:
                suggestions.append("High cardinality categorical columns detected. Consider encoding or grouping:")
                for col, nunique in high_cardinality[:5]:  # Show top 5
                    suggestions.append(f"- {col}: {nunique} unique values")
                if len(high_cardinality) > 5:
                    suggestions.append(f"- ... and {len(high_cardinality) - 5} more")
            
            # Display suggestions
            if suggestions:
                for i, sugg in enumerate(suggestions):
                    st.write(f"{i+1}. {sugg}")
            else:
                st.info("No specific transformation suggestions detected.")
            
            # Plot histograms of numeric columns
            st.markdown("#### Distribution of Numeric Columns")
            selected_col = st.selectbox("Select column for distribution", num_cols)
            
            fig = px.histogram(df, x=selected_col, marginal="box", 
                              title=f"Distribution of {selected_col}")
            st.plotly_chart(fig, use_container_width=True)
            
            # QQ plot to check normality
            qq_fig = go.Figure()
            
            # Get data without NaN
            data = df[selected_col].dropna()
            
            # Calculate QQ data
            quantiles = np.linspace(0.01, 0.99, min(100, len(data)))
            x_quantiles = stats.norm.ppf(quantiles)
            y_quantiles = np.quantile(data, quantiles)
            
            # Add scatter plot
            qq_fig.add_trace(go.Scatter(
                x=x_quantiles,
                y=y_quantiles,
                mode='markers',
                marker=dict(color='blue'),
                name='QQ Plot'
            ))
            
            # Add diagonal line
            min_val = min(x_quantiles.min(), y_quantiles.min())
            max_val = max(x_quantiles.max(), y_quantiles.max())
            qq_fig.add_trace(go.Scatter(
                x=[min_val, max_val],
                y=[min_val, max_val],
                mode='lines',
                line=dict(color='red', dash='dash'),
                name='Normal Line'
            ))
            
            qq_fig.update_layout(
                title=f"QQ Plot for {selected_col}",
                xaxis_title="Theoretical Quantiles",
                yaxis_title="Sample Quantiles",
                showlegend=True
            )
            
            st.plotly_chart(qq_fig, use_container_width=True)
            
            # Normality test
            stat, p_value = stats.shapiro(data) if len(data) <= 5000 else stats.normaltest(data)
            st.write(f"Normality test p-value: {p_value:.6f}")
            if p_value < 0.05:
                st.write("The distribution appears to be non-normal (p < 0.05)")
            else:
                st.write("The distribution appears to be normal (p ≥ 0.05)")
    
    # ─── footer nav buttons ───
    st.markdown("---")
    create,h,select  = st.columns(3)

    with h:
        if st.button("🏠 Home", key="tf_home2"): go_home()
    with create:
        if st.button("Back to Create"):
            st.session_state["page"] = "create_section3"
            st.rerun()
    with select:
        if st.button("Go to Select"):
            st.session_state["page"] = "select_section3"
            st.rerun()

def select_page():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    from sklearn.model_selection import train_test_split
    from xgboost import XGBRegressor, XGBClassifier
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    from sklearn.feature_selection import (
        mutual_info_regression, mutual_info_classif,
        SelectKBest, f_regression, chi2
    )
    from sklearn.inspection import permutation_importance
    from sklearn.linear_model import Lasso, LogisticRegression

    # 1. Load DataFrame
    df = (
        st.session_state.get("transform_data")
        or st.session_state.get("dataframe1")
        or st.session_state.get("D0")
    )
    if df is None or df.empty:
        st.warning("No data available. Run the previous steps first.")
        st.stop()

    # ─────────────────────────────────────────
    # 2. Target & Scenario (inside an expander)
    # ─────────────────────────────────────────
    with st.expander("🎯 Target & Selection Objective", expanded=True):
        col_target, col_scenario = st.columns(2)
        with col_target:
            all_cols = df.columns.tolist()
            target = st.selectbox(
                "Select target variable (Y)",
                all_cols,
                index=len(all_cols) - 1,
                key="select_target"
            )
        with col_scenario:
            st.subheader("Selection Objective")
            scenario = st.selectbox(
                "What’s your primary goal?",
                [
                    "Reduce multicollinearity",
                    "Pick strongest linear predictors",
                    "Capture non‑linear relations",
                    "Model‑based ranking"
                ],
                key="select_scenario"
            )
            guidance = {
                "Reduce multicollinearity":
                    "Use the **VIF** tab: drop features with VIF > 5 to avoid redundant predictors.",
                "Pick strongest linear predictors":
                    "Use the **Correlation** tab: select features with high |r| (e.g. > 0.5).",
                "Capture non‑linear relations":
                    "Use **Mutual Information** or **Univariate F‑test/Chi²** tabs to surface non‑linear dependencies.",
                "Model‑based ranking":
                    "Use **XGBoost Importances** or **Permutation Importance** tabs to keep top‑ranked features."
            }
            st.markdown(
                f"<div style='background-color:#41C185;color:white;"
                f"padding:8px;border-radius:4px;font-family:Inter;'>"
                f"{guidance[scenario]}</div>",
                unsafe_allow_html=True
            )
    st.markdown("---")

    # ─────────────────────────────────────────
    # 3. Filters & Feature Removal (single expander)
    # ─────────────────────────────────────────
    with st.expander("🔍 Filters & Remove Features", expanded=True):
        # Data Filters in 4 columns
        filter_cols = [
            "Market", "Channel", "Region", "Category", "SubCategory",
            "Brand", "Variant", "PackType", "PPG", "PackSize",
            "Year", "Month", "Week"
        ]
        cols = st.columns(4)
        for i, col_name in enumerate(filter_cols):
            if col_name in df.columns:
                with cols[i % 4]:
                    opts = sorted(df[col_name].dropna().unique())
                    sel = st.multiselect(
                        col_name, opts, default=opts, key=f"filter_{col_name}"
                    )
                    df = df[df[col_name].isin(sel)]

        st.markdown("---")

        # Remove Features in 2 columns
        rem_col, info_col = st.columns([3,1])
        with rem_col:
            numeric_feats = [
                c for c in df.columns 
                if c != target and pd.api.types.is_numeric_dtype(df[c])
            ]
            to_remove = st.multiselect(
                "🗑️ Exclude from diagnostics",
                options=numeric_feats,
                default=[],
                key="filter_remove"
            )
            features = [f for f in numeric_feats if f not in to_remove]
        with info_col:
            st.write(f"✅ **{len(features)}** features will be analyzed")

        # Build X/y for downstream tabs
        X_full = df[features].dropna()
        y_full = df.loc[X_full.index, target]

    st.markdown("---")

    # 4. Styling constants
    CHART_COLOR  = "#FFBD59"  # primary accent
    FONT_FAMILY  = "Inter"
    FONT_COLOR   = "#333333"
    SECONDARY_BG = "#FFE7C2"

    def style_fig(fig):
        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_family=FONT_FAMILY,
            font_color=FONT_COLOR,
            title_font_family=FONT_FAMILY,
            title_font_color=FONT_COLOR,
            margin=dict(l=20, r=20, t=30, b=20)
        )
        return fig

    def styled_table(df: pd.DataFrame):
        return df.style.set_table_styles([
            {"selector":"th",
             "props":[("background-color","#41C185"),
                      ("color","white"),
                      ("font-family",FONT_FAMILY),
                      ("padding","6px")]},
            {"selector":"td",
             "props":[("color",FONT_COLOR),
                      ("font-family",FONT_FAMILY),
                      ("padding","6px")]},
        ])

    # 5. Progress bar + Diagnostics Tabs
    num_tabs = 7
    progress = st.progress(0)
    tabs = st.tabs([
        "Correlation", "Multicollinearity (VIF)",
        "Mutual Information", "Univariate F‑test/Chi²",
        "XGBoost Importances", "Permutation Importance",
        "LASSO Selection"
    ])

    # Correlation
    with tabs[0]:
        st.subheader("Correlation with Target")
        st.markdown(
            f"<div style='background-color:{SECONDARY_BG};color:{FONT_COLOR};"
            "padding:6px;border-radius:4px;font-family:Inter;'>"
            "Absolute Pearson r measures linear relationship; values near 1 = strong.</div>",
            unsafe_allow_html=True
        )
        corr_thresh = st.slider("Corr threshold", 0.0, 1.0, 0.0, 0.05)
        corr = df[features + [target]].corr()[target].drop(target).abs().sort_values(ascending=False)
        corr = corr[corr >= corr_thresh]
        fig = px.bar(
            corr.reset_index().rename(columns={"index":"Feature", target:"|r|"}),
            x="Feature", y="|r|",
            color_discrete_sequence=[CHART_COLOR]
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.dataframe(styled_table(corr.to_frame("|r|")), use_container_width=True)
    progress.progress(1/num_tabs)

    # VIF
    with tabs[1]:
        st.subheader("Variance Inflation Factor (VIF)")
        st.markdown(
            f"<div style='background-color:{SECONDARY_BG};color:{FONT_COLOR};"
            "padding:6px;border-radius:4px;font-family:Inter;'>"
            "VIF > 5 flags multicollinearity risk.</div>",
            unsafe_allow_html=True
        )
        vif_thresh = st.slider("VIF threshold", 1.0, 20.0, 5.0, 0.5)
        vif_df = pd.DataFrame({
            "Feature": features,
            "VIF": [variance_inflation_factor(X_full.values, i) for i in range(len(features))]
        }).sort_values("VIF", ascending=False)
        vif_df = vif_df[vif_df["VIF"] <= vif_thresh]
        fig = px.bar(vif_df, x="Feature", y="VIF", color_discrete_sequence=[CHART_COLOR])
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.dataframe(styled_table(vif_df), use_container_width=True)
    progress.progress(2/num_tabs)

    # Mutual Information
    with tabs[2]:
        st.subheader("Mutual Information")
        st.markdown(
            f"<div style='background-color:{SECONDARY_BG};color:{FONT_COLOR};"
            "padding:6px;border-radius:4px;font-family:Inter;'>"
            "MI captures any dependency (linear or non‑linear).</div>",
            unsafe_allow_html=True
        )
        mi = (
            mutual_info_regression(X_full, y_full, random_state=0)
            if pd.api.types.is_numeric_dtype(y_full)
            else mutual_info_classif(X_full, y_full, random_state=0)
        )
        mi_ser = pd.Series(mi, index=features).sort_values(ascending=False)
        mi_thresh = st.slider("MI threshold", 0.0, float(mi_ser.max()), 0.0)
        mi_ser = mi_ser[mi_ser >= mi_thresh]
        fig = px.bar(
            mi_ser.reset_index().rename(columns={"index":"Feature", 0:"MI"}),
            x="Feature", y="MI",
            color_discrete_sequence=[CHART_COLOR]
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.dataframe(styled_table(mi_ser.to_frame("MI")), use_container_width=True)
    progress.progress(3/num_tabs)

    # Univariate F‑test / Chi²
    with tabs[3]:
        st.subheader("Univariate Test Scores")
        st.markdown(
            f"<div style='background-color:{SECONDARY_BG};color:{FONT_COLOR};"
            "padding:6px;border-radius:4px;font-family:Inter;'>"
            "F‑test/χ²: measures individual predictive power.</div>",
            unsafe_allow_html=True
        )
        X_proc = X_full.clip(lower=0) if not pd.api.types.is_numeric_dtype(y_full) else X_full
        scorer = f_regression if pd.api.types.is_numeric_dtype(y_full) else chi2
        selector = SelectKBest(score_func=scorer, k="all").fit(X_proc, y_full)
        scores = pd.Series(selector.scores_, index=features).sort_values(ascending=False)
        score_thresh = st.slider("Score threshold", 0.0, float(scores.max()), 0.0)
        scores = scores[scores >= score_thresh]
        fig = px.bar(
            scores.reset_index().rename(columns={"index":"Feature", 0:"Score"}),
            x="Feature", y="Score",
            color_discrete_sequence=[CHART_COLOR]
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.dataframe(styled_table(scores.to_frame("Score")), use_container_width=True)
    progress.progress(4/num_tabs)

    # XGBoost Importances
    with tabs[4]:
        st.subheader("XGBoost Importances")
        st.markdown(
            f"<div style='background-color:{SECONDARY_BG};color:{FONT_COLOR};"
            "padding:6px;border-radius:4px;font-family:Inter;'>"
            "Tree‑based ranking by split importance.</div>",
            unsafe_allow_html=True
        )
        test_pct = st.slider("Test set size (%)", 10, 50, 20)
        X_train, X_test, y_train, y_test = train_test_split(
            df[features], df[target], test_size=test_pct/100, random_state=42
        )
        model = (
            XGBRegressor(use_label_encoder=False, eval_metric="rmse")
            if pd.api.types.is_numeric_dtype(y_train)
            else XGBClassifier(use_label_encoder=False, eval_metric="logloss")
        )
        model.fit(X_train, y_train)
        imp = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
        fig = px.bar(
            imp.reset_index().rename(columns={"index":"Feature", 0:"Importance"}),
            x="Feature", y="Importance",
            color_discrete_sequence=[CHART_COLOR]
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.dataframe(styled_table(imp.to_frame("Importance")), use_container_width=True)
    progress.progress(5/num_tabs)

    # Permutation Importance
    with tabs[5]:
        st.subheader("Permutation Importance")
        st.markdown(
            f"<div style='background-color:{SECONDARY_BG};color:{FONT_COLOR};"
            "padding:6px;border-radius:4px;font-family:Inter;'>"
            "Performance drop when each feature is shuffled.</div>",
            unsafe_allow_html=True
        )
        perm = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=0)
        perm_ser = pd.Series(perm.importances_mean, index=features).sort_values(ascending=False)
        fig = px.bar(
            perm_ser.reset_index().rename(columns={"index":"Feature", 0:"PermImp"}),
            x="Feature", y="PermImp",
            color_discrete_sequence=[CHART_COLOR]
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.dataframe(styled_table(perm_ser.to_frame("PermImp")), use_container_width=True)
    progress.progress(6/num_tabs)

    # LASSO Selection
    with tabs[6]:
        st.subheader("LASSO Selection")
        st.markdown(
            f"<div style='background-color:{SECONDARY_BG};color:{FONT_COLOR};"
            "padding:6px;border-radius:4px;font-family:Inter;'>"
            "LASSO shrinks less important features to zero.</div>",
            unsafe_allow_html=True
        )
        alpha = st.slider("α (regularization strength)", 0.01, 1.0, 0.1, 0.01)
        lasso_model = (
            Lasso(alpha=alpha, random_state=42)
            if pd.api.types.is_numeric_dtype(y_full)
            else LogisticRegression(C=1/alpha, max_iter=1000)
        )
        lasso_model.fit(X_full, y_full)
        coefs = pd.Series(np.abs(lasso_model.coef_.ravel()), index=features).sort_values(ascending=False)
        fig = px.bar(
            coefs.reset_index().rename(columns={"index":"Feature", 0:"|coef|"}),
            x="Feature", y="|coef|",
            color_discrete_sequence=[CHART_COLOR]
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.dataframe(styled_table(coefs.to_frame("|coef|")), use_container_width=True)
    progress.progress(7/num_tabs)

    # Clean up progress bar
    progress.empty()
        
    st.markdown("---")
    create, home,build  = st.columns(3)

    with home:
        if st.button("Home"):
            go_home()
    with create:
        if st.button("Back to Transform"):
            st.session_state["page"] = "transform_section3"
            st.rerun()
    with build:
        if st.button("Go to Build"):
            st.session_state.page = "Build_1"
            st.rerun()






def build_page():
    """
    COMPLETE: Price/Promo Elasticity code + Model Selection & Filtering in a single page.

    This function:
      1) Runs the aggregator pipeline, modeling, storing results in session_state.
      2) Lets the user filter & select models with st_aggrid.
      3) Displays contribution, radar, and bar charts.
      4) Allows final saving of models.
    """

    import streamlit as st
    import pandas as pd
    import numpy as np
    import math
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    from statsmodels.tsa.seasonal import STL
    from pykalman import KalmanFilter

    from sklearn.base import BaseEstimator, RegressorMixin
    from sklearn.model_selection import KFold
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, BayesianRidge
    from sklearn.metrics import r2_score, mean_absolute_percentage_error

    from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

    # ─────────────────────────────────────────────────────────────────────────────
    # 1) NAVIGATION BUTTONS
    # ─────────────────────────────────────────────────────────────────────────────
    nav_home,  nav_transform,nav_model = st.columns(3)

    with nav_home:
        if st.button("🏠 Home", key="build_nav_home"):
            go_home()

    with nav_transform:
        if st.button("🔄 Back to select", key="build_nav_transform"):
            go_to("select_section3")
    with nav_model:
        if st.button("🧪 Evaluate", key="build_nav_model"):
            go_to("model_selection")


    # ─── END DATE FILTER ───────────────────────────────────────────




    # ─────────────────────────────────────────────────────────────────────────────
    # 2) CUSTOM MODEL CLASSES
    # ─────────────────────────────────────────────────────────────────────────────
    class CustomConstrainedRidge(BaseEstimator, RegressorMixin):
        def __init__(self, l2_penalty=0.1, learning_rate=0.001, iterations=100000,
                     adam=False, beta1=0.9, beta2=0.999, epsilon=1e-8):
            self.learning_rate = learning_rate
            self.iterations = iterations
            self.l2_penalty = l2_penalty
            self.adam = adam
            self.beta1 = beta1
            self.beta2 = beta2
            self.epsilon = epsilon

        def fit(self, X, Y, feature_names):
            self.m, self.n = X.shape
            self.W = np.zeros(self.n)
            self.b = 0
            self.X = X
            self.Y = Y
            self.feature_names = feature_names
            self.rpi_ppu_indices = [
                i for i, name in enumerate(feature_names)
                if name.endswith("_RPI") or name == "PPU"
            ]
            self.d1_index = next((i for i, name in enumerate(feature_names) if name == "D1"), None)

            if self.adam:
                self.m_W = np.zeros(self.n)
                self.v_W = np.zeros(self.n)
                self.m_b = 0
                self.v_b = 0
                self.t = 0

            for _ in range(self.iterations):
                self.update_weights()

            self.intercept_ = self.b
            self.coef_ = self.W
            return self

        def update_weights(self):
            Y_pred = self.predict(self.X)
            grad_w = (
                -(2 * (self.X.T).dot(self.Y - Y_pred))
                + 2 * self.l2_penalty * self.W
            ) / self.m
            grad_b = -(2 / self.m) * np.sum(self.Y - Y_pred)

            if self.adam:
                self.t += 1
                self.m_W = self.beta1 * self.m_W + (1 - self.beta1) * grad_w
                self.m_b = self.beta1 * self.m_b + (1 - self.beta1) * grad_b
                self.v_W = self.beta2 * self.v_W + (1 - self.beta2) * (grad_w ** 2)
                self.v_b = self.beta2 * self.v_b + (1 - self.beta2) * (grad_b ** 2)

                m_W_hat = self.m_W / (1 - self.beta1 ** self.t)
                m_b_hat = self.m_b / (1 - self.beta1 ** self.t)
                v_W_hat = self.v_W / (1 - self.beta2 ** self.t)
                v_b_hat = self.v_b / (1 - self.beta2 ** self.t)

                self.W -= self.learning_rate * m_W_hat / (np.sqrt(v_W_hat) + self.epsilon)
                self.b -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)
            else:
                self.W -= self.learning_rate * grad_w
                self.b -= self.learning_rate * grad_b

            # Constraints
            for i in range(self.n):
                if i in self.rpi_ppu_indices and self.W[i] > 0:
                    self.W[i] = 0
                if i == self.d1_index and self.W[i] < 0:
                    self.W[i] = 0

        def predict(self, X):
            return X.dot(self.W) + self.b


    class ConstrainedLinearRegression(BaseEstimator, RegressorMixin):
        def __init__(self, learning_rate=0.001, iterations=10000,
                     adam=False, beta1=0.9, beta2=0.999, epsilon=1e-8):
            self.learning_rate = learning_rate
            self.iterations = iterations
            self.adam = adam
            self.beta1 = beta1
            self.beta2 = beta2
            self.epsilon = epsilon

        def fit(self, X, Y, feature_names):
            self.m, self.n = X.shape
            self.W = np.zeros(self.n)
            self.b = 0
            self.X = X
            self.Y = Y
            self.feature_names = feature_names
            self.rpi_ppu_indices = [
                i for i, name in enumerate(feature_names)
                if name.endswith('_RPI') or name == 'PPU'
            ]
            self.d1_index = next((i for i, name in enumerate(feature_names) if name == 'D1'), None)

            if self.adam:
                self.m_W = np.zeros(self.n)
                self.v_W = np.zeros(self.n)
                self.m_b = 0
                self.v_b = 0
                self.t = 0

            for _ in range(self.iterations):
                self.update_weights()

            self.intercept_ = self.b
            self.coef_ = self.W
            return self

        def update_weights(self):
            Y_pred = self.predict(self.X)
            dW = -(2 * self.X.T.dot(self.Y - Y_pred)) / self.m
            db = -2 * np.sum(self.Y - Y_pred) / self.m

            if self.adam:
                self.t += 1
                self.m_W = self.beta1 * self.m_W + (1 - self.beta1) * dW
                self.m_b = self.beta1 * self.m_b + (1 - self.beta1) * db
                self.v_W = self.beta2 * self.v_W + (1 - self.beta2) * (dW ** 2)
                self.v_b = self.beta2 * self.v_b + (1 - self.beta2) * (db ** 2)

                m_W_hat = self.m_W / (1 - self.beta1 ** self.t)
                m_b_hat = self.m_b / (1 - self.beta1 ** self.t)
                v_W_hat = self.v_W / (1 - self.beta2 ** self.t)
                v_b_hat = self.v_b / (1 - self.beta2 ** self.t)

                self.W -= self.learning_rate * m_W_hat / (np.sqrt(v_W_hat) + self.epsilon)
                self.b -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)
            else:
                self.W -= self.learning_rate * dW
                self.b -= self.learning_rate * db

            # enforce constraints
            self.W[self.rpi_ppu_indices] = np.minimum(self.W[self.rpi_ppu_indices], 0)
            if self.d1_index is not None:
                self.W[self.d1_index] = max(self.W[self.d1_index], 0)

        def predict(self, X):
            return X.dot(self.W) + self.b

    # ─────────────────────────────────────────────────────────────────────────────
    # 3) MODELS DICTIONARY
    # ─────────────────────────────────────────────────────────────────────────────
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Lasso Regression": Lasso(alpha=0.1),
        "ElasticNet Regression": ElasticNet(alpha=0.1, l1_ratio=0.5),
        "Bayesian Ridge Regression": BayesianRidge(),
        "Custom Constrained Ridge": CustomConstrainedRidge(l2_penalty=0.1, learning_rate=0.001, iterations=10000),
        "Constrained Linear Regression": ConstrainedLinearRegression(learning_rate=0.001, iterations=10000)
    }
   
    # ─────────────────────────────────────────────────────────────────────────────
    # 4) HELPER FUNCTIONS
    # ─────────────────────────────────────────────────────────────────────────────
    def safe_mape(y_true, y_pred):
        y_true = np.array(y_true, dtype=float)
        y_pred = np.array(y_pred, dtype=float)
        nonzero_mask = (y_true != 0)
        y_true_nonzero = y_true[nonzero_mask]
        y_pred_nonzero = y_pred[nonzero_mask]
        if len(y_true_nonzero) == 0:
            return float("nan")
        return np.mean(np.abs((y_true_nonzero - y_pred_nonzero) / y_true_nonzero)) * 100
    
 
    
 
    def run_full_pipeline(raw_df, group_keys, pivot_keys, use_kalman=True, use_ratio_flag=False):
        """
        Cleans data, computes PPU, brand shares, outliers, etc.
        Returns a final df with 'FilteredVolume' for modeling.
        """
        import streamlit as st
        import pandas as pd
        import numpy as np
        from statsmodels.tsa.seasonal import STL
        from pykalman import KalmanFilter

        st.write("Running FULL PIPELINE ...")

        # ── 1) Identify & convert your date column ─────────────────────────────────
        date_col = next((c for c in raw_df.columns if c.strip().lower() == 'date'), None)
        if not date_col:
            st.error("DataFrame must have a 'date' column.")
            st.stop()
        raw_df[date_col] = pd.to_datetime(raw_df[date_col], errors='coerce')
        all_dates = raw_df[date_col].dt.date.dropna()
        if all_dates.empty:
            st.error("No valid dates in your data.")
            st.stop()
        min_date, max_date = all_dates.min(), all_dates.max()



        # ── 3) Helper functions ────────────────────────────────────────────────────
        def adjust_volume_column(df, chosen_col):
            df = df.copy()
            c = chosen_col.strip().lower()
            if c == 'volume':
                df.drop(columns=['VolumeUnits'], errors='ignore', inplace=True)
            elif c == 'volumeunits':
                df.drop(columns=['Volume'], errors='ignore', inplace=True)
                df.rename(columns={'VolumeUnits': 'Volume'}, inplace=True, errors='ignore')
            else:
                st.warning(f"Unrecognized volume column '{chosen_col}'.")
            return df

        def compute_category_weighted_price(df, d_date, d_channel):
            df = df.copy()
            df[d_date] = pd.to_datetime(df[d_date], errors='coerce')
            grp = df.groupby([d_channel, d_date])
            return (
                grp.apply(lambda g: (g['PPU']*g['Volume']).sum()/g['Volume'].sum()
                        if g['Volume'].sum() else 0)
                .reset_index(name='Cat_Weighted_Price')
            )

        def compute_cat_down_up(df, d_date, d_channel, l0=None, l2=None):
            df = df.copy()
            df[d_date] = pd.to_datetime(df[d_date], errors='coerce')
            mean_keys = [d_channel] + ([l0] if l0 else []) + ([l2] if l2 else [])
            daily_keys = [d_channel, d_date] + ([l0] if l0 else []) + ([l2] if l2 else [])
            mean_df = (
                df.groupby(mean_keys)['PPU']
                .mean().reset_index()
                .rename(columns={'PPU':'mean_ppu'})
            )
            daily = (
                df.groupby(daily_keys)['Volume']
                .sum().reset_index()
                .merge(mean_df, on=mean_keys, how='left')
            )
            total = (
                daily.groupby([d_channel, d_date])['Volume']
                    .sum().reset_index().rename(columns={'Volume':'total_volume'})
            )
            daily = daily.merge(total, on=[d_channel, d_date], how='left')
            daily['weighted_contrib'] = daily['mean_ppu'] * (daily['Volume']/daily['total_volume'])
            return (
                daily.groupby([d_channel, d_date])['weighted_contrib']
                    .sum().reset_index()
                    .rename(columns={'weighted_contrib':'Cat_Down_Up'})
            )

        # ── 4) Adjust volume column ────────────────────────────────────────────────
        df_proc = raw_df.copy()   # start with the already-filtered data
        selected_volume = st.session_state.get("selected_volume", "Volume")
        df_proc = adjust_volume_column(df_proc, selected_volume)

        # ── 5) Identify date & channel columns ────────────────────────────────────
        d_date = next((c for c in df_proc.columns if c.strip().lower()=='date'), date_col)
        d_channel = next((c for c in df_proc.columns if c.strip().lower()=='channel'), 'Channel')

        # ── 6) Aggregate to PPU ───────────────────────────────────────────────────
        if "Price" in df_proc.columns and "SalesValue" in df_proc.columns:
            agg_df = (
                df_proc.groupby(group_keys)
                    .agg({"Volume":"sum","Price":"mean","SalesValue":"sum"})
                    .reset_index()
                    .rename(columns={"Price":"PPU"})
            )
        elif "Price" in df_proc.columns:
            agg_df = (
                df_proc.groupby(group_keys)
                    .agg({"Volume":"sum","Price":"mean"})
                    .reset_index()
                    .rename(columns={"Price":"PPU"})
            )
        else:
            agg_df = (
                df_proc.groupby(group_keys)
                    .agg({"Volume":"sum","SalesValue":"sum"})
                    .reset_index()
            )
            agg_df["PPU"] = np.where(
                agg_df["Volume"] != 0,
                agg_df["SalesValue"]/agg_df["Volume"],
                0
            )

        # Add Year/Month/Week and a datetime64 'Date' for internal joins
        agg_df[d_date] = pd.to_datetime(agg_df[d_date], errors='coerce')
        agg_df['Year']  = agg_df[d_date].dt.year
        agg_df['Month'] = agg_df[d_date].dt.month
        agg_df['Week']  = agg_df[d_date].dt.isocalendar().week
        agg_df['Date']  = agg_df[d_date].dt.normalize()    # datetime64[ns]

        # ── 7) Pivot competitor PPUs → flatten → merge → compute RPI ─────────────
        if pivot_keys:
            pivot_df = agg_df.pivot_table(
                index=[d_date, d_channel],
                columns=pivot_keys,
                values='PPU'
            )
            pivot_df.columns = [
                "_".join(map(str,col)) + "_PPU" if isinstance(col,tuple)
                else f"{col}_PPU"
                for col in pivot_df.columns
            ]
            pivot_flat = pivot_df.reset_index()
            agg_df = agg_df.merge(pivot_flat, on=[d_date, d_channel], how='left')

            # zero self comparisons
            if len(pivot_keys)==1:
                pk=pivot_keys[0]
                for val in pivot_flat[pk].unique():
                    agg_df.loc[agg_df[pk]==val, f"{val}_PPU"] = np.nan
            else:
                for col in pivot_flat.columns:
                    if col.endswith("_PPU"):
                        parts = col[:-4].split("_", len(pivot_keys)-1)
                        mask = True
                        for i, pk in enumerate(pivot_keys):
                            mask &= (agg_df[pk] == parts[i])
                        agg_df.loc[mask, col] = np.nan

            # compute RPI and drop PPUs
            for ppu in [c for c in agg_df if c.endswith("_PPU")]:
                agg_df[ppu.replace("_PPU","_RPI")] = np.where(
                    agg_df[ppu].notna() & (agg_df[ppu]!=0),
                    agg_df["PPU"]/agg_df[ppu], 0
                )
            agg_df.drop(columns=[c for c in agg_df if c.endswith("_PPU")], inplace=True)

        # ── 8) Category & market‐share metrics ────────────────────────────────────
        catvol = (
            agg_df.groupby([d_channel, d_date])['Volume']
                .sum().reset_index(name='CatVol')
        )
        agg_df = agg_df.merge(catvol, on=[d_channel, d_date], how='left')
        agg_df['NetCatVol'] = agg_df['CatVol'] - agg_df['Volume']

        # Prepare brand_totals for later
        keys_for_brand = [d_channel] + (pivot_keys or [])
        brand_totals = (
            raw_df.groupby(keys_for_brand)['SalesValue']
                .sum().reset_index(name='BrandSales')
        )
        channel_totals = (
            raw_df.groupby(d_channel)['SalesValue']
                .sum().reset_index(name='ChannelSales')
        )
        brand_totals = brand_totals.merge(channel_totals, on=[d_channel], how='left')
        brand_totals['MarketShare_overall'] = (
            brand_totals['BrandSales']/brand_totals['ChannelSales']*100
        ).fillna(0)

        # ── 9) Seasonality & price trend ─────────────────────────────────────────
        season = (
            agg_df.groupby([d_channel,'Month'])['Volume']
                .mean().reset_index(name='CatSeasonality')
        )
        agg_df = agg_df.merge(season, on=[d_channel,'Month'], how='left')

        cwp = compute_category_weighted_price(agg_df, d_date, d_channel)
        cdu = compute_cat_down_up(
            agg_df, d_date, d_channel,
            pivot_keys[0] if pivot_keys else None,
            pivot_keys[1] if len(pivot_keys or [])>1 else None
        )
        trend = pd.merge(cwp, cdu, on=[d_channel, d_date], how='inner')
        trend['mean_cat_down_up'] = trend.groupby(d_channel)['Cat_Down_Up'].transform('mean')
        trend['Cat_Price_trend_over_time'] = (
            trend['Cat_Weighted_Price'] *
            (trend['mean_cat_down_up']/trend['Cat_Down_Up'])
        )
        agg_df = agg_df.merge(
            trend[[d_channel,d_date,'Cat_Weighted_Price','Cat_Down_Up','Cat_Price_trend_over_time']],
            on=[d_channel,d_date], how='left'
        )

        # ── 10) Outlier detection ─────────────────────────────────────────────────
        final_df = agg_df.copy().set_index(d_date)
        final_df[['residual','z_score_residual','is_outlier']] = np.nan, np.nan, 0
        outlier_keys = [d_channel] + (pivot_keys or [])
        for name, grp in final_df.groupby(outlier_keys):
            if len(grp)<2: continue
            grp0 = grp.reset_index()
            try:
                res = STL(grp0['Volume'], seasonal=13, period=13).fit()
                grp0['residual'] = res.resid
                grp0['z_score_residual'] = (
                    (grp0['residual']-grp0['residual'].mean())/grp0['residual'].std()
                )
                grp0['is_outlier'] = (grp0['z_score_residual'].abs()>3).astype(int)
                for _, row in grp0.iterrows():
                    dt = row[d_date]
                    final_df.at[dt,'residual'] = row['residual']
                    final_df.at[dt,'z_score_residual'] = row['z_score_residual']
                    final_df.at[dt,'is_outlier'] = row['is_outlier']
            except Exception as e:
                st.warning(f"STL failed for {name}: {e}")

        final_df.reset_index(inplace=True)
        final_df.sort_values(by=d_date, inplace=True)

        # ── 11) Kalman smoothing ───────────────────────────────────────────────────
        if use_kalman:
            def apply_kf(vals):
                kf = KalmanFilter(initial_state_mean=vals[0], n_dim_obs=1)
                means,_ = kf.filter(vals)
                return means.flatten()

            final_df['FilteredVolume'] = np.nan
            for _, grp in final_df.groupby([d_channel] + (pivot_keys or [])):
                grp_s = grp.sort_values(d_date).reset_index()
                filt = apply_kf(grp_s['Volume'].values)
                final_df.loc[grp_s['index'],'FilteredVolume'] = filt
        else:
            final_df['FilteredVolume'] = final_df['Volume']

        if use_ratio_flag:
            final_df['FilteredVolume'] = np.where(
                final_df['CatVol']!=0,
                final_df['FilteredVolume']/final_df['CatVol'],
                0
            )

        final_df.fillna(0, inplace=True)

        # ── 12) Merge back extra raw columns ────────────────────────────────────────
        raw_copy = raw_df.copy()
        raw_copy[date_col] = pd.to_datetime(raw_copy[date_col], errors='coerce')
        # both sides use datetime64 normalized to midnight
        raw_copy['Date'] = raw_copy[date_col].dt.normalize()
        final_df['Date']   = final_df['Date'].dt.normalize()

        merge_keys = [d_channel, 'Date'] + (pivot_keys or [])
        used = list(final_df.columns) + merge_keys
        extras = [c for c in raw_copy.columns if c not in used]
        extra_df = raw_copy[merge_keys + extras].drop_duplicates(subset=merge_keys)

        final_df = final_df.merge(extra_df, on=merge_keys, how='left').fillna(0)

        # ── 13) Attach market share as 'Contribution' ─────────────────────────────
        final_df = final_df.merge(
            brand_totals[keys_for_brand + ['MarketShare_overall']],
            on=keys_for_brand, how='left'
        )
        final_df.rename(columns={'MarketShare_overall':'Contribution'}, inplace=True)
        final_df['Contribution'] = final_df['Contribution'].fillna(0)

        return final_df


    # ────────────────────────────────────────────────────────────────────────
    #  PER‑FOLD MODEL PIPELINE  •  uses in‑fold own‑price for MCV
    # ────────────────────────────────────────────────────────────────────────
    def run_model_pipeline(
            final_df,
            grouping_keys,
            X_columns,
            target_col,
            k_folds,
            chosen_std_cols
        ):
        """
        Returns one row per fold with columns:
            grouping_keys + ["Model","Fold","CSF","MCV","SelfElasticity",
                            "PPU_at_Elasticity",
                            "B0 (Original)","R2 Train","R2 Test","MAPE Train","MAPE Test",
                            "MSE Train","MSE Test",
                            <mean‑X columns>, <Beta_… columns>, "ElasticityFlag"]
        Fold numbering restarts at 1 for every model‑within‑group.
        """

        import numpy as np, pandas as pd, streamlit as st
        from sklearn.model_selection import KFold
        from sklearn.preprocessing import StandardScaler
        from sklearn.metrics import r2_score

        rows, preds_records = [], []          # collect results here

        # helper to append Beta_… cols
        def _add_beta_cols(d, names, coefs):
            for c, b in zip(names, coefs):
                d[f"Beta_{c}"] = b

        grouped = final_df.groupby(grouping_keys) if grouping_keys else [((None,), final_df)]

        for gvals, gdf in grouped:

            gvals = (gvals,) if not isinstance(gvals, tuple) else gvals
            contrib = gdf.get("Contribution", np.nan).iloc[0]

            present_cols = [c for c in X_columns if c in gdf.columns]
            if len(present_cols) < len(X_columns):
                st.warning(f"Skipping {gvals} — missing predictors.");  continue

            X_full = gdf[present_cols].fillna(0).copy()
            y_full = gdf[target_col].copy()
            if len(X_full) < k_folds:
                continue

            kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)

            for mname, mdl in models.items():
                fold_id = 0                                         # restart per model

                for tr_idx, te_idx in kf.split(X_full, y_full):
                    fold_id += 1

                    X_tr, X_te = X_full.iloc[tr_idx].copy(), X_full.iloc[te_idx].copy()
                    y_tr, y_te = y_full.iloc[tr_idx], y_full.iloc[te_idx]

                    # optional standardisation
                    scaler = {}
                    if chosen_std_cols:
                        sc = StandardScaler().fit(X_tr[chosen_std_cols])
                        X_tr[chosen_std_cols] = sc.transform(X_tr[chosen_std_cols])
                        X_te[chosen_std_cols] = sc.transform(X_te[chosen_std_cols])
                        scaler = {c: (m, s) for c, m, s
                                in zip(chosen_std_cols, sc.mean_, sc.scale_)}

                    # fit / predict
                    if mname in ["Custom Constrained Ridge", "Constrained Linear Regression"]:
                        mdl.fit(X_tr.values, y_tr.values, X_tr.columns.tolist())
                        y_tr_pred, y_te_pred = mdl.predict(X_tr.values), mdl.predict(X_te.values)
                        B0_std, B1_std = mdl.intercept_, mdl.coef_
                    else:
                        mdl.fit(X_tr, y_tr)
                        y_tr_pred, y_te_pred = mdl.predict(X_tr), mdl.predict(X_te)
                        B0_std, B1_std = mdl.intercept_, mdl.coef_

                    # metrics
                    r2_tr, r2_te = r2_score(y_tr, y_tr_pred), r2_score(y_te, y_te_pred)
                    mape_tr, mape_te = safe_mape(y_tr, y_tr_pred), safe_mape(y_te, y_te_pred)
                    mse_tr,  mse_te  = np.mean((y_tr - y_tr_pred)**2), np.mean((y_te - y_te_pred)**2)

                    # back‑transform coefs if std‑ised
                    raw_int, raw_coefs = B0_std, B1_std.copy()
                    for i, col in enumerate(present_cols):
                        if col in scaler:
                            mu, sd = scaler[col]
                            raw_coefs[i] = raw_coefs[i] / sd
                            raw_int     -= raw_coefs[i] * mu

                    # elasticity
                    mean_x = X_full.mean(numeric_only=True).to_dict()
                    q_hat  = raw_int + sum(raw_coefs[i] * mean_x.get(c, 0) for i, c in enumerate(present_cols))

                    dQdP = 0.0
                    if "PPU" in present_cols:
                        dQdP += raw_coefs[present_cols.index("PPU")]
                    for c in [c for c in present_cols if c.endswith("_RPI")]:
                        idx, ratio = present_cols.index(c), mean_x.get(c, 0)
                        P_own = mean_x.get("PPU", 0)
                        if ratio and P_own:
                            dQdP += raw_coefs[idx] / (P_own / ratio)

                    self_elas = (dQdP * mean_x.get("PPU", 0) / q_hat
                                if (q_hat > 0 and mean_x.get("PPU", 0) > 0) else np.nan)
                    elas_flag = "ELASTICITY>100" if np.isfinite(self_elas) and abs(self_elas) > 100 else ""

                    # assemble row
                    d = {k: v for k, v in zip(grouping_keys, gvals)}
                    d.update({
                        "Model": mname,
                        "Fold":  fold_id,
                        "SelfElasticity": self_elas,
                        "PPU_at_Elasticity": mean_x.get("PPU", np.nan),
                        "B0 (Original)": raw_int,
                        "R2 Train": r2_tr, "R2 Test": r2_te,
                        "MAPE Train": mape_tr, "MAPE Test": mape_te,
                        "MSE Train": mse_tr,  "MSE Test": mse_te,
                        "ElasticityFlag": elas_flag,
                        "Contribution": contrib
                    })
                    # mean‑X cols
                    for c, v in mean_x.items(): d[c] = v
                    # Beta_… cols
                    _add_beta_cols(d, present_cols, raw_coefs)
                    rows.append(d)

                    # predictions
                    pr = gdf.loc[X_te.index].copy()
                    pr["Actual"], pr["Predicted"] = y_te.values, y_te_pred
                    pr["Model"], pr["Fold"] = mname, fold_id
                    preds_records.append(pr)

        if not rows:
            st.warning("No fold‑level results.");  return None, None

        df = pd.DataFrame(rows)

        # KPI columns
        df["CSF"] = df["SelfElasticity"].apply(lambda x: 1 - (1/x) if x and x != 0 else np.nan)
        df["MCV"] = df["CSF"] * df["PPU_at_Elasticity"]

        # tidy order (optional)
        front = grouping_keys + ["Model","Fold","CSF","MCV","SelfElasticity","PPU_at_Elasticity"]
        metric_block = ["B0 (Original)","R2 Train","R2 Test","MAPE Train","MAPE Test",
                        "MSE Train","MSE Test","Contribution","ElasticityFlag"]
        mean_x_cols  = [c for c in df.columns
                        if c not in front + metric_block and not c.startswith("Beta_")]
        beta_cols    = [c for c in df.columns if c.startswith("Beta_")]
        df = df[front + metric_block + mean_x_cols + beta_cols]

        df.sort_values(by=grouping_keys + ["Model","Fold"], inplace=True, ignore_index=True)

        preds_df = pd.concat(preds_records, ignore_index=True) if preds_records else None
        return df, preds_df



    # ─────────────────────────────────────────────────────────────────────────────
    # 5) MAIN STREAMLIT UI LOGIC
    # ─────────────────────────────────────────────────────────────────────────────
    st.subheader("Price/Promo Elasticity – Aggregation & Modeling")

    # Retrieve main data
    dataframe = st.session_state.get("D0", None)
    if dataframe is None:
        st.error("No data found (st.session_state['D0']). Please upload a file.")
        return


    # ─── START DATE FILTER ─────────────────────────────────────────
    date_col = next(c for c in dataframe.columns if c.strip().lower() == "date")
    dataframe[date_col] = pd.to_datetime(dataframe[date_col], errors="coerce")

    valid_dates = dataframe[date_col].dt.date.dropna()
    min_date, max_date = valid_dates.min(), valid_dates.max()

    if "filter_start_date" not in st.session_state:
        st.session_state["filter_start_date"] = min_date
    if "filter_end_date" not in st.session_state:
        st.session_state["filter_end_date"] = max_date

    st.sidebar.subheader("⏳ Time Period Filter")
    st.sidebar.date_input(
        "Start Date",
        value=st.session_state["filter_start_date"],
        min_value=min_date,
        max_value=max_date,
        key="filter_start_date",
    )
    st.sidebar.date_input(
        "End Date",
        value=st.session_state["filter_end_date"],
        min_value=min_date,
        max_value=max_date,
        key="filter_end_date",
    )

    df_filtered = dataframe[
        (dataframe[date_col].dt.date >= st.session_state["filter_start_date"])
        & (dataframe[date_col].dt.date <= st.session_state["filter_end_date"])
    ].copy()

    if df_filtered.empty:
        st.error("No data in the chosen date range.")
        return
    # ─── END DATE FILTER ───────────────────────────────────────────
    
        # ─── RESET CACHES WHEN DATE FILTER CHANGES ─────────────────────
    start_new = st.session_state["filter_start_date"]
    end_new   = st.session_state["filter_end_date"]

    # remember last dates across reruns
    if "last_filter_start" not in st.session_state:
        st.session_state["last_filter_start"] = start_new
        st.session_state["last_filter_end"]   = end_new

    # if user changed either start or end, clear cached results
    if (start_new != st.session_state["last_filter_start"] or
        end_new   != st.session_state["last_filter_end"]):

        st.session_state["last_filter_start"] = start_new
        st.session_state["last_filter_end"]   = end_new

        # wipe cached aggregations & model outputs
        st.session_state["final_df"]          = None
        st.session_state["combined_results"]  = None
        st.session_state["predictions_df"]    = None
        st.session_state["type2_dfs"]         = {}
        st.session_state["type2_results"]     = {}
        st.session_state["type2_predictions"] = {}
    # ─── END RESET BLOCK ───────────────────────────────────────────
    
    # ─── Choose aggregator parameters ───────────────────────────────
    col1, col2 = st.columns(2)

    # Volume selector
    with col1:
        vol_options = []
        if "Volume" in dataframe.columns:
            vol_options.append("Volume")
        if "VolumeUnits" in dataframe.columns:
            vol_options.append("VolumeUnits")
        selected_volume = st.selectbox("Select Volume column:", options=vol_options)
        st.session_state["selected_volume"] = selected_volume

    # Model-type selector
    with col2:
        model_type = st.radio(
            "Select Model Type:",
            options=["Type 1 (Three Distinct Keys)", "Type 2 (Multiple Single Keys)"]
        )

    # <-- NEW LOGIC: If user changes model_type, reset old stored results
    if "previous_model_type" not in st.session_state:
        st.session_state["previous_model_type"] = model_type
    if st.session_state["previous_model_type"] != model_type:
        st.session_state["previous_model_type"] = model_type
        st.session_state["final_df"] = None
        st.session_state["combined_results"] = None
        st.session_state["predictions_df"] = None
        st.session_state["type2_dfs"] = {}
        st.session_state["type2_results"] = {}
        st.session_state["type2_predictions"] = {}

    use_kalman = st.checkbox("Use Kalman Filter?", value=True)
    use_ratio  = st.checkbox("Use FilteredVolume as Ratio?", value=False)

    if model_type == "Type 1 (Three Distinct Keys)":
        possible_keys = [c for c in ["Brand","Variant","PackType","PPG","PackSize"] if c in dataframe.columns]
        c1,c2,c3 = st.columns(3)
        with c1:
            key1 = st.selectbox("Key 1:", options=possible_keys)
        with c2:
            remainA = [x for x in possible_keys if x!=key1]
            key2 = st.selectbox("Key 2:", options=remainA)
        with c3:
            remainB = [x for x in remainA if x!=key2]
            key3 = st.selectbox("Key 3:", options=remainB)

        selected_keys = [key1,key2,key3]
        group_keys = [
            next((c for c in dataframe.columns if c.strip().lower()=='date'), 'date'),
            next((c for c in dataframe.columns if c.strip().lower()=='channel'),'Channel')
        ] + selected_keys

        # RUN FULL PIPELINE only if we haven't done it yet (or if user wants to refresh)
        if "final_df" not in st.session_state or st.session_state["final_df"] is None:
            # Actually run the aggregator
            final_agg_df = run_full_pipeline(
                df_filtered,
                group_keys=group_keys,
                pivot_keys=selected_keys,
                use_kalman=use_kalman,
                use_ratio_flag=use_ratio
            )
            st.session_state["final_df"] = final_agg_df
        else:
            final_agg_df = st.session_state["final_df"]

        with st.expander("📊 Aggregated Data (Type 1)", expanded=False):
            st.dataframe(final_agg_df, height=600, use_container_width=True)

        st.session_state.model_type = "Type 1"

        # MODELING
        st.title("Modeling")
        modeling_df = st.session_state.get("final_df", None)
        if modeling_df is None:
            st.warning("No aggregated DataFrame found for Type 1.")
            return

        available_cols = sorted(modeling_df.columns)
        default_predictors = [
            c for c in available_cols
            if c.endswith("_RPI") or c in ["PPU","D1","is_outlier","NetCatVol","Cat_Down_Up"]
        ]
        selected_predictors = st.multiselect(
            "Select Predictor Columns:",
            options=available_cols,
            default=default_predictors
        )
        grouping_keys_model = [
            next((col for col in modeling_df.columns if col.strip().lower()=='channel'),'Channel')
        ] + selected_keys
        X_columns = [c for c in selected_predictors if c not in grouping_keys_model]
        target_col = "FilteredVolume"
        k_folds = st.number_input("Number of folds (k):", min_value=2, max_value=20, value=5)

        numeric_in_X = [
            c for c in X_columns
            if c in modeling_df.columns and pd.api.types.is_numeric_dtype(modeling_df[c])
        ]
        default_std = [
            c for c in numeric_in_X
            if c in ["D1","PPU","NetCatVol","Cat_Weighted_Price","Cat_Down_Up"]
        ]
        chosen_std_cols = st.multiselect(
            "Select columns to standardize:",
            numeric_in_X,
            default=default_std
        )

        # <-- NEW LOGIC: If we already have results in session, show them; else give button to run
        if "combined_results" in st.session_state and st.session_state["combined_results"] is not None:
            st.write("### Existing Model Results (Type 1)")
            st.dataframe(st.session_state["combined_results"], height=500, use_container_width=True)

            # Add a button to re-run if desired
            if st.button("Re-run Models"):
                res, preds = run_model_pipeline(
                    modeling_df,
                    grouping_keys_model,
                    X_columns,
                    target_col,
                    k_folds,
                    chosen_std_cols
                )
                st.session_state["combined_results"] = res
                st.session_state["predictions_df"]   = preds
                if res is not None:
                    st.dataframe(res, height=500, use_container_width=True)

        else:
            # We don't have results yet, show "Run Models" button
            if st.button("Run Models"):
                res, preds = run_model_pipeline(
                    modeling_df,
                    grouping_keys_model,
                    X_columns,
                    target_col,
                    k_folds,
                    chosen_std_cols
                )
                st.session_state["combined_results"] = res
                st.session_state["predictions_df"]   = preds
                if res is not None:
                    st.dataframe(res, height=500, use_container_width=True)


    else:
        # TYPE 2 LOGIC
        st.session_state.model_type = "Type 2"
        if "type2_dfs" not in st.session_state:
            st.session_state["type2_dfs"] = {}
        multi_keys = st.multiselect(
            "Select L0 keys to aggregate separately:",
            options=[c for c in ["Brand","Variant","PackType","PPG","PackSize"] if c in dataframe.columns]
        )

        for key in multi_keys:
            group_keys = [
                next((c for c in dataframe.columns if c.strip().lower()=='date'), 'date'),
                next((c for c in dataframe.columns if c.strip().lower()=='channel'),'Channel'),
                key
            ]
            # If we haven't built an agg df for this key yet, do so
            if key not in st.session_state["type2_dfs"]:
                agg_df_key = run_full_pipeline(
                    df_filtered,
                    group_keys,
                    [key],
                    use_kalman=use_kalman,
                    use_ratio_flag=use_ratio
                )
                st.session_state["type2_dfs"][key] = agg_df_key

            with st.expander(f"📊 Aggregated Data — {key}", expanded=False):
                st.dataframe(st.session_state["type2_dfs"][key], height=600, use_container_width=True)

        st.markdown("## Type 2 Modeling Parameters")
        type2_params = {}
        for key in multi_keys:
            agg_df = st.session_state["type2_dfs"][key]
            available_cols = sorted(agg_df.columns)
            default_predictors = [
                c for c in available_cols
                if c.endswith("_RPI") or c in ["PPU","D1","is_outlier","NetCatVol","Cat_Down_Up","Cat_Price_trend_over_time"]
            ]
            selected_predictors = st.multiselect(
                f"Select Predictor Columns for '{key}':",
                options=available_cols,
                default=default_predictors,
                key=f"pred_cols_{key}"
            )
            grouping_keys_model = [
                next((col for col in agg_df.columns if col.strip().lower()=='channel'),'Channel'),
                key
            ]
            X_cols = [c for c in selected_predictors if c not in grouping_keys_model]
            target_col = "FilteredVolume"
            k_folds = st.number_input(
                f"Number of folds (k) for {key}:",
                min_value=2, max_value=20, value=5,
                key=f"kfold_{key}"
            )
            numeric_in_X = [
                c for c in X_cols
                if c in agg_df.columns and pd.api.types.is_numeric_dtype(agg_df[c])
            ]
            default_std = [
                c for c in numeric_in_X
                if c in ["D1","PPU","NetCatVol","Cat_Weighted_Price",
                         "Cat_Down_Up","Cat_Price_trend_over_time","is_outlier"]
            ]
            chosen_std = st.multiselect(
                f"Select columns to standardize for {key}:",
                numeric_in_X,
                default=default_std,
                key=f"std_{key}"
            )
            type2_params[key] = {
                "agg_df": agg_df,
                "grouping_keys_model": grouping_keys_model,
                "X_cols": X_cols,
                "target_col": target_col,
                "k_folds": k_folds,
                "chosen_std": chosen_std
            }

        # Check if we already have results stored
        if "type2_results" not in st.session_state:
            st.session_state["type2_results"] = {}
        if "type2_predictions" not in st.session_state:
            st.session_state["type2_predictions"] = {}

        # If results are found, let user see them or re-run
        if st.session_state["type2_results"]:
            st.write("### Existing Model Results (Type 2)")
            for key, df_res in st.session_state["type2_results"].items():
                if df_res is not None:
                    st.write(f"**Results for {key}**:")
                    st.dataframe(df_res, height=500, use_container_width=True)
                    if key in st.session_state["type2_predictions"]:
                        st.write(f"**Predictions sample for {key}**:")
                        st.dataframe(st.session_state["type2_predictions"][key].head(10))

            if st.button("Re-run Type 2 Models"):
                type2_results = {}
                for key, params in type2_params.items():
                    res, preds = run_model_pipeline(
                        params["agg_df"],
                        params["grouping_keys_model"],
                        params["X_cols"],
                        params["target_col"],
                        params["k_folds"],
                        params["chosen_std"]
                    )
                    type2_results[key] = res
                    if preds is not None:
                        st.session_state["type2_predictions"][key] = preds

                st.session_state.type2_results = type2_results
                # show updated results
                for key, df_res in type2_results.items():
                    if df_res is not None:
                        st.write(f"**Results for {key}** (updated):")
                        st.dataframe(df_res, height=500, use_container_width=True)
                        if key in st.session_state["type2_predictions"]:
                            st.write(f"**Predictions sample for {key}**:")
                            st.dataframe(st.session_state["type2_predictions"][key].head(10))

        else:
            # No existing type2 results: show a button to run
            if st.button("Run Models for all Type 2 Keys"):
                type2_results = {}
                for key, params in type2_params.items():
                    res, preds = run_model_pipeline(
                        params["agg_df"],
                        params["grouping_keys_model"],
                        params["X_cols"],
                        params["target_col"],
                        params["k_folds"],
                        params["chosen_std"]
                    )
                    type2_results[key] = res
                    if preds is not None:
                        st.session_state["type2_predictions"][key] = preds

                st.session_state.type2_results = type2_results
                # display
                for key, df_res in type2_results.items():
                    st.markdown(f"### Results for **{key}**")
                    if df_res is not None:
                        st.dataframe(df_res, height=500, use_container_width=True)
                    if key in st.session_state["type2_predictions"]:
                        st.markdown(f"#### Sample Actual vs. Predicted for **{key}**")
                        st.dataframe(st.session_state["type2_predictions"][key].head(20))


    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
    import textwrap

    # ──────────────────────────────────────────────────────────────────────────
    # 1)  PULL IN THE MODELING RESULTS
    # ──────────────────────────────────────────────────────────────────────────
    selected_key = None  # will only be set for Type‑2

    if "df_filteredPromo" in st.session_state:
        df_all = st.session_state["df_filteredPromo"].copy()
        model_type = "Type 1"

    elif st.session_state.get("combined_results") is not None:
        df_all = st.session_state["combined_results"].copy()
        model_type = "Type 1"

    elif st.session_state.get("type2_results"):
        keys         = list(st.session_state["type2_results"].keys())
        selected_key = st.selectbox("Choose Type 2 Key:", keys)
        df_all       = st.session_state["type2_results"][selected_key].copy()
        model_type   = "Type 2"

    else:
        st.error("Please run the Models.")
        st.stop()

    if "SelfElasticity" not in df_all.columns:
        st.error("Your results must include a 'SelfElasticity' column.")
        st.stop()

    # ──────────────────────────────────────────────────────────────────────────
    # 2)  ADD A HUMAN‑READABLE LABEL (if not already there)
    # ──────────────────────────────────────────────────────────────────────────
    if "Label" not in df_all.columns:
        def make_label(r):
            parts = []
            for k in ["Channel", "Brand", "Variant", "PackType", "PPG", "PackSize"]:
                if k in r and pd.notnull(r[k]):
                    parts.append(f"{k}={r[k]}")
            base = r.get("Model", "?")
            return f"{base} ({', '.join(parts)})" if parts else base
        df_all["Label"] = df_all.apply(make_label, axis=1)

    # ──────────────────────────────────────────────────────────────────────────
    # 3)  PAGE LAYOUT  +  FILTER PANEL  (unchanged)
    # ──────────────────────────────────────────────────────────────────────────
    left, right = st.columns([4, 1], gap="large")

    with right:
        with st.expander("Filters", expanded=True):

            # ── 3‑A  • ALWAYS‑PRESENT FILTERS ────────────────────────────────
            c1, c2 = st.columns(2)
            model_choice   = c1.selectbox("Model",   ["All"] + sorted(df_all["Model"].unique()))
            channel_choice = c2.selectbox("Channel", ["All"] + sorted(df_all["Channel"].unique()))

            # ── 3‑B  • OPTIONAL COLUMN FILTERS (Brand, Variant, ...) ─────────
            optional_cols = ["Brand", "Variant", "PackType", "PPG", "PackSize"]
            filter_vals   = {}

            for col in optional_cols:
                if col in df_all.columns:
                    options = ["All"] + sorted(df_all[col].dropna().unique())
                    filter_vals[col] = st.selectbox(col, options, key=f"{col}_filter")
                else:
                    filter_vals[col] = "All"

            # ── 3‑C  • SLIDERS & RADIO FILTERS ───────────────────────────────
            r2a, r2b, r2c = st.columns(3)
            se_low, se_high = r2a.slider("Self‑Elasticity", -1000.0, 1000.0, (-1000.0, 10.0), 0.1)

            if "CSF" in df_all.columns:
                csf_low, csf_high = r2b.slider("CSF", 0.0, 1000.0, (0.0, 1000.0), 0.1)
            else:
                csf_low = csf_high = None

            if "Contribution" in df_all.columns:
                c_low, c_high = r2c.slider("Contribution %", 0.0, 100.0, (0.0, 100.0), 1.0)
            else:
                c_low = c_high = None

            r3a, r3b, r3c = st.columns(3)
            r2_col = next((col for col in ["R2", "R2 Test"] if col in df_all.columns), None)
            if r2_col:
                slider_max = max(1.0, float(df_all[r2_col].max()))
                r2_low, r2_high = r3a.slider(r2_col, 0.0, slider_max, (0.0, slider_max), 0.01)
            else:
                r2_low = r2_high = None

            mape_col = next((col for col in ["MAPE", "MAPE Test"] if col in df_all.columns), None)
            if mape_col:
                m_low, m_high = r3b.slider(mape_col, 1.0, 60000.0, (1.0, 60000.0), 1.0)
            else:
                m_low = m_high = None

            beta_sign = (
                r3c.radio("β‑PPU sign", ["All", "Positive", "Negative"], horizontal=True)
                if "Beta_PPU" in df_all.columns else "All"
            )

    # ──────────────────────────────────────────────────────────────────────────
    # 4)  APPLY BOOLEAN MASK (unchanged)
    # ──────────────────────────────────────────────────────────────────────────
    mask = pd.Series(True, index=df_all.index)
    if model_choice   != "All": mask &= df_all["Model"]   == model_choice
    if channel_choice != "All": mask &= df_all["Channel"] == channel_choice
    for col, val in filter_vals.items():
        if val != "All":
            mask &= df_all[col] == val

    mask &= df_all["SelfElasticity"].between(se_low, se_high)
    if r2_col  and r2_low is not None:  mask &= df_all[r2_col].between(r2_low,  r2_high)
    if mape_col and m_low is not None:  mask &= df_all[mape_col].between(m_low, m_high)
    if csf_low  is not None:            mask &= df_all["CSF"].between(csf_low,  csf_high)
    if c_low    is not None:            mask &= df_all["Contribution"].between(c_low, c_high)
    if beta_sign != "All" and "Beta_PPU" in df_all.columns:
        mask &= (df_all["Beta_PPU"] > 0) if beta_sign == "Positive" else (df_all["Beta_PPU"] < 0)

    df = df_all[mask].copy()
    st.success(f"Rows after filters: {len(df)}")

    # ──────────────────────────────────────────────────────────────────────────
    # 5)  LEFT SIDE  •  STACKED BAR + AG‑GRID  (chart code unchanged)
    # ──────────────────────────────────────────────────────────────────────────
    with left:
        df["Tick"] = df["Label"].apply(lambda s: "<br>".join(textwrap.wrap(s, 25)))
        bar_w, fig_h = 180, 700
        fig_w        = max(1200, bar_w * len(df))
        ymax         = max(1e-6, df["SelfElasticity"].abs().max())
        y_range      = [-1.1 * ymax, 1.1 * ymax]

        bars_fig = go.Figure()
        if "Fold" in df.columns:
            palette = ["#FFBD59", "#458EE2", "#6DD400", "#FF5C8D", "#9B59B6", "#34495E"]
            for i, f in enumerate(sorted(df["Fold"].unique())):
                grp = df[df["Fold"] == f]
                bars_fig.add_bar(
                    x=grp["Tick"], y=grp["SelfElasticity"],
                    name=f"Fold {f}",
                    marker_color=palette[i % len(palette)],
                    customdata=grp["Label"],
                    hovertemplate="<b>%{customdata}</b><br>Fold="
                                + str(f) + "<br>SelfElasticity=%{y:.2f}<extra></extra>")
        else:
            bars_fig.add_bar(
                x=df["Tick"], y=df["SelfElasticity"],
                marker_color="#FFBD59",
                customdata=df["Label"],
                hovertemplate="<b>%{customdata}</b><br>SelfElasticity=%{y:.2f}<extra></extra>")

        bars_fig.update_layout(width=fig_w, barmode="stack",
                            xaxis=dict(tickangle=-45, tickfont=dict(size=10),
                                        automargin=True, title="Models →"),
                            yaxis=dict(showticklabels=False, range=y_range, zeroline=False),
                            height=fig_h, margin=dict(l=10, r=10, t=60, b=120))
        bars_fig.add_shape(type="line", x0=-0.5, y0=0, x1=len(df)-0.5, y1=0,
                        line=dict(color="black", width=1.5))

        axis_fig = go.Figure(go.Scatter(x=[0, 0], y=[0, 0], mode="markers", marker_opacity=0))
        axis_fig.update_layout(width=120,
                            yaxis=dict(title="SelfElasticity", range=y_range, zeroline=False),
                            xaxis=dict(visible=False),
                            height=fig_h, margin=dict(l=10, r=10, t=60, b=120))
        axis_fig.add_shape(type="line", x0=0, y0=0, x1=1, y1=0,
                        line=dict(color="black", width=1.5))

        combo_html = f"""
        <div style='display:flex; border:1px solid #ddd;'>
        <div style='flex:0 0 120px; overflow:hidden;'>{axis_fig.to_html(include_plotlyjs='cdn', full_html=False)}</div>
        <div style='flex:1 1 auto; overflow-x:auto;'>{bars_fig.to_html(include_plotlyjs=False, full_html=False)}</div>
        </div>
        """
        st.components.v1.html(combo_html, height=fig_h + 100, scrolling=True)

        # ──────────────────────────────────────────────────────────────────────
        # 6)  AG‑GRID  •  MULTI‑SELECT  +  **NEW SAVE LOGIC**
        # ──────────────────────────────────────────────────────────────────────
        st.subheader("Select model(s) → Save")
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_selection("multiple", use_checkbox=True)
        gb.configure_column("Label", wrapText=True, autoHeight=True)
        grid_out = AgGrid(df, gridOptions=gb.build(),
                        update_mode=GridUpdateMode.SELECTION_CHANGED,
                        theme="material", height=500)

        selected_df = pd.DataFrame(grid_out["selected_rows"])

        if model_type == "Type 1":
            if st.button("Save Selected Model(s)", key="save_type1"):
                if selected_df.empty:
                    st.warning("No rows selected.")
                else:
                    st.session_state["selected_models_type1"] = selected_df.copy()
                    st.success(f"Saved {len(selected_df)} model(s) for Type 1.")

        else:  # Type 2
            if st.button("Save Selected Model(s)", key="save_type2"):
                if selected_df.empty:
                    st.warning("No rows selected.")
                else:
                    if "selected_models_type2" not in st.session_state:
                        st.session_state["selected_models_type2"] = {}
                    st.session_state["selected_models_type2"][selected_key] = selected_df.copy()
                    st.success(f"Saved {len(selected_df)} model(s) for key “{selected_key}” (Type 2).")

    # ──────────────────────────────────────────────────────────────────────
    # 7)  SAVED‑MODELS OVERVIEW  •  Nicely‑formatted tabs & Ag‑Grid
    # ──────────────────────────────────────────────────────────────────────
    st.markdown("## 📋 Saved Models")

    tab_t1, tab_t2 = st.tabs(["Type 1", "Type 2"])

    # ----------------------------------------------------------------------
    # TAB 1 • TYPE 1
    # ----------------------------------------------------------------------
    with tab_t1:
        df_t1 = st.session_state.get("selected_models_type1")
        if isinstance(df_t1, pd.DataFrame) and not df_t1.empty:
            st.caption(f"Total saved Type 1 models: **{len(df_t1)}**")
            gb1 = GridOptionsBuilder.from_dataframe(df_t1)
            gb1.configure_default_column(filter=True, sortable=True, resizable=True)
            AgGrid(df_t1, gridOptions=gb1.build(),
                theme="material", height=300, fit_columns_on_grid_load=True)
        else:
            st.info("No Type 1 models saved yet.")

    # ----------------------------------------------------------------------
    # TAB 2 • TYPE 2
    # ----------------------------------------------------------------------
    with tab_t2:
        saved_t2 = st.session_state.get("selected_models_type2", {})
        if not saved_t2:
            st.info("No Type 2 models saved yet.")
        else:
            key_list = list(saved_t2.keys())
            key_choice = st.selectbox("Select a Type 2 key", key_list, index=0)
            df_key = saved_t2[key_choice]

            st.caption(f"Models saved for key **{key_choice}**: **{len(df_key)}**")
            gb2 = GridOptionsBuilder.from_dataframe(df_key)
            gb2.configure_default_column(filter=True, sortable=True, resizable=True)
            AgGrid(df_key, gridOptions=gb2.build(),
                theme="material", height=300, fit_columns_on_grid_load=True)

            # Optional: combined view for quick export
            with st.expander("🔄  Show ALL Type 2 models combined"):
                combined_df = pd.concat(saved_t2.values(), keys=saved_t2.keys(), names=["Selected Key"])
                # Move the key index into a column so it shows in Ag‑Grid
                combined_df = combined_df.reset_index().rename(columns={"level_0": "Selected Key"})
                gb_all = GridOptionsBuilder.from_dataframe(combined_df)
                gb_all.configure_default_column(filter=True, sortable=True, resizable=True)
                AgGrid(combined_df, gridOptions=gb_all.build(),
                    theme="material", height=350, fit_columns_on_grid_load=True)



def model_selection_page():

    # ───────── Imports ─────────
    import streamlit as st, pandas as pd, numpy as np
    import textwrap, plotly.express as px, plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

    # ───────── Session pick-up ─────────
    selected_key = None
    if "selected_models_type1" in st.session_state and not st.session_state["selected_models_type1"].empty:
        df_all, model_type = st.session_state["selected_models_type1"].copy(), "Type 1"
    elif st.session_state.get("selected_models_type2"):
        avail = {k: df for k, df in st.session_state["selected_models_type2"].items() if not df.empty}
        if not avail:
            st.warning("No saved models.  Go back and save some first.");  return
        selected_key = st.selectbox("Choose Type 2 Key:", sorted(avail))
        df_all, model_type = avail[selected_key].copy(), "Type 2"
    else:
        st.warning("No saved models.  Go back and save some first.");  return

    # ───────── Nav buttons ─────────
    c1,c2,c3 = st.columns(3)
    with c1: st.button("🏠 Home",   on_click=lambda: go_home())
    with c2: st.button("🔄 Back to Build", on_click=lambda: go_to("Build_1"))
    with c3: st.button("🧪 Go to Review",  on_click=lambda: go_to("model_selection"))

    st.title(f"Evaluation Model Selector – {model_type}" + (f" | {selected_key}" if selected_key else ""))

    # ───────── Ensure a readable label ─────────
    if "Label" not in df_all.columns:
        def _mk(r):
            bits=[r.get("Model","?")]
            for k in ["Channel","Brand","Variant","PackType","PPG","PackSize"]:
                if k in r and pd.notnull(r[k]): bits.append(f"{k}={r[k]}")
            return " | ".join(bits)
        df_all["Label"] = df_all.apply(_mk, axis=1)

    # ───────── Filter panel (unchanged) ─────────
    left, right = st.columns([4,1], gap="large")
    with right:
        with st.expander("Filters", True):
            c1,c2 = st.columns(2)
            model_choice   = c1.selectbox("Model",   ["All"]+sorted(df_all["Model"].unique()))
            channel_choice = c2.selectbox("Channel", ["All"]+sorted(df_all["Channel"].unique()))
            opts = ["Brand","Variant","PackType","PPG","PackSize"]
            opt_vals={}
            for col in opts:
                opt_vals[col]=st.selectbox(col, ["All"]+sorted(df_all[col].dropna().unique()) if col in df_all else ["All"],
                                           key=f"{col}_flt")
            se_low,se_high = st.slider("Self-Elasticity", -10.0,10.0,(-10.0,10.0),0.1)
            csf_low,csf_high = st.slider("CSF",0.0,10.0,(0.0,10.0),0.1) if "CSF" in df_all else (None,None)
            c_low,c_high     = st.slider("Contribution %",0.0,100.0,(0.0,100.0),1.0) if "Contribution" in df_all else (None,None)
            r2_col = next((c for c in ["R2","R2 Test"] if c in df_all.columns),None)
            if r2_col:
                r2_low,r2_high = st.slider(r2_col,0.0,max(1.0,float(df_all[r2_col].max())),
                                           (0.0,max(1.0,float(df_all[r2_col].max()))),0.01)
            else: r2_low=r2_high=None
            mape_col = next((c for c in ["MAPE","MAPE Test"] if c in df_all.columns),None)
            if mape_col:
                m_low,m_high = st.slider(mape_col,1.0,40.0,(1.0,40.0),1.0)
            else: m_low=m_high=None
            beta_sign = st.radio("β-PPU sign",["All","Positive","Negative"],horizontal=True) if "Beta_PPU" in df_all else "All"

    # ───────── Boolean mask ─────────
    mask = pd.Series(True,index=df_all.index)
    if model_choice!="All": mask &= df_all["Model"]==model_choice
    if channel_choice!="All": mask &= df_all["Channel"]==channel_choice
    for col,val in opt_vals.items():
        if val!="All": mask &= df_all[col]==val
    mask &= df_all["SelfElasticity"].between(se_low,se_high)
    if r2_col:  mask &= df_all[r2_col].between(r2_low,r2_high)
    if mape_col:mask &= df_all[mape_col].between(m_low,m_high)
    if csf_low is not None: mask &= df_all["CSF"].between(csf_low,csf_high)
    if c_low   is not None: mask &= df_all["Contribution"].between(c_low,c_high)
    if beta_sign!="All" and "Beta_PPU" in df_all:
        mask &= (df_all["Beta_PPU"]>0) if beta_sign=="Positive" else (df_all["Beta_PPU"]<0)

    df_filt = df_all[mask].copy()
    st.success(f"Rows after filters: {len(df_filt)}")

    # ───────── Bar + grid (unchanged visuals) ─────────
    with left:
        df_filt["Tick"] = df_filt["Label"].apply(lambda s:"<br>".join(textwrap.wrap(s,25)))
        bar_w,fig_h=180,700
        ymax=max(1e-6,df_filt["SelfElasticity"].abs().max())
        fig=go.Figure(go.Bar(
            x=df_filt["Tick"],y=df_filt["SelfElasticity"],marker_color="#FFBD59",
            customdata=df_filt["Label"],
            hovertemplate="<b>%{customdata}</b><br>SelfElasticity=%{y:.2f}<extra></extra>"))
        fig.update_layout(width=max(1200,bar_w*len(df_filt)),height=fig_h,
                          xaxis=dict(tickangle=-45),yaxis=dict(showticklabels=False,range=[-1.1*ymax,1.1*ymax]),
                          margin=dict(l=10,r=10,t=60,b=120))
        st.components.v1.html(fig.to_html(include_plotlyjs='cdn',full_html=False),
                              height=fig_h+70,scrolling=True)

        st.subheader("Select model(s) → Run Statistical Checks")
        gb=GridOptionsBuilder.from_dataframe(df_filt)
        gb.configure_selection("multiple", use_checkbox=True)
        gb.configure_column("Label",wrapText=True,autoHeight=True)
        grid_out=AgGrid(df_filt,gridOptions=gb.build(),update_mode=GridUpdateMode.SELECTION_CHANGED,
                        theme="material",height=500)
        selected_df=pd.DataFrame(grid_out["selected_rows"])

    # ───────── Run Statistical Checks button ─────────
    if st.button("Run Statistical Checks"):
        if selected_df.empty:
            st.warning("Nothing selected.")
        else:
            st.session_state["_stats_rows"]=selected_df.copy()
            if model_type=="Type 1":
                st.session_state["_stats_preds"]=st.session_state.get("predictions_df")
            else:
                st.session_state["_stats_preds"]=st.session_state.get("type2_predictions",{}).get(selected_key)
            st.session_state["_show_stats"]=True
            st.rerun()

    # ░░░░░  STATS + INSIGHTS  ░░░░░
    if st.session_state.get("_show_stats"):

        sel_df=st.session_state["_stats_rows"];  preds_df=st.session_state.get("_stats_preds")

        # ───────── Tabs (full width) ─────────
        stats_tab, insights_tab = st.tabs(["📊 Statistical Checks","💡 Insights"])

        # █████  STATS  █████
        with stats_tab:
            # 1️⃣ Pred vs Actual
            st.subheader("1️⃣ Predicted vs Actual")
            if preds_df is not None and not preds_df.empty:
                j=preds_df.merge(sel_df[["Model","Fold"]].drop_duplicates(),
                                 on=["Model","Fold"],how="inner")
                if not j.empty:
                    fig_pa=px.scatter(j,x="Actual",y="Predicted",color="Model",
                                      trendline="ols",height=400,hover_data=j.columns)
                    a_min,a_max=j["Actual"].min(),j["Actual"].max()
                    fig_pa.add_shape(type="line",x0=a_min,y0=a_min,x1=a_max,y1=a_max,
                                     line=dict(dash="dash"))
                    st.plotly_chart(fig_pa,use_container_width=True)
                else: st.info("No matching prediction rows.")
            else: st.info("Prediction DataFrame unavailable.")

            # 2️⃣ MAPE
            st.subheader("2️⃣ MAPE (Train vs Test)")
            if {"MAPE Train","MAPE Test"}.issubset(sel_df.columns):
                ml=sel_df.melt(id_vars=["Label"] if "Label" in sel_df else ["Model"],
                               value_vars=["MAPE Train","MAPE Test"],
                               var_name="Stage",value_name="MAPE")
                st.plotly_chart(px.bar(ml,x="Stage",y="MAPE",
                                       color="Label" if "Label" in sel_df else "Model",
                                       barmode="group",height=300,text_auto=".1f"),
                                use_container_width=True)
            else: st.info("MAPE columns not found.")

            # ---------- 3️⃣ Contribution ----------
            st.subheader("3️⃣ Key‑Driver Contribution Analysis")

            PRIMARY_YELLOW = "#FFBD59"
            TERTIARY_BLUE  = "#458EE2"

            def _build_label(r, key_cols, base_col):
                parts = [str(r[base_col])]
                for k in key_cols:
                    if k in r and pd.notnull(r[k]):
                        parts.append(f"{k}={r[k]}")
                return " | ".join(parts)

            label_col   = "Model"
            non_metrics = [c for c in sel_df.columns
                        if sel_df[c].dtype == "object"
                        and not c.startswith("Beta_")
                        and c not in [label_col, "DisplayLabel"]]
            sel_df["DisplayLabel"] = sel_df.apply(
                lambda r: _build_label(r, non_metrics, label_col), axis=1
            )
            beta_cols = [c for c in sel_df.columns if c.startswith("Beta_")]

            if not beta_cols:
                st.info("No Beta_ coefficients found in selected rows.")
            else:
                for _, row in sel_df.iterrows():
                    mlabel = row["DisplayLabel"]
                    st.markdown(f"**{mlabel}**")

                    intercept = row.get("B0 (Original)", 0)
                    pred_mean = intercept + sum(
                        row[bc] * row.get(bc.replace("Beta_", ""), 0) for bc in beta_cols
                    )

                    contrib_pairs = []
                    if pred_mean:
                        for bc in beta_cols:
                            pname = bc.replace("Beta_", "")
                            contrib_val = (row[bc] * row.get(pname, 0)) / pred_mean
                            if contrib_val != 0:
                                contrib_pairs.append((pname, contrib_val))

                    if contrib_pairs:
                        cdf = (pd.DataFrame(contrib_pairs,
                                            columns=["Predictor", "Contribution"])
                            .sort_values("Contribution", ascending=False))
                        colours = [PRIMARY_YELLOW if v >= 0 else TERTIARY_BLUE
                                for v in cdf["Contribution"]]
                        fig_c = go.Figure(go.Bar(
                            x=cdf["Predictor"], y=cdf["Contribution"],
                            marker_color=colours,
                            text=cdf["Contribution"].round(2),
                            textposition="inside", textfont_color="white",
                            hovertemplate="<b>%{x}</b><br>Contribution = %{y:.3f}<extra></extra>"
                        ))
                        fig_c.update_layout(template="plotly_white",
                                            xaxis_tickangle=-45,
                                            height=350,
                                            margin=dict(l=20, r=20, t=30, b=40))
                        tcol, ccol = st.columns([1, 2])
                        tcol.dataframe(cdf, use_container_width=True)
                        ccol.plotly_chart(fig_c, use_container_width=True)
                    else:
                        st.info("All contributions are zero for this row.")

                    # # ---------- 4️⃣ Year-on-Year Waterfall ----------
                    # st.subheader("4️⃣ Year-on-Year Waterfall")

                    # if preds_df is None or preds_df.empty or "Date" not in preds_df.columns:
                    #     st.info("Need prediction rows with a ‘Date’ column to build YoY charts.")
                    # else:
                    #     # ── join predictions with the rows you actually selected ────────────────
                    #     join_df = preds_df.merge(
                    #         sel_df[["Model", "Fold"]].drop_duplicates(),
                    #         on=["Model", "Fold"],
                    #         how="inner"
                    #     )
                    #     join_df["Date"]     = pd.to_datetime(join_df["Date"], errors="coerce")
                    #     join_df["Year"]     = join_df["Date"].dt.year
                    #     join_df["Half"]     = np.where(join_df["Date"].dt.month <= 6, "H1", "H2")
                    #     join_df["YearHalf"] = join_df["Year"].astype(str) + " " + join_df["Half"]

                    #     periods = sorted(join_df["YearHalf"].unique())
                    #     if len(periods) >= 2:
                    #         col_p1, col_p2 = st.columns(2)
                    #         p1 = col_p1.selectbox("Period 1", periods, index=0, key="yoy_p1_tab")
                    #         p2 = col_p2.selectbox("Period 2", periods, index=len(periods)-1, key="yoy_p2_tab")

                    #         if p1 != p2:
                    #             beta_cols = [c for c in sel_df.columns if c.startswith("Beta_")]

                    #             # ---- pull the coefficient row(s) that match the predictions -----
                    #             coeff_row = (
                    #                 sel_df
                    #                 .merge(join_df[["Model", "Fold"]].drop_duplicates(),
                    #                     on=["Model", "Fold"])
                    #                 .iloc[0]          # 1st row is fine because Model/Fold are unique
                    #             )

                    #             contrib_d = {}
                    #             for per in (p1, p2):
                    #                 subset = join_df[join_df["YearHalf"] == per]

                    #                 # pandas 3-proof numeric mean
                    #                 means = (
                    #                     subset
                    #                     .select_dtypes(include="number")
                    #                     .mean()
                    #                     .to_dict()
                    #                 )

                    #                 base = coeff_row.get("B0 (Original)", 0) + sum(
                    #                     coeff_row[bc] * means.get(bc.replace("Beta_", ""), 0)
                    #                     for bc in beta_cols
                    #                 )
                    #                 if base == 0:
                    #                     base = np.finfo(float).eps      # avoid div-by-zero

                    #                 contribs = {
                    #                     bc.replace("Beta_", ""):
                    #                     (coeff_row[bc] * means.get(bc.replace("Beta_", ""), 0)) / base
                    #                     for bc in beta_cols
                    #                 }
                    #                 contrib_d[per] = contribs

                    #             # ---------- build Δ-table ---------------------------------------
                    #             predictors = sorted(set(contrib_d[p1]) | set(contrib_d[p2]))
                    #             delta_df = pd.DataFrame({
                    #                 "Predictor": predictors,
                    #                 "Delta": [
                    #                     contrib_d[p2].get(p, 0) - contrib_d[p1].get(p, 0)
                    #                     for p in predictors
                    #                 ]
                    #             }).sort_values("Delta", ascending=False)

                    #             total_delta = delta_df["Delta"].sum()

                    #             # ---------- plot -------------------------------------------------
                    #             wf = go.Figure(go.Waterfall(
                    #                 orientation="v",
                    #                 measure=["relative"] * len(delta_df) + ["total"],
                    #                 x=list(delta_df["Predictor"]) + ["Total"],
                    #                 y=(delta_df["Delta"] * 100).tolist() + [total_delta * 100],  # now in %
                    #                 text=[f"{v*100:.2f}%" for v in delta_df["Delta"]]
                    #                     + [f"{total_delta*100:.2f}%"],
                    #                 decreasing={"marker": {"color": "#DB2B39"}},
                    #                 increasing={"marker": {"color": "#9BC53D"}},
                    #                 totals={"marker": {"color": "#0047AB"}},
                    #             ))

                    #             wf.update_layout(
                    #                 title={
                    #                     "text": f"{p1} vs {p2} Waterfall",
                    #                     "font": {"size": 16, "color": "#0047AB"}
                    #                 },
                    #                 yaxis_title="Δ Contribution (%)",
                    #                 template="plotly_white",
                    #                 height=350,
                    #                 margin=dict(l=20, r=20, t=60, b=40),
                    #             )

                    #             st.plotly_chart(wf, use_container_width=True)
                                
            
            
            

        # ░░░░░░░░░░░░░░░  💡 INSIGHTS TAB  ░░░░░░░░░░░░░░░
        with insights_tab:

            import numpy as np, pandas as pd
            import plotly.graph_objects as go
            from plotly.subplots import make_subplots

            # ── Quant-Matrix palette (Style-Guide) ───────────────────────────
            P_YEL   = "#FFBD59"   # primary yellow
            ACC_BLUE= "#458EE2"   # accent blue
            S_GREEN = "#41C185"   # success green
            D_RED   = "#DB2B39"   # danger red

            # helper – modelling DataFrame for predictor means
            mod_df = (st.session_state.get("final_df")
                    if model_type == "Type 1"
                    else st.session_state.get("type2_dfs", {}).get(selected_key))
            if mod_df is None or mod_df.empty:
                st.info("Modelling DataFrame not found.");  st.stop()

            promo_bins = st.session_state.get("final_clusters_depth", {})

            # ── iterate over each user-selected model row ────────────────────
            for _, row in sel_df.iterrows():

                # -------- essentials from the row --------
                mlabel    = row.get("DisplayLabel", row.get("Model", "Model"))
                intercept = row.get("B0 (Original)")
                betas     = {c.replace("Beta_", ""): row[c]
                            for c in row.index if c.startswith("Beta_")}
                if intercept is None or "PPU" not in betas or betas["PPU"] == 0:
                    st.warning(f"Skipping **{mlabel}** – missing intercept / β-PPU.");  continue

                base_ppu  = row.get("PPU_at_Elasticity", mod_df["PPU"].mean())
                base_elas = row.get("SelfElasticity",   np.nan)
                means     = mod_df.mean(numeric_only=True).to_dict()

                # -------- prediction, elasticity helpers --------
                def q_hat(price: float) -> float:
                    """Predict volume at price (uses row’s betas & average predictors)."""
                    q = intercept
                    for pred, beta in betas.items():
                        if pred == "PPU":
                            q += beta * price
                        elif pred.endswith("_RPI"):
                            pc = base_ppu / means.get(pred, 1)
                            q += beta * (price/pc if pc else 0)
                        else:
                            q += beta * means.get(pred, 0)
                    return max(q, 0)

                def own_price_elasticity(price: float) -> float:
                    """Point-elasticity dQ/dP · (P/Q) with competitor-ratio terms."""
                    dQdP = betas["PPU"]
                    for pred, beta in betas.items():
                        if pred.endswith("_RPI"):
                            pc = base_ppu / means.get(pred, 1)
                            if pc: dQdP += beta / pc           # ∂(P/Pc)/∂P = 1/Pc
                    Q = q_hat(price)
                    return dQdP * price / Q if Q else np.nan

                # -------- domains ------------------------------------------------
                prices_full = np.linspace(0, 2.5*base_ppu, 120)      # for VALUE curve
                vols_full   = [q_hat(p) for p in prices_full]
                revs_full   = [p*v for p,v in zip(prices_full, vols_full)]
                vmax_i      = int(np.argmax(revs_full))

                vol_max   = vols_full[vmax_i]
                price_max = prices_full[vmax_i]
                rev_max   = revs_full[vmax_i]

                # demand curve – use full domain of VALUE curve for a long line
                dem_vols, dem_prices = vols_full, prices_full

                # -------- key baseline metrics ----------------------------------
                base_q   = q_hat(base_ppu)
                base_rev = base_ppu * base_q

                # -------- metric strip ------------------------------------------
                st.markdown(f"### {mlabel}")
                m1,m2,m3,m4 = st.columns(4)
                m1.metric("Baseline PPU", f"${base_ppu:,.2f}")
                m2.metric("Volume",       f"{base_q:,.0f}")
                m3.metric("Revenue",      f"${base_rev:,.0f}")
                m4.metric("Elasticity",   f"{base_elas:.2f}" if np.isfinite(base_elas) else "N/A")

                # -------- side-by-side plots ------------------------------------
                fig = make_subplots(
                    rows=1, cols=2, horizontal_spacing=0.12,
                    subplot_titles=("Demand Curve  (Volume → Price)",
                                    "Value Curve  (Price → Revenue)"))

                # Demand (left)
                fig.add_trace(go.Scatter(
                    x=dem_vols, y=dem_prices,
                    mode="lines+markers",
                    line=dict(color=ACC_BLUE,width=2), marker=dict(color=ACC_BLUE)), 1,1)
                # shaded baseline + max-rev rectangles
                fig.add_shape(type="rect", x0=0,x1=base_q,  y0=0,y1=base_ppu,
                            fillcolor=ACC_BLUE, opacity=0.20, line_width=0, row=1,col=1)
                fig.add_shape(type="rect", x0=0,x1=vol_max, y0=0,y1=price_max,
                            fillcolor=S_GREEN, opacity=0.15, line_width=0, row=1,col=1)
                fig.add_trace(go.Scatter(
                    x=[base_q], y=[base_ppu], mode="markers+text",
                    text=["Baseline"], textposition="bottom center",
                    marker=dict(symbol="x",size=10,color=ACC_BLUE)), 1,1)
                fig.add_trace(go.Scatter(
                    x=[vol_max], y=[price_max], mode="markers+text",
                    text=["Max-Rev P"], textposition="top center",
                    marker=dict(symbol="diamond",size=10,color=S_GREEN)), 1,1)
                fig.update_xaxes(title_text="Volume (Q)",  row=1,col=1)
                fig.update_yaxes(title_text="Price (PPU)", row=1,col=1)

                # Value (right)
                fig.add_trace(go.Scatter(
                    x=prices_full, y=revs_full,
                    mode="lines+markers",
                    line=dict(color=P_YEL,width=2), marker=dict(color=P_YEL)), 1,2)
                fig.add_shape(type="rect", x0=0,x1=base_ppu,  y0=0,y1=base_rev,
                            fillcolor=ACC_BLUE, opacity=0.20, line_width=0, row=1,col=2)
                fig.add_shape(type="rect", x0=0,x1=price_max, y0=0,y1=rev_max,
                            fillcolor=S_GREEN, opacity=0.15, line_width=0, row=1,col=2)
                fig.add_trace(go.Scatter(
                    x=[base_ppu], y=[base_rev], mode="markers+text",
                    text=["Baseline"], textposition="bottom center",
                    marker=dict(symbol="x",size=10,color=ACC_BLUE)), 1,2)
                fig.add_trace(go.Scatter(
                    x=[price_max], y=[rev_max], mode="markers+text",
                    text=["Max Rev"], textposition="top center",
                    marker=dict(symbol="diamond",size=10,color=S_GREEN)), 1,2)
                fig.update_xaxes(title_text="Price (PPU)", row=1,col=2)
                fig.update_yaxes(title_text="Revenue",     row=1,col=2)

                fig.update_layout(template="plotly_white", height=450, showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

                # -------- Cross-elasticities (β-RPI) -----------------------------
                xbeta = {p[:-4]:b for p,b in betas.items() if p.endswith("_RPI")}
                if xbeta:
                    ce_df = (pd.DataFrame(xbeta.items(), columns=["Competitor","Beta"])
                            .sort_values("Beta"))
                    bar_cols = [S_GREEN if b>0 else D_RED for b in ce_df["Beta"]]
                    fig_ce = go.Figure(go.Bar(
                        x=ce_df["Beta"], y=ce_df["Competitor"], orientation="h",
                        marker_color=bar_cols,
                        text=[f"{b:.2f}" for b in ce_df["Beta"]],
                        textposition="outside"))
                    fig_ce.update_layout(
                        title="Cross-Elasticity Coefficients (β-RPI)",
                        xaxis_title="β value", yaxis_title="Competitor",
                        template="plotly_white", height=300)
                    st.plotly_chart(fig_ce, use_container_width=True)
                else:
                    st.info("No *_RPI coefficients for this model.")

                # -------- Promotional-Elasticity Table --------------------------
                key_tuple = tuple(row.get(k) for k in ["Channel","Brand","Variant","PPG"])
                bins = promo_bins.get(key_tuple)
                if bins:
                    st.markdown("#### Promotional-Elasticity Table")
                    rows = []

                    # Baseline
                    rows.append(dict(PromoBin="Baseline", Discount=0.0,
                                    Price=base_ppu, Volume=base_q,
                                    Revenue=base_rev,
                                    Elasticity=own_price_elasticity(base_ppu)))

                    for b in bins:
                        disc   = float(b["Centroid"])
                        price  = base_ppu * (1 - disc/100)
                        vol    = q_hat(price)
                        rev    = price * vol
                        elas   = own_price_elasticity(price)
                        rows.append(dict(PromoBin=b["ClusterName"], Discount=disc,
                                        Price=price, Volume=vol,
                                        Revenue=rev, Elasticity=elas))

                    promo_df = (pd.DataFrame(rows)
                                .assign(Price=lambda d: d["Price"].round(2),
                                        Volume=lambda d: d["Volume"].round(0),
                                        Revenue=lambda d: d["Revenue"].round(0),
                                        Elasticity=lambda d: d["Elasticity"].round(2)))
                    st.dataframe(promo_df, use_container_width=True)
                else:
                    st.info("No promo-depth clusters found for this model.")

                st.divider()


                if st.button("❌ Hide Statistical Checks"):
                    # drop flag so block disappears on next rerun
                    for k in ["_show_stats", "_stats_rows", "_stats_preds"]:
                        st.session_state.pop(k, None)
                    st.rerun()


    # ░░░░░░░░░░░░░░░  PRICE-RELATIONSHIP DASHBOARD  ░░░░░░░░░░░░░░░
    # put this right after the tabs section
    st.markdown("---")
    st.header("📈 Price-Relationship Analysis")

    # ─────────────────────────────────────────────────────────────
    # Get the first available raw DataFrame: D0 → dataframe1 → dataframe
    # ─────────────────────────────────────────────────────────────
    base_df = None
    for _k in ("D0", "dataframe1", "dataframe"):
        cand = st.session_state.get(_k)
        if isinstance(cand, pd.DataFrame) and not cand.empty:
            base_df = cand.copy()
            break      # stop at the first non-empty DataFrame

    if base_df is None:
        st.error("No raw data found in session (D0 / dataframe1 / dataframe).")
        st.stop()

    # ensure Date column exists & is datetime
    if "Date" not in base_df.columns:
        st.error("Raw data needs a 'Date' column.");  st.stop()
    base_df = base_df.copy()
    base_df["Date"] = pd.to_datetime(base_df["Date"], errors="coerce")

    # --- 2) scope = first selected model row --------------------------------
    sc_row = sel_df.iloc[0]         # sel_df already exists from earlier block
    scope = {c: sc_row.get(c) for c in ["Channel","Brand","Variant","PPG"] if c in base_df.columns}

    # split into BRAND data vs TOTAL market ----------------------------------
    brand_df = base_df.copy()
    for k,v in scope.items():
        if v is not None and not pd.isna(v):
            brand_df = brand_df[brand_df[k]==v]

    if brand_df.empty:
        st.warning("No rows in raw data match the selected model’s scope."); st.stop()

    # weekly calendar keys
    brand_df["Year"] = brand_df["Date"].dt.isocalendar().year
    brand_df["Week"] = brand_df["Date"].dt.isocalendar().week
    brand_df["YearWeek"] = brand_df["Year"].astype(str)+"-W"+brand_df["Week"].astype(str).str.zfill(2)

    # aggregate BRAND --------------------------------------------------------
    gb_cols = ["Year","Week","YearWeek"]
    agg_brand = (brand_df
                .groupby(gb_cols, as_index=False)
                .agg({"SalesValue":"sum","Volume":"sum","D1":"mean"}))
    agg_brand = agg_brand[agg_brand["Volume"]>0]
    agg_brand["Price"] = agg_brand["SalesValue"] / agg_brand["Volume"]

    # aggregate TOTAL --------------------------------------------------------
    tot_df = base_df.copy()
    tot_df["Year"] = tot_df["Date"].dt.isocalendar().year
    tot_df["Week"] = tot_df["Date"].dt.isocalendar().week
    tot_df["YearWeek"] = tot_df["Year"].astype(str)+"-W"+tot_df["Week"].astype(str).str.zfill(2)

    agg_tot = (tot_df
            .groupby(["Year","Week","YearWeek"],as_index=False)
            .agg({"SalesValue":"sum"}).rename(columns={"SalesValue":"TotalSales"}))

    # merge & compute market-share ------------------------------------------
    merged = pd.merge(agg_brand, agg_tot, on=gb_cols, how="left")
    merged["MarketShare"] = (merged["SalesValue"]/merged["TotalSales"]).clip(upper=1)*100

    # correlations for titles ------------------------------------------------
    def _corr(a,b): 
        return merged[a].corr(merged[b]) if merged[a].std()>0 and merged[b].std()>0 else np.nan
    c1 = _corr("Price","Volume")
    c2 = _corr("Price","SalesValue")
    c3 = _corr("D1","Volume")
    c4 = _corr("Price","MarketShare")

    from plotly.subplots import make_subplots
    rel_fig = make_subplots(
        rows=2, cols=2, specs=[[{"secondary_y":True}]*2]*2,
        subplot_titles=[
            f"Price vs Volume (r={c1:.2f})",
            f"Price vs Sales (r={c2:.2f})",
            f"Distribution vs Volume (r={c3:.2f})",
            f"Market-Share vs Price (r={c4:.2f})"
        ]
    )

    # ---- Sub-plot 1 --------------------------------------------------------
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["Price"],
                        mode="lines+markers", name="Price", line=dict(color="#458EE2"),
                        row=1,col=1, secondary_y=False)
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["Volume"],
                        mode="lines+markers", name="Volume", line=dict(color="#DB2B39"),
                        row=1,col=1, secondary_y=True)

    # ---- Sub-plot 2 --------------------------------------------------------
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["Price"],
                        mode="lines+markers", showlegend=False, line=dict(color="#458EE2"),
                        row=1,col=2, secondary_y=False)
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["SalesValue"],
                        mode="lines+markers", name="SalesValue", line=dict(color="#41C185"),
                        row=1,col=2, secondary_y=True)

    # ---- Sub-plot 3 --------------------------------------------------------
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["D1"],
                        mode="lines+markers", name="Distribution", line=dict(color="#8E44AD"),
                        row=2,col=1, secondary_y=False)
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["Volume"],
                        mode="lines+markers", showlegend=False, line=dict(color="#DB2B39"),
                        row=2,col=1, secondary_y=True)

    # ---- Sub-plot 4 --------------------------------------------------------
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["MarketShare"],
                        mode="lines+markers", name="MarketShare", line=dict(color="#FFBD59"),
                        row=2,col=2, secondary_y=False)
    rel_fig.add_scatter(x=merged["YearWeek"], y=merged["Price"],
                        mode="lines+markers", showlegend=False, line=dict(color="#458EE2", dash="dot"),
                        row=2,col=2, secondary_y=True)

    rel_fig.update_layout(
        height=900,  template="plotly_white",
        title_text=f"Price-Relationship Dashboard  |  {scope}"
    )
    st.plotly_chart(rel_fig, use_container_width=True)

    # ──────────────────────────────────────────────────────────────
    #  BOTTOM-OF-PAGE:  Go → Review
    # ──────────────────────────────────────────────────────────────
    if st.button("📝 Go to Review", key="goto_review_bottom"):
        # stash the rows the user was working with
        st.session_state["review_rows"]   = st.session_state.get("_stats_rows", pd.DataFrame())
        st.session_state["review_preds"]  = st.session_state.get("_stats_preds")      # optional
        go_to("model_review")             # ← route to the review page

# ──────────────────────────────────────────────────────────────
#  MODEL-REVIEW  (new page)
# ──────────────────────────────────────────────────────────────
def model_review_page():
    import streamlit as st
    import pandas as pd
    import plotly.express as px

    # ----------  NAVIGATION  ----------
    nav_l, nav_r = st.columns([1, 1])
    with nav_l:
        if st.button("◀ Back to Selector", key="review_back"):
            go_to("model_selection")
            st.stop()
    with nav_r:
        if st.button("🏠 Home", key="review_home"):
            go_home()
            st.stop()

    st.title("Model Review")

    # ----------  WHAT DID WE RECEIVE?  ----------
    rows_df  = st.session_state.get("review_rows",  pd.DataFrame())
    preds_df = st.session_state.get("review_preds")          # may be None

    if rows_df.empty:
        st.info("No rows were passed in. Go back to the selector, tick some rows and click **Run Statistical Checks → Go to Review**.")
        return

    # Quick peek at what we have
    with st.expander("Show rows now under review"):
        st.dataframe(rows_df, use_container_width=True)

    # ----------  TWO-TAB LAYOUT  ----------
    inter_tab, intra_tab = st.tabs(["🌐 Inter-Brand", "🏷️ Intra-Brand"])

    # ======================================================================
    # 🌐  INTER-BRAND  – placeholder
    # ======================================================================
    with inter_tab:
        st.subheader("Inter-Brand Review")

        # ↘️  Add your inter-brand visuals here.
        #     For example: compare SelfElasticity across brands, brand–share trends, etc.

        if "Brand" in rows_df.columns:
            fig = px.bar(
                rows_df,
                x="Brand",
                y="SelfElasticity",
                color="Brand",
                title="Self-Elasticity by Brand (placeholder)",
                text_auto=".2f",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No ‘Brand’ column found in the rows you passed. Add your own inter-brand logic here.")

    # ======================================================================
    # 🏷️  INTRA-BRAND  – placeholder
    # ======================================================================
    with intra_tab:
        # ────────────────────────────────────────────────────────────────
        # 📊  INTRA-BRAND – Self-Elasticity from “saved” models
        # ────────────────────────────────────────────────────────────────
        import streamlit as st
        import pandas as pd
        import plotly.express as px

        # 0) Pull the master results DF that was stored by the Build-page selector
        if "selected_models_type1" in st.session_state and not st.session_state["selected_models_type1"].empty:
            df_models = st.session_state["selected_models_type1"].copy()
            model_origin = "Type 1"
        elif "selected_models_type2" in st.session_state and st.session_state["selected_models_type2"]:
            # flatten the dict-of-DFs into one frame (add the key name as a column)
            frames = []
            for keyname, df in st.session_state["selected_models_type2"].items():
                if df is not None and not df.empty:
                    tmp = df.copy()
                    tmp["Type2_Key"] = keyname   # so you can still see where it came from
                    frames.append(tmp)
            if not frames:
                st.info("No saved Type 2 models found."); st.stop()
            df_models = pd.concat(frames, ignore_index=True)
            model_origin = "Type 2"
        else:
            st.info("No saved models found in session_state."); st.stop()

        # 1) sanity-check required columns
        needed_cols = {"Brand", "SelfElasticity", "Model"}
        missing = needed_cols.difference(df_models.columns)
        if missing:
            st.warning(f"Saved models are missing column(s): {', '.join(missing)}"); st.stop()

        # 2) select brand(s)
        brand_options = sorted(df_models["Brand"].dropna().unique())
        chosen_brands = st.multiselect("Choose Brand(s) for intra-brand comparison:", brand_options,
                                    default=brand_options[:1])
        if not chosen_brands:
            st.info("Pick at least one brand."); st.stop()

        sub_df = df_models[df_models["Brand"].isin(chosen_brands)].copy()
        if sub_df.empty:
            st.info("No saved models under the selected brand(s)."); st.stop()

        # 3) build a readable label (so different models don’t look identical)
        def _make_label(row):
            bits = [row.get("Model", "?")]
            for k in ["Channel", "Variant", "PPG", "PackType", "Type2_Key"]:
                if k in sub_df.columns and pd.notnull(row.get(k)):
                    bits.append(f"{k}={row[k]}")
            return " | ".join(bits)

        sub_df["DisplayLabel"] = sub_df.apply(_make_label, axis=1)

        # 4) plot
        fig = px.bar(
            sub_df,
            x="DisplayLabel",
            y="SelfElasticity",
            color="Model",
            text="SelfElasticity",
            color_discrete_sequence=["#FFBD59", "#458EE2", "#41C185", "#DB2B39", "#8E44AD"],
            height=480
        )
        fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
        fig.update_layout(
            title=f"Intra-Brand Self-Elasticity ({model_origin}) – {', '.join(chosen_brands)}",
            xaxis_title="Saved Models",
            yaxis_title="Self-Elasticity",
            xaxis_tickangle=-35,
            uniformtext_minsize=8,
            uniformtext_mode="hide",
            showlegend=True,
            template="plotly_white",
            margin=dict(l=20, r=20, t=80, b=120)
        )
        st.plotly_chart(fig, use_container_width=True)

        # 5) compact table for reference
        cols_to_show = [c for c in [
            "DisplayLabel", "Brand", "Model", "SelfElasticity",
            "CSF", "MCV", "R2 Test", "MAPE Test"
        ] if c in sub_df.columns]

        with st.expander("Show details table", expanded=False):
            st.dataframe(sub_df[cols_to_show], use_container_width=True)

    # ────────────────────────────────────────────────────────────────
    # 📝 Analyst Notes – with threaded replies
    # ────────────────────────────────────────────────────────────────
    import datetime as _dt
    import streamlit as st
    from typing import Dict, List, Optional
    import uuid

    # Constants
    ROLES = ["Business Head", "Data-Science Team", "Product Manager", "Marketing", "Other"]
    NOTE_PLACEHOLDER = "Enter your observation or recommendation here..."
    REPLY_PLACEHOLDER = "Type your reply here..."

    def migrate_legacy_notes(notes_list):
        """Ensure all notes have required fields for compatibility with older data"""
        for note in notes_list:
            # Add ID if missing
            if "id" not in note:
                note["id"] = str(uuid.uuid4())
            
            # Add pinned status if missing
            if "pinned" not in note:
                note["pinned"] = False
                
            # Make sure replies exist
            if "replies" not in note:
                note["replies"] = []
                
            # Ensure all replies have IDs
            for reply in note.get("replies", []):
                if "id" not in reply:
                    reply["id"] = str(uuid.uuid4())
        
        return notes_list

    def initialize_notes_store():
        """Initialize the notes storage in session state if it doesn't exist"""
        if "intra_brand_notes" not in st.session_state:
            # Structure: {view_key: [{"id", "ts", "role", "note", "replies":[...]}, ...]}
            st.session_state["intra_brand_notes"] = {}
        
        # Derive unique key for current view
        view_key = f"{model_origin}|{'|'.join(sorted(chosen_brands))}"
        
        # Get or create note store for this view
        note_store = st.session_state["intra_brand_notes"].setdefault(view_key, [])
        
        # Migrate any legacy notes to new format
        note_store = migrate_legacy_notes(note_store)
        st.session_state["intra_brand_notes"][view_key] = note_store
        
        return note_store, view_key

    def create_new_note(note_store: List[Dict], view_key: str):
        """Component for creating a new top-level note"""
        with st.container(border=True):
            st.markdown("### ✍️ New note")
            
            # Role selection and save button in columns
            col1, col2 = st.columns([3, 1])
            with col1:
                role = st.selectbox(
                    "Audience",
                    ROLES,
                    key=f"role_new_{view_key}"
                )
            
            # Note text area
            note_text = st.text_area(
                "Observation or recommendation",
                placeholder=NOTE_PLACEHOLDER,
                height=120,
                key=f"txt_new_{view_key}"
            )
            
            with col2:
                save_btn = st.button(
                    "💾 Save Note", 
                    type="primary",
                    key=f"save_new_{view_key}",
                    disabled=not note_text.strip()
                )
            
            if save_btn and note_text.strip():
                # Create new note with unique ID
                note_store.append({
                    "id": str(uuid.uuid4()),
                    "ts": _dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "role": role,
                    "note": note_text.strip(),
                    "replies": [],
                    "pinned": False
                })
                st.success("Note saved successfully!")
                # Clear the input
                st.session_state[f"txt_new_{view_key}"] = ""
                st.rerun()

    def display_reply(reply: Dict):
        """Render a single reply with styling"""
        return f"""
        <div style="margin-left: 20px; padding: 8px 12px; background-color: #f0f2f6; border-radius: 5px; margin-bottom: 8px;">
            <div style="font-size: 0.85rem; color: #555; margin-bottom: 4px;">
                <b>{reply['role']}</b> • {reply['ts']}
            </div>
            <div>{reply['note']}</div>
        </div>
        """

    def handle_reply(note: Dict, note_idx: int, view_key: str):
        """Component for displaying existing replies and adding new ones"""
        # Display existing replies
        if note.get("replies", []):  # Use get() with default for safety
            st.markdown("##### 💬 Replies")
            for reply in note["replies"]:
                st.markdown(display_reply(reply), unsafe_allow_html=True)
        else:
            st.info("No replies yet")
        
        # Add new reply
        st.markdown("##### ↩️ Add a reply")
        
        # Create a stable unique identifier that doesn't depend on possibly missing 'id'
        # Fall back to index and timestamp if id is missing
        note_identifier = note.get("id", f"{note_idx}_{note.get('ts', '')}")
        reply_id = f"{view_key}_{note_identifier}_{note_idx}"
        
        col1, col2 = st.columns([3, 1])
        with col1:
            reply_role = st.selectbox(
                "Reply as",
                ROLES,
                key=f"role_rep_{reply_id}"
            )
        
        reply_text = st.text_area(
            "Reply",
            placeholder=REPLY_PLACEHOLDER,
            height=100,
            key=f"draft_rep_{reply_id}"
        )
        
        with col2:
            save_reply_btn = st.button(
                "💾 Add Reply",
                type="primary",
                key=f"save_rep_{reply_id}",
                disabled=not reply_text.strip()
            )
        
        if save_reply_btn and reply_text.strip():
            # Make sure replies list exists
            if "replies" not in note:
                note["replies"] = []
                
            # Add the reply
            note["replies"].append({
                "id": str(uuid.uuid4()),
                "ts": _dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "role": reply_role,
                "note": reply_text.strip()
            })
            st.success("Reply added!")
            # Clear the input
            st.session_state[f"draft_rep_{reply_id}"] = ""
            st.rerun()

    def display_note_history(note_store: List[Dict], view_key: str):
        """Display all notes with their replies"""
        if not note_store:
            st.info("No notes yet for this view")
            return
        
        # Filter and sort options
        st.markdown("### 📚 Note History")
        col1, col2 = st.columns(2)
        with col1:
            filter_role = st.multiselect(
                "Filter by role",
                options=ROLES,
                key=f"filter_role_{view_key}"
            )
        
        with col2:
            sort_order = st.radio(
                "Sort order",
                options=["Newest first", "Oldest first", "Pinned first"],
                horizontal=True,
                key=f"sort_order_{view_key}"
            )
        
        # Apply filters
        filtered_notes = note_store
        if filter_role:
            filtered_notes = [n for n in filtered_notes if n["role"] in filter_role]
        
        # Apply sorting
        if sort_order == "Oldest first":
            sorted_notes = list(enumerate(filtered_notes))
        elif sort_order == "Pinned first":
            # Sort by pinned status, then by timestamp (newest first)
            sorted_notes = sorted(
                enumerate(filtered_notes),
                key=lambda x: (not x[1].get("pinned", False), -filtered_notes.index(x[1]))
            )
        else:  # "Newest first" (default)
            sorted_notes = list(reversed(list(enumerate(filtered_notes))))
        
        # Display each note
        for idx, note in sorted_notes:
            # Use get() with default values for safety
            pin_icon = "📌 " if note.get("pinned", False) else ""
            header = f"{pin_icon}{note['role']} | {note['ts']}"
            
            with st.expander(header, expanded=False):
                # Display note content
                st.markdown(note["note"])
                
                # Action buttons (pin/unpin)
                col1, col2 = st.columns([1, 9])
                with col1:
                    # Generate a stable key using index if id is missing
                    note_id = note.get("id", f"note_{idx}")
                    pin_text = "Unpin" if note.get("pinned", False) else "Pin"
                    if st.button(
                        f"{pin_text}",
                        key=f"pin_{view_key}_{note_id}",
                        type="secondary",
                        use_container_width=True
                    ):
                        note["pinned"] = not note.get("pinned", False)
                        st.rerun()
                
                st.divider()
                
                # Handle replies
                handle_reply(note, idx, view_key)

    def main():
        """Main function to render the Analyst Notes component"""
        st.markdown("## 📝 Analyst Notes")
        
        # Initialize note storage
        note_store, view_key = initialize_notes_store()
        
        # Component to create new notes
        create_new_note(note_store, view_key)
        
        # Display note history with replies
        display_note_history(note_store, view_key)

    # Run the component
    if __name__ == "__main__":
        main()
    else:
        main()  # Run when imported as a module



# ────────────────────────────────────────────────────────────────
# 📑  REPORT PAGE  –  All notes + visuals in one place
# ────────────────────────────────────────────────────────────────
import streamlit as st
from typing import Dict, List, Any
import datetime as _dt
import base64
import uuid
from streamlit_extras.colored_header import colored_header


# ────────────────────────────
# ▼ Utility helpers
# ────────────────────────────
def generate_download_link(content: str, filename: str, text: str) -> str:
    """Return an <a> tag that downloads the given content as a file."""
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text}</a>'


def _render_reply(rep: Dict) -> str:
    """Return HTML for a single reply bubble."""
    return f"""
    <div style="margin-left:25px;padding:10px 15px;background:#f5f7fa;
         border-left:3px solid #cfd8e6;border-radius:4px;margin-bottom:8px;">
        <div style="font-size:0.85rem;color:#5f6b7a;margin-bottom:4px;">
            <b>{rep['role']}</b> • {rep['ts']}</div>
        <div style="color:#2c3e50;">{rep['note']}</div>
    </div>"""


def _render_note_block(note: Dict, *, include_replies: bool = True) -> str:
    """Return HTML for a note – optionally with its replies."""
    pin_icon = "📌 " if note.get("pinned", False) else ""
    html = f"""
    <div style="padding:12px 15px;background:#fff;border:1px solid #e0e0e0;
         border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,0.1);margin-bottom:15px;">
        <div style="font-size:0.9rem;color:#333;margin-bottom:8px;">
            <b>{pin_icon}{note['role']}</b> • {note['ts']}</div>
        <div style="color:#1f2937;margin-bottom:10px;">{note['note']}</div>"""

    if include_replies and note.get("replies"):
        html += "<div style='margin-top:10px;'>"
        for rep in note["replies"]:
            html += _render_reply(rep)
        html += "</div>"

    html += "</div>"
    return html


# ────────────────────────────
# ▼ Filtering helpers
# ────────────────────────────
def filter_notes(notes: List[Dict], filters: Dict[str, Any]) -> List[Dict]:
    """Return the subset of notes that pass all filters."""
    out = notes.copy()

    # role filter
    if filters.get("roles"):
        out = [n for n in out if n["role"] in filters["roles"]]

    # date-range filter
    if filters.get("date_range"):
        start_d, end_d = filters["date_range"]
        out = [
            n for n in out if start_d <= _dt.datetime.strptime(n["ts"], "%Y-%m-%d %H:%M").date() <= end_d
        ]

    # keyword filter
    if kw := filters.get("keyword"):
        kw = kw.lower()
        out = [
            n for n in out
            if kw in n["note"].lower()
            or any(kw in r["note"].lower() for r in n.get("replies", []))
        ]

    # pinned-only flag
    if filters.get("show_pinned_only"):
        out = [n for n in out if n.get("pinned", False)]

    return out


# ────────────────────────────
# ▼ Notes & comments section
# ────────────────────────────
def notes_section(notes_src: Dict[str, List[Dict]]):
    colored_header("📝 Analyst Notes & Comments", description="View and filter analyst observations")

    if not notes_src:
        st.info("No analyst notes have been recorded yet.")
        return

    # ── filter panel
    with st.container(border=True):
        st.write("🔍 **Filter Options**")

        all_roles = sorted({n["role"] for notes in notes_src.values() for n in notes})
        c1, c2 = st.columns(2)

        with c1:
            selected_roles = st.multiselect("Filter by role", all_roles, default=all_roles)
            keyword_search = st.text_input("Search in notes & replies", placeholder="Enter keywords…")
        with c2:
            dates = [
                _dt.datetime.strptime(n["ts"], "%Y-%m-%d %H:%M").date()
                for notes in notes_src.values() for n in notes
            ]
            min_d, max_d = (min(dates) if dates else _dt.date.today() - _dt.timedelta(30),
                            max(dates) if dates else _dt.date.today())
            date_range = st.date_input("Date range", value=(min_d, max_d),
                                       min_value=min_d, max_value=max_d)
            show_pinned = st.checkbox("Show pinned notes only")

    filters = dict(roles=selected_roles, keyword=keyword_search,
                   date_range=date_range if len(date_range) == 2 else None,
                   show_pinned_only=show_pinned)

    tab1, tab2 = st.tabs(["By Analysis View", "Chronological View"])

    # ─── by-view tab
    with tab1:
        for view_key, notes in notes_src.items():
            parts = view_key.split("|")
            origin, brands = parts[0], (parts[1:] or ["All"])
            flt = filter_notes(notes, filters)
            if not flt:
                continue

            flt.sort(key=lambda x: (not x.get("pinned", False),
                                    -_dt.datetime.strptime(x["ts"], "%Y-%m-%d %H:%M").timestamp()))
            st.markdown(f"### 🔹 {origin} – {', '.join(brands)}")
            for n in flt:
                st.markdown(_render_note_block(n), unsafe_allow_html=True)
            st.divider()

    # ─── chronological tab
    with tab2:
        all_notes = []
        for view_key, notes in notes_src.items():
            parts = view_key.split("|")
            origin, brands = parts[0], (parts[1:] or ["All"])
            for n in notes:
                n2 = n.copy()
                n2["view"] = f"{origin} – {', '.join(brands)}"
                all_notes.append(n2)

        flt = filter_notes(all_notes, filters)
        if not flt:
            st.info("No notes match your filter criteria.")
        else:
            flt.sort(key=lambda x: (not x.get("pinned", False),
                                    -_dt.datetime.strptime(x["ts"], "%Y-%m-%d %H:%M").timestamp()))
            for n in flt:
                ctx = f"<div style='font-size:0.8rem;color:#6b7280;margin-bottom:4px;'><i>From view:</i> <b>{n['view']}</b></div>"
                st.markdown(ctx + _render_note_block(n), unsafe_allow_html=True)

    # ─── export
    st.divider()
    exp_col1, exp_col2 = st.columns([1, 3])
    with exp_col1:
        fmt = st.selectbox("Export format", ["HTML", "Markdown", "Text"])
    with exp_col2:
        if st.button("📥 Export Filtered Notes", type="primary"):
            export_notes = flt if 'flt' in locals() else []
            file_txt = generate_export_content(export_notes, fmt)
            fname = f"analyst_notes_{_dt.datetime.now():%Y%m%d}.{fmt.lower()}"
            st.markdown(generate_download_link(file_txt, fname, "📄 Download Report"), unsafe_allow_html=True)


# ────────────────────────────
# ▼ Dashboard section
# ────────────────────────────
def dashboard_section(notes_src: Dict[str, List[Dict]], figs_src: Dict[str, List]):
    colored_header("📊 Presentation Dashboard", description="Ready-to-present view of key insights")

    if not figs_src:
        st.info("No visualizations have been captured yet.")
        return

    # choose which views to include
    view_names = {vk: f"{vk.split('|')[0]} – {', '.join(vk.split('|')[1:] or ['All'])}" for vk in figs_src}
    sel = st.multiselect("Select views", options=list(figs_src),
                         format_func=lambda k: view_names[k],
                         default=list(figs_src)[:min(3, len(figs_src))])

    col1, col2 = st.columns(2)
    with col1:
        layout = st.radio("Dashboard layout", ["Full width", "Two columns"], horizontal=True)
    with col2:
        show_notes = st.checkbox("Include pinned notes", value=True)

    st.divider()

    for i, vk in enumerate(sel):
        st.markdown(f"### {i+1}. {view_names[vk]}")
        figs = figs_src.get(vk, [])

        if layout == "Two columns" and figs:
            cols = st.columns(2)
            for j, fig in enumerate(figs):
                with cols[j % 2]:
                    st.plotly_chart(fig, use_container_width=True)
        else:
            for fig in figs:
                st.plotly_chart(fig, use_container_width=True)

        if show_notes:
            pinned = [n for n in notes_src.get(vk, []) if n.get("pinned", False)]
            if pinned:
                st.markdown("#### Key Observations")
                for n in pinned:
                    st.markdown(_render_note_block(n, include_replies=False), unsafe_allow_html=True)

        if i < len(sel) - 1:
            st.divider()

    if st.button("📥 Export Dashboard as PDF", type="primary"):
        st.info("PDF export would require an HTML-to-PDF service. Not implemented in this demo.")


# ────────────────────────────
# ▼ Export content generator
# ────────────────────────────
def generate_export_content(notes: List[Dict], fmt: str) -> str:
    """Return notes in HTML / Markdown / Text."""
    ts_now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    if fmt == "HTML":
        out = f"""<html><head><style>
                  body{{font-family:Arial, sans-serif;margin:20px}}
                  .note{{padding:15px;margin-bottom:20px;border:1px solid #ddd;border-radius:5px}}
                  .reply{{margin-left:20px;padding:10px;background:#f5f5f5;border-radius:5px;margin-top:10px}}
                  .meta{{color:#666;font-size:0.9em;margin-bottom:10px}}
                  </style></head><body>
                  <h1>Analyst Notes Report</h1><p>Generated on: {ts_now}</p>"""
        for n in notes:
            view = f"<i>View: {n['view']}</i>" if 'view' in n else ""
            out += f"""<div class="note"><div class="meta"><b>{n['role']}</b> • {n['ts']} {view}</div>{n['note']}"""
            for r in n.get("replies", []):
                out += f"""<div class="reply"><div class="meta"><b>{r['role']}</b> • {r['ts']}</div>{r['note']}</div>"""
            out += "</div>"
        out += "</body></html>"
        return out

    if fmt == "Markdown":
        out = f"# Analyst Notes Report\nGenerated on: {ts_now}\n\n"
        for n in notes:
            view = f" _(View: {n['view']})_" if 'view' in n else ""
            out += f"## {n['role']} • {n['ts']}{view}\n\n{n['note']}\n\n"
            if n.get("replies"):
                out += "### Replies\n"
                for r in n["replies"]:
                    out += f"- **{r['role']}** ({r['ts']}): {r['note']}\n"
            out += "\n---\n\n"
        return out

    # plain text
    out = f"ANALYST NOTES REPORT\nGenerated on: {ts_now}\n\n"
    for n in notes:
        view = f" (View: {n['view']})" if 'view' in n else ""
        out += f"{n['role']} • {n['ts']}{view}\n{n['note']}\n"
        if n.get("replies"):
            out += "REPLIES:\n"
            for r in n["replies"]:
                out += f"- {r['role']} ({r['ts']}): {r['note']}\n"
        out += "\n" + "-"*40 + "\n\n"
    return out


# ────────────────────────────
# ▼ MAIN entry – Report page
# ────────────────────────────
def report_page():
    """Render the consolidated report page."""

    # ░░ Navigation bar ░░═══════════════════════════════════════
    nav1, nav2, _ = st.columns([1, 8, 1])
    with nav1:
        if st.button("🏠 Home", use_container_width=True):
            # Replace with your own navigator / router
            # e.g.  st.session_state["current_page"] = "home"
            go_home()

    st.title("📑 Consolidated Analyst Report")

    # get data from session state
    notes_src = st.session_state.get("intra_brand_notes", {})
    figs_src  = st.session_state.get("view_figs", {})

    if not notes_src and not figs_src:
        st.warning("No data available yet. Analyse some views first.")
        return

    tab1, tab2 = st.tabs(["📝 Notes & Comments", "📊 Presentation Dashboard"])
    with tab1:
        notes_section(notes_src)
    with tab2:
        dashboard_section(notes_src, figs_src)


# ═══════════════  END OF MODULE  ═══════════════



# =================================================================================
# CALL THIS PAGE FROM YOUR NAVIGATION WHEN USER CLICKS “Go to Review”
# =================================================================================

def post_modelling_page():

    """
    SECTION 2 – MODULE 2: Post Modeling
    This encapsulates all your "final model summary" code, 
    competitor pricing, elasticity, scenario planning, etc.
    """

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go

    # ------------------------------
    # Helper: MAPE ignoring zero actuals
    # ------------------------------
    def compute_mape(actual_vals, pred_vals):
        mask = (actual_vals != 0)
        if not np.any(mask):
            return np.nan
        return np.mean(np.abs((actual_vals[mask] - pred_vals[mask]) / actual_vals[mask])) * 100

    # ------------------------------
    # For neat elasticity display
    # ------------------------------
    def format_elas(e_):
        if e_ is not None and not np.isnan(e_):
            return f"{e_:.2f}"
        return "N/A"



    # ------------------------------
    # Inject enhanced CSS style
    # ------------------------------
    st.markdown(
        """
        <style>
        /* Overall background color */
        body {
            background: linear-gradient(120deg, #f0f4f8, #f8faff);
        }

        /* Card-like container styling */
        .card-container {
            background-color: white;
            border-radius: 0.5rem;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
            margin-bottom: 1rem;
        }
        
        /* Section headers */
        .section-header {
            color: #1F618D;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #EBF5FB;
        }
        
        /* Metric tiles */
        .metric-container {
            background-color: #F8F9F9;
            padding: 1rem;
            border-radius: 0.3rem;
            text-align: center;
        }
        
        .metric-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #2C3E50;
        }
        
        .metric-label {
            font-size: 0.9rem;
            color: #7F8C8D;
        }
        
        /* Make tables more readable */
        .dataframe-container {
            font-size: 0.9rem !important;
        }
        
        .dataframe-container td, .dataframe-container th {
            padding: 0.5rem !important;
        }

        /* Slightly larger font for subheaders */
        .custom-subheader {
            font-size: 1.15rem !important;
            font-weight: 600 !important;
            color: #2C3E50 !important;
            margin-top: 1rem !important;
            margin-bottom: 0.5rem !important;
        }

        /* Table text smaller */
        .dataframe table td, .dataframe table th {
            font-size: 0.95rem !important;
        }

        /* Additional margin for code clarity */
        .stMarkdown {
            margin-bottom: 1rem !important;
        }

        /* Make expander headers more colorful */
        .streamlit-expanderHeader {
            font-size: 1.05rem;
            font-weight: 600;
            color: #1F618D;
        }

        /* Slight accent for number input fields */
        .stNumberInput>div>div>input {
            background-color: #FBFCFC;
            border: 1px solid #BBBDC1;
            color: #2C3E50;
        }

        /* Tweak st.info, st.warning, st.success with pastel backgrounds */
        .stAlert, .stWarning, .stInfo, .stSuccess {
            border-radius: 0.5rem;
        }
        .stAlert {
            background-color: #FEF9E7; /* pale yellow */
        }
        .stInfo {
            background-color: #EBF5FB; /* pale blue */
        }
        .stSuccess {
            background-color: #E9F7EF; /* pale green */
        }
        .stWarning {
            background-color: #FDF2E9; /* pale orange */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------
    # MAIN "Post Modelling" content
    # ------------------------------

    st.title("Post Modelling – Final Model Summary (Type 1 & Type 2)")



    # ───────────────── Navigation Header ─────────────────
    nav_l, nav_r = st.columns([1, 1])

    with nav_l:
        if st.button("◀ Back to Build"):
            # route back
            st.session_state.page = "Build_1"
            st.rerun()

    with nav_r:
        if st.button("🏠 Home"):
            st.session_state.page = "home"
            st.rerun()


        
    # (A) Let user pick a data source from session state
    st.markdown("<div class='custom-subheader'>Data Source for Post Modelling</div>", unsafe_allow_html=True)
    possible_sources = []
    if "D0" in st.session_state and st.session_state["D0"] is not None:
        possible_sources.append("D0")
    if "dataframe1" in st.session_state and st.session_state["dataframe1"] is not None:
        possible_sources.append("dataframe1")
    if "dataframe" in st.session_state and st.session_state["dataframe"] is not None:
        possible_sources.append("dataframe")

    if not possible_sources:
        st.error("No suitable data sources found in session.")
        st.stop()

    chosen_data_source = st.selectbox("Select Data Source:", possible_sources)
    df_source = st.session_state[chosen_data_source].copy()
    st.markdown(f"**Chosen data source**: {chosen_data_source}")

    # ------------- Check for Type1 or Type2 final models -------------
    def have_type1_models():
        if "final_saved_models_type1" not in st.session_state:
            return False
        val = st.session_state["final_saved_models_type1"]
        if val is None:
            return False
        if isinstance(val, list):
            return (len(val) > 0)
        if isinstance(val, pd.DataFrame):
            return not val.empty
        return False

    def have_type2_models():
        if "final_saved_models_type2" not in st.session_state:
            return False
        val = st.session_state["final_saved_models_type2"]
        return (val is not None) and (len(val) > 0)

    is_type1 = have_type1_models()
    is_type2 = have_type2_models()

    if not is_type1 and not is_type2:
        st.error("No Type 1 or Type 2 final models found in session.")
        st.stop()

    model_options = []
    if is_type1:
        model_options.append("Type 1")
    if is_type2:
        model_options.append("Type 2")

    if len(model_options) == 1:
        selected_model_type = model_options[0]
        st.markdown(f"<b>Only one model type found:</b> **{selected_model_type}**", unsafe_allow_html=True)
    else:
        selected_model_type = st.radio("Choose Model Type:", model_options, horizontal=True)

    st.markdown("---", unsafe_allow_html=True)

    # ============================= TYPE 1 =============================
# ============================= TYPE 1 =============================
# ============================= TYPE 1 =============================
    if selected_model_type == "Type 1":
        st.markdown("## Type 1: Single Aggregated Model Analysis")

        # — Load & validate your saved Type 1 models —
        raw_models = st.session_state.get("final_saved_models_type1")
        # 1) Nothing ever saved
        if raw_models is None:
            st.error("No Type 1 models found in session.")
            st.stop()

        # 2) Convert lists to DataFrames, or copy an existing one
        import pandas as pd
        df_type1 = (
            pd.DataFrame(raw_models)
            if isinstance(raw_models, list)
            else raw_models.copy()
        )

        # 3) Guard against an empty table
        if df_type1.empty:
            st.error("Type 1 model list is empty.")
            st.stop()

        # — Build unified labels showing Model + keys —
        label_to_index = {}
        options = []
        for idx, row in df_type1.iterrows():
            model_name = row.get("Model", f"Model {idx}")
            attrs = []
            for key in ("Channel", "Brand", "Variant", "PPG"):
                if key in df_type1.columns:
                    attrs.append(f"{key}:{row[key]}")
            label = model_name + (f" ({' | '.join(attrs)})" if attrs else "")
            label_to_index[label] = idx
            options.append(label)

        # Replace radio buttons with a dropdown
        chosen_label = st.selectbox("Select a Type 1 model to analyze:", options)
        sel_idx = label_to_index[chosen_label]
        row_selected = df_type1.loc[sel_idx]

        # — Show key attributes and metrics in a compact layout —
        col1, col2, col3 = st.columns(3)
        if "R2" in row_selected:
            col1.metric("R²", f"{row_selected['R2']:.4f}")
        if "MAPE" in row_selected:
            col2.metric("MAPE", f"{row_selected['MAPE']:.2f}%")
        
        # Show channel/brand in the third column
        if "Channel" in row_selected and "Brand" in row_selected:
            col3.metric("Scope", f"{row_selected['Channel']}-{row_selected['Brand']}")

        # — Show full details in an expander to save space —
        with st.expander("View Complete Model Details", expanded=False):
            st.dataframe(row_selected.to_frame().T, use_container_width=True)


        # Identify the model name from the chosen row
        if "Model" not in row_selected:
            st.error("No 'Model' column found in final Type 1 DataFrame. Cannot identify the model automatically.")
            st.stop()
        model_name_in_row = row_selected["Model"]

        # aggregator columns
        channel_ = row_selected.get("Channel", None)
        brand_   = row_selected.get("Brand", None)
        variant_ = row_selected.get("Variant", None)
        ppg_     = row_selected.get("PPG", None)

        # intercept
        intercept_col = "B0 (Original)"
        if intercept_col not in row_selected:
            st.error(f"Missing intercept col '{intercept_col}'. Aborting.")
            st.stop()
        raw_intercept = float(row_selected[intercept_col])

        # Identify Beta_ columns
        beta_cols = [c for c in df_type1.columns if c.startswith("Beta_")]
        if not beta_cols:
            st.error("No Beta_ columns found. Stopping.")
            st.stop()
        betas = {}
        for bc in beta_cols:
            predictor = bc.replace("Beta_", "")
            betas[predictor] = float(row_selected[bc])

        # gather default values
        missing_cols = []
        default_vals = {}
        for p_ in betas.keys():
            if p_ not in row_selected or pd.isna(row_selected[p_]):
                missing_cols.append(p_)
            else:
                default_vals[p_] = float(row_selected[p_])
        if missing_cols:
            st.error(f"Missing or NaN columns for {missing_cols}. Aborting.")
            st.stop()

        # competitor ratio columns
        rpi_cols = []
        for predictor in betas:
            if predictor.endswith("_RPI") and betas[predictor] != 0:
                rpi_cols.append(predictor)

        # IMPROVED PRICE & SCENARIO SETUP
        st.markdown("### Analysis Parameters")
        
        param_col1, param_col2 = st.columns(2)
        
        with param_col1:
            user_own_price = st.number_input("My Current Price (PPU):", 
                                            value=default_vals.get("PPU", 5.0), 
                                            step=0.5)
        
        with param_col2:
            competitor_impact = st.checkbox("Enable Competitor Impact Analysis", value=False)

        # Advanced parameter configuration
        with st.expander("Advanced: Predictor Configuration", expanded=False):
            config_col1, config_col2 = st.columns(2)
            
            user_overrides_orig = {}
            user_competitor_prices = {}
            
            with config_col1:
                st.markdown("#### Non-Price Predictors")
                non_rpi_predictors = [p for p in betas.keys() if not p.endswith("_RPI") and p != "PPU"]
                for p_ in non_rpi_predictors:
                    user_overrides_orig[p_] = st.number_input(
                        f"{p_}:",
                        value=default_vals[p_],
                        step=0.5
                    )
            
            if competitor_impact and rpi_cols:
                with config_col2:
                    st.markdown("#### Competitor Prices")
                    old_own_price = default_vals.get("PPU", 5.0)
                    for rp_ in rpi_cols:
                        old_ratio = default_vals[rp_]
                        old_comp_price = old_own_price / old_ratio if old_ratio != 0 else 0.0
                        user_competitor_prices[rp_] = st.number_input(
                            f"{rp_[:-4]} Price:",
                            value=old_comp_price,
                            step=0.5
                        )

        # Check PPU validity
        if ("PPU" not in betas) or (betas["PPU"] == 0):
            st.error("No 'PPU' or Beta_PPU=0 => can't invert volume vs price. Aborting.")
            st.stop()

        b_own = betas["PPU"]

        # Helper functions for scenario generation and elasticity
        def scenario_rpi_dict(my_price: float, new_scenario: bool) -> dict:
            d_out = {}
            for rp_ in rpi_cols:
                if (not competitor_impact) or (not new_scenario):
                    d_out[rp_] = default_vals[rp_]
                else:
                    new_cp = user_competitor_prices[rp_]
                    ratio = 0.0 if (new_cp == 0) else (my_price / new_cp)
                    d_out[rp_] = ratio
            return d_out

        def compute_current_volume(betas, raw_int, my_price, user_over, rpi_vals):
            sum_others = 0.0
            for c_ in betas:
                if (not c_.endswith("_RPI")) and (c_ != "PPU"):
                    sum_others += betas[c_] * user_over.get(c_, 0.0)
            sum_rpi = 0.0
            for rp_ in rpi_cols:
                sum_rpi += betas[rp_] * rpi_vals[rp_]
            return raw_int + sum_others + sum_rpi + betas["PPU"] * my_price

        def compute_elasticity_full(betas, price_val, volume_val, rpi_vals):
            """
            betas     : dict of all β's, including 'PPU' and any '<brand>_RPI'
            price_val : the own‐price P at which we evaluate
            volume_val: the predicted Q at that price
            rpi_vals  : dict mapping each '<brand>_RPI' to its P_own/P_comp ratio
            """
            if volume_val <= 0 or price_val <= 0:
                return np.nan

            # Start with the own‐price slope
            derivative = betas.get("PPU", 0.0)

            # Add competitor‐ratio contribution: ∂(P/Pc)/∂P = 1/Pc
            for rp_col, ratio in rpi_vals.items():
                beta_r = betas.get(rp_col, 0.0)
                if ratio and beta_r:
                    P_comp = price_val / ratio
                    if P_comp > 0:
                        derivative += beta_r / P_comp

            # Scale to get elasticity
            return derivative * (price_val / volume_val)

        def build_curve_df(betas, raw_int, my_price, user_over, rpi_vals, n_points=15):
            b_own_ = betas["PPU"]
            sum_others = 0.0
            for c_ in betas:
                if (not c_.endswith("_RPI")) and (c_ != "PPU"):
                    sum_others += betas[c_] * user_over.get(c_, 0.0)
            sum_rpi = 0.0
            for rp_ in rpi_cols:
                sum_rpi += betas[rp_] * rpi_vals[rp_]
            zero_x = raw_int + sum_others + sum_rpi
            if b_own_ > 0:
                if zero_x < 0: zero_x = 10
                max_vol = 2 * zero_x
            else:
                if zero_x <= 0: zero_x = 10
                max_vol = zero_x
            if max_vol <= 0:
                max_vol = 10

            volumes = np.linspace(0, max_vol, n_points)
            price_list = []
            rev_list = []
            elas_list = []

            for Q_ in volumes:
                p_ = (Q_ - zero_x) / b_own_ if b_own_ != 0 else 0
                p_ = max(p_, 0)
                rev_ = p_ * Q_
                e_ = compute_elasticity_full(betas, p_, Q_, rpi_vals)
                price_list.append(p_)
                rev_list.append(rev_)
                elas_list.append(e_)

            df_out = pd.DataFrame({
                "Price": price_list,
                "Volume": volumes,
                "Revenue": rev_list,
                "Elasticity": elas_list
            })
            df_out.sort_values("Price", inplace=True)
            df_out.reset_index(drop=True, inplace=True)
            return df_out

        # Original scenario
        rpi_old = scenario_rpi_dict(user_own_price, new_scenario=False)
        df_old = build_curve_df(betas, raw_intercept, user_own_price, user_overrides_orig, rpi_old, 15)
        Q_cur_old = compute_current_volume(betas, raw_intercept, user_own_price, user_overrides_orig, rpi_old)
        elas_old = compute_elasticity_full(betas, user_own_price, Q_cur_old, rpi_old)

        idx_oldmax = df_old["Revenue"].idxmax() if not df_old["Revenue"].empty else None
        vol_oldmax, pri_oldmax = 0, 0
        if idx_oldmax is not None:
            vol_oldmax = df_old.loc[idx_oldmax, "Volume"]
            pri_oldmax = df_old.loc[idx_oldmax, "Price"]

        df_new = None
        Q_cur_new = None
        elas_new = np.nan
        if competitor_impact and (rpi_cols):
            rpi_new = scenario_rpi_dict(user_own_price, new_scenario=True)
            df_new = build_curve_df(betas, raw_intercept, user_own_price, user_overrides_orig, rpi_new, 15)
            Q_cur_new = compute_current_volume(betas, raw_intercept, user_own_price, user_overrides_orig, rpi_new)
            elas_new = compute_elasticity_full(betas, user_own_price, Q_cur_new, rpi_new)

        # Plotly figure
        fig = go.Figure()
        fig.update_layout(
            colorway=["#1F77B4", "#D62728", "#2CA02C", "#FF7F0E"],
            plot_bgcolor="rgba(245,245,250,0.9)",
            paper_bgcolor="rgba(245,245,250,0.9)"
        )

        # Original scenario line
        fig.add_trace(go.Scatter(
            x=df_old["Volume"], y=df_old["Price"],
            mode="lines+markers",
            name="Original RPI",
            line=dict(color="blue", width=2),
        ))
        if (Q_cur_old > 0) and (user_own_price > 0):
            fig.add_shape(
                type="rect", xref="x", yref="y",
                x0=0, y0=0, x1=Q_cur_old, y1=user_own_price,
                fillcolor="blue", opacity=0.25,
                line=dict(color="blue", width=2, dash="dash")
            )
            fig.add_trace(go.Scatter(
                x=[Q_cur_old], y=[user_own_price],
                mode="markers",
                name="My Price (Orig)",
                marker=dict(color="blue", size=8, symbol="x")
            ))
        if (vol_oldmax > 0) and (pri_oldmax > 0):
            fig.add_shape(
                type="rect", xref="x", yref="y",
                x0=0, y0=0, x1=vol_oldmax, y1=pri_oldmax,
                fillcolor="blue", opacity=0.10,
                line=dict(color="blue", width=1, dash="dot")
            )
            fig.add_trace(go.Scatter(
                x=[vol_oldmax], y=[pri_oldmax],
                mode="markers",
                name="MaxRev (Orig)",
                marker=dict(color="blue", size=6),
            ))

        # Competitor scenario line
        if competitor_impact and (df_new is not None) and not df_new.empty:
            fig.add_trace(go.Scatter(
                x=df_new["Volume"], y=df_new["Price"],
                mode="lines+markers",
                name="New RPI",
                line=dict(color="purple", width=2, dash="dot")
            ))
            if (Q_cur_new is not None) and (Q_cur_new > 0) and (user_own_price > 0):
                fig.add_shape(
                    type="rect", xref="x", yref="y",
                    x0=0, y0=0, x1=Q_cur_new, y1=user_own_price,
                    fillcolor="purple", opacity=0.25,
                    line=dict(color="purple", width=2, dash="dash")
                )
                fig.add_trace(go.Scatter(
                    x=[Q_cur_new], y=[user_own_price],
                    mode="markers",
                    name="My Price (New)",
                    marker=dict(color="purple", size=8, symbol="x")
                ))

        elas_old_str = f"Elas(Orig)= {format_elas(elas_old)}"
        fig.add_annotation(
            x=0.98, y=0.85, xref="paper", yref="paper",
            text=elas_old_str,
            showarrow=False,
            font=dict(size=12, color="blue"),
            bgcolor="white"
        )
        if competitor_impact and df_new is not None:
            elas_new_str = f"Elas(New)= {format_elas(elas_new)}"
            fig.add_annotation(
                x=0.98, y=0.75, xref="paper", yref="paper",
                text=elas_new_str,
                showarrow=False,
                font=dict(size=12, color="purple"),
                bgcolor="white"
            )

        fig.update_layout(
            title="Demand Curve – Own Price + Competitor Impact",
            xaxis_title="Volume (Q)",
            yaxis_title="Price (P)",
            template="plotly_white"
        )
        
        
        # ────────────────────────────────────────────────────────────────
        #  BASELINE  (avg PPU, default predictors, default RPI)
        # ────────────────────────────────────────────────────────────────
        baseline_key = f"baseline_type1_{sel_idx}"

        if baseline_key not in st.session_state:
            # --- 1.  Baseline inputs ------------------------------------
            base_price = default_vals.get("PPU", 5.0)

            # Non‑price predictors at their stored averages
            non_rpi_predictors = [p for p in betas if (p != "PPU") and (not p.endswith("_RPI"))]
            base_overrides = {p: default_vals[p] for p in non_rpi_predictors}

            # Competitor ratios at their stored averages
            base_rpi = {rp: default_vals[rp] for rp in rpi_cols}

            # --- 2.  Compute baseline volume, revenue, elasticity -------
            base_vol  = compute_current_volume(betas, raw_intercept,
                                            base_price, base_overrides, base_rpi)
            base_rev  = base_price * base_vol
            base_elas = compute_elasticity_full(betas, base_price, base_vol, base_rpi)

            # --- 3.  Save so it never recalculates on rerun --------------
            st.session_state[baseline_key] = {
                "price":       base_price,
                "volume":      base_vol,
                "revenue":     base_rev,
                "elasticity":  base_elas
            }

        # Retrieve stored metrics
        baseline = st.session_state[baseline_key]

        # --- 4.  Display strip of metrics right above the demand curve --
        st.markdown("### Baseline (Avg PPU) Metrics")
        b1, b2, b3, b4 = st.columns(4)
        b1.metric("Avg PPU",     f"${baseline['price']:.2f}")
        b2.metric("Volume",      f"{baseline['volume']:.0f}")
        b3.metric("Revenue",     f"${baseline['revenue']:,.0f}")
        b4.metric("Elasticity",  format_elas(baseline['elasticity']))
        st.markdown("---")   # visual divider before the demand‑curve section

        # IMPROVED DEMAND CURVE VISUALIZATION
        st.markdown("### Demand Curve Analysis")
        
        curve_col1, curve_col2 = st.columns([3, 1])
        
        with curve_col1:
            st.plotly_chart(fig, use_container_width=True)
            # just AFTER you call st.plotly_chart(fig, use_container_width=True)
            st.session_state.setdefault("view_figs", {}).setdefault(view_key, []).append(fig)

        
        with curve_col2:
            # More compact metrics display
            metric_col1, metric_col2 = st.columns(2)
            
            metric_col1.metric(
                label="Current Price",
                value=f"${user_own_price:.2f}"
            )
            
            Q_cur_old_val = max(0, Q_cur_old)
            metric_col2.metric(
                label="Volume", 
                value=f"{Q_cur_old_val:.0f}"
            )
            
            # Second row of metrics
            metric_col3, metric_col4 = st.columns(2)
            
            metric_col3.metric(
                label="Revenue",
                value=f"${Q_cur_old_val * user_own_price:,.0f}"
            )
            
            metric_col4.metric(
                label="Elasticity",
                value=format_elas(elas_old)
            )
            
            # Optional divider for visual separation
            st.markdown("---")
            
            # Revenue max info in more compact format
            if idx_oldmax is not None:
                st.markdown("#### Revenue Maximization")
                max_col1, max_col2 = st.columns(2)
                
                rev_old_max_ = df_old.loc[idx_oldmax, "Revenue"]
                pri_old_max_ = df_old.loc[idx_oldmax, "Price"]
                vol_old_max_ = df_old.loc[idx_oldmax, "Volume"]
                
                max_col1.metric(
                    label="Optimal Price",
                    value=f"${pri_old_max_:.2f}"
                )
                
                max_col2.metric(
                    label="Max Revenue",
                    value=f"${rev_old_max_:.0f}"
                )
                
        # ---------------------------------------------------------------
        #  PRICE‑vs‑REVENUE CURVE  (place at ROOT level, not in a column)
        #  (paste just BEFORE the promo‑elasticity section)
        # ---------------------------------------------------------------
        st.markdown("### Price ⇢ Revenue Curve")

        # ----------------------------------------------------------------
        # 1) Ensure your current price appears in the data grid
        # ----------------------------------------------------------------
        if competitor_impact and (Q_cur_new is not None):
            cur_Q = Q_cur_new       # scenario with new RPI
            use_df = df_new.copy() if df_new is not None else df_old.copy()
        else:
            cur_Q = Q_cur_old
            use_df = df_old.copy()

        cur_rev = user_own_price * cur_Q if (cur_Q is not None) else np.nan

        # If the point is outside the existing price range, append it
        if user_own_price not in use_df["Price"].values:
            use_df.loc[len(use_df)] = {
                "Price": user_own_price,
                "Revenue": cur_rev,
                # columns you don’t care about can be NaN
            }

        # Re‑establish df_old / df_new for plotting (so they now include the point)
        if use_df is df_old:
            df_old = use_df.sort_values("Price")
        else:
            df_new = use_df.sort_values("Price")

        # ----------------------------------------------------------------
        # 2) Build the plot
        # ----------------------------------------------------------------
        fig_rev = go.Figure()
        fig_rev.update_layout(
            plot_bgcolor="rgba(245,245,250,0.9)",
            paper_bgcolor="rgba(245,245,250,0.9)",
            xaxis_title="Price (P)",
            yaxis_title="Revenue (P × Q)",
            template="plotly_white",
            colorway=["#1F77B4", "#8E44AD"]
        )

        # ---------- original scenario ----------
        fig_rev.add_trace(go.Scatter(
            x=df_old["Price"],
            y=df_old["Revenue"],
            mode="lines+markers",
            name="Orig RPI"
        ))
        if idx_oldmax is not None:
            fig_rev.add_trace(go.Scatter(
                x=[pri_oldmax],
                y=[df_old.loc[idx_oldmax, "Revenue"]],
                mode="markers+text",
                text=["Max rev"],
                textposition="bottom center",
                marker=dict(size=9, symbol="diamond", color="#1F77B4"),
                showlegend=False
            ))

        # ---------- competitor‑impact ----------
        if competitor_impact and (df_new is not None) and not df_new.empty:
            fig_rev.add_trace(go.Scatter(
                x=df_new["Price"],
                y=df_new["Revenue"],
                mode="lines+markers",
                name="New RPI",
                line=dict(dash="dot")
            ))
            idx_newmax = df_new["Revenue"].idxmax()
            fig_rev.add_trace(go.Scatter(
                x=[df_new.loc[idx_newmax, "Price"]],
                y=[df_new.loc[idx_newmax, "Revenue"]],
                mode="markers+text",
                text=["Max rev (new)"],
                textposition="bottom center",
                marker=dict(size=9, symbol="diamond", color="#8E44AD"),
                showlegend=False
            ))

        # ---------- YOUR CURRENT POSITION ----------
        fig_rev.add_trace(go.Scatter(
            x=[user_own_price],
            y=[cur_rev],
            mode="markers+text",
            text=[f"Current (${user_own_price:.2f}, {cur_rev:,.0f})"],
            textposition="top center",
            marker=dict(size=12, symbol="diamond", color="#27AE60"),
            name="My current price",
            showlegend=False
        ))

        st.plotly_chart(fig_rev, use_container_width=True)

        st.session_state.setdefault("view_figs", {}).setdefault(view_key, []).append(fig)


        # Data tables in expanders for less vertical space
        with st.expander("View Detailed Data Tables", expanded=False):
            st.markdown("#### Original Scenario Data")
            st.dataframe(df_old, use_container_width=True)
            
            if competitor_impact and df_new is not None and not df_new.empty:
                st.markdown("#### Competitor Impact Scenario Data")
                st.dataframe(df_new, use_container_width=True)
                
                idx_new_max_ = df_new["Revenue"].idxmax()
                rev_new_max_ = df_new.loc[idx_new_max_, "Revenue"]
                pri_new_max_ = df_new.loc[idx_new_max_, "Price"]
                vol_new_max_ = df_new.loc[idx_new_max_, "Volume"]
                
                st.markdown(
                    f"**New scenario:** Max Revenue= **{rev_new_max_:.2f}** "
                    f"at Price=**{pri_new_max_:.2f}**, Volume=**{vol_new_max_:.2f}**"
                )

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # PROMO CLUSTERS (Type 1) – Additional Promo Elasticities
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        st.markdown("### Promotional Elasticity Analysis")
        
        if "final_clusters_depth" in st.session_state and st.session_state["final_clusters_depth"]:
            final_data = st.session_state["final_clusters_depth"]
            key_tup = (channel_, brand_, variant_, ppg_)
            
            if key_tup in final_data:
                st.markdown(f"**Found cluster definitions** for: {key_tup}")
                cluster_defs = final_data[key_tup]
                
                if not cluster_defs:
                    st.info("No promotional cluster bins defined for this model.")
                else:
                    promo_col1, promo_col2 = st.columns([1, 2])
                    
                    with promo_col1:
                        st.markdown("**Cluster Definitions:**")
                        st.dataframe(pd.DataFrame(cluster_defs))
                        
                        cluster_names = [cd["ClusterName"] for cd in cluster_defs]
                        chosen_cluster = st.selectbox("Select a promotion bin:", cluster_names)
                        cobj = next(cd for cd in cluster_defs if cd["ClusterName"] == chosen_cluster)
                        discount_pct = float(cobj["Centroid"])
                        
                        st.markdown(f"**Selected discount**: {discount_pct}%")
                        promo_price = user_own_price * (1 - discount_pct / 100.0)
                        st.metric(label="Promotional Price", value=f"${promo_price:.2f}")
                    
                    with promo_col2:
                        # Scenario calculation
                        Q_promo = compute_current_volume(betas, raw_intercept, promo_price, user_overrides_orig, rpi_old)
                        elas_promo = compute_elasticity_full(betas, promo_price, Q_promo, rpi_old)
                        
                        # Build summary table for all bins
                        base_vol = Q_cur_old
                        bins_info = []
                        bins_info.append({"BinName":"Promo1 (Base)","Discount":0.0})
                        for cd_ in cluster_defs:
                            bins_info.append({
                                "BinName": cd_["ClusterName"],
                                "Discount": float(cd_["Centroid"])
                            })
                        
                        table_rows = []
                        for binrow in bins_info:
                            binname = binrow["BinName"]
                            disc_ = binrow["Discount"]
                            new_price = user_own_price * (1 - disc_ / 100.0)
                            Q_ = compute_current_volume(betas, raw_intercept, new_price, user_overrides_orig, rpi_old)
                            e_ = compute_elasticity_full(betas, new_price, Q_, rpi_old)
                            
                            if binname == "Promo1 (Base)":
                                vol_chg_str = "-"
                            else:
                                if base_vol > 0:
                                    vol_chg_pct = (Q_ - base_vol) / base_vol * 100.0
                                    vol_chg_str = f"{vol_chg_pct:.1f}%"
                                else:
                                    vol_chg_str = "N/A"
                                    
                            table_rows.append({
                                "PromoBin": binname,
                                "Discount%": round(disc_, 2),
                                "Price": round(new_price, 2),
                                "VolumeChange%": vol_chg_str,
                                "Volume": round(Q_, 2),
                                "Elasticity": round(e_, 2) if not np.isnan(e_) else None
                            })
                        
                        df_summary = pd.DataFrame(table_rows)
                        df_summary = df_summary[["PromoBin", "Discount%", "Price", "VolumeChange%", "Volume", "Elasticity"]]
                        
                        st.markdown("**Promotional Bin Summary:**")
                        st.dataframe(df_summary, use_container_width=True)
            else:
                st.info(f"No promotional clusters defined for {key_tup}")
        else:
            st.info("No promotional clusters data available in session.")

        # ────────────────────────────────────────────────────────────────
        #  CROSS‑ELASTICITY ANALYSIS  (drop‑in replacement)
        # ────────────────────────────────────────────────────────────────
        st.markdown("### Cross‑Elasticity Analysis")

        if len(rpi_cols) == 0:
            st.info("No competitor RPI columns found. Cross‑elasticity analysis not applicable.")
        else:
            cross_col1, cross_col2 = st.columns([1, 1])

            with cross_col1:
                # Decide which volume (Q) to use in the elasticity denominator
                if competitor_impact and (Q_cur_new is not None):
                    Q_scenario = Q_cur_new
                    st.info(f"Using competitor‑impact scenario volume: {Q_scenario:.2f}")
                else:
                    Q_scenario = Q_cur_old if (Q_cur_old is not None) else 1.0
                    st.info(f"Using original scenario volume: {Q_scenario:.2f}")

                competitor_data = []
                st.markdown("#### Competitor Price Overrides")

                # ── LOOP OVER EVERY *_RPI COLUMN ─────────────────────────
                for rp_ in rpi_cols:
                    comp_name  = rp_[:-4]          # strip "_RPI"
                    beta_i     = betas[rp_]
                    old_ratio  = default_vals.get(rp_, 0.0)

                    # 1) KEY for this competitor price box (fixed → no resets)
                    key_price = f"{comp_name}_price"

                    # 2) Initialise once: average‑price / average‑ratio
                    if key_price not in st.session_state:
                        base_comp_price = default_vals["PPU"] / old_ratio if old_ratio else 0.0
                        st.session_state[key_price] = round(base_comp_price, 2)

                    col1, col2 = st.columns([3, 2])

                    # 3) NUMBER INPUT always shows the stored value
                    with col1:
                        user_price = st.number_input(
                            f"{comp_name} Price:",
                            value=st.session_state[key_price],
                            step=0.5,
                            key=key_price
                        )

                    # 4) Compute cross elasticity with live ratio
                    with col2:
                        if (user_price > 0) and (Q_scenario > 0):
                            cross_elas = -beta_i * (user_own_price / user_price) / Q_scenario
                        else:
                            cross_elas = np.nan
                        st.markdown(f"**Cross‑Elasticity**: {cross_elas:.4f}")

                    # 5) Store for summary table
                    competitor_data.append({
                        "Competitor": comp_name,
                        "Beta": round(beta_i, 5),
                        "Price": round(user_price, 2),
                        "CrossElasticity": round(cross_elas, 4) if not np.isnan(cross_elas) else None
                    })

            with cross_col2:
                st.markdown("#### Cross‑Elasticity Summary")
                df_cross = pd.DataFrame(competitor_data)
                df_cross.sort_values("CrossElasticity", ascending=False, inplace=True, ignore_index=True)
                st.dataframe(df_cross, use_container_width=True)

                if not df_cross.empty:
                    st.markdown("#### Interpretation")
                    st.markdown("""
                    * **Positive value** → competitor is a **substitute**  
                    (they raise price, you gain volume)  
                    * **Negative value** → competitor is a **complement**  
                    (they raise price, you lose volume)  
                    * **Higher magnitude** → stronger competitive link
                    """)

        st.stop()

    # ============================= TYPE 2 =============================
    st.title("Post Modelling – Final Model Summary (Brand + PPG, Shares Computed From Data)")
    st.subheader("Final Saved Models (Type 2)")

    if "final_saved_models_type2" in st.session_state and st.session_state["final_saved_models_type2"]:
        for key_name, model_list in st.session_state["final_saved_models_type2"].items():
            with st.expander(f"Type 2 Models – Key: {key_name}", expanded=False):
                if model_list:
                    df_type2 = pd.DataFrame(model_list)
                    st.dataframe(df_type2, use_container_width=True)
                else:
                    st.write(f"No final models under key='{key_name}'.")
    else:
        st.info("No final models for Type 2 found.")

    st.write("---")
    st.subheader("Promo Depth Clusters (if any)")
    if "final_clusters_depth" in st.session_state and st.session_state["final_clusters_depth"]:
        final_data = st.session_state["final_clusters_depth"]
        all_rows= []
        for combo_key, bins_list in final_data.items():
            all_rows.extend(bins_list)
        if all_rows:
            df_clusters = pd.DataFrame(all_rows)
            st.markdown("Below are the cluster definitions from the Promo Depth Estimator:")
            st.dataframe(df_clusters, use_container_width=True)
        else:
            st.info("final_clusters_depth is present but empty.")
    else:
        st.info("No final clusters from the Promo Depth module found.")

    st.write("---")
    st.subheader("Data for Post-Modelling Analysis (Type 2 aggregator)")
    with st.expander("Show DataFrame", expanded=False):
        st.dataframe(df_source, use_container_width=True)

    required_cols = {"Date","Channel","Brand","PPG","Volume","SalesValue"}
    if not required_cols.issubset(df_source.columns):
        st.error(f"The chosen DataFrame must have columns: {required_cols}.")
        st.stop()

    df_source["Date"] = pd.to_datetime(df_source["Date"], errors="coerce")
    if df_source["Date"].isna().all():
        st.error("All dates are NaN after converting 'Date'.")
        st.stop()

    st.markdown("#### Select Time Range (Type 2)")
    time_options= ["Last Quarter (3 mo)","Last 12 Months","Entire Data"]
    time_choice= st.radio("Time Range for Type 2:", time_options, index=1)

    max_date= df_source["Date"].max()
    df_filtered= df_source.copy()
    import pandas as pd
    if time_choice == "Last Quarter (3 mo)":
        cutoff_date= max_date - pd.DateOffset(months=3)
        df_filtered= df_filtered[df_filtered["Date"]>=cutoff_date]
    elif time_choice == "Last 12 Months":
        cutoff_date= max_date - pd.DateOffset(months=12)
        df_filtered= df_filtered[df_filtered["Date"]>=cutoff_date]

    if df_filtered.empty:
        st.warning("No data left after the selected time range.")
        st.stop()

    # Summaries for Type 2 aggregator approach
    df_price = (
        df_filtered
        .groupby(["Channel","Brand","PPG"], as_index=False)
        .agg({"SalesValue":"sum","Volume":"sum"})
    )
    df_price["Price"] = df_price["SalesValue"] / df_price["Volume"].replace(0, np.inf)
    df_price.rename(columns={"Volume":"SumVolume"}, inplace=True)

    df_filtered["YearMonth"] = df_filtered["Date"].dt.to_period("M")
    group_ym = (
        df_filtered
        .groupby(["Channel","Brand","PPG"])["YearMonth"]
        .nunique()
        .reset_index(name="MonthsCount")
    )
    df_price = pd.merge(df_price, group_ym, on=["Channel","Brand","PPG"], how="left")
    df_price["AvgVolume"] = df_price["SumVolume"] / df_price["MonthsCount"].replace(0,1)

    # Retrieve your stored model picks
    df_brand_models= pd.DataFrame(st.session_state["final_saved_models_type2"]["Brand"])
    df_ppg_models  = pd.DataFrame(st.session_state["final_saved_models_type2"]["PPG"])
    df_brand_models.rename(columns={"MCV":"brand_MCV"}, inplace=True)
    df_ppg_models.rename(columns={"MCV":"ppg_MCV"}, inplace=True)

    df_merged= pd.merge(
        df_price,
        df_brand_models[["Channel","Brand","brand_MCV"]],
        on=["Channel","Brand"],
        how="inner"
    )
    df_merged= pd.merge(
        df_merged,
        df_ppg_models[["Channel","PPG","ppg_MCV"]],
        on=["Channel","PPG"],
        how="inner"
    )

    brand_vol= (
        df_merged.groupby(["Channel","Brand"], as_index=False)["SumVolume"]
        .sum()
        .rename(columns={"SumVolume":"brandVol"})
    )
    df_merged= pd.merge(df_merged, brand_vol, on=["Channel","Brand"], how="left")
    df_merged["ppg_share"]= df_merged["SumVolume"]/ df_merged["brandVol"].replace(0, np.inf)
    df_merged["ppg_partial"]= df_merged["ppg_share"]* df_merged["ppg_MCV"]
    brand_index= (
        df_merged.groupby(["Channel","Brand"], as_index=False)["ppg_partial"]
        .sum()
        .rename(columns={"ppg_partial":"brand_index"})
    )
    df_merged= pd.merge(df_merged, brand_index, on=["Channel","Brand"], how="left")
    df_merged["final_mcv"] = (df_merged["brand_MCV"]* df_merged["ppg_MCV"])/ df_merged["brand_index"].replace(0,np.inf)
    df_merged["c"]= df_merged["final_mcv"]
    df_merged["m"]= (df_merged["Price"]- df_merged["c"])/ df_merged["AvgVolume"].replace(0, np.inf)

    def compute_elasticity(row):
        m_= row["m"]
        p_= row["Price"]
        q_= row["AvgVolume"]
        if (m_==0) or (q_==0):
            return np.nan
        return (1.0/ m_)*(p_/ q_)

    df_merged["Elasticity"]= df_merged.apply(compute_elasticity, axis=1)

    with st.expander("Final Merged Table (Type 2)", expanded=False):
        st.dataframe(df_merged, use_container_width=True)

    st.markdown("<b>Demand Curves (Volume vs. Price) + Elasticity (Type 2)</b>", unsafe_allow_html=True)

    # Demand curves for Type 2
    for idx, row in df_merged.iterrows():
        channel_   = row["Channel"]
        brand_     = row["Brand"]
        ppg_       = row["PPG"]
        intercept  = row["c"]
        slope_     = row["m"]
        avg_vol    = row["AvgVolume"]
        avg_price  = row["Price"]
        elasticity = row["Elasticity"]

        if avg_vol<=0:
            st.write(f"Skipping {channel_}-{brand_}-{ppg_}, no positive volume.")
            continue

        max_domain_vol= 1.5* avg_vol
        if slope_<0:
            zero_cross= -intercept/ slope_
            if 0< zero_cross< max_domain_vol:
                max_domain_vol= zero_cross
        if max_domain_vol<=0:
            st.write(f"Skipping {channel_}-{brand_}-{ppg_} (domain negative).")
            continue

        volumes= np.linspace(0, max_domain_vol, 100)
        prices= intercept+ slope_* volumes
        prices[prices<0]= 0
        revenues= volumes* prices
        idx_max_= np.argmax(revenues)
        vol_max= volumes[idx_max_]
        rev_max= revenues[idx_max_]
        price_max= prices[idx_max_]

        fig= go.Figure()
        fig.update_layout(
            colorway=["#17BECF","#BCBD22","#9467BD"],
            plot_bgcolor="rgba(245,245,250,0.9)",
            paper_bgcolor="rgba(245,245,250,0.9)"
        )
        fig.add_trace(go.Scatter(
            x=volumes, y=prices,
            mode="lines", name="Demand Curve",
            line=dict(color="blue",width=2),
        ))
        fig.update_layout(
            shapes=[
                dict(
                    type="rect", xref="x", yref="y",
                    x0=0, y0=0,
                    x1= avg_vol, y1= avg_price,
                    fillcolor="limegreen",
                    opacity=0.3,
                    line=dict(color="red",width=2,dash="dash")
                )
            ]
        )
        fig.add_trace(go.Scatter(
            x=[avg_vol], y=[avg_price],
            mode="markers",
            name="Avg Price & Volume",
            marker=dict(color="orange", size=10),
        ))
        if vol_max>0 and price_max>0:
            fig.add_shape(
                type="rect",
                xref="x", yref="y",
                x0=0, y0=0,
                x1=vol_max, y1= price_max,
                fillcolor="red", opacity=0.15,
                line=dict(color="red",width=1,dash="dot")
            )
            fig.add_trace(go.Scatter(
                x=[vol_max], y=[price_max],
                mode="markers",
                name="Max Revenue",
                marker=dict(color="red", size=10),
            ))
        elas_str= f"{elasticity:.2f}" if not np.isnan(elasticity) else "N/A"
        fig.add_annotation(
            x=0.5, y=1.06, xref="paper", yref="paper",
            text=f"<b>Elasticity: {elas_str}</b>",
            showarrow=False,
            font=dict(size=14, color="black"),
        )
        fig.update_layout(
            title=f"Demand Curve – (Channel={channel_}, Brand={brand_}, PPG={ppg_})",
            xaxis_title="Volume (Q)",
            yaxis_title="Price",
            template="plotly_white",
            legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.5)"),
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.session_state.setdefault("view_figs", {}).setdefault(view_key, []).append(fig)





    
###########################################################v2#########################################################################


# ----------------
#   PAGE ROUTER
# ----------------
page = st.session_state.page

if page == "home":
    home_page()

elif page.startswith("section") and "_" not in page:
    section_number = page.replace("section", "")
    section_page(section_number)


elif "_" in page:
    # Could be subpages like: section1_baseprice, section1_promodepth, ...
    # or the universal action pages: section2_action1, etc.
    if page == "preprocess_validate":
        validate_page()
    elif page == "preprocess_feature_overview":
        feature_overview_page()
    elif page == "preprocess_prepare":
        prepare_page()
    elif page == "preprocess_base_price":
        base_price_page()
        
    elif page == "preprocess_promo_depth":
        promo_depth_page()
        
    # --- NEW SUB-PAGES FOR SECTION 2 ---
    elif page == "market_construct":
        market_construct_page()
    elif page == "price_ladder":
        price_ladder_page()

    elif page == "feature_overview_2":
        feature_overview_page_2()
    elif page == "create_section3":
        create_page()
    elif page == "transform_section3":
        transform_page()
    elif page == "select_section3":
        select_page()

    elif page == "Build_1":
        build_page()

    elif page == "model_selection":
        model_selection_page()
    elif page == "post_modelling":
        post_modelling_page()
        
    elif page == "model_review":
        model_review_page()
        
    elif page == "report_1":
        report_page()
        
        
    elif page == "type2_combine":
            type2_combine_page()
        
    else:
        # fallback
        section_number, action_number = page.replace("section", "").split("_action")
        action_page(section_number, action_number)


# ─────────────────────────── Persisted File Uploads ──────────────────────────
st.sidebar.header("📂 File Management")

# 1️⃣ Rehydrate previously uploaded files
st.session_state.setdefault("uploaded_files", {})
file_names = load_state(pid, "uploaded_file_names", [])
for name in file_names:
    if name not in st.session_state.uploaded_files:
        blob = load_state(pid, f"file_{name}", None)
        if blob is not None:
            df = pd.read_json(blob, orient="split")
            st.session_state.uploaded_files[name] = df

# 2️⃣ File uploader
uploaded = st.sidebar.file_uploader(
    "Upload your CSV/Excel files:",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)

# 3️⃣ Process & persist new uploads
if uploaded:
    file_list = load_state(pid, "uploaded_file_names", [])
    for file in uploaded:
        if file.name not in st.session_state.uploaded_files:
            df = pd.read_csv(file) if file.name.lower().endswith(".csv") else pd.read_excel(file)
            st.session_state.uploaded_files[file.name] = df
            save_state(pid, f"file_{file.name}", df.to_json(orient="split"))
            file_list.append(file.name)
    save_state(pid, "uploaded_file_names", file_list)

# 4️⃣ Let the user pick & delete
if st.session_state.uploaded_files:
    file_list = list(st.session_state.uploaded_files.keys())
    # use last saved selection, or fallback
    last_sel = load_state(pid, "selected_file", None)
    default_idx = file_list.index(last_sel) if last_sel in file_list else 0

    selected = st.sidebar.selectbox(
        "Choose a file for analysis:",
        options=file_list,
        index=default_idx
    )
    st.sidebar.success(f"Using file: `{selected}`")

    # stash & persist choice
    df = st.session_state.uploaded_files[selected]
    st.session_state["D0"] = df
    save_state(pid, "selected_file", selected)
    save_state(pid, "selected_file_index", file_list.index(selected))

    # 🗑 Delete action
    if st.sidebar.button("🗑 Delete file"):
        # remove from session
        st.session_state.uploaded_files.pop(selected, None)

        # update master list
        new_list = list(st.session_state.uploaded_files.keys())
        save_state(pid, "uploaded_file_names", new_list)

        # delete blobs & selection metadata
        conn = _db()
        conn.execute("DELETE FROM project_state WHERE project_id=? AND key=?", (pid, f"file_{selected}"))
        conn.execute("DELETE FROM project_state WHERE project_id=? AND key=?", (pid, "selected_file"))
        conn.execute("DELETE FROM project_state WHERE project_id=? AND key=?", (pid, "selected_file_index"))
        conn.commit()

        st.sidebar.success(f"Deleted `{selected}`!")
        st.experimental_rerun()

else:
    st.sidebar.warning("Please upload at least one file.")
