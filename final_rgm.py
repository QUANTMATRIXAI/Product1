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
    background-color: #FFBD59; /* Primary Yellow */
    color: #333333;
    border: none;
    padding: 0.6em 1.2em;
    border-radius: 4px;
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

# Section Names
section_names = {
    "1": "Base/Promo Detection",
    "2": "Price/Promo Elasticity",
    "3": "RGM Pillars",
    "4": "Engineer"  # <-- newly added
}

# ----------------
#     HOME PAGE
# ----------------
def home_page():
    st.title("Welcome to RGM App")
    st.write("Below are three sections of the app. Click on their respective buttons to navigate.")

    col1, col2, col3, col4 = st.columns(4)

    # Card for Section 1
    with col1:
        st.markdown(
            """
            <div class='custom-card'>
              <h3 style="margin-top:0;">Base/Promo Detection</h3>
              <p>Analyze, detect, and manage base/promo scenarios with advanced logic.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Go to Base/Promo Detection"):
            go_to("section1")

    # Card for Section 2
    with col2:
        st.markdown(
            f"""
            <div class='custom-card'>
              <h3 style="margin-top:0;">{section_names['2']}</h3>
              <p>Additional functionalities, data processing, or analytics for Section 2.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Go to Price/Promo Elasticity"):
            go_to("section2")

    # Card for Section 3
    with col3:
        st.markdown(
            f"""
            <div class='custom-card'>
              <h3 style="margin-top:0;">{section_names['3']}</h3>
              <p>Expand or explore tasks, visualizations, or reports for Section 3.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Go to RGM Pillars"):
            go_to("section3")

    # --- New Section 4: Engineer ---
    with col4:
        st.markdown(
            f"""
            <div class='custom-card'>
              <h3 style="margin-top:0;">{section_names['4']}</h3>
              <p>Manage engineering tasks, processes, or workflows.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Go to Engineer"):
            go_to("section4")
    
    
    # --------------------------------------------------------
    # Subheading: "Other Advanced Tools from Quant Matrix AI"
    # --------------------------------------------------------
    st.markdown("---")  # horizontal rule
    st.markdown("## Additional Advanced Solutions from Quant Matrix AI")

# 4th Card: EDA (QuantMatrix Solutions)
    st.markdown(
        """
        <div class='custom-card'>
          <h3 style="margin-top:0;">QuantMatrix EDA Suite</h3>
          <p>Perform advanced Exploratory Data Analysis, Clustering, Feature Importance, and more.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Go to EDA App"):
        go_to("myEDA")  
        
        
        
# 4th Card: EDA (QuantMatrix Solutions)
    st.markdown(
        """
        <div class='custom-card'>
          <h3 style="margin-top:0;">QuantMatrix Modeling Suite</h3>
          <p>Perform advanced Exploratory Data Analysis, Clustering, Feature Importance, and more.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Go to Modeling Suite"):
        go_to("modelingSuite")  # or whichever route you use



    st.markdown("""
    ---
    <div style='text-align:center; color:#666; font-size:0.9rem;'>
    © 2025 RGM Tool &nbsp;|&nbsp; Powered by Quant Matrix AI &nbsp;–&nbsp; All Rights Reserved
    </div>
    """, unsafe_allow_html=True)

        
# ------------------------------
#  SECTION PAGE (Multi-Purpose)
# ------------------------------
def section_page(section_number):
    displayed_name = section_names.get(section_number, f"Section {section_number}")
    st.header(displayed_name)

    # Only do special layout for section 1
    if section_number == "1":
        st.write("Below are the **three modules** for Base/Promo Detection.")
        col1, col2, col3 = st.columns(3)
        
        # 1) Automated Base Price Estimator
        with col1:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Automated Base Price Estimator</h4>
                  <p>Automatically estimate base prices using advanced ML or rule-based methods.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Base Price Estimator"):
                go_to("section1_baseprice")
        
        # 2) Automatic Promo Depth Estimator
        with col2:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Automatic Promo Depth Estimator</h4>
                  <p>Automatically suggest promo depths or discounts based on historical data.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Promo Depth Estimator"):
                go_to("section1_promodepth")
        
        # 3) Promo Calendar Comparison
        with col3:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Promo Calendar Comparison</h4>
                  <p>Compare different promo calendars, overlaps, and timing impact.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Calendar Comparison"):
                go_to("section1_calendar")
                
                
        with col1:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Market Construct</h4>
                  <p>Compare different promo calendars, overlaps, and timing impact.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Market Construct",key= "market"):
                go_to("section1_market_construct")
                
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
            st.write("Below are the **three modules** for Price/Promo Elasticity.")
            
            col1, col2, col3 = st.columns(3)

            # ============= MODULE 1 =============
            with col1:
                st.markdown(
                    """
                    <div class='custom-card'>
                    <h4 style="margin-top:0;">Price/Promo Elasticity</h4>
                    <p>Compute and analyze price/promo elasticity using various models.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Price/Promo Elasticity"):
                    go_to("section2_module1")  # route name

            # ============= MODULE 2 =============
            with col2:
                st.markdown(
                    """
                    <div class='custom-card'>
                    <h4 style="margin-top:0;">Post Modelling</h4>
                    <p>Assess model outputs, validate results, and refine assumptions.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Post Modelling"):
                    go_to("section2_module2")

            # ============= MODULE 3 =============
            with col3:
                st.markdown(
                    """
                    <div class='custom-card'>
                    <h4 style="margin-top:0;">Scenario Planner</h4>
                    <p>Explore ‘what-if’ scenarios and potential outcomes.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Scenario Planner"):
                    go_to("section2_module3")

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
            st.write("Below are the advanced modules for RGM analsyis.")
            
            col1, col2, col3 = st.columns(3)

            # ============= MODULE 1 =============
            with col1:
                st.markdown(
                    """
                    <div class='custom-card'>
                    <h4 style="margin-top:0;">🔖 Price Pack Architecture</h4>
                    <p>Compute and analyze price/promo elasticity using various models.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Price Pack Architecture"):
                    go_to("section3_module1")  # route name

            # ============= MODULE 2 =============
            with col2:
                st.markdown(
                    """
                    <div class='custom-card'>
                    <h4 style="margin-top:0;">📶 Brand Ladder Analysis</h4>
                    <p>Assess model outputs, validate results, and refine assumptions.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Brand Ladder Analysis"):
                    go_to("section3_module2")

            # ============= MODULE 3 =============
            with col3:
                st.markdown(
                    """
                    <div class='custom-card'>
                    <h4 style="margin-top:0;">🧮 Distribution Opportunity Analysis</h4>
                    <p>Explore ‘what-if’ scenarios and potential outcomes.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Go to Distribution Opportunity Analysis"):
                    go_to("section3_module3")
                    
                    




    # 2) New Section 4 Layout
    elif section_number == "4":
        st.write("Below are the modules available for our Engineering workflows.")

        # Four columns for the four modules
        col1, col2, col3, col4 = st.columns(4)

        # Module: Feature Overview
        with col1:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Feature Overview</h4>
                  <p>Inspect and manage high-level feature sets.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Feature Overview"):
                go_to("section4_feature_overview")

        # Module: Transform
        with col3:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Transform</h4>
                  <p>Clean, transform, or reshape data through automated pipelines.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Transform"):
                go_to("section4_transform")

        # Module: Create
        with col2:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Create</h4>
                  <p>Generate new models, features, or engineering workflows.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Create"):
                go_to("section4_create")

        # Module: Select
        with col4:
            st.markdown(
                """
                <div class='custom-card'>
                  <h4 style="margin-top:0;">Select</h4>
                  <p>Choose from different engineering strategies and approaches.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Go to Select"):
                go_to("section4_select")

        # Navigation controls
        st.markdown("---")
        nav_col1, nav_col2 = st.columns(2)
        with nav_col1:
            if st.button("Back"):
                go_back()
        with nav_col2:
            if st.button("Home"):
                go_home()



#########################################def Engineer
###############inter page navigation



################################################

def Feature_Overview_page():


    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

    # -----------------------------------------------------------------------
    # 1) CUSTOM CSS (Your Style Guide)
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

    # Accent colors for your charts
    STYLE_COLORS = [
        "#FFBD59",  # gold
        "#FFC87A",  # lighter gold
        "#41C185",  # green
        "#458EE2",  # blue
        "#FF7F7F",  # red
    ]

    # -----------------------------------------------------------------------
    # 2) MAIN HEADER & NAVIGATION
    # -----------------------------------------------------------------------
    st.markdown('<h1 class="custom-header">Feature Overview</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Radio-based aggregator filtering plus advanced analysis features – all in a user-friendly layout.</p>', unsafe_allow_html=True)
    st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)


    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()

    # -----------------------------------------------------------------------
    # 3) RETRIEVE DATA
    # -----------------------------------------------------------------------
    df = st.session_state.get("D0", None)
    if df is None or df.empty:
        st.warning("No data found in st.session_state['D0']. Please load your dataset.")
        st.stop()

    # -----------------------------------------------------------------------
    # CARD 0: MULTI-COLUMN FILTER (RADIO-BASED)
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)


    cat_cols_all = df.select_dtypes(include=["object","category"]).columns.tolist()
    if not cat_cols_all:
        st.info("No categorical columns found. No aggregator filter applied.")
    else:
        agg_cols_picked = st.multiselect(
            "Pick aggregator columns to filter (radio-based):",
            cat_cols_all,
            default=[]
        )
        for colname in agg_cols_picked:
            distinct_vals = sorted(df[colname].dropna().unique().tolist())
            all_option = "All"
            options_for_radio = [all_option] + distinct_vals
            selected_val = st.radio(
                f"{colname}:",
                options_for_radio,
                index=0,  # default to "All"
                key=f"AggRadio_{colname}",
                horizontal=True
            )
            if selected_val != all_option:
                df = df[df[colname]==selected_val]
                if df.empty:
                    st.warning(f"No data left after filtering on {colname} = {selected_val}.")
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.stop()

    st.markdown('</div>', unsafe_allow_html=True)

    # # -----------------------------------------------------------------------
    # # CARD 1: QUICK STATS
    # # -----------------------------------------------------------------------
    # st.markdown('<div class="card">', unsafe_allow_html=True)
    # st.write("## 1) Quick Stats")

    # n_rows, n_cols = df.shape
    # mem_mb = df.memory_usage(deep=True).sum()/1e6
    # total_cells = n_rows*n_cols
    # missing_count = df.isna().sum().sum()
    # perc_missing = (missing_count/total_cells*100) if total_cells else 0

    # colA, colB, colC = st.columns(3)
    # with colA:
    #     st.markdown("**Shape**")
    #     st.write(f"{n_rows} rows × {n_cols} columns")

    # with colB:
    #     st.markdown("**Memory Usage**")
    #     st.write(f"{mem_mb:.2f} MB")

    # with colC:
    #     st.markdown("**Overall Missing**")
    #     st.write(f"{missing_count} ({perc_missing:.2f}%)")

    # st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 2: COLUMN DETAILS
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 1) Column Details")

    column_info = []
    for c in df.columns:
        ctype = str(df[c].dtype)
        miss = df[c].isna().sum()
        uniq = df[c].nunique(dropna=True)
        sample_vals = df[c].dropna().unique()[:3]
        sample_str = ", ".join(map(str, sample_vals)) if len(sample_vals)>0 else "N/A"
        column_info.append({
            "Column": c,
            "Type": ctype,
            "Missing": miss,
            "Unique": uniq,
            "Examples": sample_str
        })
    detail_df = pd.DataFrame(column_info)
    st.dataframe(detail_df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Identify numeric/categorical columns in the aggregator-filtered dataset
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object","category"]).columns.tolist()

    # -----------------------------------------------------------------------
    # CARD 3: NUMERIC & CATEGORICAL INSIGHTS
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 3) Numeric & Categorical Insights")

    cNum, cCat = st.columns(2)

    # 3.1 Numeric side
    with cNum:
        st.markdown("### Numeric Columns")
        if numeric_cols:
            desc_stats = df[numeric_cols].describe().T
            st.write("**Descriptive Stats**")
            st.dataframe(desc_stats, use_container_width=True)

            outlier_toggle = st.checkbox("Check for Potential Outliers (1.5×IQR)?", key="OutlierCheck")
            if outlier_toggle:
                outlier_info = []
                for coln in numeric_cols:
                    q1 = df[coln].quantile(0.25)
                    q3 = df[coln].quantile(0.75)
                    iqr = q3 - q1
                    lb = q1 - 1.5*iqr
                    ub = q3 + 1.5*iqr
                    out_count = ((df[coln]<lb)|(df[coln]>ub)).sum()
                    outlier_info.append({
                        "Column": coln,
                        "Outliers": out_count,
                        "LowerBound": f"{lb:.2f}",
                        "UpperBound": f"{ub:.2f}"
                    })
                st.dataframe(pd.DataFrame(outlier_info), use_container_width=True)
        else:
            st.info("No numeric columns in the filtered subset.")

    # 3.2 Categorical side
    with cCat:
        st.markdown("### Categorical Columns")
        if cat_cols:
            st.write("**Frequency Table**")
            pick_cat = st.selectbox("Pick a categorical column:", cat_cols, key="CatColPick")
            top_k = st.slider("Show top K categories:", 1, 20, 5, key="CatTopK")
            freq_s = df[pick_cat].value_counts(dropna=False).head(top_k)
            freq_df = freq_s.rename_axis(pick_cat).reset_index(name="Count")
            freq_df["Percent"] = freq_df["Count"]/freq_df["Count"].sum()*100
            st.dataframe(freq_df, use_container_width=True)
        else:
            st.info("No categorical columns in the filtered subset.")

    # Now we do a full-width advanced cat-cat section, **below** the columns
    st.markdown("---")  # a separator
    st.markdown("### Advanced Categorical-Categorical Analysis (Full Width)")

    if len(cat_cols) >= 2:
        adv_catcat_toggle = st.checkbox("Enable cross-tab analysis?", key="CatCatToggle")
        if adv_catcat_toggle:
            # user picks two distinct cat columns
            st.write("Pick two different categorical columns for cross-tab analysis:")
            cat1 = st.selectbox("Column A:", cat_cols, key="CatCatCol1")
            cat2 = st.selectbox("Column B:", cat_cols, key="CatCatCol2")

            if cat1 and cat2 and cat1!=cat2:
                crosstab_data = pd.crosstab(df[cat1], df[cat2])
                st.write("**Cross-Tab (Counts)**")
                st.dataframe(crosstab_data, use_container_width=True)

                # optional heatmap
                show_heatmap = st.checkbox("Show Cross-Tab Heatmap?", key="CatCatHeatmap")
                if show_heatmap:
                    fig_heat = px.imshow(
                        crosstab_data,
                        text_auto=True,
                        aspect="auto",
                        title=f"{cat1} vs. {cat2} Cross-Tab"
                    )
                    st.plotly_chart(fig_heat, use_container_width=True)
            else:
                st.info("Please pick two distinct columns for cross-tab.")
    else:
        st.info("Fewer than 2 categorical columns remain after filtering, so cross-tab is not available.")

    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 4: DISTRIBUTIONS
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 4) Distributions")

    distL, distR = st.columns(2)

    # numeric histogram
    with distL:
        st.markdown("**Histogram (Numeric)**")
        if numeric_cols:
            pick_num = st.selectbox("Select numeric column:", ["(None)"]+numeric_cols, key="NumDistPick")
            if pick_num!="(None)":
                log_check = st.checkbox("Log-scale Y-axis?", key="HistLogY")
                fig_hist = px.histogram(
                    df, x=pick_num, nbins=30,
                    title=f"Distribution of {pick_num}",
                    color_discrete_sequence=[STYLE_COLORS[0]]
                )
                if log_check:
                    fig_hist.update_yaxes(type="log")
                st.plotly_chart(fig_hist, use_container_width=True)

    # categorical bar
    with distR:
        st.markdown("**Bar Chart (Categorical)**")
        if cat_cols:
            pick_cat2 = st.selectbox("Select categorical column:", ["(None)"]+cat_cols, key="CatDistPick2")
            if pick_cat2!="(None)":
                freq_s = df[pick_cat2].value_counts(dropna=False)
                freq_df = freq_s.rename_axis(pick_cat2).reset_index(name="Count")
                freq_df["Percent"] = freq_df["Count"] / freq_df["Count"].sum()*100

                bar_mode = st.selectbox("Bar Mode:", ["Absolute Count","Percent"], key="CatBarMode")
                y_axis = "Count" if bar_mode=="Absolute Count" else "Percent"
                fig_bar = px.bar(
                    freq_df, x=pick_cat2, y=y_axis,
                    title=f"Bar Chart of {pick_cat2}",
                    color_discrete_sequence=[STYLE_COLORS[1]]
                )
                if bar_mode=="Percent":
                    fig_bar.update_yaxes(title="Percent")
                st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 5: CORRELATION (FULL WIDTH)
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 5) Correlation Matrix")

    numeric_cols_filtered = [nc for nc in numeric_cols if df[nc].nunique() > 1]
    if len(numeric_cols_filtered) > 1:
        corr_method = st.selectbox("Correlation method:", ["pearson","spearman","kendall"], key="CorrMethodPick")
        corr_thresh = st.slider("Correlation threshold (mask smaller correlations):", 0.0,1.0,0.0,0.01, key="CorrThresh")
        corr_mat = df[numeric_cols_filtered].corr(method=corr_method)
        if corr_thresh>0:
            mask = corr_mat.abs()<corr_thresh
            corr_mat = corr_mat.mask(mask, np.nan)

        fig_corr = px.imshow(
            corr_mat, text_auto=True, aspect="auto",
            title=f"{corr_method.capitalize()} Correlation (≥ |{corr_thresh}| shown)",
            color_continuous_scale="RdBu"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    else:
        st.info("Not enough numeric columns (with variety) for correlation in the filtered data.")

    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 6: SAMPLE ROWS
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 6) Sample Rows")

    n_samp = st.slider("Number of sample rows:",1,50,5)
    st.dataframe(df.head(n_samp), use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)



def Transform_page():
    
    
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px



    # =============================================================================
    # CUSTOM CSS
    # =============================================================================
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
        padding: 1.2rem;
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

    # =============================================================================
    # MAIN HEADER & NAVIGATION
    # =============================================================================
    st.markdown('<h1 class="custom-header">Transform Page</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Filter data from your "Create" page, apply scaling transformations, and compare before–after results.</p>', unsafe_allow_html=True)
    st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)

    nav_left, nav_right = st.columns(2)
    with nav_left:
        if st.button("Back", key="transform_btnBack"):
            go_back()
    with nav_right:
        if st.button("Home", key="transform_btnHome"):
            go_home()

    # =============================================================================
    # RETRIEVE Data from st.session_state["create_data"]
    # =============================================================================
    if "create_data" not in st.session_state:
        st.warning("No data found in st.session_state['create_data']. Please ensure your 'Create' page populates it.")
        st.stop()

    # Start with the latest saved data.
    data = st.session_state["create_data"]
    df = data.copy()  # working copy

    # =============================================================================
    # CARD 0: Aggregator Filter (Categorical)
    # =============================================================================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 0) Aggregator Filter (Categorical)")

    # Get the list of categorical columns.
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if cat_cols:
        # Allow user to choose which categorical columns they want to filter
        filter_cols = st.multiselect("Select categorical columns to filter:", cat_cols, key="filter_cols")
        for col in filter_cols:
            # Build options: "All" plus all unique non-null values
            unique_vals = sorted(df[col].dropna().unique().tolist())
            opts = ["All"] + unique_vals
            chosen_val = st.radio(f"Filter {col} by:", opts, index=0, horizontal=True, key=f"filter_{col}")
            if chosen_val != "All":
                df = df[df[col] == chosen_val]
                if df.empty:
                    st.warning(f"No data left after filtering {col} = {chosen_val}")
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.stop()
    else:
        st.info("No categorical columns available for filtering.")
    st.markdown('</div>', unsafe_allow_html=True)

    # =============================================================================
    # CARD 1: Scaling Transformations for X and Y Columns
    # =============================================================================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 1) Scaling Transformations")

    # Identify numeric columns from the (possibly filtered) DataFrame.
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    colX, colY = st.columns(2)

    with colX:
        st.markdown("### X Columns (Multiple)")
        if numeric_cols:
            x_cols = st.multiselect("Choose one or more X numeric columns:", numeric_cols, key="x_cols")
            x_method = st.selectbox("Select scaling method (X):", ["Standard", "MinMax", "Robust", "MeanNorm"], key="x_method")
            x_suffix = st.text_input("Suffix for transformed X columns:", "_xScaled", key="x_suffix")
        else:
            st.info("No numeric columns available for X transformations.")
            x_cols = []

    with colY:
        st.markdown("### Y Column (Single)")
        if numeric_cols:
            y_col = st.selectbox("Choose one Y numeric column:", ["None"] + numeric_cols, key="y_col")
            if y_col != "None":
                y_method = st.selectbox("Select scaling method (Y):", ["Standard", "MinMax", "Robust", "MeanNorm"], key="y_method")
                y_suffix = st.text_input("Suffix for transformed Y column:", "_yScaled", key="y_suffix")
            else:
                y_method, y_suffix = None, ""
        else:
            st.info("No numeric columns available for Y transformation.")
            y_col = "None"

    # Helper function to perform scaling transformation.
    def do_scale_transform(series: pd.Series, method: str) -> pd.Series:
        s_clean = series.dropna()
        if method == "Standard":
            mu = s_clean.mean()
            sigma = s_clean.std()
            if sigma == 0:
                return pd.Series(np.nan, index=series.index)
            return (series - mu) / sigma
        elif method == "MinMax":
            mn = s_clean.min()
            mx = s_clean.max()
            if mx == mn:
                return pd.Series(np.nan, index=series.index)
            return (series - mn) / (mx - mn)
        elif method == "Robust":
            med = s_clean.median()
            q1 = s_clean.quantile(0.25)
            q3 = s_clean.quantile(0.75)
            iqr = q3 - q1
            if iqr == 0:
                return pd.Series(np.nan, index=series.index)
            return (series - med) / iqr
        else:  # "MeanNorm"
            mu = s_clean.mean()
            mn = s_clean.min()
            mx = s_clean.max()
            denom = mx - mn
            if denom == 0:
                return pd.Series(np.nan, index=series.index)
            return (series - mu) / denom

    if st.button("Apply & Save Transformations", key="apply_transform_btn"):
        # Apply transformation for each X column.
        for col in x_cols:
            new_col = col + x_suffix
            df[new_col] = do_scale_transform(df[col], x_method)
        # Apply transformation for the Y column.
        if y_col != "None":
            new_y = y_col + y_suffix
            df[new_y] = do_scale_transform(df[y_col], y_method)
        # Save updated data.
        st.session_state["create_data"] = df.copy()
        st.success("Transformations applied and data updated.")
    st.markdown('</div>', unsafe_allow_html=True)

    # =============================================================================
    # CARD 2: Comparison Chart ("Before vs After")
    # =============================================================================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 2) Comparison Chart")

    # Re-read the latest updated data.
    df_latest = st.session_state.get("create_data").copy()

    # Build dynamic options for "original" and "transformed" columns.
    orig_options = []
    trans_options = []

    # Original options come from the selected X columns and Y column.
    if x_cols:
        orig_options.extend(x_cols)
    if y_col != "None":
        orig_options.append(y_col)

    # Build list of transformed column names.
    for col in x_cols:
        candidate = col + x_suffix
        if candidate in df_latest.columns:
            trans_options.append(candidate)
    if y_col != "None":
        candidate = y_col + y_suffix
        if candidate in df_latest.columns:
            trans_options.append(candidate)

    orig_choice = st.selectbox("Select Original Column:", ["None"] + orig_options, key="orig_choice")
    trans_choice = st.selectbox("Select Transformed Column:", ["None"] + trans_options, key="trans_choice")

    chart_choice = st.radio("Select Chart Type:", ["Line", "Bar"], horizontal=True, key="chart_choice")
    n_rows = st.slider("Rows to display in chart:", 5, 50, 10, key="chart_rows")

    if orig_choice != "None" and trans_choice != "None":
        comp_df = df_latest[[orig_choice, trans_choice]].head(n_rows).reset_index()
        if chart_choice == "Line":
            fig = px.line(comp_df, x="index", y=[orig_choice, trans_choice], markers=True)
        else:
            fig = px.bar(comp_df, x="index", y=[orig_choice, trans_choice], barmode="group")
        fig.update_layout(margin=dict(l=40, r=40, t=40, b=40))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Select an original and a transformed column to display a comparison chart.")
    st.markdown('</div>', unsafe_allow_html=True)

    # =============================================================================
    # CARD 3: Final DataFrame Preview and Universal Save Button
    # =============================================================================
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 3) Final DataFrame Preview (Top 10 Rows)")
    st.dataframe(df_latest.head(10), use_container_width=True)

    # Universal Save Button: Save all current changes.
    if st.button("Universal Save: Save All Changes", key="universal_save"):
        st.session_state["create_data"] = df_latest.copy()
        st.success("All changes have been universally saved to session state!")
    st.markdown('</div>', unsafe_allow_html=True)



    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()
            


def Create_page():
    
    
    import streamlit as st
    import pandas as pd
    import numpy as np

    # -----------------------------------------------------------------------
    # Load the DataFrame: Use updated data if available, otherwise use D0.
    # -----------------------------------------------------------------------
    if "create_data" in st.session_state:
        local_df = st.session_state["create_data"].copy()
    else:
        df = st.session_state.get("D0", None)
        if df is None or df.empty:
            st.warning("No data found in st.session_state['D0']. Please load or define it first.")
            st.stop()
        local_df = df.copy()
        st.session_state["create_data"] = local_df.copy()

    # -----------------------------------------------------------------------
    # 1) Custom CSS
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

    st.markdown('<h1 class="custom-header">New Feature Creation</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Side-by-side aggregator filtering, numeric transforms, interactions, group-based, and date/time features. Final save at the bottom.</p>', unsafe_allow_html=True)
    st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 0: Aggregator Filter
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 0) Aggregator (Categorical) Filter")

    cat_cols = local_df.select_dtypes(include=["object", "category"]).columns.tolist()
    if cat_cols:
        colAggLeft, colAggRight = st.columns(2)
        with colAggLeft:
            st.markdown("**Pick aggregator columns:**")
            agg_multisel = st.multiselect(
                "Aggregator columns",
                cat_cols,
                default=[],
                key="agg_cols_multisel"
            )
        with colAggRight:
            if agg_multisel:
                st.markdown("**Choose category values**")
                for colname in agg_multisel:
                    distinct_vals = sorted(local_df[colname].dropna().unique())
                    all_opt = "All"
                    radio_opts = [all_opt] + list(distinct_vals)
                    chosen_val = st.radio(
                        f"{colname} Filter:",
                        radio_opts,
                        index=0,
                        horizontal=True,
                        key=f"aggfilter_{colname}"
                    )
                    if chosen_val != all_opt:
                        local_df = local_df[local_df[colname] == chosen_val]
                        if local_df.empty:
                            st.warning(f"No data left after {colname} = {chosen_val}")
                            st.markdown('</div>', unsafe_allow_html=True)
                            st.stop()
        # Button to apply the aggregator filter changes
        if st.button("Apply Aggregator Filter", key="btn_apply_agg"):
            st.session_state["create_data"] = local_df.copy()
            st.success("Aggregator filter applied.")
    else:
        st.info("No categorical columns found.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Get numeric columns from the updated DataFrame.
    numeric_cols = local_df.select_dtypes(include=[np.number]).columns.tolist()

    # -----------------------------------------------------------------------
    # CARD 1: Basic Numeric Transforms
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 1) Basic Numeric Transforms")

    colNumLeft, colNumRight = st.columns(2)
    with colNumLeft:
        new_basic_col = st.text_input("New Numeric Feature Name", "NewNumeric1", key="basic_newcol")
        basic_mode = st.radio("Mode:", ["Two-Column Arithmetic", "Single-Column"], horizontal=True, key="basic_mode_radio")
    with colNumRight:
        if basic_mode == "Two-Column Arithmetic":
            if numeric_cols:
                cA = st.selectbox("Column A:", ["(None)"] + numeric_cols, key="arith_colA")
                cB_ = st.selectbox("Column B:", ["(None)"] + numeric_cols, key="arith_colB")
                operation = st.selectbox("Operation:", ["Add", "Subtract", "Multiply", "Divide"], key="arith_op_sel")
                if cA != "(None)" and cB_ != "(None)" and cA != cB_:
                    if st.button("Create Feature", key="btn_basic_two"):
                        if operation == "Add":
                            local_df[new_basic_col] = local_df[cA] + local_df[cB_]
                        elif operation == "Subtract":
                            local_df[new_basic_col] = local_df[cA] - local_df[cB_]
                        elif operation == "Multiply":
                            local_df[new_basic_col] = local_df[cA] * local_df[cB_]
                        else:  # "Divide"
                            local_df[new_basic_col] = np.where(local_df[cB_] != 0, local_df[cA] / local_df[cB_], np.nan)
                        st.session_state["create_data"] = local_df.copy()
                        st.success(f"Created '{new_basic_col}' (not saved yet).")
            else:
                st.info("No numeric columns to transform.")
        else:
            if numeric_cols:
                single_col = st.selectbox("Pick numeric column:", ["(None)"] + numeric_cols, key="single_sel")
                single_op = st.selectbox("Transform:", ["Log", "Sqrt", "Negate"], key="single_op")
                if single_col != "(None)":
                    if st.button("Create Feature", key="btn_basic_single"):
                        if single_op == "Log":
                            local_df[new_basic_col] = np.where(local_df[single_col] > 0, np.log(local_df[single_col]), np.nan)
                        elif single_op == "Sqrt":
                            local_df[new_basic_col] = np.where(local_df[single_col] >= 0, np.sqrt(local_df[single_col]), np.nan)
                        else:
                            local_df[new_basic_col] = -1 * local_df[single_col]
                        st.session_state["create_data"] = local_df.copy()
                        st.success(f"Created '{new_basic_col}' (not saved yet).")
            else:
                st.info("No numeric columns to transform.")
    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 2: Interaction Features
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 2) Interaction Features")

    colIntLeft, colIntRight = st.columns(2)
    with colIntLeft:
        interact_mode = st.radio("Interaction:", ["Pairwise Numeric", "Feature Crossing (Categorical)", "Min/Max of Columns"], horizontal=True, key="interact_mode_sel")
        new_interact_col = st.text_input("New Interaction Column:", "NewInteract1", key="interact_col_name")
    with colIntRight:
        if interact_mode == "Pairwise Numeric":
            if numeric_cols:
                x_col = st.selectbox("Numeric X:", ["(None)"] + numeric_cols, key="pairwise_x")
                y_col = st.selectbox("Numeric Y:", ["(None)"] + numeric_cols, key="pairwise_y")
                if x_col != "(None)" and y_col != "(None)" and x_col != y_col:
                    if st.button("Create Pairwise Numeric", key="btn_pairwise"):
                        local_df[new_interact_col] = local_df[x_col] * local_df[y_col]
                        st.session_state["create_data"] = local_df.copy()
                        st.success(f"Created '{new_interact_col}' (not saved yet).")
            else:
                st.info("No numeric columns remain.")
        elif interact_mode == "Feature Crossing (Categorical)":
            cat_after = local_df.select_dtypes(include=["object", "category"]).columns.tolist()
            if cat_after:
                catA = st.selectbox("Categorical A:", ["(None)"] + cat_after, key="catA_sel")
                catB = st.selectbox("Categorical B:", ["(None)"] + cat_after, key="catB_sel")
                if catA != "(None)" and catB != "(None)" and catA != catB:
                    if st.button("Create Feature Crossing", key="btn_catCross"):
                        local_df[new_interact_col] = local_df[catA].astype(str) + "_" + local_df[catB].astype(str)
                        st.session_state["create_data"] = local_df.copy()
                        st.success(f"Created '{new_interact_col}' (not saved yet).")
            else:
                st.info("No categorical columns remain.")
        else:
            multi_sel = st.multiselect("Pick numeric columns:", numeric_cols, key="minmax_multi")
            mm_mode = st.selectbox("Compute:", ["Min", "Max"], key="minmax_mode")
            if multi_sel:
                if st.button("Create Min/Max", key="btn_minmax"):
                    if mm_mode == "Min":
                        local_df[new_interact_col] = local_df[multi_sel].min(axis=1)
                    else:
                        local_df[new_interact_col] = local_df[multi_sel].max(axis=1)
                    st.session_state["create_data"] = local_df.copy()
                    st.success(f"Created '{new_interact_col}' (not saved yet).")
    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 3: Group-Based Features
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 3) Group-Based Features")

    colGrpLeft, colGrpRight = st.columns(2)
    with colGrpLeft:
        cat_after_filter = local_df.select_dtypes(include=["object", "category"]).columns.tolist()
        group_col = st.selectbox("Group Column:", ["(None)"] + cat_after_filter, key="group_col_sel")
        group_newcol = st.text_input("New Group Feature Name:", "NewGroup1", key="group_newcol_name")
    with colGrpRight:
        group_op = st.selectbox("Operation:", ["Mean", "Count", "Difference from Mean"], key="group_op_mode")
        if numeric_cols:
            group_num = st.selectbox("Numeric Column for group stats:", ["(None)"] + numeric_cols, key="group_num_sel")
        else:
            group_num = "(None)"
        if group_col != "(None)" and group_num != "(None)" and group_op and group_newcol:
            if st.button("Create Group Feature", key="btn_group_feat"):
                grouping = local_df.groupby(group_col)[group_num]
                if group_op == "Mean":
                    local_df[group_newcol] = grouping.transform("mean")
                elif group_op == "Count":
                    local_df[group_newcol] = local_df.groupby(group_col)[group_col].transform("count")
                else:
                    mean_vals = grouping.transform("mean")
                    local_df[group_newcol] = local_df[group_num] - mean_vals
                st.session_state["create_data"] = local_df.copy()
                st.success(f"Created '{group_newcol}' with {group_op} of {group_num} (not saved yet).")
    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 4: Date/Time Features
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 4) Date/Time Features")

    colDtLeft, colDtRight = st.columns(2)
    with colDtLeft:
        all_cols = local_df.columns.tolist()
        time_col_pick = st.selectbox("Pick a date/time column:", ["(None)"] + all_cols, key="time_colPick")
        new_timecol = st.text_input("New Time Feature Name:", "NewTime1", key="new_timecol_text")
    with colDtRight:
        time_op = st.selectbox("Time Operation:", ["Extract Day/Month", "Delta from Now", "Lag by 1 row"], key="time_op_type")
        if time_col_pick != "(None)":
            if np.issubdtype(local_df[time_col_pick].dtype, np.datetime64):
                pass
            elif local_df[time_col_pick].dtype == object:
                local_df[time_col_pick] = pd.to_datetime(local_df[time_col_pick], errors="coerce")
                st.info(f"Converted {time_col_pick} to datetime64. Some rows might be NaT if parse failed.")
            if not np.issubdtype(local_df[time_col_pick].dtype, np.datetime64):
                st.warning(f"Column '{time_col_pick}' not valid datetime. Time-based transform might fail.")
            else:
                if st.button("Create Time Feature", key="btn_timefeat"):
                    if time_op == "Extract Day/Month":
                        local_df[new_timecol + "_day"] = local_df[time_col_pick].dt.day
                        local_df[new_timecol + "_month"] = local_df[time_col_pick].dt.month
                        st.success(f"Created {new_timecol+'_day'} and {new_timecol+'_month'} (not saved yet).")
                    elif time_op == "Delta from Now":
                        now = pd.to_datetime("today")
                        local_df[new_timecol] = (now - local_df[time_col_pick]).dt.days
                        st.success(f"Created '{new_timecol}' as day difference from now (not saved yet).")
                    else:  # Lag by 1 row
                        local_df[new_timecol] = local_df[time_col_pick].shift(1)
                        st.success(f"Created lag column '{new_timecol}' from {time_col_pick} (not saved yet).")
                    st.session_state["create_data"] = local_df.copy()
    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 5: Preview & Save
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## 5) Preview & Save")
    st.dataframe(local_df.head(10), use_container_width=True)
    st.write("Confirm & Save new features to st.session_state['transform_data'].")
    if st.button("Save All Changes", key="save_all_final"):
        st.session_state["transform_data"] = local_df.copy()
        st.success("All changes have been saved to st.session_state['transform_data']!")
    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # Navigation Buttons
    # -----------------------------------------------------------------------
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()


def Select_page():
    import streamlit as st
    import pandas as pd
    import numpy as np

    from sklearn.feature_selection import VarianceThreshold
    from xgboost import XGBClassifier, XGBRegressor

    st.title("Feature Selection Page")
    st.write("Select features from the data in `st.session_state['transform_data']` using various techniques.")

    # -----------------------------------------------------------------------
    # A) Check for transform_data in session_state
    # -----------------------------------------------------------------------
    if "transform_data" not in st.session_state:
        st.error("No data found in st.session_state['transform_data']. Please run the transform page first.")
        st.stop()

    # Copy the data for local use
    df = st.session_state["transform_data"].copy()

    st.markdown("### Initial Data Preview")
    st.dataframe(df.head(10), use_container_width=True)

    all_columns = df.columns.tolist()
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # -----------------------------------------------------------------------
    # B) Pick Your Target (Y) and XGBoost Task
    # -----------------------------------------------------------------------
    st.markdown("## Select Target Variable & Task Type")
    y_col = st.selectbox("Pick your target (Y) column:", ["(None)"] + all_columns, index=0)
    task_type = st.radio("Task type for XGBoost:", ["Classifier", "Regressor"], index=0)
    st.write("---")

    # Helper: Minimal label encoding for classification if Y is not numeric
    def label_encode_series(series: pd.Series) -> pd.Series:
        """Converts any series into numeric codes (0, 1, 2...) for classification."""
        return pd.Series(pd.factorize(series)[0], index=series.index)

    # -----------------------------------------------------------------------
    # C) Manual Feature Selection
    # -----------------------------------------------------------------------
    st.markdown("## A. Manual Feature Selection")
    selected_manual = st.multiselect(
        "Manually pick columns to keep:",
        options=all_columns,
        default=all_columns
    )

    st.write("Preview of manually selected columns:")
    st.dataframe(df[selected_manual].head(10), use_container_width=True)

    # -----------------------------------------------------------------------
    # D) Correlation-Based Selection
    # -----------------------------------------------------------------------
    st.markdown("## B. Correlation-Based Selection")
    selected_corr_cols = []

    # Only attempt correlation if Y is numeric and not None
    if y_col != "(None)" and y_col in numeric_cols:
        corr_threshold = st.slider(
            "Correlation threshold (absolute value):",
            min_value=0.0, max_value=1.0,
            value=0.0,  # default to minimal threshold
            step=0.01
        )
        # DataFrame of only numeric columns
        numeric_data = df[numeric_cols]
        corrs = numeric_data.corr()[y_col].dropna()
        # Filter columns by correlation threshold
        high_corr = corrs[abs(corrs) >= corr_threshold]
        selected_corr_cols = high_corr.index.tolist()  # includes y_col as well

        st.write(f"Correlation with target '{y_col}' (above ±{corr_threshold}):")
        st.dataframe(corrs.to_frame("Correlation"), use_container_width=True)
        st.write(f"Columns with |corr| ≥ {corr_threshold}: {selected_corr_cols}")
    else:
        st.info("Correlation-based filtering skipped (either target is '(None)' or not numeric).")

    # -----------------------------------------------------------------------
    # E) Variance Threshold Filtering
    # -----------------------------------------------------------------------
    st.markdown("## C. Variance Threshold Filtering")
    selected_var_cols = []

    if numeric_cols:
        var_threshold_value = st.slider(
            "Variance threshold:",
            min_value=0.0, max_value=10.0,
            value=0.0, step=0.1
        )

        if st.button("Apply Variance Threshold"):
            vt = VarianceThreshold(threshold=var_threshold_value)
            numeric_data = df[numeric_cols].copy()

            vt.fit(numeric_data)
            keep_mask = vt.get_support()  # Boolean array
            selected_var_cols = [col for col, keep in zip(numeric_cols, keep_mask) if keep]

            st.write(f"Columns passing variance threshold of {var_threshold_value}:")
            st.write(selected_var_cols if selected_var_cols else "(None)")
        else:
            st.info("Click 'Apply Variance Threshold' to see which columns pass the filter.")
    else:
        st.info("No numeric columns found for variance threshold selection.")

    # -----------------------------------------------------------------------
    # F) XGBoost Feature Importance
    # -----------------------------------------------------------------------
    st.markdown("## D. XGBoost Feature Importance")
    selected_xgb_cols = []

    # We'll fit a quick XGBoost model if the user has chosen a valid Y.
    if y_col != "(None)":
        # Let user trigger the feature-importance calculation.
        if st.button("Compute XGBoost Feature Importances"):
            # Prepare X, y for XGBoost
            X = df.drop(columns=[y_col], errors="ignore").copy()

            # Filter to numeric columns only for X
            X = X.select_dtypes(include=[np.number])
            # If Y is not numeric but the user wants classification, label-encode
            y_series = df[y_col]
            if task_type == "Classifier":
                if y_series.dtype not in [np.number, np.float64, np.int64]:
                    # Perform label encoding
                    y_series = label_encode_series(y_series)
                model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
            else:
                # Regressor
                # If y is not numeric, we can't do a simple regression
                if y_series.dtype not in [np.number, np.float64, np.int64]:
                    st.warning("Y is non-numeric. XGBRegressor won't work properly. Skipping.")
                    st.stop()
                model = XGBRegressor()

            # Train quickly
            try:
                model.fit(X, y_series)
                importances = model.feature_importances_
                col_importances = sorted(
                    zip(X.columns, importances),
                    key=lambda x: x[1],
                    reverse=True
                )

                st.write("XGBoost Feature Importances (descending):")
                st.dataframe(pd.DataFrame(col_importances, columns=["Feature", "Importance"]), use_container_width=True)

                # Let user set an importance threshold or top-k
                imp_threshold = st.slider("Minimum importance threshold:", 0.0, 1.0, 0.0, 0.01)
                # Filter columns by threshold
                selected_xgb_cols = [col for col, imp in col_importances if imp >= imp_threshold]

                st.write(f"Columns with importance ≥ {imp_threshold}: {selected_xgb_cols if selected_xgb_cols else '(None)'}")
            except Exception as e:
                st.error(f"Error training XGBoost model: {e}")
        else:
            st.info("Click 'Compute XGBoost Feature Importances' to see XGBoost-based filtering.")
    else:
        st.info("XGBoost feature importance skipped (no Y selected).")

    # -----------------------------------------------------------------------
    # G) Combine & Save Final Selection
    # -----------------------------------------------------------------------
    st.markdown("## E. Combine & Save Final Selection")
    st.write("""
    You can choose how to combine your selected sets:

    - **Manual Only**  
    - **Intersection of All** (Manual ∩ Correlation ∩ Variance ∩ XGBoost)  
    - **Union of All** (Manual ∪ Correlation ∪ Variance ∪ XGBoost)
    """)

    combine_option = st.radio(
        "How do you want to combine the selected sets?",
        ["Manual Only", "Intersection of All", "Union of All"],
        index=0
    )

    # Build sets from each selection method
    manual_set = set(selected_manual)
    corr_set = set(selected_corr_cols) if selected_corr_cols else set()
    var_set = set(selected_var_cols) if selected_var_cols else set()
    xgb_set = set(selected_xgb_cols) if selected_xgb_cols else set()

    if combine_option == "Manual Only":
        final_selection = list(manual_set)
    elif combine_option == "Intersection of All":
        # Intersect only the non-empty sets
        sets_to_combine = [manual_set]
        if corr_set:
            sets_to_combine.append(corr_set)
        if var_set:
            sets_to_combine.append(var_set)
        if xgb_set:
            sets_to_combine.append(xgb_set)

        final_selection = list(set.intersection(*sets_to_combine)) if sets_to_combine else []
    else:  # "Union of All"
        sets_to_combine = [manual_set, corr_set, var_set, xgb_set]
        final_selection = list(set.union(*sets_to_combine))

    st.write(f"**Final selection**: {final_selection if final_selection else '(None)'}")

    if final_selection:
        st.dataframe(df[final_selection].head(10), use_container_width=True)
    else:
        st.warning("No columns selected!")

    # Button to save final selection
    if st.button("Save Final Selection"):
        st.session_state["selected_features"] = final_selection
        st.success(f"Selected features saved to session_state['selected_features']: {final_selection}")


    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()
            











































































































# def market_construct_page():
#     import streamlit as st
#     import pandas as pd
#     import numpy as np
#     import plotly.express as px

#     # -----------------------------------------------------------------------
#     # 1) Retrieve Data
#     # -----------------------------------------------------------------------
#     df = st.session_state.get("D0", None)
#     if df is None or df.empty:
#         st.warning("No data uploaded yet. Please upload a file in the sidebar.")
#         st.stop()

#     # -----------------------------------------------------------------------
#     # 2) Prepare Filter Options
#     # -----------------------------------------------------------------------
#     def sorted_or_all(col):
#         if col in df.columns:
#             return ["All"] + sorted(df[col].unique())
#         else:
#             return ["All"]

#     market_options   = sorted_or_all("Market")
#     channel_options  = sorted_or_all("Channel")
#     metric_options   = ["MS Value", "Volume", "Price", "MS Volume"]
#     time_options     = ["Weekly", "Monthly", "Yearly"]
#     brand_options    = sorted_or_all("Brand")
#     variant_options  = sorted_or_all("Variant")
#     packtype_options = sorted_or_all("PackType")
#     ppg_options      = sorted_or_all("PPG")

#     # If any dimension has >5 items, enable radio wrap
#     max_length = max(len(brand_options), len(variant_options), 
#                      len(packtype_options), len(ppg_options))
#     if max_length > 5:
#         st.markdown("""
#         <style>
#         div[data-baseweb="radio"] > div {
#             display: flex !important;
#             flex-wrap: wrap !important;
#         }
#         div[data-baseweb="radio"] label {
#             margin-right: 1rem; 
#             margin-bottom: 0.5rem;
#         }
#         </style>
#         """, unsafe_allow_html=True)

#     # -----------------------------------------------------------------------
#     # 3) CUSTOM CSS
#     # -----------------------------------------------------------------------
#     st.markdown("""
#     <style>
#     .stApp {
#         background-color: #F5F5F5;
#     }
#     .custom-header {
#         font-family: 'Inter', sans-serif;
#         font-size: 36px; 
#         font-weight: 600;
#         color: #333333;
#         margin-bottom: 0.2rem;
#     }
#     .accent-hr {
#         border: 0;
#         height: 2px;
#         background: linear-gradient(to right, #FFBD59, #FFC87A);
#         margin: 0.5rem 0 1.5rem 0;
#     }
#     div[data-testid="stHorizontalBlock"] button {
#         background-color: #FFBD59 !important; 
#         color: #333333 !important;
#         font-weight: 600 !important;
#         border-radius: 4px !important;
#         border: none !important;
#         margin-bottom: 0.5rem;
#     }
#     div[data-testid="stHorizontalBlock"] button:hover {
#         background-color: #FFC87A !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # -----------------------------------------------------------------------
#     # 4) Page Header
#     # -----------------------------------------------------------------------
#     st.markdown('<h1 class="custom-header">Market Construct</h1>', unsafe_allow_html=True)

#     # -----------------------------------------------------------------------
#     # 5) Two-column layout for top filters
#     # -----------------------------------------------------------------------
#     left_col, right_col = st.columns([2, 3])

#     with right_col:
#         # Market & Channel
#         top_r1_c1, top_r1_c2 = st.columns(2)
#         with top_r1_c1:
#             st.markdown("##### Market")
#             chosen_market = st.selectbox("", market_options)
#         with top_r1_c2:
#             st.markdown("##### Channel")
#             chosen_channel = st.selectbox("", channel_options)

#         # Metric & Time
#         st.markdown("##### Metric & Time")
#         bottom_r_c1, bottom_r_c2 = st.columns(2)
#         with bottom_r_c1:
#             chosen_metric = st.radio("Metric:", metric_options, horizontal=True)
#         with bottom_r_c2:
#             chosen_time = st.radio("Time:", time_options, horizontal=True)

#     with left_col:
#         st.markdown("##### Product Filters")
#         # 4 columns in a single row
#         c_brand, c_variant, c_pt, c_ppg = st.columns(4)
#         with c_brand:
#             chosen_brand = st.radio("Brand:", brand_options, index=0, horizontal=True)
#         with c_variant:
#             chosen_variant = st.radio("Variant:", variant_options, index=0, horizontal=True)
#         with c_pt:
#             chosen_packtype = st.radio("PackType:", packtype_options, index=0, horizontal=True)
#         with c_ppg:
#             chosen_ppg = st.radio("PPG:", ppg_options, index=0, horizontal=True)

#     st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)

#     # -----------------------------------------------------------------------
#     # 6) Filter Data
#     # -----------------------------------------------------------------------
#     # Category-level subset => only Market & Channel
#     cat_df = df.copy()
#     if "Market" in cat_df.columns and chosen_market != "All":
#         cat_df = cat_df[cat_df["Market"] == chosen_market]
#     if "Channel" in cat_df.columns and chosen_channel != "All":
#         cat_df = cat_df[cat_df["Channel"] == chosen_channel]

#     # brand-level subset => also brand, variant, packtype, ppg
#     brand_subset = cat_df.copy()
#     if "Brand" in brand_subset.columns and chosen_brand != "All":
#         brand_subset = brand_subset[brand_subset["Brand"] == chosen_brand]
#     if "Variant" in brand_subset.columns and chosen_variant != "All":
#         brand_subset = brand_subset[brand_subset["Variant"] == chosen_variant]
#     if "PackType" in brand_subset.columns and chosen_packtype != "All":
#         brand_subset = brand_subset[brand_subset["PackType"] == chosen_packtype]
#     if "PPG" in brand_subset.columns and chosen_ppg != "All":
#         brand_subset = brand_subset[brand_subset["PPG"] == chosen_ppg]

#     # If cat_df is empty => no Category data
#     # If brand_subset empty => no brand-level data

#     # -----------------------------------------------------------------------
#     # 7) Time Grouping
#     # -----------------------------------------------------------------------
#     cat_df["Date"] = pd.to_datetime(cat_df.get("Date",""), errors="coerce")
#     cat_df.dropna(subset=["Date"], inplace=True)
#     brand_subset["Date"] = pd.to_datetime(brand_subset.get("Date",""), errors="coerce")
#     brand_subset.dropna(subset=["Date"], inplace=True)

#     def set_time_key(df_, freq):
#         df_ = df_.copy()
#         if df_.empty:
#             df_["TimeKey"] = []
#             return df_
#         if freq == "Weekly":
#             df_["TimeKey"] = df_["Date"].dt.to_period("W").apply(lambda r: r.start_time)
#         elif freq == "Monthly":
#             df_["TimeKey"] = df_["Date"].dt.to_period("M").apply(lambda r: r.start_time)
#         elif freq == "Yearly":
#             df_["TimeKey"] = df_["Date"].dt.year
#         else:
#             df_["TimeKey"] = df_["Date"]
#         return df_

#     cat_df = set_time_key(cat_df, chosen_time)
#     brand_subset = set_time_key(brand_subset, chosen_time)

#     for col in ["SalesValue","Volume"]:
#         if col not in cat_df.columns:
#             cat_df[col] = 0.0
#         if col not in brand_subset.columns:
#             brand_subset[col] = 0.0

#     # -----------------------------------------------------------------------
#     # 8) Category aggregator => correct denominator
#     # -----------------------------------------------------------------------
#     cat_agg = cat_df.groupby("TimeKey", as_index=False).agg(
#         CatSalesValue=("SalesValue","sum"),
#         CatVolume=("Volume","sum")
#     )

#     # We'll define a function that merges brand-level aggregator with cat_agg
#     # but also EXCLUDES aggregator dimension values that are e.g. "Cat1", "AllVariant", etc.

#     # Let's define sets of dimension values to exclude:
#     # You can adapt as needed
#     EXCLUDED_BRANDS    = {"Cat1", "AllVariant", "AllBrand", "AllPPG", "AnyOtherAggregator"}
#     EXCLUDED_VARIANTS  = {"AllVariantGroup", "CatVariant"}
#     EXCLUDED_PACKTYPES = {"AllPack", "CatPack"}
#     EXCLUDED_PPG       = {"AllPPG", "CatPPG"}

#     def aggregator_for_dimension(df_, dim_col):
#         """
#         Groups brand_subset by [TimeKey, dim_col],
#         merges with cat_agg for correct denominator,
#         excludes aggregator dimension labels (like 'AllVariant'),
#         and then computes 'Value' based on chosen_metric.
#         """
#         if df_.empty:
#             return df_.assign(Value=[], CatSalesValue=[], CatVolume=[])

#         # group
#         grouped = df_.groupby(["TimeKey", dim_col], as_index=False).agg(
#             SalesValue=("SalesValue","sum"),
#             Volume=("Volume","sum")
#         )
#         # exclude aggregator dimension values
#         # e.g. if dimension==Brand => skip brand in EXCLUDED_BRANDS
#         if dim_col == "Brand":
#             grouped = grouped[~grouped["Brand"].isin(EXCLUDED_BRANDS)]
#         elif dim_col == "Variant":
#             grouped = grouped[~grouped["Variant"].isin(EXCLUDED_VARIANTS)]
#         elif dim_col == "PackType":
#             grouped = grouped[~grouped["PackType"].isin(EXCLUDED_PACKTYPES)]
#         elif dim_col == "PPG":
#             grouped = grouped[~grouped["PPG"].isin(EXCLUDED_PPG)]

#         # merge cat_agg => get CatSalesValue, CatVolume
#         merged = pd.merge(grouped, cat_agg, on="TimeKey", how="left")

#         if chosen_metric == "MS Value":
#             merged["Value"] = np.where(
#                 merged["CatSalesValue"]!=0,
#                 merged["SalesValue"]/merged["CatSalesValue"],
#                 0
#             )
#         elif chosen_metric == "Volume":
#             merged["Value"] = merged["Volume"]
#         elif chosen_metric == "Price":
#             merged["Value"] = np.where(
#                 merged["Volume"]!=0,
#                 merged["SalesValue"]/merged["Volume"],
#                 0
#             )
#         elif chosen_metric == "MS Volume":
#             merged["Value"] = np.where(
#                 merged["CatVolume"]!=0,
#                 merged["Volume"]/merged["CatVolume"],
#                 0
#             )
#         else:
#             merged["Value"] = 0
#         return merged

#     # Category aggregator
#     # We'll store for Category the dimension col "Dimension"= "Category"
#     category_agg = cat_agg.copy()
#     # compute "Value" for category itself
#     if chosen_metric == "MS Value":
#         # total / total => 1 if >0
#         category_agg["Value"] = np.where(
#             category_agg["CatSalesValue"]!=0, 1, 0
#         )
#     elif chosen_metric == "Volume":
#         category_agg["Value"] = category_agg["CatVolume"]
#     elif chosen_metric == "Price":
#         category_agg["Value"] = np.where(
#             category_agg["CatVolume"]!=0,
#             category_agg["CatSalesValue"]/category_agg["CatVolume"],
#             0
#         )
#     elif chosen_metric == "MS Volume":
#         category_agg["Value"] = np.where(
#             category_agg["CatVolume"]!=0, 1, 0
#         )
#     else:
#         category_agg["Value"] = 0
#     category_agg["Dimension"] = "Category"

#     # brand aggregator
#     brand_agg = aggregator_for_dimension(brand_subset, "Brand")
#     # packtype aggregator
#     packtype_agg = aggregator_for_dimension(brand_subset, "PackType")
#     # ppg aggregator
#     ppg_agg = aggregator_for_dimension(brand_subset, "PPG")
#     # variant aggregator
#     variant_agg = aggregator_for_dimension(brand_subset, "Variant")

#     st.markdown(f"### {chosen_metric} ({chosen_time})")

#     # We'll store them in a list
#     all_charts = []
#     if not category_agg.empty:
#         all_charts.append(("Category", category_agg, "Dimension"))
#     if not brand_agg.empty:
#         all_charts.append(("Brand", brand_agg, "Brand"))
#     if not packtype_agg.empty:
#         all_charts.append(("PackType", packtype_agg, "PackType"))
#     if not ppg_agg.empty:
#         all_charts.append(("PPG", ppg_agg, "PPG"))
#     if not variant_agg.empty:
#         all_charts.append(("Variant", variant_agg, "Variant"))

#     def build_chart(df_, dim_col):
#         df_ = df_.copy().sort_values("TimeKey")
#         if chosen_time == "Weekly":
#             fig = px.line(df_, x="TimeKey", y="Value", color=dim_col,
#                           markers=True, template="plotly_white")
#         else:
#             fig = px.bar(df_, x="TimeKey", y="Value", color=dim_col,
#                          barmode="group", template="plotly_white")
#         fig.update_layout(margin=dict(l=10, r=10, t=40, b=40))
#         return fig

#     # layout logic for multiple charts
#     def layout_chunks(n):
#         if n <= 4:
#             return [n]
#         elif n == 5:
#             return [3,2]
#         elif n == 6:
#             return [3,3]
#         elif n == 7:
#             return [4,3]
#         elif n == 8:
#             return [4,4]
#         else:
#             leftover = n - 8
#             return [4,4,leftover]

#     n_charts = len(all_charts)
#     if n_charts == 0:
#         st.info("No dimension charts to display.")
#         return

#     chunk_sizes = layout_chunks(n_charts)
#     idx = 0
#     for size in chunk_sizes:
#         row_data = all_charts[idx: idx+size]
#         idx += size
#         cols = st.columns(size)
#         for i, (title, aggregator_df, dimension_col) in enumerate(row_data):
#             with cols[i]:
#                 st.write(f"#### {title} ({chosen_metric})")
#                 fig = build_chart(aggregator_df, dimension_col)
#                 st.plotly_chart(fig, use_container_width=True)
#                 st.text_area(f"Comments ({title})", "")

#     st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)
def market_construct_page():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

    # -----------------------------------------------------------------------
    # 1) Retrieve Data
    # -----------------------------------------------------------------------
    df = st.session_state.get("D0", None)
    if df is None or df.empty:
        st.warning("No data uploaded yet. Please upload a file in the sidebar.")
        st.stop()

    # -----------------------------------------------------------------------
    # 1a) Remove any rows where Brand == "cat 1"
    #     (Happens before any filters/options so "cat 1" is never visible)
    # -----------------------------------------------------------------------
    if "Brand" in df.columns:
        df = df[df["Brand"] != "cat1"]

    # -----------------------------------------------------------------------
    # 2) Prepare Options
    # -----------------------------------------------------------------------
    def sorted_or_all(col):
        if col in df.columns:
            return ["All"] + sorted(df[col].unique())
        else:
            return ["All"]

    market_options   = sorted_or_all("Market")
    channel_options  = sorted_or_all("Channel")
    metric_options   = ["MS Value", "Volume", "Price", "MS Volume"]
    time_options     = ["Weekly", "Monthly", "Yearly"]
    brand_options    = sorted_or_all("Brand")
    variant_options  = sorted_or_all("Variant")
    packtype_options = sorted_or_all("PackType")
    ppg_options      = sorted_or_all("PPG")

    # If large dimension, wrap radios
    max_length = max(len(brand_options), len(variant_options), len(packtype_options), len(ppg_options))
    if max_length > 5:
        st.markdown("""
        <style>
        div[data-baseweb="radio"] > div {
            display: flex !important;
            flex-wrap: wrap !important;
        }
        div[data-baseweb="radio"] label {
            margin-right: 1rem; 
            margin-bottom: 0.5rem;
        }
        </style>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # 3) CUSTOM CSS
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
    .accent-hr {
        border: 0;
        height: 2px;
        background: linear-gradient(to right, #FFBD59, #FFC87A);
        margin: 0.5rem 0 1.5rem 0;
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
    </style>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # 4) Page Header
    # -----------------------------------------------------------------------
    st.markdown('<h1 class="custom-header">Market Construct</h1>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # 5) Two-column layout for top filters
    # -----------------------------------------------------------------------
    left_col, right_col = st.columns([2,3])

    with right_col:
        # Market & Channel
        top_c1, top_c2 = st.columns(2)
        with top_c1:
            st.markdown("##### Market")
            chosen_market = st.selectbox("", market_options)
        with top_c2:
            st.markdown("##### Channel")
            chosen_channel = st.selectbox("", channel_options)

        st.markdown("##### Metric & Time")
        bot_c1, bot_c2 = st.columns(2)
        with bot_c1:
            chosen_metric = st.radio("Metric:", metric_options, horizontal=True)
        with bot_c2:
            chosen_time = st.radio("Time:", time_options, horizontal=True)

    with left_col:
        st.markdown("##### Product Filters")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            chosen_brand = st.radio("Brand:", brand_options, index=0, horizontal=True)
        with c2:
            chosen_variant = st.radio("Variant:", variant_options, index=0, horizontal=True)
        with c3:
            chosen_packtype = st.radio("PackType:", packtype_options, index=0, horizontal=True)
        with c4:
            chosen_ppg = st.radio("PPG:", ppg_options, index=0, horizontal=True)

    st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # 6) Category Filter => Market & Channel
    # -----------------------------------------------------------------------
    cat_df = df.copy()
    if "Market" in cat_df.columns and chosen_market != "All":
        cat_df = cat_df[cat_df["Market"] == chosen_market]
    if "Channel" in cat_df.columns and chosen_channel != "All":
        cat_df = cat_df[cat_df["Channel"] == chosen_channel]

    # brand-level subset => brand, variant, packtype, ppg
    brand_subset = cat_df.copy()
    if "Brand" in brand_subset.columns and chosen_brand != "All":
        brand_subset = brand_subset[brand_subset["Brand"] == chosen_brand]
    if "Variant" in brand_subset.columns and chosen_variant != "All":
        brand_subset = brand_subset[brand_subset["Variant"] == chosen_variant]
    if "PackType" in brand_subset.columns and chosen_packtype != "All":
        brand_subset = brand_subset[brand_subset["PackType"] == chosen_packtype]
    if "PPG" in brand_subset.columns and chosen_ppg != "All":
        brand_subset = brand_subset[brand_subset["PPG"] == chosen_ppg]

    # -----------------------------------------------------------------------
    # 7) Time Key
    # -----------------------------------------------------------------------
    cat_df["Date"] = pd.to_datetime(cat_df.get("Date",""), errors="coerce")
    cat_df.dropna(subset=["Date"], inplace=True)

    brand_subset["Date"] = pd.to_datetime(brand_subset.get("Date",""), errors="coerce")
    brand_subset.dropna(subset=["Date"], inplace=True)

    def set_time(df_, freq):
        df_ = df_.copy()
        if df_.empty:
            df_["TimeKey"] = []
            return df_
        if freq=="Weekly":
            df_["TimeKey"] = df_["Date"].dt.to_period("W").apply(lambda r: r.start_time)
        elif freq=="Monthly":
            df_["TimeKey"] = df_["Date"].dt.to_period("M").apply(lambda r: r.start_time)
        elif freq=="Yearly":
            df_["TimeKey"] = df_["Date"].dt.year
        else:
            df_["TimeKey"] = df_["Date"]
        return df_

    cat_df = set_time(cat_df, chosen_time)
    brand_subset = set_time(brand_subset, chosen_time)

    for col in ["SalesValue","Volume"]:
        if col not in cat_df.columns:
            cat_df[col] = 0
        if col not in brand_subset.columns:
            brand_subset[col] = 0

    # -----------------------------------------------------------------------
    # 8) Category aggregator => sums for correct denominator
    # -----------------------------------------------------------------------
    cat_agg = cat_df.groupby("TimeKey", as_index=False).agg(
        CatSalesValue=("SalesValue","sum"),
        CatVolume=("Volume","sum")
    )

    # aggregator for dimension with correct share
    def aggregator_for_dimension(df_, dim_col):
        if df_.empty:
            return df_.assign(Value=[], CatSalesValue=[], CatVolume=[])

        grouped = df_.groupby(["TimeKey",dim_col], as_index=False).agg(
            SalesValue=("SalesValue","sum"),
            Volume=("Volume","sum")
        )

        # Merge with cat_agg => get CatSalesValue, CatVolume
        merged = pd.merge(grouped, cat_agg, on="TimeKey", how="left")

        if chosen_metric == "MS Value":
            merged["Value"] = np.where(
                merged["CatSalesValue"] != 0,
                merged["SalesValue"] / merged["CatSalesValue"],
                0
            )
        elif chosen_metric == "Volume":
            merged["Value"] = merged["Volume"]
        elif chosen_metric == "Price":
            merged["Value"] = np.where(
                merged["Volume"] != 0,
                merged["SalesValue"] / merged["Volume"],
                0
            )
        elif chosen_metric == "MS Volume":
            merged["Value"] = np.where(
                merged["CatVolume"] != 0,
                merged["Volume"] / merged["CatVolume"],
                0
            )
        else:
            merged["Value"] = 0
        return merged

    # We also define a function to check if dimension aggregator has only 1 unique value
    # if user left dimension == "All", we'll skip aggregator if it has 1 unique dimension label
    def skip_if_only_one(dim_df, dim_col, user_chosen):
        """
        Return True if we should skip aggregator because it has only 1 distinct dim_col
        AND user_chosen is "All".
        """
        if user_chosen != "All":
            return False  # user explicitly picked, so don't skip
        distinct_vals = dim_df[dim_col].nunique()
        return (distinct_vals <= 1)

    # Category aggregator => dimension col "Dimension" = "Category"
    # We'll compute Value for category aggregator
    category_agg = cat_agg.copy()
    if chosen_metric == "MS Value":
        category_agg["Value"] = np.where(category_agg["CatSalesValue"]!=0, 1, 0)
    elif chosen_metric == "Volume":
        category_agg["Value"] = category_agg["CatVolume"]
    elif chosen_metric == "Price":
        category_agg["Value"] = np.where(
            category_agg["CatVolume"]!=0,
            category_agg["CatSalesValue"]/category_agg["CatVolume"],
            0
        )
    elif chosen_metric == "MS Volume":
        category_agg["Value"] = np.where(category_agg["CatVolume"]!=0, 1, 0)
    else:
        category_agg["Value"] = 0
    category_agg["Dimension"] = "Category"

    brand_agg = aggregator_for_dimension(brand_subset, "Brand")
    pt_agg = aggregator_for_dimension(brand_subset, "PackType")
    ppg_agg = aggregator_for_dimension(brand_subset, "PPG")
    var_agg = aggregator_for_dimension(brand_subset, "Variant")

    st.markdown(f"### {chosen_metric} ({chosen_time})")

    # Collect all dimension chart data
    dimension_charts = []

    # Category aggregator is always included if not empty
    if not category_agg.empty:
        dimension_charts.append(("Category", category_agg, "Dimension"))

    # Brand aggregator
    if not brand_agg.empty:
        if not skip_if_only_one(brand_agg, "Brand", chosen_brand):
            dimension_charts.append(("Brand", brand_agg, "Brand"))
        else:
            st.warning("Skipped Brand aggregator because it has only one distinct brand, and user is at 'All' brand.")
    else:
        st.warning("No brand data after product filters.")

    # PackType aggregator
    if not pt_agg.empty:
        if not skip_if_only_one(pt_agg, "PackType", chosen_packtype):
            dimension_charts.append(("PackType", pt_agg, "PackType"))
        else:
            st.warning("Skipped PackType aggregator because it has only one distinct packtype, and user is at 'All'.")
    else:
        st.warning("No packtype data after product filters.")

    # PPG aggregator
    if not ppg_agg.empty:
        if not skip_if_only_one(ppg_agg, "PPG", chosen_ppg):
            dimension_charts.append(("PPG", ppg_agg, "PPG"))
        else:
            st.warning("Skipped PPG aggregator because it has only one distinct PPG, and user is at 'All'.")
    else:
        st.warning("No PPG data after product filters.")

    # Variant aggregator
    if not var_agg.empty:
        if not skip_if_only_one(var_agg, "Variant", chosen_variant):
            dimension_charts.append(("Variant", var_agg, "Variant"))
        else:
            st.warning("Skipped Variant aggregator because it has only one distinct variant, and user is at 'All'.")
    else:
        st.warning("No variant data after product filters.")

    # Chart-building function
    def build_chart(df_, dim_col):
        df_ = df_.copy().sort_values("TimeKey")
        if chosen_time == "Weekly":
            fig = px.line(df_, x="TimeKey", y="Value", color=dim_col, markers=True, template="plotly_white")
        else:
            fig = px.bar(df_, x="TimeKey", y="Value", color=dim_col, barmode="group", template="plotly_white")
        fig.update_layout(margin=dict(l=10, r=10, t=40, b=40))
        return fig

    # Layout logic
    def layout_chunks(n):
        if n <= 4:
            return [n]
        elif n == 5:
            return [3,2]
        elif n == 6:
            return [3,3]
        elif n == 7:
            return [4,3]
        elif n == 8:
            return [4,4]
        else:
            leftover = n - 8
            return [4,4,leftover]

    # Output the aggregator charts
    n_charts = len(dimension_charts)
    if n_charts == 0:
        st.info("No dimension charts to display.")
        return

    chunk_sizes = layout_chunks(n_charts)
    idx = 0
    for row_size in chunk_sizes:
        row_data = dimension_charts[idx : idx+row_size]
        idx += row_size
        cols = st.columns(row_size)
        for i, (title, aggregator_df, dimension_col) in enumerate(row_data):
            with cols[i]:
                st.write(f"#### {title} ({chosen_metric})")
                fig = build_chart(aggregator_df, dimension_col)
                st.plotly_chart(fig, use_container_width=True)
                st.text_area(f"Comments ({title})", "")

    st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)




    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()
            




# def Engineer_page():
    
def base_price_estimator_page():

    
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go

    st.subheader("📊 Automated Base Price Estimator")
    
    
        # Retrieve the uploaded dataframe from session state (set in the file management section)
    dataframe = st.session_state.get("D0", None) 
    
    # Make sure the global 'dataframe' is not None (it comes from your file upload module)
    if dataframe is not None:
        # Ensure "BasePrice" column exists
        if "BasePrice" not in dataframe.columns:
            dataframe["BasePrice"] = np.nan

        # Upward transition check (unchanged)
        def validate_upward_transition(prices, candidate_price, base_price, threshold_5, threshold_3, promo_weeks):
            above_thresh = np.sum(prices >= base_price * (1 + threshold_5 / 100))
            within_range = np.sum((prices >= candidate_price * 0.97) & (prices <= candidate_price * 1.03))
            return (above_thresh >= promo_weeks // 2) and (within_range >= promo_weeks // 2)

        # Downward transition check: require that, in the next 12 weeks,
        # at least 9 weeks have prices within ±2% of the candidate price.
        def validate_downward_transition_strict(prices, candidate_price, promo_weeks=12, required=9, tolerance=0.02):
            if len(prices) < promo_weeks:
                return False
            count = np.sum((prices >= candidate_price * (1 - tolerance)) &
                        (prices <= candidate_price * (1 + tolerance)))
            return count >= required

        # --- User selections ---
        channel_selected = st.selectbox("Select a Channel", options=dataframe["Channel"].dropna().unique())
        channel_data = dataframe[dataframe["Channel"] == channel_selected]

        if channel_data.empty:
            st.warning(f"No data available for the selected Channel: {channel_selected}")
        else:
            brands_in_channel = channel_data["Brand"].dropna().unique()
            brand_selected = st.radio("Select a Brand", options=brands_in_channel, horizontal=True)
            brand_data = channel_data[channel_data["Brand"] == brand_selected]

            aggregator_options = ["Variant", "PackType", "PackSize"]
            aggregator_col = st.selectbox("Select Aggregator Dimension", aggregator_options)
            if aggregator_col not in brand_data.columns:
                st.warning(f"Column '{aggregator_col}' not found in the data.")
                st.stop()
            aggregator_values = brand_data[aggregator_col].dropna().unique()
            if len(aggregator_values) == 0:
                st.warning(f"No non-empty values for '{aggregator_col}' in Brand: {brand_selected}")
                st.stop()
            aggregator_selected = st.radio(f"Select {aggregator_col}", options=aggregator_values, horizontal=True)
            aggregator_data = brand_data[brand_data[aggregator_col] == aggregator_selected]
            if aggregator_data.empty:
                st.warning(f"No data available for {aggregator_col} = {aggregator_selected}")
                st.stop()
                            
            # Save aggregator selection in session state
            st.session_state['aggregator_selected'] = aggregator_selected

            # Loop over each PPG in aggregator_data
            ppgs_in_aggregator = aggregator_data["PPG"].dropna().unique()
            for idx, ppg in enumerate(ppgs_in_aggregator):
                filtered_data = aggregator_data[aggregator_data["PPG"] == ppg]
                if filtered_data.empty:
                    continue

                # Advanced settings expander with force recalculation option.
                key_suffix = f"_{brand_selected}_{aggregator_selected}_{ppg}_{idx}"
                with st.expander(f"Advanced Settings for {brand_selected}, {aggregator_col}: {aggregator_selected}, PPG: {ppg}", expanded=False):
                    force_modification = st.checkbox(
                        "Force recalculation even if BasePrice exists", 
                        value=False, 
                        key=f"force_mod{key_suffix}"
                    )
                    col1, col2, col3, col4, col5 = st.columns(5)
                    rolling_period = col1.number_input(
                        "Rolling Period (weeks):", min_value=4, max_value=52, value=12, step=1,
                        key=f"rolling_period{key_suffix}"
                    )
                    upward_threshold = col2.number_input(
                        "Upward Transition Threshold (%):", min_value=1.0, max_value=20.0, value=5.0, step=0.5,
                        key=f"upward_threshold{key_suffix}"
                    )
                    downward_threshold = col3.number_input(
                        "Downward Transition Threshold (%):", min_value=1.0, max_value=20.0, value=5.0, step=0.5,
                        key=f"downward_threshold{key_suffix}"
                    )
                    weeks_for_promo_check = col4.number_input(
                        "Weeks for Validation:", min_value=2, max_value=18, value=12, step=1,
                        key=f"promo_weeks{key_suffix}"
                    )
                    promo_percentile = col5.number_input(
                        "Percentile for Base Price:", min_value=50.0, max_value=100.0, value=75.0, step=5.0,
                        key=f"promo_percentile{key_suffix}"
                    )

                # If BasePrice is already computed for all rows and not forcing recalculation, skip heavy calculation.
                if filtered_data["BasePrice"].notnull().all() and not force_modification:
                    st.info(f"BasePrice already exists for {brand_selected} - {aggregator_selected} - {ppg}. Skipping calculations...")
                    weekly_data = filtered_data.groupby(["Year", "Month", "Week"]).agg({
                        "SalesValue": "sum",
                        "Volume": "sum",
                        "BasePrice": "mean"
                    }).reset_index()
                    weekly_data["Price"] = weekly_data["SalesValue"] / weekly_data["Volume"]
                    weekly_data = weekly_data.sort_values(by=["Year", "Week"]).reset_index(drop=True)
                    weekly_data["WeekYear"] = weekly_data["Year"].astype(str) + "-W" + weekly_data["Week"].astype(str)
                    
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=weekly_data["WeekYear"],
                        y=weekly_data["Price"],
                        mode="lines+markers",
                        name="Weekly Price",
                        line=dict(color="blue")
                    ))
                    fig.add_trace(go.Scatter(
                        x=weekly_data["WeekYear"],
                        y=weekly_data["BasePrice"],
                        mode="lines",
                        name="Base Price",
                        line=dict(color="red", dash="dash")
                    ))
                    st.plotly_chart(fig, use_container_width=True)
                    continue  # Skip heavy calculation for this PPG

                # Otherwise, perform the heavy calculation:
                weekly_data = filtered_data.groupby(["Year", "Month", "Week"]).agg({
                    "SalesValue": "sum",
                    "Volume": "sum"
                }).reset_index()
                weekly_data["Price"] = weekly_data["SalesValue"] / weekly_data["Volume"]
                weekly_data = weekly_data.sort_values(by=["Year", "Week"]).reset_index(drop=True)
                weekly_data["WeekYear"] = weekly_data["Year"].astype(str) + "-W" + weekly_data["Week"].astype(str)
                if len(weekly_data) < rolling_period:
                    st.warning(f"Not enough data for PPG: {ppg}, {aggregator_col}: {aggregator_selected}, Brand: {brand_selected}")
                    continue

                # --- Optimized Base Price Calculation ---
                price_array = weekly_data["Price"].values
                n = len(price_array)
                base_prices = np.empty(n)
                transition_points = []
                current_base_price = np.percentile(price_array[:rolling_period], promo_percentile)
                last_transition_week = -rolling_period

                for i in range(n):
                    current_price = price_array[i]
                    future_prices = price_array[i: i + weeks_for_promo_check]
                    if len(future_prices) < weeks_for_promo_check:
                        base_prices[i] = current_base_price
                        continue
                    upward = False
                    if current_price >= current_base_price * (1 + upward_threshold / 100) and (i - last_transition_week >= rolling_period):
                        if validate_upward_transition(future_prices, current_price, current_base_price, upward_threshold, 3, weeks_for_promo_check):
                            current_base_price = max(np.percentile(future_prices, promo_percentile), current_price)
                            transition_points.append(i)
                            last_transition_week = i
                            upward = True
                    if (not upward and current_price <= current_base_price * (1 - downward_threshold / 100) and (i - last_transition_week >= rolling_period)):
                        if validate_downward_transition_strict(future_prices, current_price, promo_weeks=weeks_for_promo_check, required=9, tolerance=0.02):
                            current_base_price = min(np.percentile(future_prices, promo_percentile), current_price)
                            transition_points.append(i)
                            last_transition_week = i
                    base_prices[i] = current_base_price

                weekly_data["BasePrice"] = base_prices
                weekly_data["IsTransition"] = np.isin(np.arange(n), transition_points)

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=weekly_data["WeekYear"],
                    y=weekly_data["Price"],
                    mode="lines+markers",
                    name="Weekly Price",
                    line=dict(color="blue")
                ))
                fig.add_trace(go.Scatter(
                    x=weekly_data["WeekYear"],
                    y=weekly_data["BasePrice"],
                    mode="lines",
                    name="Base Price",
                    line=dict(color="red", dash="dash")
                ))
                for t in transition_points:
                    fig.add_trace(go.Scatter(
                        x=[weekly_data["WeekYear"].iloc[t]],
                        y=[weekly_data["BasePrice"].iloc[t]],
                        mode="markers",
                        name="Transition Point",
                        marker=dict(color="orange", size=12, symbol="diamond")
                    ))
                st.plotly_chart(fig, use_container_width=True)

                if st.button(f"Save {brand_selected} - {aggregator_selected} - {ppg}"):
                    for i, row in weekly_data.iterrows():
                        mask = (
                            (dataframe["Year"] == row["Year"]) &
                            (dataframe["Month"] == row["Month"]) &
                            (dataframe["Week"] == row["Week"]) &
                            (dataframe["Brand"] == brand_selected) &
                            (dataframe[aggregator_col] == aggregator_selected) &
                            (dataframe["PPG"] == ppg)
                        )
                        dataframe.loc[mask, "BasePrice"] = row["BasePrice"]
                    st.success(f"Base Price saved for {brand_selected} - {aggregator_selected} - {ppg}")

            # Save All Base Prices button:
            if st.button("Save All Base Prices"):
                updated_dataframe = dataframe.copy()
                aggregator_options = ["Variant", "PackType", "PackSize"]
                for channel in updated_dataframe["Channel"].dropna().unique():
                    ch_df = updated_dataframe[updated_dataframe["Channel"] == channel]
                    for br in ch_df["Brand"].dropna().unique():
                        br_df = ch_df[ch_df["Brand"] == br]
                        for agg_col in aggregator_options:
                            if agg_col not in br_df.columns:
                                continue
                            for agg_val in br_df[agg_col].dropna().unique():
                                agg_df = br_df[br_df[agg_col] == agg_val]
                                for ppg in agg_df["PPG"].dropna().unique():
                                    filtered_data = agg_df[agg_df["PPG"] == ppg]
                                    if filtered_data.empty:
                                        continue
                                    weekly_data = filtered_data.groupby(["Channel", "Brand", agg_col, "PPG", "Year", "Month", "Week"], as_index=False).agg({
                                        "SalesValue": "sum",
                                        "Volume": "sum"
                                    })
                                    weekly_data["Price"] = weekly_data["SalesValue"] / weekly_data["Volume"]
                                    weekly_data["SortKey"] = (weekly_data["Year"].astype(str) +
                                                            weekly_data["Month"].astype(str).str.zfill(2) +
                                                            weekly_data["Week"].astype(str).str.zfill(2))
                                    weekly_data = weekly_data.sort_values("SortKey").reset_index(drop=True)
                                    weekly_data["WeekYear"] = (weekly_data["Year"].astype(str) +
                                                            "-W" +
                                                            weekly_data["Week"].astype(str).str.zfill(2))
                                    if len(weekly_data) < 12:
                                        continue
                                    price_array = weekly_data["Price"].values
                                    n = len(price_array)
                                    base_prices = np.empty(n)
                                    transition_points = []
                                    current_base_price = np.percentile(price_array[:12], 75.0)
                                    last_transition_week = -12
                                    for i in range(n):
                                        current_price = price_array[i]
                                        future_prices = price_array[i: i + 12]
                                        if len(future_prices) < 12:
                                            base_prices[i] = current_base_price
                                            continue
                                        upward = False
                                        if current_price >= current_base_price * 1.05 and (i - last_transition_week >= 12):
                                            if validate_upward_transition(future_prices, current_price, current_base_price, 5, 3, 12):
                                                new_bp = max(np.percentile(future_prices, 75.0), current_price)
                                                current_base_price = new_bp
                                                transition_points.append(i)
                                                last_transition_week = i
                                                upward = True
                                        if not upward and current_price <= current_base_price * 0.95 and (i - last_transition_week >= 12):
                                            if validate_downward_transition_strict(future_prices, current_price, promo_weeks=12, required=9, tolerance=0.02):
                                                new_bp = min(np.percentile(future_prices, 75.0), current_price)
                                                current_base_price = new_bp
                                                transition_points.append(i)
                                                last_transition_week = i
                                        base_prices[i] = current_base_price
                                    weekly_data["BasePrice"] = base_prices
                                    weekly_data["IsTransition"] = np.isin(np.arange(n), transition_points)
                                    for i, row in weekly_data.iterrows():
                                        mask = (
                                            (updated_dataframe["Channel"] == row["Channel"]) &
                                            (updated_dataframe["Brand"] == row["Brand"]) &
                                            (updated_dataframe[agg_col] == row[agg_col]) &
                                            (updated_dataframe["PPG"] == row["PPG"]) &
                                            (updated_dataframe["Year"] == row["Year"]) &
                                            (updated_dataframe["Month"] == row["Month"]) &
                                            (updated_dataframe["Week"] == row["Week"])
                                        )
                                        updated_dataframe.loc[mask, "Price"] = row["Price"]
                                        cond_na = mask & updated_dataframe["BasePrice"].isna()
                                        updated_dataframe.loc[cond_na, "BasePrice"] = row["BasePrice"]
                st.session_state["dataframe1"] = updated_dataframe
                dataframe = updated_dataframe
                st.success("✅ Missing Base Prices computed & updated!")
                st.download_button(label="📥 Download Updated Dataset",
                                data=dataframe.to_csv(index=False),
                                file_name="updated_dataset_with_base_price.csv",
                                mime="text/csv",
                                key="download_updated_data")
    else:
        st.warning("No data available.")

    # Navigation buttons
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()


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
    # If 'dataframe' has the needed columns, use that; else try 'dataframe1'
    # ---------------------------------------------------------------------
    if dataframe is not None and has_required_columns(dataframe):
        df = dataframe
        st.write("Using `dataframe` for promo_depth because it has BasePrice & Price.")
    elif (
        "dataframe1" in st.session_state
        and st.session_state["dataframe1"] is not None
        and has_required_columns(st.session_state["dataframe1"])
    ):
        df = st.session_state["dataframe1"]
        st.write("Using `st.session_state['dataframe1']` for promo_depth because it has BasePrice & Price.")
    else:
        st.error(
            "Neither the selected file nor `dataframe1` in session state contains both "
            "'BasePrice' and 'Price' columns. Please upload a valid file (or compute them in the Base Price step)."
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

    # ---------------------------------
    # NAVIGATION BUTTONS (Back / Home)
    # ---------------------------------
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()


def calendar_comparison_page():
    
    import plotly.express as px
    st.subheader("Promo Calendar Comparison")
    st.write("This module helps you compare and evaluate different promo calendars.")
    st.markdown("---")
    
    # -----------------------------------------
    # Caching: Aggregate Weekly Data Function
    # -----------------------------------------
    @st.cache_data
    def aggregate_weekly_data(df, retailer, brands):
        df_filtered = df[(df["Channel"] == retailer) & (df["Brand"].isin(brands))].copy()
        grouping_cols = ["Year", "Week", "Brand", "PPG"]
        agg_dict = {
            "SalesValue": "sum",
            "Volume": "sum",
            "Price": "mean",       # initial average; will be recalculated
            "BasePrice": "mean"    # assume BasePrice is correct
        }
        weekly = df_filtered.groupby(grouping_cols, as_index=False).agg(agg_dict)
        # Recalculate weighted Price:
        weekly["Price"] = weekly["SalesValue"] / weekly["Volume"]
        # Compute promo depth (relative drop from BasePrice) and express as percentage:
        weekly["PromoDepth"] = (weekly["BasePrice"] - weekly["Price"]) / weekly["BasePrice"]
        weekly["PromoDepthPercent"] = weekly["PromoDepth"] * 100
        # Create WeekStartDate and WeekLabel:
        weekly["WeekStartDate"] = pd.to_datetime(
            weekly["Year"].astype(str) + weekly["Week"].astype(str).str.zfill(2) + "1",
            format="%G%V%u", errors="coerce"
        )
        weekly.dropna(subset=["WeekStartDate"], inplace=True)
        weekly.sort_values("WeekStartDate", inplace=True)
        weekly["WeekLabel"] = weekly["WeekStartDate"].dt.strftime("%Y-W%V")
        return weekly

    # --- Step 1. Select Retailer and Brand(s) in One Row ---
    col1, col2 = st.columns([1, 2])
    with col1:
        retailer = st.selectbox(
            "Select Retailer",
            options=sorted(st.session_state["dataframe1"]["Channel"].dropna().unique())
        )
    with col2:
        available_brands = sorted(
            st.session_state["dataframe1"][
                st.session_state["dataframe1"]["Channel"] == retailer
            ]["Brand"].dropna().unique()
        )
        selected_brands = st.multiselect("Select Brand(s)", options=available_brands, default=available_brands)
    
    # --- Step 2. Aggregate Weekly Data ---
    weekly_data = aggregate_weekly_data(st.session_state["dataframe1"], retailer, selected_brands)
    
    # --- Step 3. Determine Effective Price Level for Each Week ---
    # Use saved cluster definitions from the previous promo depth flow.
    # st.session_state["final_clusters_depth"] is expected to be a dict keyed by (Channel, Brand, PPG)
    def assign_level(row):
        promo_depth_percent = row["PromoDepthPercent"]
        # If discount is very low (< 5%), consider it as Base Price
        if promo_depth_percent < 5:
            return "Base Price", 0
        # Look up the final cluster definitions for this combination
        key = (retailer, row["Brand"], row["PPG"])
        if "final_clusters_depth" in st.session_state and key in st.session_state["final_clusters_depth"]:
            cluster_defs = st.session_state["final_clusters_depth"][key]
            # cluster_defs should be a list of dicts with keys "Min", "Max", "Centroid", "ClusterName"
            for cd in cluster_defs:
                if float(cd["Min"]) <= promo_depth_percent <= float(cd["Max"]):
                    return cd["ClusterName"], float(cd["Centroid"])
            return "Base Price", 0
        else:
            return "Base Price", 0

    # Apply assign_level row-wise; create two new columns: Level and Discount (centroid)
    weekly_data[["Level", "Discount"]] = weekly_data.apply(
        lambda row: pd.Series(assign_level(row)), axis=1
    )
    
    def compute_effective_price(row):
        if row["Level"] == "Base Price":
            return row["BasePrice"]
        else:
            # Use the centroid discount to compute effective price
            return row["BasePrice"] * (1 - row["Discount"] / 100)
    
    weekly_data["EffectivePrice"] = weekly_data.apply(compute_effective_price, axis=1)
    
    # --- Step 4. For Each Pack (PPG): Plot and Display Summary Table ---
    st.subheader("Promo Calendar and Summary by Pack")
    unique_ppgs = sorted(weekly_data["PPG"].unique())
    
    def style_summary_table(df):
        def highlight(row):
            # Highlight rows where Level is not "Base Price" in light yellow.
            return ['background-color: lightyellow' if row["Level"] != "Base Price" else '' for _ in row]
        return df.style.apply(highlight, axis=1)
    
    for ppg in unique_ppgs:
        st.markdown(f"### Pack: {ppg}")
        data_ppg = weekly_data[weekly_data["PPG"] == ppg].copy()
        if data_ppg.empty:
            continue
        # Use two columns: one for the chart and one for the summary table.
        col1, col2 = st.columns([1.5, 1])
        with col1:
            fig = px.line(
                data_ppg,
                x="WeekStartDate",
                y="EffectivePrice",
                color="Brand",
                title=f"Promo Calendar for Pack {ppg}",
                labels={"WeekStartDate": "Week", "EffectivePrice": "Effective Price"}
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            # Build a summary table grouped by Brand and Level.
            summary = data_ppg.groupby(["Brand", "Level"]).agg(
                AvgBasePrice=("BasePrice", "mean"),
                WeeksCount=("Week", "count"),
                TotalVol=("Volume", "sum")
            ).reset_index()
            summary["VolPerWeek"] = summary["TotalVol"] / summary["WeeksCount"]
            # Compute total volume per Brand for that pack.
            brand_pack_vol = data_ppg.groupby(["Brand"])["Volume"].sum().reset_index().rename(columns={"Volume": "BrandPackTotalVol"})
            summary = summary.merge(brand_pack_vol, on="Brand")
            summary["VolContribution%"] = 100 * summary["TotalVol"] / summary["BrandPackTotalVol"]
            display_cols = ["Brand", "Level", "AvgBasePrice", "WeeksCount", "VolPerWeek", "VolContribution%"]
            st.dataframe(style_summary_table(summary[display_cols]))
                    
                    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            go_back()
    with col2:
        if st.button("Home"):
            go_home()
            
            
            
###############def funtion for calendar
def section2_module1_page():
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

    # -----------------------
    #   CUSTOM CLASSES
    # -----------------------
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

            self.W[self.rpi_ppu_indices] = np.minimum(self.W[self.rpi_ppu_indices], 0)
            if self.d1_index is not None:
                self.W[self.d1_index] = max(self.W[self.d1_index], 0)

        def predict(self, X):
            return X.dot(self.W) + self.b


    ########################################################
    # Models Dictionary
    ########################################################
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Lasso Regression": Lasso(alpha=0.1),
        "ElasticNet Regression": ElasticNet(alpha=0.1, l1_ratio=0.5),
        "Bayesian Ridge Regression": BayesianRidge(),
        "Custom Constrained Ridge": CustomConstrainedRidge(l2_penalty=0.1, learning_rate=0.001, iterations=10000),
        "Constrained Linear Regression": ConstrainedLinearRegression(learning_rate=0.001, iterations=10000)
    }

    ########################################################################
    # HELPER: safe_mape, run_full_pipeline, run_model_pipeline
    ########################################################################
    def safe_mape(y_true, y_pred):
        y_true = np.array(y_true, dtype=float)
        y_pred = np.array(y_pred, dtype=float)
        nonzero_mask = (y_true != 0)
        y_true_nonzero = y_true[nonzero_mask]
        y_pred_nonzero = y_pred[nonzero_mask]
        if len(y_true_nonzero) == 0:
            return float("nan")
        return np.mean(np.abs((y_true_nonzero - y_pred_nonzero) / y_true_nonzero)) * 100

    def run_full_pipeline(
        raw_df,
        group_keys,
        pivot_keys,
        use_kalman=True,
        use_ratio_flag=False
    ):
        selected_volume = st.session_state.get("selected_volume", "Volume")

        def convert_and_arrange(df):
            date_col = next((col for col in df.columns if col.strip().lower() == 'date'), None)
            if not date_col:
                st.error("DataFrame must have a 'date' column.")
                st.stop()
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
            df = df.dropna(subset=[date_col])
            return df.sort_values(by=[date_col])

        def adjust_volume_column(df, chosen_col):
            df = df.copy()
            chosen = chosen_col.strip().lower()
            if chosen == 'volume':
                if 'VolumeUnits' in df.columns:
                    df.drop(columns=['VolumeUnits'], inplace=True)
            elif chosen == 'volumeunits':
                if 'Volume' in df.columns:
                    df.drop(columns=['Volume'], inplace=True)
                if 'VolumeUnits' in df.columns:
                    df.rename(columns={'VolumeUnits': 'Volume'}, inplace=True)
                else:
                    st.warning("Warning: 'VolumeUnits' column not found.")
            else:
                st.warning(f"Unrecognized volume column '{chosen_col}'.")
            return df

        def compute_category_weighted_price(df, d_date, d_channel):
            df = df.copy()
            df[d_date] = pd.to_datetime(df[d_date], errors='coerce')
            grouping = [d_channel, d_date]
            weighted_price = df.groupby(grouping).apply(
                lambda g: (g['PPU'] * g['Volume']).sum() / g['Volume'].sum()
                if g['Volume'].sum() != 0 else 0
            ).reset_index(name='Cat_Weighted_Price')
            return weighted_price

        def compute_cat_down_up(df, d_date, d_channel, l0_key=None, l2_key=None):
            df = df.copy()
            df[d_date] = pd.to_datetime(df[d_date], errors='coerce')
            group_keys_for_mean = [d_channel]
            if l0_key is not None:
                group_keys_for_mean.append(l0_key)
            if l2_key is not None:
                group_keys_for_mean.append(l2_key)

            group_mean = (
                df.groupby(group_keys_for_mean)['PPU']
                .mean().reset_index().rename(columns={'PPU': 'mean_ppu'})
            )

            group_keys_daily = [d_channel, d_date]
            if l0_key is not None:
                group_keys_daily.append(l0_key)
            if l2_key is not None:
                group_keys_daily.append(l2_key)

            daily_group = df.groupby(group_keys_daily)['Volume'].sum().reset_index()
            daily_group = daily_group.merge(group_mean, on=group_keys_for_mean, how='left')
            total_volume = (
                daily_group.groupby([d_channel, d_date])['Volume']
                .sum().reset_index().rename(columns={'Volume': 'total_volume'})
            )
            daily_group = daily_group.merge(total_volume, on=[d_channel, d_date], how='left')
            daily_group['weighted_contrib'] = daily_group['mean_ppu'] * (daily_group['Volume'] / daily_group['total_volume'])

            cat_down_up = (
                daily_group.groupby([d_channel, d_date])['weighted_contrib']
                .sum().reset_index().rename(columns={'weighted_contrib': 'Cat_Down_Up'})
            )
            return cat_down_up

        df_proc = convert_and_arrange(raw_df.copy())
        df_proc = adjust_volume_column(df_proc, selected_volume)

        d_date = next((c for c in df_proc.columns if c.strip().lower()=='date'), 'date')
        d_channel = next((c for c in df_proc.columns if c.strip().lower()=='channel'), 'Channel')

        # Summaries for Price & SalesValue
        if "Price" in df_proc.columns and "SalesValue" in df_proc.columns:
            agg_df = (
                df_proc.groupby(group_keys)
                .agg({"Volume": "sum", "Price": "mean", "SalesValue": "sum"})
                .reset_index()
            )
            agg_df.rename(columns={"Price": "PPU"}, inplace=True)
        elif "Price" in df_proc.columns:
            agg_df = (
                df_proc.groupby(group_keys)
                .agg({"Volume": "sum", "Price": "mean"})
                .reset_index()
            )
            agg_df.rename(columns={"Price": "PPU"}, inplace=True)
        elif "SalesValue" in df_proc.columns:
            agg_df = (
                df_proc.groupby(group_keys)
                .agg({"Volume": "sum", "SalesValue": "sum"})
                .reset_index()
            )
            agg_df["PPU"] = np.where(
                agg_df["Volume"] != 0,
                agg_df["SalesValue"] / agg_df["Volume"],
                0
            )

        # Add date parts
        agg_df['Year']  = pd.to_datetime(agg_df[d_date], errors='coerce').dt.year
        agg_df['Month'] = pd.to_datetime(agg_df[d_date], errors='coerce').dt.month
        agg_df['Week']  = pd.to_datetime(agg_df[d_date], errors='coerce').dt.isocalendar().week
        agg_df['Date']  = pd.to_datetime(agg_df[d_date], errors='coerce').dt.date

        # Pivot competitor PPU
        if pivot_keys:
            pivot_df = agg_df.pivot_table(index=[d_date, d_channel], columns=pivot_keys, values='PPU')
            agg_df = pd.concat([agg_df.set_index([d_date, d_channel]), pivot_df], axis=1).reset_index()
            if isinstance(pivot_df.columns, pd.MultiIndex):
                for col_tuple in pivot_df.columns:
                    comp_col = "_".join(map(str, col_tuple)) + "_PPU"
                    agg_df[comp_col] = agg_df[col_tuple]
                    cond = True
                    for i, key in enumerate(pivot_keys):
                        cond &= (agg_df[key] == col_tuple[i])
                    agg_df.loc[cond, comp_col] = np.nan
            else:
                for val in pivot_df.columns:
                    comp_col = f"{val}_PPU"
                    agg_df[comp_col] = agg_df[val]
                    cond = (agg_df[pivot_keys[0]] == val)
                    agg_df.loc[cond, comp_col] = np.nan

            try:
                agg_df.drop(columns=pivot_df.columns, inplace=True)
            except Exception as e:
                st.warning("Could not drop pivot columns: " + str(e))

        # Convert pivoted -> RPI
        agg_df.columns = [
            c.replace('_PPU','_RPI') if isinstance(c,str) and c.endswith('_PPU') else c
            for c in agg_df.columns
        ]
        own_ppu = agg_df["PPU"]
        for col in agg_df.columns:
            if isinstance(col, str) and col.endswith('_RPI') and col != "PPU_RPI":
                agg_df[col] = np.where(agg_df[col] != 0, own_ppu / agg_df[col], 0)

        catvol_df = agg_df.groupby([d_channel, d_date])['Volume'].sum().reset_index(name='CatVol')
        agg_df = pd.merge(agg_df, catvol_df, on=[d_channel,d_date], how='left')
        agg_df['NetCatVol'] = agg_df['CatVol'] - agg_df['Volume']

        # Summarize brand-level vs channel-level
        keys_for_brand = [d_channel] + pivot_keys
        brand_totals = raw_df.groupby(keys_for_brand)['SalesValue'].sum().reset_index(name='BrandSales')
        channel_totals = raw_df.groupby(d_channel)['SalesValue'].sum().reset_index(name='ChannelSales')
        brand_totals = brand_totals.merge(channel_totals, on=[d_channel], how='left')
        brand_totals['MarketShare_overall'] = brand_totals['BrandSales']/brand_totals['ChannelSales']*100
        brand_totals['MarketShare_overall'] = brand_totals['MarketShare_overall'].fillna(0)

        # Monthly seasonality
        monthly_seasonality = (
            agg_df.groupby([d_channel,'Month'])['Volume']
            .mean().reset_index().rename(columns={'Volume':'CatSeasonality'})
        )
        agg_df = pd.merge(agg_df, monthly_seasonality, on=[d_channel,'Month'], how='left')

        # Category Weighted Price & Cat_Down_Up
        cwp_df = compute_category_weighted_price(agg_df, d_date, d_channel)
        cdu_df = compute_cat_down_up(
            agg_df, d_date, d_channel,
            pivot_keys[0] if pivot_keys else None,
            pivot_keys[1] if pivot_keys and len(pivot_keys)>1 else None
        )
        agg_df[d_date] = pd.to_datetime(agg_df[d_date], errors='coerce')
        cat_price_trend_df = pd.merge(cwp_df, cdu_df, on=[d_channel,d_date], how='inner')
        cat_price_trend_df['mean_cat_down_up'] = cat_price_trend_df.groupby(d_channel)['Cat_Down_Up'].transform('mean')
        cat_price_trend_df['Cat_Price_trend_over_time'] = (
            cat_price_trend_df['Cat_Weighted_Price'] *
            (cat_price_trend_df['mean_cat_down_up']/cat_price_trend_df['Cat_Down_Up'])
        )
        agg_df = pd.merge(
            agg_df,
            cat_price_trend_df[[d_channel,d_date,'Cat_Weighted_Price','Cat_Down_Up','Cat_Price_trend_over_time']],
            on=[d_channel,d_date], how='left'
        )

        # Outlier detection (STL)
        if pivot_keys and len(pivot_keys)>1:
            outlier_keys = [d_channel] + pivot_keys
        else:
            outlier_keys = [d_channel] + ([pivot_keys[0]] if pivot_keys else [])

        final_df = agg_df.copy()
        final_df.set_index(d_date, inplace=True)
        final_df['residual'] = np.nan
        final_df['z_score_residual'] = np.nan
        final_df['is_outlier'] = 0

        for name, group in final_df.groupby(outlier_keys):
            if len(group)<2:
                continue
            try:
                orig_index = group.index.copy()
                group_reset = group.reset_index()
                stl = STL(group_reset['Volume'], seasonal=13, period=13)
                result = stl.fit()
                group_reset['residual'] = result.resid
                group_reset['z_score_residual'] = (
                    (group_reset['residual']-group_reset['residual'].mean()) /
                    group_reset['residual'].std()
                )
                group_reset['is_outlier'] = np.where(
                    np.abs(group_reset['z_score_residual'])>3, 1, 0
                )
                for idx, orig in enumerate(orig_index):
                    final_df.at[orig, 'residual'] = group_reset.at[idx, 'residual']
                    final_df.at[orig, 'z_score_residual'] = group_reset.at[idx, 'z_score_residual']
                    final_df.at[orig, 'is_outlier'] = group_reset.at[idx, 'is_outlier']
            except Exception as e:
                st.warning(f"STL failed for group {name}: {e}")

        final_df.reset_index(inplace=True)
        final_df.sort_values(by=d_date, inplace=True)

        # Kalman filter or direct
        if use_kalman:
            def apply_kalman_filter(df, y_col='Volume'):
                vals = df[y_col].values
                initial = vals[0]
                kf = KalmanFilter(initial_state_mean=initial, n_dim_obs=1)
                state_means, _ = kf.filter(vals)
                return state_means.flatten()

            final_df['FilteredVolume'] = np.nan
            kalman_keys = [d_channel]
            if pivot_keys:
                kalman_keys.extend(pivot_keys)

            for grp_name, grp_df in final_df.groupby(kalman_keys):
                grp_df_sorted = grp_df.sort_values(d_date).reset_index().rename(columns={'index':'orig_index'})
                filt_vals = apply_kalman_filter(grp_df_sorted, y_col='Volume')
                final_df.loc[grp_df_sorted['orig_index'], 'FilteredVolume'] = filt_vals
        else:
            final_df['FilteredVolume'] = final_df['Volume']

        if use_ratio_flag:
            final_df['FilteredVolume'] = np.where(
                final_df['CatVol']!=0,
                final_df['FilteredVolume']/final_df['CatVol'],
                0
            )

        final_df.fillna(0, inplace=True)
     
        raw_df_copy = raw_df.copy()
        raw_df_copy[d_date] = pd.to_datetime(raw_df_copy[d_date], errors='coerce')
        raw_df_copy['Date'] = raw_df_copy[d_date].dt.date

        # Merge keys for re-joining raw data
        merge_keys = [d_channel, 'Date']
        if pivot_keys:
            merge_keys += pivot_keys

        # Identify columns that final_df doesn’t yet have
        final_cols_set = set(final_df.columns)
        raw_cols_set = set(raw_df_copy.columns)
        # Subset of raw cols that are NOT already in final_df
        additional_cols = list(raw_cols_set - final_cols_set - set(merge_keys))

        # Create a reduced DataFrame of merge-keys + any extra columns
        extra_df = raw_df_copy[merge_keys + additional_cols].drop_duplicates(subset=merge_keys)

        # Merge these columns into final_df
        final_df['Date'] = pd.to_datetime(final_df['Date'], errors='coerce').dt.date
        final_df = final_df.merge(extra_df, on=merge_keys, how='left')

        final_df.fillna(0, inplace=True)

        # === Merge brand_totals => 'Contribution' - same as before ===
        keys_for_brand = [d_channel] + pivot_keys
        final_df = final_df.merge(
            brand_totals[keys_for_brand + ['MarketShare_overall']],
            on=keys_for_brand, how='left'
        )
        final_df.rename(columns={'MarketShare_overall': 'Contribution'}, inplace=True)
        final_df['Contribution'] = final_df['Contribution'].fillna(0)

        # ----------------------------------------------------------
        # RETURN THE FINAL DATA
        # ----------------------------------------------------------
        return final_df

        # # Merge extra columns
        # raw_df_copy = raw_df.copy()
        # raw_df_copy[d_date] = pd.to_datetime(raw_df_copy[d_date], errors='coerce')
        # raw_df_copy['Date'] = raw_df_copy[d_date].dt.date

        # extra_cols = ['Trend','Weekend','D1']
        # existing_extras = [c for c in extra_cols if c in raw_df_copy.columns]

        # merge_keys = [d_channel,'Date']
        # if pivot_keys:
        #     merge_keys += pivot_keys

        # extra_df = raw_df_copy[merge_keys+existing_extras].drop_duplicates(subset=merge_keys)
        # final_df['Date'] = pd.to_datetime(final_df['Date'], errors='coerce').dt.date

        # dup_extras = [c for c in existing_extras if c in final_df.columns]
        # if dup_extras:
        #     final_df.drop(columns=dup_extras, inplace=True)

        # final_df = final_df.merge(extra_df, on=merge_keys, how='left')
        # final_df.fillna(0, inplace=True)

        # # Merge brand_totals => 'Contribution'
        # final_df = final_df.merge(
        #     brand_totals[keys_for_brand + ['MarketShare_overall']],
        #     on=keys_for_brand, how='left'
        # )
        # final_df.rename(columns={'MarketShare_overall':'Contribution'}, inplace=True)
        # final_df['Contribution'] = final_df['Contribution'].fillna(0)

        # return final_df

    def run_model_pipeline(final_df, grouping_keys, X_columns, target_col, k_folds, chosen_std_cols):
        model_results = {m: [] for m in models.keys()}
        predictions_records = []

        if grouping_keys:
            grouping_data = final_df.groupby(grouping_keys)
        else:
            grouping_data = [((None,), final_df)]

        fold_global = 0

        for group_vals, group_df in grouping_data:
            try:
                market_share_for_group = group_df["Contribution"].iloc[0]
            except:
                market_share_for_group = np.nan

            if not isinstance(group_vals, tuple):
                group_vals = (group_vals,)

            present_cols = [col for col in X_columns if col in group_df.columns]
            if len(present_cols) < len(X_columns):
                st.warning(f"Not all predictors {X_columns} available in group {group_vals}. Skipping.")
                continue

            X_data = group_df[present_cols].copy()
            y_data = group_df[target_col].copy()
            if len(X_data)<k_folds:
                continue

            mean_y = y_data.mean()
            n_samples = len(X_data)
            p_num = len(present_cols)

            for col in present_cols:
                if pd.api.types.is_numeric_dtype(X_data[col]):
                    X_data[col].fillna(0, inplace=True)

            from sklearn.model_selection import KFold
            kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)
            fold_store = {m: [] for m in models.keys()}
            fold_means = {m: [] for m in models.keys()}
            fold_stds = {m: [] for m in models.keys()}

            for train_idx, test_idx in kf.split(X_data, y_data):
                fold_global += 1
                X_train = X_data.iloc[train_idx].copy()
                X_test  = X_data.iloc[test_idx].copy()
                y_train = y_data.iloc[train_idx]
                y_test  = y_data.iloc[test_idx]

                scaler_info = {}
                if chosen_std_cols:
                    sc = StandardScaler()
                    sc.fit(X_train[chosen_std_cols])
                    means_ = sc.mean_
                    stds_  = sc.scale_
                    X_train[chosen_std_cols] = sc.transform(X_train[chosen_std_cols])
                    X_test[chosen_std_cols]  = sc.transform(X_test[chosen_std_cols])
                    for i, c in enumerate(chosen_std_cols):
                        scaler_info[c] = (means_[i], stds_[i])

                for mname,mobj in models.items():
                    if mname in ["Custom Constrained Ridge","Constrained Linear Regression"]:
                        mobj.fit(X_train.values, y_train.values, X_train.columns.tolist())
                        y_train_pred = mobj.predict(X_train.values)
                        y_test_pred  = mobj.predict(X_test.values)
                        B0_std_ = getattr(mobj, "intercept_", 0)
                        B1s_std_ = getattr(mobj, "coef_", np.zeros(p_num))
                    else:
                        mobj.fit(X_train, y_train)
                        y_train_pred = mobj.predict(X_train)
                        y_test_pred  = mobj.predict(X_test)
                        B0_std_ = getattr(mobj, "intercept_", 0)
                        B1s_std_ = getattr(mobj, "coef_", np.zeros(p_num))

                    r2_tr = r2_score(y_train, y_train_pred)
                    r2_te = r2_score(y_test, y_test_pred)
                    n_tr = len(X_train)
                    n_te = len(X_test)
                    adj_tr = (1 - (1-r2_tr)*(n_tr-1)/(n_tr-p_num-1)) if (n_tr-p_num-1)>0 else np.nan
                    adj_te = (1 - (1-r2_te)*(n_te-1)/(n_te-p_num-1)) if (n_te-p_num-1)>0 else np.nan

                    mape_tr = safe_mape(y_train, y_train_pred)
                    mape_te = safe_mape(y_test, y_test_pred)
                    mse_tr  = np.mean((y_train-y_train_pred)**2)
                    mse_te  = np.mean((y_test-y_test_pred)**2)

                    fold_store[mname].append({
                        "r2_train": r2_tr, "r2_test": r2_te,
                        "adj_tr": adj_tr, "adj_te": adj_te,
                        "mape_tr": mape_tr, "mape_te": mape_te,
                        "mse_train": mse_tr, "mse_test": mse_te,
                        "B0_std": B0_std_,
                        "B1s_std": B1s_std_,
                    })
                    fold_means[mname].append({c: scaler_info[c][0] if c in scaler_info else 0.0 for c in present_cols})
                    fold_stds[mname].append({c: scaler_info[c][1] if c in scaler_info else 1.0 for c in present_cols})

                    pred_df = group_df.loc[X_test.index].copy()
                    pred_df["Actual"] = y_test.values
                    pred_df["Predicted"] = y_test_pred
                    pred_df["Model"] = mname
                    pred_df["Fold"] = fold_global
                    predictions_records.append(pred_df)

            for mname in models.keys():
                fdata = fold_store[mname]
                if not fdata:
                    continue

                r2_tr_ = np.mean([fd["r2_train"] for fd in fdata])
                r2_te_ = np.mean([fd["r2_test"] for fd in fdata])
                adj_tr_ = np.mean([fd["adj_tr"] for fd in fdata])
                adj_te_ = np.mean([fd["adj_te"] for fd in fdata])
                mape_tr_ = np.mean([fd["mape_tr"] for fd in fdata])
                mape_te_ = np.mean([fd["mape_te"] for fd in fdata])
                mse_tr_  = np.mean([fd["mse_train"] for fd in fdata])
                mse_te_  = np.mean([fd["mse_test"]  for fd in fdata])

                B0_std_mean = np.mean([fd["B0_std"] for fd in fdata])
                B1s_std_arrays = [fd["B1s_std"] for fd in fdata]
                B1s_std_mean = np.mean(B1s_std_arrays, axis=0)

                avg_scale_info = {}
                for cc in present_cols:
                    col_means = [d[cc] for d in fold_means[mname]]
                    col_stds  = [d[cc] for d in fold_stds[mname]]
                    avg_scale_info[cc] = (np.mean(col_means), np.mean(col_stds))

                raw_intercept = B0_std_mean
                raw_coefs = B1s_std_mean.copy()
                for idx, cc in enumerate(present_cols):
                    if cc in chosen_std_cols:
                        mu_c, std_c = avg_scale_info[cc]
                        raw_coef_c = raw_coefs[idx]/std_c
                        raw_intercept -= (raw_coefs[idx]*(mu_c/std_c))
                        raw_coefs[idx] = raw_coef_c

                predicted_Q = raw_intercept
                mean_x_d = X_data.mean(numeric_only=True).to_dict()
                for i, col_name in enumerate(present_cols):
                    predicted_Q += raw_coefs[i] * mean_x_d.get(col_name, 0.0)

                derivative = 0.0
                if "PPU" in present_cols:
                    ppu_idx = present_cols.index("PPU")
                    derivative += raw_coefs[ppu_idx]
                competitor_ratio_cols = [cc for cc in present_cols if cc.endswith("_RPI")]
                avg_own_price = mean_x_d.get("PPU", 0.0)
                for c_ in competitor_ratio_cols:
                    i_idx = present_cols.index(c_)
                    ratio_beta = raw_coefs[i_idx]
                    ratio_avg  = X_data[c_].mean()
                    if ratio_avg and not np.isnan(ratio_avg) and avg_own_price>0:
                        competitor_price = avg_own_price / ratio_avg
                        if competitor_price>0:
                            derivative += ratio_beta / competitor_price

                if (predicted_Q>0) and (avg_own_price>0):
                    self_elas = derivative * (avg_own_price/predicted_Q)
                else:
                    self_elas = np.nan
                elasticity_flag = ""
                if not np.isnan(self_elas) and abs(self_elas)>100:
                    elasticity_flag = "ELASTICITY>100"
                    st.warning(f"Elasticity > 100 for group {group_vals}: {self_elas:.2f}")

                model_results[mname].append(
                    list(group_vals) + [market_share_for_group] +
                    [ raw_intercept, r2_tr_, r2_te_, adj_tr_, adj_te_,
                      mape_tr_, mape_te_, B0_std_mean ]
                    + list(mean_x_d.values())
                    + list(raw_coefs)
                    + [self_elas, elasticity_flag, avg_own_price]
                )

        all_frames = []
        for mname, rows in model_results.items():
            if not rows:
                continue
            df_tmp = pd.DataFrame(
                rows,
                columns=(grouping_keys
                    + ["Contribution"]
                    + ["B0 (Original)","R2 Train","R2 Test","Adjusted R2 Train","Adjusted R2 Test",
                       "MAPE Train","MAPE Test","B0_std_mean"]
                    + list(mean_x_d.keys())
                    + ["Beta_" + c for c in present_cols]
                    + ["SelfElasticity","ElasticityFlag","PPU_at_Elasticity"]
                )
            )
            df_tmp["Model"] = mname
            all_frames.append(df_tmp)

        if not all_frames:
            st.warning("No modeling results. Possibly no valid data/folds.")
            return None, None

        combined_results_df = pd.concat(all_frames, ignore_index=True)
        date_col_model = next((c for c in final_df.columns if c.strip().lower()=='date'), None)
        if date_col_model:
            final_df[date_col_model] = pd.to_datetime(final_df[date_col_model])
            latest_date = final_df[date_col_model].max()
            last_period = final_df[final_df[date_col_model] >= (latest_date - pd.DateOffset(months=12))]
            avg_PPU_by_group = (
                last_period.groupby(grouping_keys)["PPU"].mean()
                .reset_index().rename(columns={"PPU":"PPU_last_12M"})
            )
            combined_results_df = combined_results_df.merge(avg_PPU_by_group, on=grouping_keys, how='left')
            combined_results_df["CSF"] = combined_results_df["SelfElasticity"].apply(
                lambda x: 1-(1/x) if x and x!=0 else np.nan
            )
            combined_results_df["MCV"] = combined_results_df["CSF"] * combined_results_df["PPU_at_Elasticity"]

        new_order = (grouping_keys+["Model","CSF","MCV","SelfElasticity","PPU_last_12M"]+[
            c for c in combined_results_df.columns
            if c not in grouping_keys+["Model","CSF","MCV","SelfElasticity","PPU_last_12M"]
        ])
        combined_results_df = combined_results_df[new_order]
        combined_results_df.sort_values(by=grouping_keys+["Model"], inplace=True, ignore_index=True)
        preds_concat = None
        if predictions_records:
            preds_concat = pd.concat(predictions_records, ignore_index=True)
        return combined_results_df, preds_concat

    # ------------------------------------------------------------------------
    # PART 1: AGGREGATION & MODELING
    # ------------------------------------------------------------------------
    st.subheader("Price/Promo Elasticity – Aggregation & Modeling")

    # Retrieve main data
    dataframe = st.session_state.get("D0", None)
    if dataframe is None:
        st.error("No data found (st.session_state['D0']). Please upload a file.")
        return

    # UI for aggregator
    colA,colB,colC = st.columns(3)
    with colA:
        channels = dataframe["Channel"].dropna().unique().tolist()
        selected_channel = st.selectbox("Select a Channel:", options=channels)
    with colB:
        vol_options = []
        if "Volume" in dataframe.columns:
            vol_options.append("Volume")
        if "VolumeUnits" in dataframe.columns:
            vol_options.append("VolumeUnits")
        selected_volume = st.selectbox("Select Volume column:", options=vol_options)
        st.session_state["selected_volume"] = selected_volume
    with colC:
        model_type = st.radio("Select Model Type:", options=["Type 1 (Three Distinct Keys)","Type 2 (Multiple Single Keys)"])

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
        pivot_keys = [key1,key2,key3]

        use_kalman = st.checkbox("Use Kalman Filter?", value=True)
        use_ratio  = st.checkbox("Use FilteredVolume as Ratio?", value=False)
        group_keys = [
            next((c for c in dataframe.columns if c.strip().lower()=='date'), 'date'),
            next((c for c in dataframe.columns if c.strip().lower()=='channel'),'Channel')
        ] + selected_keys

        final_agg_df = run_full_pipeline(
            dataframe,
            group_keys=group_keys,
            pivot_keys=pivot_keys,
            use_kalman=use_kalman,
            use_ratio_flag=use_ratio
        )
        st.subheader("Aggregated Data (Type 1)")
        st.dataframe(final_agg_df, height=600, use_container_width=True)

        st.session_state.final_df = final_agg_df
        st.session_state.model_type = "Type 1"

    else:
        st.session_state.type2_dfs = {}
        use_kalman = st.checkbox("Use Kalman Filter?", value=True)
        use_ratio  = st.checkbox("Use FilteredVolume as Ratio?", value=False)

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
            agg_df_key = run_full_pipeline(
                dataframe,
                group_keys,
                [key],
                use_kalman=use_kalman,
                use_ratio_flag=use_ratio
            )
            st.markdown(f"### Aggregated Data for key: **{key}**")
            st.dataframe(agg_df_key, height=600, use_container_width=True)
            st.session_state.type2_dfs[key] = agg_df_key
        st.session_state.model_type = "Type 2"

    # MODELING
    st.title("Modeling")

    if st.session_state.model_type == "Type 1":
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
        if target_col not in modeling_df.columns:
            st.error("No 'FilteredVolume' in final DataFrame. Check pipeline.")
            return
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

        if st.button("Run Models"):
            res, preds = run_model_pipeline(
                modeling_df,
                grouping_keys_model,
                X_columns,
                target_col,
                k_folds,
                chosen_std_cols
            )
            st.session_state.combined_results = res
            st.session_state.predictions_df   = preds
            if res is not None:
                st.dataframe(res, height=500, use_container_width=True)
            if preds is not None:
                st.session_state["type1_predictions"] = preds
                st.subheader("Sample Actual vs. Predicted (Type 1)")
                st.dataframe(preds.head(20))

    else:
        st.markdown("## Type 2 Modeling Parameters")
        if "type2_dfs" not in st.session_state:
            st.warning("No Type 2 aggregated data found.")
            return
        type2_params = {}
        for key, agg_df in st.session_state["type2_dfs"].items():
            st.markdown(f"### Parameters for key: **{key}**")
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
            if target_col not in agg_df.columns:
                st.error(f"No '{target_col}' found for key {key}.")
                continue
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
                st.markdown(f"### Results for **{key}**")
                if res is not None:
                    st.dataframe(res, height=500, use_container_width=True)
                if preds is not None:
                    if "type2_predictions" not in st.session_state:
                        st.session_state["type2_predictions"] = {}
                    st.session_state["type2_predictions"][key] = preds
                    st.markdown(f"#### Sample Actual vs. Predicted for **{key}**")
                    st.dataframe(preds.head(20))
            st.session_state.type2_results = type2_results

    # ------------------------------------------------------------------------
    # PART 2: MODEL SELECTION & FILTERING, CHARTS, FINAL MODEL SAVE
    # ------------------------------------------------------------------------
    st.markdown("---")
    st.title("Model Selection & Post-Modeling Analysis")

    ###############################################################################
    # Helper function for combined label
    ###############################################################################
    def build_model_label(row, l0_key=None, l2_key=None):
        label = str(row.get("Model", "UnknownModel"))
        relevant_keys = ["Channel", "Brand", "Variant", "PackType", "PPG", "PackSize"]
        if l0_key and l0_key not in relevant_keys:
            relevant_keys.append(l0_key)
        if l2_key and l2_key not in relevant_keys:
            relevant_keys.append(l2_key)
        sub_vals = []
        for k in relevant_keys:
            if k in row and pd.notnull(row[k]):
                sub_vals.append(f"{k}={row[k]}")
        if sub_vals:
            label += " (" + ", ".join(sub_vals) + ")"
        return label

    st.markdown("## Model Selection & Filtering")

    # 1) Check if modeling results exist in session state
    if st.session_state.model_type == "Type 1":
        if "combined_results" not in st.session_state:
            st.info("Modeling results are not available yet. Please run the modeling page first.")
            st.stop()
        df_all = st.session_state["combined_results"].copy()

    elif st.session_state.model_type == "Type 2":
        if "type2_results" not in st.session_state or not st.session_state["type2_results"]:
            st.info("Modeling results are not available yet. Please run the modeling page first.")
            st.stop()
        keys = list(st.session_state["type2_results"].keys())
        selected_key = st.selectbox("Select Key for Model Results", options=keys)
        df_all = st.session_state["type2_results"][selected_key].copy()
    else:
        st.error("Unknown model type in session state.")
        st.stop()

    # 2) Optional L0, L2 keys from session
    l0_key = st.session_state.get("selected_key_L0", "L0")
    l2_key = st.session_state.get("selected_key_L2", "L2")

    # ------------------------------------------------------------------------
    # CREATE WIDGETS (7 columns + 2 more for the extra row)
    # We won't filter immediately. We'll store the user choices, then do filtering
    # only when the user clicks "Apply Filters".
    # ------------------------------------------------------------------------
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        if "Channel" in df_all.columns:
            channel_opts = ["All"] + sorted(df_all["Channel"].dropna().unique().tolist())
            channel_choice = st.selectbox("Channel", channel_opts, index=0)
        else:
            channel_choice = "All"

        # Additional keys to filter
        keys_to_filter = ["Brand", "Variant", "PackType", "PPG", "PackSize"]
        key_filter_choices = {}
        for k_ in keys_to_filter:
            if k_ in df_all.columns:
                opts = ["All"] + sorted(df_all[k_].dropna().unique().tolist())
                key_filter_choices[k_] = st.selectbox(k_, opts, index=0)
            else:
                key_filter_choices[k_] = "All"

    with col2:
        if l0_key in df_all.columns:
            l0_opts = ["All"] + sorted(df_all[l0_key].dropna().unique().tolist())
            l0_choice = st.selectbox(f"{l0_key}", l0_opts, index=0)
        else:
            l0_choice = "All"

    with col3:
        if l2_key in df_all.columns:
            l2_opts = ["All"] + sorted(df_all[l2_key].dropna().unique().tolist())
            l2_choice = st.selectbox(f"{l2_key}", l2_opts, index=0)
        else:
            l2_choice = "All"

    with col4:
        if "Model" in df_all.columns:
            model_opts = ["All"] + sorted(df_all["Model"].dropna().unique().tolist())
            model_choice = st.selectbox("Model", model_opts, index=0)
        else:
            model_choice = "All"

    with col5:
        st.write("Self Elas.")
        min_self_elas, max_self_elas = st.slider(
            " ",
            min_value=-10.0,
            max_value=10.0,
            value=(-10.0, 10.0),
            step=0.5,
            label_visibility="collapsed"
        )

    with col7:
        st.write("R2 Range")
        min_r2, max_r2 = st.slider(
            "   ",
            min_value=0.0,
            max_value=1.0,
            value=(0.0,1.0),
            step=0.01,
            label_visibility="collapsed"
        )

    # Extra row for Contribution & CSF
    colC, colCSF = st.columns(2)
    with colC:
        st.write("Contribution")
        min_contrib, max_contrib = st.slider(
            " ",
            min_value=0.0,
            max_value=100.0,
            value=(0.0, 100.0),
            step=1.0,
            label_visibility="collapsed"
        )
    with colCSF:
        st.write("CSF")
        min_csf, max_csf = st.slider(
            "  ",
            min_value=0.0,
            max_value=10.0,
            value=(0.0,10.0),
            step=0.1,
            label_visibility="collapsed"
        )

    # ------------------------------------------------------------------------
    # CHANGED: Single "Apply Filters" button
    # We'll store the filtered DataFrame in st.session_state["df_filteredPromo"]
    # so we don't re-run on every slider change.
    # ------------------------------------------------------------------------
    apply_button = st.button("Apply Filters")

    if "df_filteredPromo" not in st.session_state:
        st.session_state["df_filteredPromo"] = df_all.copy()  # default

    if apply_button:
        # Re-run the same filter logic, but only now
        df_temp = df_all.copy()

        # Filter
        if channel_choice != "All" and "Channel" in df_temp.columns:
            df_temp = df_temp[df_temp["Channel"] == channel_choice]
        if l0_choice != "All" and l0_key in df_temp.columns:
            df_temp = df_temp[df_temp[l0_key] == l0_choice]
        if l2_choice != "All" and l2_key in df_temp.columns:
            df_temp = df_temp[df_temp[l2_key] == l2_choice]
        if model_choice != "All" and "Model" in df_temp.columns:
            df_temp = df_temp[df_temp["Model"] == model_choice]
        for k_, choice_ in key_filter_choices.items():
            if choice_ != "All":
                df_temp = df_temp[df_temp[k_] == choice_]

        # Sliders
        if "SelfElasticity" in df_temp.columns:
            df_temp = df_temp[
                (df_temp["SelfElasticity"] >= min_self_elas) &
                (df_temp["SelfElasticity"] <= max_self_elas)
            ]
        if "R2 Test" in df_temp.columns:
            df_temp = df_temp[
                (df_temp["R2 Test"] >= min_r2) &
                (df_temp["R2 Test"] <= max_r2)
            ]
        if "Contribution" in df_temp.columns:
            df_temp = df_temp[
                (df_temp["Contribution"] >= min_contrib) &
                (df_temp["Contribution"] <= max_contrib)
            ]
        if "CSF" in df_temp.columns:
            df_temp = df_temp[
                (df_temp["CSF"] >= min_csf) &
                (df_temp["CSF"] <= max_csf)
            ]

        st.session_state["df_filteredPromo"] = df_temp.copy()

    # Now we use st.session_state["df_filteredPromo"] for the grid
    df_filtered = st.session_state["df_filteredPromo"]

    st.write(f"Rows after filtering: {len(df_filtered)}")

    # 5) Ensure "Comment"
    if "Comment" not in df_filtered.columns:
        df_filtered.insert(0, "Comment", "")

    st.write("### Editable Grid with Pinned Columns & Row Selection")
    pinned_columns = ["Comment","Channel","Brand","PPG","PackSize","Model"]
    pinned_columns = [c for c in pinned_columns if c in df_filtered.columns]

    from st_aggrid import GridOptionsBuilder, GridUpdateMode, DataReturnMode

    gb = GridOptionsBuilder.from_dataframe(df_filtered)
    for col_ in pinned_columns:
        if col_ == "Comment":
            gb.configure_column(col_, pinned="left", editable=True)
        else:
            gb.configure_column(col_, pinned="left", editable=False)
    for col_ in df_filtered.columns:
        if col_ not in pinned_columns:
            gb.configure_column(col_, editable=True)
    gb.configure_selection("multiple", use_checkbox=True)
    gb.configure_grid_options(enableRangeSelection=True)

    # Optionally, reduce update_mode so it doesn't re-run on row selection if you want
    grid_options = gb.build()

    grid_response = AgGrid(
        df_filtered,
        gridOptions=grid_options,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        allow_unsafe_jscode=True,
        theme="material",
        height=400,
        width="100%",
    )
    df_edited = pd.DataFrame(grid_response["data"])
    selected_rows = grid_response["selected_rows"]
    df_selected = pd.DataFrame(selected_rows)

    st.write("Selected Rows:")
    st.dataframe(df_selected, use_container_width=True)

    # 9) Button to save
    if st.session_state.model_type == "Type 1":
        if st.button("Save Selected Models", key="save_sel_type1"):
            df_selected["ModelName"] = df_selected.apply(
                lambda r: build_model_label(r, l0_key, l2_key), axis=1
            )
            st.session_state["selected_models_type1"] = df_selected.copy()
            st.success("Selected models (Type 1) saved successfully!")
    elif st.session_state.model_type == "Type 2":
        if "selected_models_type2" not in st.session_state:
            st.session_state["selected_models_type2"] = {}
        if st.button("Save Selected Models", key="save_sel_type2"):
            df_selected["ModelName"] = df_selected.apply(
                lambda r: build_model_label(r, l0_key, l2_key), axis=1
            )
            st.session_state["selected_models_type2"][selected_key] = df_selected.copy()
            st.success(f"Selected models for key '{selected_key}' (Type 2) saved successfully!")

    st.markdown("## Saved Models Summary")
    summary_cols = ["ModelName","Channel","Brand","Variant","PackType","PPG","PackSize","Model"]
    if st.session_state.model_type == "Type 1":
        if "selected_models_type1" in st.session_state and not st.session_state["selected_models_type1"].empty:
            saved_df_ = st.session_state["selected_models_type1"]
            show_cols = [c for c in summary_cols if c in saved_df_.columns]
            st.dataframe(saved_df_[show_cols], use_container_width=True)
        else:
            st.info("No saved models for Type 1 yet.")
    else:
        # Type 2
        if "selected_models_type2" in st.session_state and st.session_state["selected_models_type2"]:
            import pandas as pd
            summary_dfs = []
            for key_, df_saved_ in st.session_state["selected_models_type2"].items():
                if isinstance(df_saved_, pd.DataFrame) and not df_saved_.empty:
                    temp = df_saved_.copy()
                    temp["Selected Key"] = key_
                    show_cols = [c for c in summary_cols if c in temp.columns]
                    summary_dfs.append(temp[show_cols])
            if summary_dfs:
                combined_summary = pd.concat(summary_dfs, ignore_index=True)
                st.dataframe(combined_summary, use_container_width=True)
            else:
                st.info("No saved models for Type 2 yet.")
        else:
            st.info("No saved models for Type 2 yet.")


    # ------------------------------------------------------------------------
    # Key Driver Contribution Analysis
    # ------------------------------------------------------------------------
    st.title("Key Driver Contribution Analysis (Separate Charts)")

    if st.session_state.model_type=="Type 1":
        if "selected_models_type1" not in st.session_state or st.session_state["selected_models_type1"].empty:
            st.error("No saved models for Type 1. Please save models first.")
            return
        saved_df = st.session_state["selected_models_type1"].copy()
    else:
        # Type 2
        if "selected_models_type2" not in st.session_state or not st.session_state["selected_models_type2"]:
            st.error("No saved models for Type 2. Please save models first.")
            return
        keys_ = list(st.session_state["selected_models_type2"].keys())
        selected_saved_key = st.selectbox("Select Key for Contribution Analysis", options=keys_)
        saved_df = st.session_state["selected_models_type2"][selected_saved_key].copy()

    if saved_df.empty:
        st.info("No saved models found.")
        return

    beta_cols = [c for c in saved_df.columns if c.startswith("Beta_")]
    if not beta_cols:
        st.error("No 'Beta_' columns found in the saved model data.")
        return

    st.markdown("### Contribution Charts for Each Saved Model")
    for idx, row in saved_df.iterrows():
        model_label = row.get("ModelName", row.get("Model", f"Row {idx}"))
        st.subheader(f"Contribution Chart for Model (Row #{idx}) – {model_label}")
        if "B0_std_mean" not in row or pd.isna(row["B0_std_mean"]) or row["B0_std_mean"]==0:
            st.warning("Skipping model due to missing or invalid 'B0_std_mean'.")
            continue
        mean_y = row["B0_std_mean"]

        contrib_list = []
        for bc in beta_cols:
            predictor = bc.replace("Beta_","")
            if predictor not in row:
                continue
            beta_val = row[bc]
            avg_x = row[predictor]
            contrib_val = (beta_val*avg_x)/mean_y if mean_y!=0 else 0
            if contrib_val==0:
                continue
            contrib_list.append((predictor, contrib_val))

        if not contrib_list:
            st.info("No valid contributions computed for this model.")
            continue
        contrib_df = pd.DataFrame(contrib_list, columns=["Predictor","Contribution"])
        contrib_df.sort_values("Contribution", ascending=False, inplace=True)

        fig_bar = px.bar(
            contrib_df,
            x="Predictor",
            y="Contribution",
            color="Contribution",
            color_continuous_scale="RdBu",
            title=f"Predictor Contributions (Model Row #{idx})",
            labels={"Contribution":"Contribution Value"}
        )
        fig_bar.update_coloraxes(cmid=0)
        fig_bar.update_layout(
            xaxis_tickangle=-45,
            template="plotly_white",
            margin=dict(l=20,r=20,t=40,b=20)
        )
        table_col, chart_col = st.columns([1,2])
        with table_col:
            st.write("Contributions Table:")
            st.dataframe(contrib_df, use_container_width=True)
        with chart_col:
            st.write("Contributions Chart:")
            st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown("---")
        
        




    # ------------------------------------------------------------------------
    # Comparison of CSF, MCV, and SelfElasticity
    # ------------------------------------------------------------------------
    st.title("Comparison of CSF, MCV, and SelfElasticity (Separate Scales)")

    if st.session_state.model_type=="Type 1":
        if "selected_models_type1" not in st.session_state or st.session_state["selected_models_type1"].empty:
            st.error("No saved models for Type 1. Please select and save models first.")
            return
        saved_df = st.session_state["selected_models_type1"].copy()
    else:
        if "selected_models_type2" not in st.session_state or not st.session_state["selected_models_type2"]:
            st.error("No saved models for Type 2. Please select and save models first.")
            return
        keys_ = list(st.session_state["selected_models_type2"].keys())
        selected_key_ = st.selectbox("Select Key for Contribution Metrics", options=keys_)
        saved_df = st.session_state["selected_models_type2"][selected_key_].copy()

    if saved_df.empty:
        st.info("No saved models available.")
        return

    label_col = "ModelName" if "ModelName" in saved_df.columns else "Model"
    required_cols = [label_col,"CSF","MCV","SelfElasticity","Contribution"]
    missing_cols = [c for c in required_cols if c not in saved_df.columns]
    if missing_cols:
        st.error(f"Missing columns: {missing_cols}")
        return

    for c_ in ["CSF","MCV","SelfElasticity","Contribution"]:
        saved_df[c_] = pd.to_numeric(saved_df[c_], errors="coerce")

    fig_3metrics = make_subplots(rows=1, cols=4,
        subplot_titles=["CSF","MCV","SelfElasticity","Contribution"],
        shared_yaxes=False
    )
    fig_4metrics = make_subplots(
        rows=1, cols=4,
        subplot_titles=["CSF", "MCV", "SelfElasticity", "Contribution"],
        shared_yaxes=False
    )

    # 1) CSF
    fig_4metrics.add_trace(
        go.Bar(
            x=saved_df[label_col],  
            y=saved_df["CSF"],
            text=saved_df["CSF"].round(2).astype(str),
            textposition="inside",             # <--- place labels inside
            textfont_color="white",            # <--- so text is visible against bar
            marker_color="#FFBD59",            # primary yellow
            name="CSF"
        ),
        row=1, col=1
    )

    # 2) MCV
    fig_4metrics.add_trace(
        go.Bar(
            x=saved_df[label_col],
            y=saved_df["MCV"],
            text=saved_df["MCV"].round(2).astype(str),
            textposition="inside",
            textfont_color="white",
            marker_color="#41C185",            # secondary green
            name="MCV"
        ),
        row=1, col=2
    )

    # 3) SelfElasticity
    fig_4metrics.add_trace(
        go.Bar(
            x=saved_df[label_col],
            y=saved_df["SelfElasticity"],
            text=saved_df["SelfElasticity"].round(2).astype(str),
            textposition="inside",
            textfont_color="white",
            marker_color="#458EE2",            # tertiary blue
            name="SelfElasticity"
        ),
        row=1, col=3
    )

    # 4) Contribution – using blue-violet (#8A2BE2)
    fig_4metrics.add_trace(
        go.Bar(
            x=saved_df[label_col],
            y=saved_df["Contribution"],
            text=saved_df["Contribution"].round(2).astype(str),
            textposition="inside",
            textfont_color="white",
            marker_color="#8A2BE2",  # blue-violet
            name="Contribution"
        ),
        row=1, col=4
    )

    fig_4metrics.update_layout(
        title_text="Comparison of CSF, MCV, SelfElasticity, and Contribution",
        showlegend=False,
        template="plotly_white",
        margin=dict(l=20, r=20, t=60, b=60),
        font=dict(
            family="Inter, sans-serif",
            size=14,
            color="#333333"
        )
    )

    # Optionally label each axis
    fig_4metrics.update_yaxes(title_text="CSF", row=1, col=1)
    fig_4metrics.update_yaxes(title_text="MCV", row=1, col=2)
    fig_4metrics.update_yaxes(title_text="SelfElasticity", row=1, col=3)
    fig_4metrics.update_yaxes(title_text="Contribution", row=1, col=4)

    # Finally display in Streamlit
    st.plotly_chart(fig_4metrics, use_container_width=True)

    # ------------------------------------------------------------------------
    # Final Model Save and Summary
    # ------------------------------------------------------------------------
    st.title("Final Model Save and Summary")

    if st.session_state.model_type=="Type 1":
        if "selected_models_type1" not in st.session_state or st.session_state["selected_models_type1"].empty:
            st.error("No saved models for Type 1 found. Please select and save models first.")
            return
        saved_df2 = st.session_state["selected_models_type1"].copy()
        if "Model" not in saved_df2.columns:
            saved_df2 = saved_df2.reset_index().rename(columns={"index":"Model"})
        if "ModelName" not in saved_df2.columns:
            saved_df2["ModelName"] = saved_df2.apply(lambda r: build_model_label(r,l0_key,l2_key), axis=1)
        final_mod_options = saved_df2["ModelName"].unique().tolist()
        selected_mods = st.multiselect("Select Final Model(s) to Save (Type 1)", options=final_mod_options)
        if "final_saved_models_type1" not in st.session_state:
            st.session_state["final_saved_models_type1"] = []
        if st.button("Save Selected Final Model(s) for Type 1"):
            for nm in selected_mods:
                fm = saved_df2[saved_df2["ModelName"]==nm].iloc[0]
                st.session_state["final_saved_models_type1"].append(fm)
            st.success("Selected final model(s) for Type 1 saved successfully!")
        st.markdown("### Saved Final Models for Type 1")
        if st.session_state["final_saved_models_type1"]:
            df_final = pd.DataFrame(st.session_state["final_saved_models_type1"])
            st.dataframe(df_final, use_container_width=True)
        else:
            st.info("No final models saved for Type 1 yet.")

    else:
        # Type 2
        if "selected_models_type2" not in st.session_state or not st.session_state["selected_models_type2"]:
            st.error("No saved models for Type 2 found. Please select and save models first.")
            return
        keys_2 = list(st.session_state["selected_models_type2"].keys())
        sel_key_2 = st.selectbox("Select Key for Final Model Save (Type 2)", options=keys_2)
        key_df2 = st.session_state["selected_models_type2"][sel_key_2].copy()
        if "Model" not in key_df2.columns:
            key_df2 = key_df2.reset_index().rename(columns={"index":"Model"})
        if "ModelName" not in key_df2.columns:
            key_df2["ModelName"] = key_df2.apply(lambda r: build_model_label(r,l0_key,l2_key), axis=1)
        final_mod_opts = key_df2["ModelName"].unique().tolist()
        sel_mods = st.multiselect(
            f"Select Final Model(s) to Save for Key '{sel_key_2}'",
            options=final_mod_opts
        )
        if "saved_models_type2" not in st.session_state:
            st.session_state["saved_models_type2"] = {}
        if st.button(f"Save Selected Final Model(s) for Key '{sel_key_2}'"):
            if sel_key_2 not in st.session_state["saved_models_type2"]:
                st.session_state["saved_models_type2"][sel_key_2] = []
            for nm in sel_mods:
                fm = key_df2[key_df2["ModelName"]==nm].iloc[0]
                st.session_state["saved_models_type2"][sel_key_2].append(fm)
            st.success(f"Selected final model(s) for key '{sel_key_2}' saved successfully!")

        st.markdown("### Saved Final Models for Type 2")
        if st.session_state["saved_models_type2"]:
            for k_, model_list_ in st.session_state["saved_models_type2"].items():
                st.subheader(f"Key: {k_}")
                df_key_ = pd.DataFrame(model_list_)
                st.dataframe(df_key_, use_container_width=True)
        else:
            st.info("No final models saved for Type 2 yet.")

    # ------------------------------------------------------------------------
    # NAVIGATION BUTTONS
    # ------------------------------------------------------------------------
    st.markdown("---")
    cBack, cHome, cPM = st.columns(3)
    with cBack:
        if st.button("Back", key="section2_module1_back"):
            go_back()
    with cHome:
        if st.button("Home", key="section2_module1_home"):
            go_home()
            
    with cPM:
        if st.button(" Go to Post‑Modelling"):
            go_to_post_modelling()

def go_to_modelling():
    st.session_state.page = "section2_module1"   # <- must match router
    st.rerun()                                   # use experimental_rerun() on Streamlit < 1.25

def go_to_post_modelling():
    st.session_state.page = "section2_module2"
    st.rerun()

def section2_module2_page():
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
    # Helper functions for back navigation
    # ------------------------------
    def go_back():
        # Implement navigation logic
        st.session_state["current_page"] = "previous_page"
        
    def go_home():
        # Implement navigation logic
        st.session_state["current_page"] = "home_page"

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



    if st.button("← Back to Modelling"):
        go_to_modelling()
        
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
        if "saved_models_type2" not in st.session_state:
            return False
        val = st.session_state["saved_models_type2"]
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
        if not raw_models:
            st.error("No Type 1 models found in session.")
            st.stop()
        df_type1 = pd.DataFrame(raw_models) if isinstance(raw_models, list) else raw_models.copy()
        if df_type1.empty:
            st.error("Type 1 model list is empty.")
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

    if "saved_models_type2" in st.session_state and st.session_state["saved_models_type2"]:
        for key_name, model_list in st.session_state["saved_models_type2"].items():
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
    df_brand_models= pd.DataFrame(st.session_state["saved_models_type2"]["Brand"])
    df_ppg_models  = pd.DataFrame(st.session_state["saved_models_type2"]["PPG"])
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



    # ------------------------------------------------------------------------
    # NAVIGATION BUTTONS
    # ------------------------------------------------------------------------
    st.markdown("---")
    cBack, cHome = st.columns(2)
    with cBack:
        if st.button("Back", key="section2_module1_back"):
            go_back()
    with cHome:
        if st.button("Home", key="section2_module1_home"):
            go_home()




def section2_module3_page():
    


    # ------------------------------------------------------------------------
    # NAVIGATION BUTTONS
    # ------------------------------------------------------------------------
    st.markdown("---")
    cBack, cHome = st.columns(2)
    with cBack:
        if st.button("Back", key="section2_module3_back"):
            go_back()
    with cHome:
        if st.button("Home", key="section2_module3_home"):
            go_home()

##############################section 3 
# def section3_module2_page():
#     import streamlit as st
#     import plotly.graph_objects as go

#     # -----------------------------------------------------------------------
#     # CUSTOM CSS FOR VISUAL ENHANCEMENTS
#     # -----------------------------------------------------------------------
#     st.markdown("""
#     <style>
#     /* Overall app background */
#     .stApp {
#         background-color: #F5F5F5;
#     }

#     /* Primary headers */
#     .custom-header {
#         font-family: 'Inter', sans-serif;
#         font-size: 36px; 
#         font-weight: 600;
#         color: #333333;
#         margin-bottom: 0.2rem;
#     }

#     .subheader {
#         font-family: 'Inter', sans-serif;
#         font-size: 18px;
#         color: #666666;
#         margin-top: 0;
#         margin-bottom: 1rem;
#     }

#     /* Accent horizontal rule */
#     .accent-hr {
#         border: 0;
#         height: 2px;
#         background: linear-gradient(to right, #FFBD59, #FFC87A);
#         margin: 0.5rem 0 1.5rem 0;
#     }

#     /* Card container styling */
#     .card {
#         background-color: #FFFFFF; 
#         padding: 1.2rem 1.2rem;
#         margin-bottom: 1rem;
#         border-radius: 8px;
#         box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
#     }

#     /* Card headings */
#     .card h2 {
#         font-family: 'Inter', sans-serif;
#         font-size: 24px;
#         margin: 0.2rem 0 1rem 0;
#         color: #333333;
#     }

#     /* Buttons in horizontal block (Back, Home) */
#     div[data-testid="stHorizontalBlock"] button {
#         background-color: #FFBD59 !important; 
#         color: #333333 !important;
#         font-weight: 600 !important;
#         border-radius: 4px !important;
#         border: none !important;
#         margin-bottom: 0.5rem;
#     }
#     div[data-testid="stHorizontalBlock"] button:hover {
#         background-color: #FFC87A !important;
#     }

#     /* Dataframe styling */
#     .dataframe-table {
#         font-family: 'Inter', sans-serif;
#         font-size: 14px;
#         color: #333333;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # -----------------------------------------------------------------------
#     # MAIN HEADER & NAVIGATION
#     # -----------------------------------------------------------------------
#     st.markdown('<h1 class="custom-header">📶 Brand Ladder Analysis with Custom Product Aggregation</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subheader">Compare pricing across custom-defined products, using a subtle yet cohesive design.</p>', unsafe_allow_html=True)
#     st.markdown('<hr class="accent-hr">', unsafe_allow_html=True)



#     cBack, cHome = st.columns(2)
#     with cBack:
#         if st.button("Back", key="section3_module2_back"):
#             go_back()
#     with cHome:
#         if st.button("Home", key="section3_module2_home"):
#             go_home()

#     # -----------------------------------------------------------------------
#     # RETRIEVE DATA
#     # -----------------------------------------------------------------------
#     dataframe = st.session_state.get("D0", None)

#     # -----------------------------------------------------------------------
#     # VALIDATE DATA
#     # -----------------------------------------------------------------------
#     if dataframe is None or dataframe.empty:
#         st.warning("No data uploaded yet. Please upload a file in the sidebar.")
#         st.stop()

#     # =============================================================================
#     # CARD 1: FILTERS & SELECTION
#     # =============================================================================
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.write("## Step 1: Configure Filters and Aggregations")

#     # 1) (Optional) CHANNEL SELECTION
#     channel_data = dataframe
#     if "Channel" in dataframe.columns:
#         colA, colB = st.columns(2)
#         with colA:
#             selected_channel = st.selectbox("Select Channel:", dataframe["Channel"].unique())
#         channel_data = dataframe[dataframe["Channel"] == selected_channel]
#         if channel_data.empty:
#             st.warning("No data available for the selected channel.")
#             st.markdown('</div>', unsafe_allow_html=True)
#             st.stop()
#     else:
#         st.info("No 'Channel' column found; proceeding without channel filtering.")

#     # 2) POSSIBLE AGGREGATOR COLUMNS
#     possible_aggregator_cols = ["Brand", "Variant", "PackType", "PPG", "PackSize"]
#     cols_found = [c for c in possible_aggregator_cols if c in channel_data.columns]

#     if not cols_found:
#         st.error("None of the expected columns (Brand, Variant, PackType, PPG, PackSize) exist in the data.")
#         st.markdown('</div>', unsafe_allow_html=True)
#         st.stop()

#     # Let the user pick how they want to measure volume if both columns exist
#     volume_options = []
#     if "VolumeUnits" in channel_data.columns:
#         volume_options.append("By Unit")
#     if "Volume" in channel_data.columns:
#         volume_options.append("By Litre")

#     volume_col = None
#     if volume_options:
#         # e.g., default to "By Unit" if both exist
#         user_volume_choice = st.selectbox("Choose how to compute Price:", volume_options)
#         if user_volume_choice == "By Unit":
#             volume_col = "VolumeUnits"
#         elif user_volume_choice == "By Litre":
#             volume_col = "Volume"

#     # 3-COLUMN LAYOUT: aggregator cols, base aggregator + volume checkbox, competitor aggregator
#     c1, c2, c3 = st.columns([1.2, 1.2, 1.2])

#     with c1:
#         st.markdown("**Select aggregator columns**")
#         selected_agg_cols = st.multiselect(
#             "Aggregator definition:",
#             options=cols_found,
#             default=["Brand"]
#         )
#         st.caption("Combined into a single product identifier.")

#     with c2:
#         st.markdown("**Base Aggregator & Volume**")
#         show_volume = st.checkbox("Display Volume on Secondary Y-Axis", value=False)

#     with c3:
#         st.markdown("**Competitors**")
#         # We'll define competitor aggregator after aggregator column is set.

#     if not selected_agg_cols:
#         st.warning("No aggregator columns selected. Please pick at least one column.")
#         st.markdown('</div>', unsafe_allow_html=True)
#         st.stop()

#     # Build aggregator column
#     channel_data = channel_data.copy()
#     def combine_cols(row):
#         return " - ".join(str(row[c]) for c in selected_agg_cols)

#     channel_data["Aggregator"] = channel_data.apply(combine_cols, axis=1)

#     all_aggregators = sorted(channel_data["Aggregator"].unique())
#     with c2:
#         base_agg = st.selectbox(
#             "Base Aggregator:",
#             options=all_aggregators
#         )
#     with c3:
#         comp_aggs = st.multiselect(
#             "Competitor(s):",
#             options=[a for a in all_aggregators if a != base_agg]
#         )

#     st.markdown('</div>', unsafe_allow_html=True)

#     # =============================================================================
#     # CARD 2: BRAND LADDER + MARKET SHARE (SIDE-BY-SIDE)
#     # =============================================================================
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.write("## Step 2: Brand Ladder & Market Share")

#     selected_data = channel_data[channel_data["Aggregator"].isin([base_agg] + comp_aggs)]
#     if selected_data.empty:
#         st.warning("No data found for the selected aggregators.")
#         st.markdown('</div>', unsafe_allow_html=True)
#         st.stop()

#     colLeft, colRight = st.columns([2, 1])  # Left chart is bigger, right chart narrower

#     # --------------------------
#     # BRAND LADDER (Left Column)
#     # --------------------------
#     with colLeft:
#         st.write("### Brand Ladder Chart")
        
#         # Helper function: create custom marker colors & sizes 
#         # so our brand aggregator stands out a bit, without being too bold
#         def get_marker_properties(df, base_aggregator):
#             marker_colors = []
#             marker_sizes = []
#             for _, row in df.iterrows():
#                 if row["Aggregator"] == base_agg:
#                     marker_colors.append("#FF7F7F")  # Soft red highlight
#                     marker_sizes.append(10)
#                 else:
#                     marker_colors.append("#458EE2")  # Subtle blue
#                     marker_sizes.append(7)
#             return marker_colors, marker_sizes

#         # SCENARIO A: Price & BasePrice
#         if "Price" in channel_data.columns and "BasePrice" in channel_data.columns:
#             grouped_data = (
#                 selected_data.groupby("Aggregator", as_index=False)
#                 .agg(MeanBasePrice=("BasePrice", "mean"), MeanPrice=("Price", "mean"))
#             )

#             # If either "VolumeUnits" or "Volume" is present, merge it in as "VolumeUnits" col
#             # if user wants to display volume. But this usage is optional for scenario A.
#             if volume_col and volume_col in selected_data.columns:
#                 vol_data = selected_data.groupby("Aggregator", as_index=False)[volume_col].sum()
#                 vol_data.rename(columns={volume_col: "VolumeUnits"}, inplace=True) 
#                 grouped_data = grouped_data.merge(vol_data, on="Aggregator", how="left")
#             else:
#                 grouped_data["VolumeUnits"] = 0

#             base_price_val = grouped_data.loc[grouped_data["Aggregator"] == base_agg, "MeanPrice"].values[0]
#             grouped_data["Price Difference (%)"] = (
#                 (grouped_data["MeanPrice"] - base_price_val) / base_price_val * 100
#             )
#             grouped_data.sort_values(by="MeanPrice", inplace=True)

#             marker_colors, marker_sizes = get_marker_properties(grouped_data, base_agg)

#             fig_ladder = go.Figure()
#             fig_ladder.add_trace(go.Scatter(
#                 x=grouped_data["Aggregator"],
#                 y=grouped_data["MeanPrice"],
#                 mode="lines+markers",
#                 line=dict(shape="hv", width=2, color="#666666"),
#                 marker=dict(color=marker_colors, size=marker_sizes, line=dict(width=1, color="#666")),
#                 name="Mean Price"
#             ))

#             # If show_volume is checked, display volume on secondary axis
#             if show_volume and grouped_data["VolumeUnits"].any():
#                 fig_ladder.add_trace(go.Scatter(
#                     x=grouped_data["Aggregator"],
#                     y=grouped_data["VolumeUnits"],
#                     mode="lines+markers",
#                     line=dict(shape="hv", width=2, color="#41C185"),
#                     name="Volume",
#                     yaxis="y2"
#                 ))

#             for _, row in grouped_data.iterrows():
#                 if row["Aggregator"] == base_agg:
#                     note_text = f"${row['MeanPrice']:.2f}"
#                 else:
#                     note_text = f"${row['MeanPrice']:.2f} ({row['Price Difference (%)']:+.1f}%)"
#                 fig_ladder.add_annotation(
#                     x=row["Aggregator"],
#                     y=row["MeanPrice"],
#                     text=note_text,
#                     showarrow=False,
#                     yshift=8,
#                     font=dict(family="Inter", size=12, color="#333")
#                 )

#             fig_ladder.update_layout(
#                 title="Brand Ladder (Base vs. Mean Price)",
#                 xaxis_title="Aggregators",
#                 yaxis_title="Mean Price",
#                 yaxis2=dict(title="Volume", overlaying="y", side="right"),
#                 template="plotly_white",
#                 margin=dict(l=40, r=40, t=60, b=40),
#                 font=dict(family="Inter", size=13, color="#333")
#             )

#             st.plotly_chart(fig_ladder, use_container_width=True)
#             st.dataframe(grouped_data.style.set_table_styles(
#                 [{'selector': 'th', 'props': [('font-family', 'Inter'), ('font-weight', 'normal')]}]
#             ), use_container_width=True)

#         # SCENARIO B: SalesValue & Volume
#         elif "SalesValue" in channel_data.columns and volume_col and volume_col in channel_data.columns:
#             # e.g., computing Avg Price = SalesValue / Volume
#             grouped_data = (
#                 selected_data.groupby("Aggregator", as_index=False)
#                 .agg(TotalSalesValue=("SalesValue", "sum"), TotalVolume=(volume_col, "sum"))
#             )
#             grouped_data["Avg Price"] = grouped_data["TotalSalesValue"] / grouped_data["TotalVolume"]

#             base_avg_price = grouped_data.loc[grouped_data["Aggregator"] == base_agg, "Avg Price"].values[0]
#             grouped_data["Price Difference (%)"] = (
#                 (grouped_data["Avg Price"] - base_avg_price) / base_avg_price * 100
#             )
#             grouped_data.sort_values(by="Avg Price", inplace=True)

#             marker_colors, marker_sizes = get_marker_properties(grouped_data, base_agg)

#             fig_ladder = go.Figure()
#             fig_ladder.add_trace(go.Scatter(
#                 x=grouped_data["Aggregator"],
#                 y=grouped_data["Avg Price"],
#                 mode="lines+markers",
#                 line=dict(shape="hv", width=2, color="#666666"),
#                 marker=dict(color=marker_colors, size=marker_sizes, line=dict(width=1, color="#666")),
#                 name="Avg Price"
#             ))

#             if show_volume:
#                 fig_ladder.add_trace(go.Scatter(
#                     x=grouped_data["Aggregator"],
#                     y=grouped_data["TotalVolume"],
#                     mode="lines+markers",
#                     line=dict(shape="hv", width=2, color="#41C185"),
#                     name="Total Volume",
#                     yaxis="y2"
#                 ))

#             for _, row in grouped_data.iterrows():
#                 if row["Aggregator"] == base_agg:
#                     note_text = f"${row['Avg Price']:.2f}"
#                 else:
#                     note_text = f"${row['Avg Price']:.2f} ({row['Price Difference (%)']:+.1f}%)"
#                 fig_ladder.add_annotation(
#                     x=row["Aggregator"],
#                     y=row["Avg Price"],
#                     text=note_text,
#                     showarrow=False,
#                     yshift=8,
#                     font=dict(family="Inter", size=12, color="#333")
#                 )

#             fig_ladder.update_layout(
#                 title="Brand Ladder: Price & Volume",
#                 xaxis_title="Aggregators",
#                 yaxis_title="Avg Price",
#                 yaxis2=dict(title="Total Volume", overlaying="y", side="right"),
#                 template="plotly_white",
#                 margin=dict(l=40, r=40, t=60, b=40),
#                 font=dict(family="Inter", size=13, color="#333")
#             )

#             st.plotly_chart(fig_ladder, use_container_width=True)
#             st.dataframe(grouped_data.style.set_table_styles(
#                 [{'selector': 'th', 'props': [('font-family', 'Inter'), ('font-weight', 'normal')]}]
#             ), use_container_width=True)

#         else:
#             st.error("Required columns for analysis are missing. Need either: "
#                     "('Price' & 'BasePrice') or ('SalesValue' & a chosen volume column).")

#     # --------------------------
#     # MARKET SHARE PIE (Right Column)
#     # --------------------------
#     with colRight:
#         st.write("### Market Share")
#         # We'll show aggregator-level share for the entire channel
#         pie_colors = ["#FFBD59", "#FFC87A", "#41C185", "#458EE2", "#999999"]

#         # If the user picked "VolumeUnits" or "Volume", we can do volume-based share;
#         # else if we have "SalesValue", we do sales-based share
#         # or else we warn the user
#         if volume_col and volume_col in channel_data.columns:
#             share_data = (
#                 channel_data.groupby("Aggregator", as_index=False)
#                 .agg(TotalVolume=(volume_col, "sum"))
#             )
#             total_volume = share_data["TotalVolume"].sum()
#             if total_volume == 0:
#                 st.warning("Total volume is zero, cannot compute market share.")
#             else:
#                 share_data["Share (%)"] = share_data["TotalVolume"] / total_volume * 100

#                 fig_pie = go.Figure(data=[go.Pie(
#                     labels=share_data["Aggregator"],
#                     values=share_data["TotalVolume"],
#                     hole=0.4
#                 )])
#                 fig_pie.update_layout(
#                     colorway=pie_colors,
#                     title="Market Share (Volume)",
#                     margin=dict(l=10, r=10, t=60, b=10),
#                     height=400
#                 )
#                 st.plotly_chart(fig_pie, use_container_width=True)

#                 st.dataframe(share_data.style.set_table_styles(
#                     [{'selector': 'th', 'props': [('font-family', 'Inter'), ('font-weight', 'normal')]}]
#                 ), use_container_width=True)

#         elif "SalesValue" in channel_data.columns:
#             # fallback to sales-based share
#             share_data = (
#                 channel_data.groupby("Aggregator", as_index=False)
#                 .agg(TotalSales=("SalesValue", "sum"))
#             )
#             total_sales = share_data["TotalSales"].sum()
#             if total_sales == 0:
#                 st.warning("Total sales is zero, cannot compute market share.")
#             else:
#                 share_data["Share (%)"] = share_data["TotalSales"] / total_sales * 100

#                 fig_pie = go.Figure(data=[go.Pie(
#                     labels=share_data["Aggregator"],
#                     values=share_data["TotalSales"],
#                     hole=0.4
#                 )])
#                 fig_pie.update_layout(
#                     colorway=pie_colors,
#                     title="Market Share (Sales)",
#                     margin=dict(l=10, r=10, t=60, b=10),
#                     height=400
#                 )
#                 st.plotly_chart(fig_pie, use_container_width=True)

#                 st.dataframe(share_data.style.set_table_styles(
#                     [{'selector': 'th', 'props': [('font-family', 'Inter'), ('font-weight', 'normal')]}]
#                 ), use_container_width=True)

#         else:
#             st.warning("No 'Volume'/'VolumeUnits' or 'SalesValue' columns found, so market share cannot be computed.")

#     st.markdown('</div>', unsafe_allow_html=True)

def section3_module2_page():
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



    cBack, cHome = st.columns(2)
    with cBack:
        if st.button("Back"):
            go_back()
    with cHome:
        if st.button("Home"):
            go_home()

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


def section3_module4_page():



    cBack, cHome = st.columns(2)
    with cBack:
        if st.button("Back"):
            go_back()
    with cHome:
        if st.button("Home"):
            go_home()

    # -----------------------------------------------------------------------
    # RETRIEVE DATA
    # -----------------------------------------------------------------------
    df = st.session_state.get("D0", None)  # or "dataframe1" if your data is there
    if df is None or df.empty:
        st.warning("No data uploaded yet. Please upload a file in the sidebar or store in st.session_state['D0'].")
        st.stop()

    # For this example, we assume:
    # 1) There's an "Aggregator" column or an easy way to build it
    # 2) "SalesValue" is RSV
    # 3) We'll compute "Market Share" = aggregator's SalesValue / sum(all)
    # 4) We'll compute "Brand Share" = aggregator's SalesValue / sum(all aggregator that share the aggregator's brand)
    #    * This logic is flexible. You might define brand share differently.

    # If you need to build aggregator from columns like [Brand, PackSize], do it here:
    # e.g.:
    # df["Aggregator"] = df["Brand"] + " (" + df["PackSize"] + ")"

    # Check we have "Aggregator", "SalesValue", maybe "Brand"
    needed_cols = {"Aggregator","SalesValue","Brand"}
    missing = needed_cols - set(df.columns)
    if missing:
        st.error(f"Missing columns for aggregator analysis: {missing}")
        st.stop()

    # -----------------------------------------------------------------------
    # CARD 1: FILTERS
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## Step 1: Configure Filters")

    # Optional channel, brand, etc. 
    if "Channel" in df.columns:
        channel_list = ["All"] + sorted(df["Channel"].dropna().unique())
        chosen_channel = st.selectbox("Select Channel:", channel_list)
        if chosen_channel!="All":
            df = df[df["Channel"]==chosen_channel]
            if df.empty:
                st.warning(f"No data after channel filter: {chosen_channel}")
                st.markdown('</div>', unsafe_allow_html=True)
                st.stop()

    # Possibly more filters
    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # CARD 2: TRIPLE SUBPLOT
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## Step 2: Triple Subplot: RSV, Market Share, Brand Share")

    # For each aggregator, sum SalesValue => aggregator_rsv
    aggregator_df = (
        df.groupby(["Aggregator","Brand"], as_index=False)
          .agg(SumSalesValue=("SalesValue","sum"))
    )
    if aggregator_df.empty:
        st.warning("No aggregator data after filters.")
        st.stop()

    # Market share = aggregator_rsv / total_rsv
    total_rsv = aggregator_df["SumSalesValue"].sum()
    aggregator_df["MarketShare"] = np.where(
        total_rsv!=0,
        aggregator_df["SumSalesValue"]/total_rsv,
        0
    )

    # Brand share = aggregator's sumSalesValue / sumSalesValue of brand
    # first find brand total
    brand_totals = (
        aggregator_df.groupby("Brand", as_index=False)["SumSalesValue"].sum()
        .rename(columns={"SumSalesValue":"BrandTotal"})
    )
    aggregator_df = aggregator_df.merge(brand_totals, on="Brand", how="left")
    aggregator_df["BrandShare"] = np.where(
        aggregator_df["BrandTotal"]!=0,
        aggregator_df["SumSalesValue"]/aggregator_df["BrandTotal"],
        0
    )

    # We'll store aggregator, RSV, MarketShare, BrandShare
    aggregator_df.sort_values("SumSalesValue", ascending=False, inplace=True)
    xvals = aggregator_df["Aggregator"].tolist()
    rsv = aggregator_df["SumSalesValue"].tolist()
    mk_share = aggregator_df["MarketShare"].tolist()
    br_share = aggregator_df["BrandShare"].tolist()

    # Build 3-subplot figure with shared X?
    # Actually we can do subplots with shared x, but each trace might want separate x
    # We'll do subplots w/ row=1, col=3
    fig = make_subplots(
        rows=1, cols=3,
        shared_xaxes=False,
        subplot_titles=["RSV (Sales Value)", "Market Share (%)", "Brand Share (%)"]
    )

    # Subplot 1: RSV as bar
    fig.add_trace(
        go.Bar(
            x=xvals,
            y=rsv,
            marker_color="blue",
            name="RSV (SalesValue)"
        ),
        row=1, col=1
    )

    # Subplot 2: Market Share as line
    fig.add_trace(
        go.Scatter(
            x=xvals,
            y=mk_share,
            mode="lines+markers",
            line=dict(color="orange"),
            name="Market Share (%)"
        ),
        row=1, col=2
    )

    # Subplot 3: Brand Share as line
    fig.add_trace(
        go.Scatter(
            x=xvals,
            y=br_share,
            mode="lines+markers",
            line=dict(color="green", dash="dot"),
            name="Brand Share (%)"
        ),
        row=1, col=3
    )

    # Update layout for each subplot
    fig.update_xaxes(tickangle=45, row=1, col=1)
    fig.update_xaxes(tickangle=45, row=1, col=2)
    fig.update_xaxes(tickangle=45, row=1, col=3)

    fig.update_layout(
        title="Pack/Format Price Curves Analysis",
        showlegend=False,
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=100)
    )

    # Show the figure
    st.plotly_chart(fig, use_container_width=True)

    # Show aggregator table
    st.dataframe(aggregator_df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


    cBack, cHome = st.columns(2)
    with cBack:
        if st.button("Back"):
            go_back()
    with cHome:
        if st.button("Home"):
            go_home()
            
#############################ADDITONAL APPS CODES
def myEDA():
    

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    from scipy.stats import zscore, shapiro, chi2_contingency
    import statsmodels.api as sm
    from statsmodels.tsa.seasonal import seasonal_decompose

    # Sklearn
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.cluster import KMeans
    from sklearn.ensemble import RandomForestRegressor

    # XGBoost
    try:
        from xgboost import XGBRegressor
        xgboost_available = True
    except ImportError:
        xgboost_available = False

    from io import BytesIO
    from datetime import date, datetime
    import base64

    # -------------------------
    # Insert your style snippet
    # (This is an example; adapt to your actual Style Guide code.)
    # -------------------------
    st.markdown("""
    <style>
    /* Import your font if needed
       @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap'); */

    /* Body styling */
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #F5F5F5; 
        color: #333333;
    }

    /* Title / Headings */
    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
        margin-bottom: 0.5em;
    }

    /* Buttons */
    .stButton > button {
        background-color: #FFBD59;
        color: #333333;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 4px;
        font-size: 15px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .stButton > button:hover {
        background-color: #FFCF87;
    }
    .stButton > button:active {
        background-color: #FFE7C2;
        transform: scale(0.98);
    }

    /* Expanders */
    .streamlit-expanderHeader {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1F618D;
    }

    /* Custom Card if you want it */
    .custom-card {
        background-color: #FFFFFF;
        border: 1px solid #999999;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin-bottom: 1.5rem;
    }

    /* ETC. Add any other style rules from your Style Guide. */
    </style>
    """, unsafe_allow_html=True)

    # ###############################################################################
    # # Initialize Session State (unchanged)
    # ###############################################################################
    if "modified_data" not in st.session_state:
        st.session_state["modified_data"] = None

    if "filtered_data" not in st.session_state:
        st.session_state["filtered_data"] = None

    if "global_filters" not in st.session_state:
        st.session_state["global_filters"] = {}

    if "report_items" not in st.session_state:
        st.session_state["report_items"] = []

    if "chart_counter" not in st.session_state:
        st.session_state["chart_counter"] = 0

    # ###############################################################################
    # # Helper Functions (unchanged)
    # ###############################################################################
    def export_to_excel(df):
        """Return Excel file bytes with data, summary stats, missing info, correlation."""
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Data', index=False)
            df.describe().to_excel(writer, sheet_name='Summary', index=True)
            missing_df = pd.DataFrame({
                'MissingCount': df.isnull().sum(),
                'MissingPercent': 100 * df.isnull().sum() / len(df)
            })
            missing_df.to_excel(writer, sheet_name='Missing', index=True)
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 1:
                df[numeric_cols].corr().to_excel(writer, sheet_name='Correlation', index=True)
        return output.getvalue()

    def apply_global_filter(dataframe, filter_dict):
        """Apply the global filter dict (col -> list of selected values) to a dataframe."""
        if dataframe.empty:
            return dataframe
        df_filtered = dataframe.copy()
        for col, chosen_vals in filter_dict.items():
            if chosen_vals:
                df_filtered = df_filtered[df_filtered[col].isin(chosen_vals)]
        return df_filtered

    def safe_plotly_chart(fig, name="chart"):
        st.session_state["chart_counter"] += 1
        st.plotly_chart(fig, use_container_width=True, key=f"{name}_{st.session_state['chart_counter']}")

    def clamp_date(session_key, min_d, max_d):
        if st.session_state[session_key] < min_d:
            st.session_state[session_key] = min_d
        if st.session_state[session_key] > max_d:
            st.session_state[session_key] = max_d

    # ###############################################################################
    # Main Header
    # ###############################################################################
    st.markdown('<h1 style="text-align:center;">MEGA EDA & ML Suite</h1>', unsafe_allow_html=True)

    # ###############################################################################
    # Sidebar - File Upload (unchanged)
    # ###############################################################################
    st.sidebar.title("Upload File")
    uploaded_file = st.sidebar.file_uploader("Upload CSV, Excel, or JSON", type=["csv","xlsx","json"])

    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith((".xls",".xlsx")):
                df = pd.read_excel(uploaded_file)
            elif uploaded_file.name.endswith(".json"):
                df = pd.read_json(uploaded_file)
            else:
                st.sidebar.error("Unsupported file format.")
                df = pd.DataFrame()
            st.sidebar.success(f"File uploaded: {uploaded_file.name}")
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")
            df = pd.DataFrame()
    else:
        df = pd.DataFrame()

    # Initialize st.session_state["modified_data"] if new file or if empty
    if not df.empty and (st.session_state["modified_data"] is None or uploaded_file):
        st.session_state["modified_data"] = df.copy()

    dataframe = st.session_state["modified_data"] if st.session_state["modified_data"] is not None else pd.DataFrame()

    # ###############################################################################
    # Global Sidebar Filter (unchanged)
    # ###############################################################################
    st.sidebar.title("Global Filter")
    if not dataframe.empty:
        eligible_filter_cols = []
        for c in dataframe.columns:
            if dataframe[c].nunique() <= 30:
                eligible_filter_cols.append(c)
        filtered_df = dataframe.copy()
        for col in eligible_filter_cols:
            unique_vals = sorted(filtered_df[col].dropna().unique())
            prev_sel = st.session_state["global_filters"].get(col, [])
            chosen_vals = st.sidebar.multiselect(f"{col}", unique_vals, default=prev_sel)
            st.session_state["global_filters"][col] = chosen_vals
            if chosen_vals:
                filtered_df = filtered_df[filtered_df[col].isin(chosen_vals)]

        st.session_state["filtered_data"] = filtered_df
        st.sidebar.write(f"**Filtered Shape**: {filtered_df.shape[0]} rows x {filtered_df.shape[1]} cols")
    else:
        st.sidebar.info("No data loaded.")

    # ###############################################################################
    # Identify columns
    # ###############################################################################
    if st.session_state["filtered_data"] is not None and not st.session_state["filtered_data"].empty:
        numeric_cols = st.session_state["filtered_data"].select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = st.session_state["filtered_data"].select_dtypes(include=["object","category"]).columns.tolist()
    else:
        numeric_cols = []
        cat_cols = []

    # ###############################################################################
    # TABS
    # ###############################################################################
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Data Overview",
        "Univariate / Bivariate",
        "Viz & Advanced Analysis",
        "Time Series",
        "Clustering & Feat.Imp",
        "Download",
        "Report"
    ])

    # -------------------------------------------------------------------------
    # TAB 1: DATA OVERVIEW
    # -------------------------------------------------------------------------
    with tab1:
        st.subheader("Data Overview")
        if st.session_state["filtered_data"] is None or st.session_state["filtered_data"].empty:
            st.info("No data loaded. Please upload a file.")
        else:
            df_filtered = st.session_state["filtered_data"]
            st.write(f"**Shape**: {df_filtered.shape[0]} rows x {df_filtered.shape[1]} columns")

            if st.button("Show Sample Rows", key="ov_show_sample"):
                st.write("### Sample Rows")
                st.dataframe(df_filtered.head(10))

            if st.button("Numeric Describe", key="ov_num_desc"):
                st.dataframe(df_filtered.describe())

            if st.button("Full Describe (All Columns)", key="ov_full_desc"):
                st.dataframe(df_filtered.describe(include='all'))

    ###############################################################################
    # TAB 2: UNIVARIATE / BIVARIATE
    ###############################################################################
    with tab2:
        st.subheader("Univariate & Bivariate Analysis")

        if st.session_state["filtered_data"] is None or st.session_state["filtered_data"].empty:
            st.info("No data after filtering.")
        else:
            df_ = st.session_state["filtered_data"]

            # Univariate
            st.markdown("#### Univariate Analysis")
            uni_type = st.selectbox("Type:", ["Numeric","Categorical"], key="univar_type")

            if uni_type == "Numeric":
                if numeric_cols:
                    chosen_num = st.selectbox("Select numeric col:", numeric_cols, key="univar_num")
                    if chosen_num:
                        mean_val = df_[chosen_num].mean()
                        median_val = df_[chosen_num].median()
                        fig_u = px.histogram(df_, x=chosen_num, nbins=30, title=f"Distribution of {chosen_num}")
                        fig_u.add_vline(x=mean_val, line_dash='dash', line_color='red', annotation_text='Mean')
                        fig_u.add_vline(x=median_val, line_dash='dash', line_color='green', annotation_text='Median')

                        safe_plotly_chart(fig_u, name="univar_num")
                        comment_for_uni = st.text_input("Comment on this chart:", key="univar_num_comment")
                        if st.button("Save to Report (Univariate Num)", key="univar_num_button"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"Distribution of {chosen_num}",
                                "figure": fig_u,
                                "comment": comment_for_uni
                            })
                            st.success("Chart saved to Report tab.")
                else:
                    st.warning("No numeric columns in the filtered dataset.")
            else:
                if cat_cols:
                    chosen_cat = st.selectbox("Select categorical col:", cat_cols, key="univar_cat")
                    if chosen_cat:
                        val_counts = df_[chosen_cat].value_counts(dropna=False)
                        fig_cat = px.bar(
                            x=val_counts.index, y=val_counts.values,
                            labels={"x": chosen_cat, "y": "Count"},
                            title=f"Count of {chosen_cat}"
                        )
                        safe_plotly_chart(fig_cat, name="univar_cat")
                        comment_for_uni_cat = st.text_input("Comment on this chart:", key="univar_cat_comment")
                        if st.button("Save to Report (Univariate Cat)", key="univar_cat_button"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"Count of {chosen_cat}",
                                "figure": fig_cat,
                                "comment": comment_for_uni_cat
                            })
                            st.success("Chart saved to Report tab.")
                else:
                    st.warning("No categorical columns in the filtered dataset.")

            # Bivariate
            st.markdown("#### Bivariate Analysis")
            tab_bi1, tab_bi2, tab_bi3 = st.tabs(["Numeric vs Numeric","Categorical vs Numeric","Categorical vs Categorical"])
            
            with tab_bi1:
                st.write("### Numeric vs Numeric")
                if len(numeric_cols) < 2:
                    st.warning("Need >= 2 numeric columns.")
                else:
                    x_num = st.selectbox("X-axis (numeric):", numeric_cols, key="bivar_numx")
                    possible_y = [c for c in numeric_cols if c != x_num]
                    y_num = st.selectbox("Y-axis (numeric):", possible_y, key="bivar_numy")

                    if x_num and y_num:
                        corr_val = df_[[x_num,y_num]].corr().iloc[0,1]
                        st.write(f"**Correlation ({x_num} vs {y_num})**: {corr_val:.3f}")
                        fig_n2n = px.scatter(df_, x=x_num, y=y_num, trendline="ols", 
                                            title=f"{x_num} vs {y_num}")
                        safe_plotly_chart(fig_n2n, name="bivar_num_num")
                        comment_bi1 = st.text_input("Comment on this chart:", key="bivar_num_num_comment")
                        if st.button("Save to Report (Num vs Num)", key="bivar_num_button"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"{x_num} vs {y_num}",
                                "figure": fig_n2n,
                                "comment": f"Correlation: {corr_val:.3f}\n{comment_bi1}"
                            })
                            st.success("Chart saved to Report tab.")

            with tab_bi2:
                st.write("### Categorical vs Numeric")
                if numeric_cols and cat_cols:
                    cat_sel = st.selectbox("Select categorical col:", cat_cols, key="bivar_catnum_cat")
                    num_sel = st.selectbox("Select numeric col:", numeric_cols, key="bivar_catnum_num")
                    plot_type = st.radio("Plot Type:", ["Box","Violin","Bar"], key="bivar_catnum_plot", horizontal=True)

                    unique_cats_count = df_[cat_sel].nunique()
                    if unique_cats_count > 10:
                        top_n = st.slider("Show Top N Categories", 5, 20, 10, key="bivar_catnum_top")
                        top_vals = df_[cat_sel].value_counts().nlargest(top_n).index
                        df_filtered_cat = df_[df_[cat_sel].isin(top_vals)]
                    else:
                        df_filtered_cat = df_

                    if plot_type == "Box":
                        fig_box = px.box(df_filtered_cat, x=cat_sel, y=num_sel, color=cat_sel,
                                        title=f"Box Plot: {num_sel} by {cat_sel}")
                        safe_plotly_chart(fig_box, name="bivar_catnum_box")
                        comment_box = st.text_input("Comment on this Box Plot:", key="bivar_box_comment")
                        if st.button("Save Box Plot to Report", key="bivar_box_button"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"Box Plot: {num_sel} vs {cat_sel}",
                                "figure": fig_box,
                                "comment": comment_box
                            })
                            st.success("Chart saved to Report tab.")
                    elif plot_type == "Violin":
                        fig_viol = px.violin(df_filtered_cat, x=cat_sel, y=num_sel, box=True, color=cat_sel,
                                            title=f"Violin Plot: {num_sel} by {cat_sel}")
                        safe_plotly_chart(fig_viol, name="bivar_catnum_violin")
                        comment_viol = st.text_input("Comment on this Violin Plot:", key="bivar_viol_comment")
                        if st.button("Save Violin Plot to Report", key="bivar_viol_button"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"Violin Plot: {num_sel} vs {cat_sel}",
                                "figure": fig_viol,
                                "comment": comment_viol
                            })
                            st.success("Chart saved to Report tab.")
                    else:
                        agg_df = df_filtered_cat.groupby(cat_sel)[num_sel].agg(['mean','std']).reset_index()
                        fig_bar = px.bar(agg_df, x=cat_sel, y='mean', error_y='std', color=cat_sel,
                                        title=f"Mean {num_sel} by {cat_sel}")
                        fig_bar.update_layout(yaxis_title=f"Mean {num_sel}")
                        safe_plotly_chart(fig_bar, name="bivar_catnum_bar")
                        comment_bar = st.text_input("Comment on this Bar Chart:", key="bivar_bar_comment")
                        if st.button("Save Bar Plot to Report", key="bivar_bar_button"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"Mean {num_sel} vs {cat_sel}",
                                "figure": fig_bar,
                                "comment": comment_bar
                            })
                            st.success("Chart saved to Report tab.")
                else:
                    st.warning("Need at least one numeric + one categorical col.")

            with tab_bi3:
                st.write("### Categorical vs Categorical")
                if len(cat_cols) < 2:
                    st.warning("Need >=2 categorical columns.")
                else:
                    cat_a = st.selectbox("Category A:", cat_cols, key="bivar_catcat_a")
                    possible_b = [c for c in cat_cols if c != cat_a]
                    cat_b = st.selectbox("Category B:", possible_b, key="bivar_catcat_b")

                    if cat_a and cat_b:
                        cont_tab = pd.crosstab(df_[cat_a], df_[cat_b], normalize='index')
                        st.write("Contingency Table (row-based normalization):")
                        st.dataframe(cont_tab)
                        fig_cc = px.imshow(cont_tab, text_auto='.2f',
                                        title=f"Heatmap: {cat_a} vs {cat_b}")
                        safe_plotly_chart(fig_cc, name="bivar_cat_cat")
                        comment_catcat = st.text_input("Comment on this Heatmap:", key="bivar_catcat_comment")
                        if st.button("Save Cat vs Cat Heatmap", key="bivar_catcat_button"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"Heatmap: {cat_a} vs {cat_b}",
                                "figure": fig_cc,
                                "comment": comment_catcat
                            })
                            st.success("Chart saved to Report tab.")

    ###############################################################################
    # TAB 3: VISUALIZATION & ADVANCED ANALYSIS
    ###############################################################################
    with tab3:
        st.subheader("Visualization & Advanced Analysis")

        if st.session_state["filtered_data"] is None or st.session_state["filtered_data"].empty:
            st.info("No data after filtering.")
        else:
            df_ = st.session_state["filtered_data"]

            # Quick Chart Generation
            st.markdown("### Quick Chart Generation")
            chart_opt = st.selectbox("Chart Type:", ["Bar","Scatter","Pie","Histogram","Line","Dual-Y Line"], key="viz_chart_type")
            if df_.empty:
                st.warning("Filtered dataset is empty.")
            else:
                x_sel = st.selectbox("X-axis:", df_.columns, key="viz_xsel")
                color_sel = st.selectbox("Color/Group By (optional):", ["None"]+cat_cols, key="viz_colorsel")
                if color_sel == "None":
                    color_sel = None

                if chart_opt == "Dual-Y Line":
                    st.write("Select exactly 2 numeric columns for Y-axes.")
                    dual_y = st.multiselect("2 numeric columns:", numeric_cols, key="viz_dualy")
                    chart_title = st.text_input("Chart Title:", "", key="viz_title_dualy")
                    if len(dual_y) == 2:
                        fig = make_subplots(specs=[[{"secondary_y":True}]])
                        c1, c2 = dual_y[0], dual_y[1]
                        fig.add_trace(
                            go.Scatter(x=df_[x_sel], y=df_[c1],
                                    name=c1, mode='lines+markers'),
                            secondary_y=False
                        )
                        fig.add_trace(
                            go.Scatter(x=df_[x_sel], y=df_[c2],
                                    name=c2, mode='lines+markers'),
                            secondary_y=True
                        )
                        fig.update_layout(title=chart_title or f"Dual: {c1} & {c2}")
                        fig.update_xaxes(title_text=x_sel)
                        fig.update_yaxes(title_text=c1, secondary_y=False)
                        fig.update_yaxes(title_text=c2, secondary_y=True)

                        safe_plotly_chart(fig, name="chart_dualy")
                        user_comment_dual = st.text_input("Comment on Dual-Y Chart:", key="viz_pin_dualy_comment")
                        if st.button("Save to Report (Dual-Y)", key="viz_pin_dualy"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": chart_title or "Dual-Y Chart",
                                "figure": fig,
                                "comment": user_comment_dual
                            })
                            st.success("Chart saved to Report tab.")
                    else:
                        st.warning("Pick exactly 2 numeric columns for Dual-Y line.")
                else:
                    y_sel = st.selectbox("Y-axis (numeric):", numeric_cols, key="viz_ysel_single")
                    chart_title = st.text_input("Chart Title:", "", key="viz_title_single")

                    corr_text = None
                    if x_sel in numeric_cols and y_sel in numeric_cols:
                        corr_val = df_[[x_sel, y_sel]].corr().iloc[0,1]
                        st.write(f"**Correlation**: {corr_val:.3f}")
                        corr_text = f"Correlation: {corr_val:.3f}"

                    fig = None
                    if chart_opt == "Bar":
                        fig = px.bar(df_, x=x_sel, y=y_sel, color=color_sel,
                                    title=chart_title or f"{y_sel} vs {x_sel}")
                    elif chart_opt == "Scatter":
                        fig = px.scatter(df_, x=x_sel, y=y_sel, color=color_sel,
                                        title=chart_title or f"{y_sel} vs {x_sel}")
                    elif chart_opt == "Pie":
                        fig = px.pie(df_, names=x_sel, values=y_sel,
                                    title=chart_title or "Pie Chart")
                    elif chart_opt == "Histogram":
                        fig = px.histogram(df_, x=x_sel, y=y_sel,
                                        color=color_sel, title=chart_title or f"Histogram of {x_sel}")
                    else:  # "Line"
                        fig = px.line(df_, x=x_sel, y=y_sel, color=color_sel,
                                    markers=True, title=chart_title or f"{y_sel} over {x_sel}")

                    if fig:
                        safe_plotly_chart(fig, name="chart_single")
                        user_comment_single = st.text_input("Comment on this chart:", key="viz_pin_chart_comment")
                        if st.button("Save to Report", key="viz_pin_chart"):
                            combined_comment = (corr_text + "\n" + user_comment_single) if corr_text else user_comment_single
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": chart_title or chart_opt,
                                "figure": fig,
                                "comment": combined_comment
                            })
                            st.success("Chart saved to Report tab.")

            # Additional Analysis
            st.markdown("### Additional Analysis")

            # Correlation Matrix
            with st.expander("Correlation Matrix (with Top Features)", expanded=False):
                if len(numeric_cols) < 2:
                    st.warning("Need >=2 numeric columns.")
                else:
                    corr_mat = df_[numeric_cols].corr()
                    fig_corr = px.imshow(corr_mat, text_auto=".2f", color_continuous_scale='RdBu_r',
                                        title="Correlation Matrix", zmin=-1, zmax=1)
                    fig_corr.update_layout(height=700)
                    safe_plotly_chart(fig_corr, name="corr_matrix")

                    # Top correlated pairs
                    st.write("#### Top Correlated Pairs")
                    corr_df = corr_mat.unstack().reset_index()
                    corr_df.columns = ["Feature1","Feature2","Correlation"]
                    corr_df = corr_df[corr_df["Feature1"]!=corr_df["Feature2"]]
                    corr_df["AbsCorrelation"] = corr_df["Correlation"].abs()
                    corr_df = corr_df.sort_values("AbsCorrelation", ascending=False).drop_duplicates(subset=["AbsCorrelation"])
                    corr_df["Pair"] = corr_df.apply(lambda row: "|".join(sorted([row["Feature1"], row["Feature2"]])), axis=1)
                    corr_df = corr_df.drop_duplicates(subset=["Pair"]).head(15)
                    fig_top = px.bar(corr_df, x="Correlation", y="Pair", orientation='h',
                                    color="Correlation", color_continuous_scale='RdBu_r',
                                    title="Top 15 Correlated Pairs", text="Correlation")
                    fig_top.update_traces(texttemplate='%{text:.2f}', textposition='outside')
                    safe_plotly_chart(fig_top, name="top_corr_pairs")

            with st.expander("Distribution Analysis", expanded=False):
                dist_vars = st.multiselect("Select numeric columns:", numeric_cols, key="viz_dist_vars")
                if dist_vars:
                    for col in dist_vars:
                        st.write(f"#### Distribution for: {col}")
                        c1, c2 = st.columns(2)
                        with c1:
                            fig_h = px.histogram(df_, x=col, nbins=30, title=f"Histogram: {col}")
                            safe_plotly_chart(fig_h, name=f"dist_hist_{col}")
                        with c2:
                            fig_b = px.box(df_, y=col, title=f"Box Plot: {col}")
                            safe_plotly_chart(fig_b, name=f"dist_box_{col}")
                else:
                    st.info("Select at least one numeric column to show distribution plots.")

            with st.expander("Outlier Detection", expanded=False):
                if numeric_cols:
                    out_col = st.selectbox("Select numeric col for outlier detection:", numeric_cols, key="viz_outlier_select")
                    out_method = st.selectbox("Method:", ["Z-Score","IQR","Modified Z-Score"], key="viz_outlier_method")
                    col1, col2 = st.columns(2)

                    threshold = 3.0
                    iqr_mult = 1.5
                    mz_thresh = 3.5
                    if out_method == "Z-Score":
                        threshold = col1.number_input("Z-Score threshold", 0.0, 10.0, 3.0, key="viz_outlier_z")
                    elif out_method == "IQR":
                        iqr_mult = col1.number_input("IQR multiplier", 1.0, 10.0, 1.5, key="viz_outlier_iqr")
                    else:
                        mz_thresh = col1.number_input("Modified Z threshold", 0.0, 10.0, 3.5, key="viz_outlier_mz")

                    if col2.button("Detect Outliers", key="viz_outlier_button"):
                        col_data = df_[out_col].dropna()
                        outliers = pd.DataFrame()
                        if out_method == "Z-Score":
                            zs = zscore(col_data)
                            out_idx = (zs < -threshold) | (zs > threshold)
                            outliers = df_.loc[out_idx]
                        elif out_method == "IQR":
                            Q1 = col_data.quantile(0.25)
                            Q3 = col_data.quantile(0.75)
                            IQR = Q3 - Q1
                            lower = Q1 - iqr_mult*IQR
                            upper = Q3 + iqr_mult*IQR
                            out_idx = (df_[out_col] < lower) | (df_[out_col] > upper)
                            outliers = df_.loc[out_idx]
                        else:
                            median_val = col_data.median()
                            mad = np.median(np.abs(col_data - median_val))
                            if mad == 0:
                                st.warning("MAD=0, can't compute Modified Z.")
                            else:
                                mod_z = 0.6745*(col_data - median_val)/mad
                                out_idx = (mod_z < -mz_thresh) | (mod_z > mz_thresh)
                                outliers = df_.loc[out_idx]

                        if outliers.empty:
                            st.info("No outliers found.")
                        else:
                            st.write(f"Detected {outliers.shape[0]} outliers in {out_col}")
                            st.dataframe(outliers.head(10))

            with st.expander("Pivot Table", expanded=False):
                if cat_cols and numeric_cols:
                    piv_idx = st.selectbox("Index Col:", cat_cols, key="viz_piv_idx")
                    piv_val = st.selectbox("Values Col:", numeric_cols, key="viz_piv_val")
                    piv_agg = st.selectbox("Aggregation:", ["sum","mean","count","min","max"], key="viz_piv_agg")
                    pivoted = df_.pivot_table(index=piv_idx, values=piv_val, aggfunc=piv_agg)
                    st.dataframe(pivoted)
                else:
                    st.info("Need at least one categorical + one numeric column for pivot table.")

            with st.expander("Statistical Tests", expanded=False):
                test_sel = st.selectbox("Test Type:", ["None","Shapiro-Wilk (Normality)","Chi-Square"], key="viz_stat_test")
                if test_sel == "Shapiro-Wilk (Normality)":
                    if numeric_cols:
                        s_col = st.selectbox("Numeric Column:", numeric_cols, key="viz_stat_shapcol")
                        dat = df_[s_col].dropna()
                        if not dat.empty:
                            stat,pval = shapiro(dat)
                            st.write(f"Shapiro Statistic={stat:.4f}, p={pval:.4f}")
                            if pval > 0.05:
                                st.success("Data appears normal (fail to reject H0).")
                            else:
                                st.error("Data not normal (reject H0).")
                        else:
                            st.warning("No non-null data to test.")
                    else:
                        st.warning("No numeric columns for normality test.")
                elif test_sel == "Chi-Square":
                    if len(cat_cols) < 2:
                        st.warning("Need >=2 cat columns for Chi-Square.")
                    else:
                        c1 = st.selectbox("Cat X:", cat_cols, key="viz_stat_chix")
                        c2 = st.selectbox("Cat Y:", [c for c in cat_cols if c != c1], key="viz_stat_chiy")
                        tab = pd.crosstab(df_[c1], df_[c2])
                        chi2, p, dof, exp = chi2_contingency(tab)
                        st.write(f"Chi2={chi2:.4f}, p={p:.4f}, dof={dof}")
                        if p > 0.05:
                            st.success("Likely independent (fail to reject H0).")
                        else:
                            st.error("Not independent (reject H0).")

    ###############################################################################
    # TAB 4: TIME SERIES
    ###############################################################################
    with tab4:
        st.subheader("Time Series Analysis")

        if st.session_state["filtered_data"] is None or st.session_state["filtered_data"].empty:
            st.info("No data after filtering.")
        else:
            df_ = st.session_state["filtered_data"].copy()
            col_list = df_.columns.tolist()
            date_col = st.selectbox("Select Date Column:", ["None"]+col_list, key="ts_date_sel")

            if date_col != "None":
                df_[date_col] = pd.to_datetime(df_[date_col], errors='coerce')
                df_ = df_.dropna(subset=[date_col])
                if df_.empty:
                    st.warning("No valid dates found in selected column.")
                else:
                    if numeric_cols:
                        ts_ycol = st.selectbox("Numeric Column for Time Series:", ["None"]+numeric_cols, key="ts_ycol_sel")
                    else:
                        ts_ycol = "None"

                    if ts_ycol != "None":
                        df_ts = df_.dropna(subset=[date_col, ts_ycol]).copy()
                        if not df_ts.empty:
                            min_d = df_ts[date_col].min().date()
                            max_d = df_ts[date_col].max().date()

                            if "ts_start_date" not in st.session_state:
                                st.session_state["ts_start_date"] = min_d
                            if "ts_end_date" not in st.session_state:
                                st.session_state["ts_end_date"] = max_d

                            clamp_date("ts_start_date", min_d, max_d)
                            clamp_date("ts_end_date", min_d, max_d)

                            c1, c2 = st.columns(2)
                            with c1:
                                s_date = st.date_input("Start Date",
                                                    value=st.session_state["ts_start_date"],
                                                    min_value=min_d,
                                                    max_value=max_d,
                                                    key="ts_sdate_input")
                            with c2:
                                e_date = st.date_input("End Date",
                                                    value=st.session_state["ts_end_date"],
                                                    min_value=min_d,
                                                    max_value=max_d,
                                                    key="ts_edate_input")

                            st.session_state["ts_start_date"] = s_date
                            st.session_state["ts_end_date"] = e_date

                            df_ts = df_ts[(df_ts[date_col]>=pd.to_datetime(s_date)) & (df_ts[date_col]<=pd.to_datetime(e_date))]
                            if df_ts.empty:
                                st.warning("No data in that date range.")
                            else:
                                freq_map = {"Day":"D","Week":"W","Month":"M","Quarter":"Q","Year":"Y"}
                                freq_sel = st.selectbox("Resample Frequency:", list(freq_map.keys()), key="ts_freq_sel")
                                agg_sel = st.selectbox("Aggregation:", ["sum","mean","count","min","max"], key="ts_agg_sel")

                                df_ts.set_index(date_col, inplace=True)
                                if agg_sel == "sum":
                                    ts_data = df_ts[ts_ycol].resample(freq_map[freq_sel]).sum()
                                elif agg_sel == "mean":
                                    ts_data = df_ts[ts_ycol].resample(freq_map[freq_sel]).mean()
                                elif agg_sel == "count":
                                    ts_data = df_ts[ts_ycol].resample(freq_map[freq_sel]).count()
                                elif agg_sel == "min":
                                    ts_data = df_ts[ts_ycol].resample(freq_map[freq_sel]).min()
                                else:
                                    ts_data = df_ts[ts_ycol].resample(freq_map[freq_sel]).max()

                                ts_data.dropna(inplace=True)
                                if ts_data.empty:
                                    st.warning("No data after resampling.")
                                else:
                                    fig_ts = px.line(ts_data, x=ts_data.index, y=ts_data.values,
                                                    title=f"{ts_ycol} by {freq_sel} ({agg_sel})", markers=True)
                                    fig_ts.update_layout(xaxis_title="Date", yaxis_title=ts_ycol)
                                    safe_plotly_chart(fig_ts, name="time_series_line")

                                    user_comment_ts = st.text_input("Comment on Time Series Chart:", key="ts_comment")
                                    if st.button("Save Time Series to Report", key="ts_save_report"):
                                        st.session_state["report_items"].append({
                                            "type": "figure",
                                            "title": f"Time Series: {ts_ycol}",
                                            "figure": fig_ts,
                                            "comment": user_comment_ts
                                        })
                                        st.success("Chart saved to Report tab.")

                                    show_ma = st.checkbox("Show Moving Average", key="ts_ma_show")
                                    if show_ma:
                                        window_ma = st.slider("MA window",2,20,3, key="ts_ma_window")
                                        ma_vals = ts_data.rolling(window=window_ma).mean()
                                        fig_ts.add_scatter(x=ma_vals.index, y=ma_vals.values, mode='lines',
                                                        name=f"{window_ma}-MA", line=dict(color='red'))
                                        safe_plotly_chart(fig_ts, name="time_series_line_ma")

                                    do_decomp = st.checkbox("Seasonal Decomposition", key="ts_decomp_check")
                                    if do_decomp:
                                        period_guess = {"Day":7,"Week":4,"Month":12,"Quarter":4,"Year":1}.get(freq_sel,7)
                                        try:
                                            decomp = seasonal_decompose(ts_data, period=period_guess, model="additive")
                                            fig_dec = make_subplots(rows=4, cols=1, shared_xaxes=True,
                                                                    subplot_titles=["Observed","Trend","Seasonal","Residual"])
                                            fig_dec.add_trace(
                                                go.Scatter(x=decomp.observed.index, y=decomp.observed.values, name="Observed"),
                                                row=1,col=1
                                            )
                                            fig_dec.add_trace(
                                                go.Scatter(x=decomp.trend.index, y=decomp.trend.values, name="Trend"),
                                                row=2,col=1
                                            )
                                            fig_dec.add_trace(
                                                go.Scatter(x=decomp.seasonal.index, y=decomp.seasonal.values, name="Seasonal"),
                                                row=3,col=1
                                            )
                                            fig_dec.add_trace(
                                                go.Scatter(x=decomp.resid.index, y=decomp.resid.values, name="Residual"),
                                                row=4,col=1
                                            )
                                            fig_dec.update_layout(height=800, title="Seasonal Decomposition")
                                            safe_plotly_chart(fig_dec, name="time_series_decomp")
                                        except Exception as ex:
                                            st.error(f"Decomposition failed: {ex}")
                        else:
                            st.warning("No valid numeric data for time series.")
            else:
                st.info("Select a valid date column.")

    ###############################################################################
    # TAB 5: CLUSTERING & FEATURE IMPORTANCE
    ###############################################################################
    with tab5:
        st.subheader("Clustering & Feature Importance")

        if st.session_state["filtered_data"] is None or st.session_state["filtered_data"].empty:
            st.info("No data after filtering.")
        else:
            df_ = st.session_state["filtered_data"]

            # Clustering
            st.markdown("### K-Means Clustering")
            if len(numeric_cols)<2:
                st.warning("Need >=2 numeric columns for clustering.")
            else:
                cluster_feats = st.multiselect("Select features for clustering:", numeric_cols, default=numeric_cols[:2], key="clust_feats")
                num_k = st.slider("Number of clusters (k):",2,10,3, key="clust_k")
                if cluster_feats:
                    cdf = df_[cluster_feats].dropna().copy()
                    scl = StandardScaler()
                    scaled_data = scl.fit_transform(cdf)
                    kmeans = KMeans(n_clusters=num_k, random_state=42, n_init=10)
                    labels = kmeans.fit_predict(scaled_data)
                    cdf["Cluster"] = labels
                    st.write("Cluster Counts:")
                    st.write(cdf["Cluster"].value_counts())

                    if len(cluster_feats)==2:
                        fig_k2 = px.scatter(cdf, x=cluster_feats[0], y=cluster_feats[1], color="Cluster",
                                            title="K-Means Clusters (2D)")
                        centers = kmeans.cluster_centers_
                        unscaled = scl.inverse_transform(centers)
                        for i, point in enumerate(unscaled):
                            fig_k2.add_scatter(
                                x=[point[0]], y=[point[1]],
                                mode='markers',
                                marker=dict(color='black', size=12, symbol='x'),
                                name=f"Centroid {i}"
                            )
                        safe_plotly_chart(fig_k2, name="cluster_2d")
                        comment_2d = st.text_input("Comment on 2D cluster chart:", key="cluster_2d_comment")
                        if st.button("Save 2D Clusters to Report", key="cluster_2d_save"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": "K-Means Clusters (2D)",
                                "figure": fig_k2,
                                "comment": comment_2d
                            })
                            st.success("Chart saved to Report tab.")
                    elif len(cluster_feats)==3:
                        fig_k3 = px.scatter_3d(cdf, x=cluster_feats[0], y=cluster_feats[1], z=cluster_feats[2],
                                            color="Cluster", title="K-Means Clusters (3D)")
                        safe_plotly_chart(fig_k3, name="cluster_3d")
                        comment_3d = st.text_input("Comment on 3D cluster chart:", key="cluster_3d_comment")
                        if st.button("Save 3D Clusters to Report", key="cluster_3d_save"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": "K-Means Clusters (3D)",
                                "figure": fig_k3,
                                "comment": comment_3d
                            })
                            st.success("Chart saved to Report tab.")
                    else:
                        fig_par = px.parallel_coordinates(cdf, color="Cluster",
                                                        title="K-Means (Parallel Coordinates)")
                        safe_plotly_chart(fig_par, name="cluster_parallel")
                        comment_pc = st.text_input("Comment on parallel coordinates:", key="cluster_pc_comment")
                        if st.button("Save Parallel Coordinates to Report", key="cluster_pc_save"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": "K-Means (Parallel Coordinates)",
                                "figure": fig_par,
                                "comment": comment_pc
                            })
                            st.success("Chart saved to Report tab.")

                    # Radar chart for cluster profiles
                    st.subheader("Radar Chart / Cluster Profiles")
                    prof = cdf.groupby("Cluster")[cluster_feats].mean()
                    fig_radar = go.Figure()
                    normed = prof.copy()
                    for col in cluster_feats:
                        minv=prof[col].min()
                        maxv=prof[col].max()
                        rng = maxv - minv if maxv != minv else 1
                        normed[col] = (prof[col] - minv)/rng

                    for cluster_id in normed.index:
                        fig_radar.add_trace(go.Scatterpolar(
                            r=normed.loc[cluster_id].values,
                            theta=cluster_feats,
                            fill='toself',
                            name=f'Cluster {cluster_id}'
                        ))
                    fig_radar.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0,1])),
                        title="Cluster Feature Comparison"
                    )
                    safe_plotly_chart(fig_radar, name="cluster_radar")
                    comment_radar = st.text_input("Comment on Radar Chart:", key="cluster_radar_comment")
                    if st.button("Save Radar Chart to Report", key="cluster_radar_save"):
                        st.session_state["report_items"].append({
                            "type": "figure",
                            "title": "K-Means Radar Chart",
                            "figure": fig_radar,
                            "comment": comment_radar
                        })
                        st.success("Chart saved to Report tab.")

            # Feature Importance
            st.markdown("### Feature Importance (RandomForest or XGBoost)")
            if len(numeric_cols)<2:
                st.warning("Need >=2 numeric columns for feature importance.")
            else:
                fi_target = st.selectbox("Select Target (numeric):", numeric_cols, key="fi_target")
                possible_feats = [c for c in numeric_cols if c != fi_target]
                fi_feats = st.multiselect("Select features:", possible_feats, default=possible_feats[:min(10,len(possible_feats))], key="fi_feats")

                model_choice = st.selectbox("Which model for feature importance?", ["RandomForest","XGBoost"] if xgboost_available else ["RandomForest"], key="fi_model_choice")

                if fi_feats:
                    dff = df_.dropna(subset=[fi_target])
                    X = dff[fi_feats].copy()
                    y = dff[fi_target].copy()
                    X = X.fillna(X.mean())
                    y = y.fillna(y.mean())

                    if model_choice == "XGBoost" and xgboost_available:
                        model = XGBRegressor(n_estimators=100, random_state=42)
                    else:
                        model = RandomForestRegressor(n_estimators=100, random_state=42)

                    model.fit(X, y)
                    if model_choice == "XGBoost" and xgboost_available:
                        importances = model.feature_importances_
                        title_fi = f"XGBoost Feature Importance for {fi_target}"
                    else:
                        importances = model.feature_importances_
                        title_fi = f"RandomForest FI for {fi_target}"

                    fi_df = pd.DataFrame({"feature":fi_feats,"importance":importances}).sort_values("importance",ascending=False)
                    fig_fi = px.bar(fi_df, x="importance", y="feature", orientation='h', title=title_fi)
                    safe_plotly_chart(fig_fi, name="rf_feature_importance")

                    comment_fi = st.text_input("Comment on Feature Importance:", key="fi_save_comment")
                    if st.button("Save Feature Importance to Report", key="fi_save"):
                        st.session_state["report_items"].append({
                            "type": "figure",
                            "title": title_fi,
                            "figure": fig_fi,
                            "comment": comment_fi
                        })
                        st.success("Chart saved to Report tab.")

                    st.subheader("Partial Dependence Plots (Top 3 features)")
                    top_3 = fi_df.head(min(3,len(fi_df)))["feature"].tolist()
                    for feat in top_3:
                        feat_range = np.linspace(X[feat].min(), X[feat].max(), 100)
                        pd_df = pd.DataFrame({feat: feat_range})
                        for other_feat in fi_feats:
                            if other_feat != feat:
                                pd_df[other_feat] = X[other_feat].mean()
                        preds = model.predict(pd_df[fi_feats])
                        fig_pd = px.line(x=feat_range, y=preds,
                                        title=f"Partial Dependence: {feat}",
                                        labels={"x":feat,"y":fi_target})
                        safe_plotly_chart(fig_pd, name=f"fi_pd_{feat}")
                        comment_pd = st.text_input(f"Comment on PD Plot for {feat}:", key=f"fi_pd_save_{feat}")
                        if st.button(f"Save PD Plot for {feat}", key=f"fi_pd_btn_{feat}"):
                            st.session_state["report_items"].append({
                                "type": "figure",
                                "title": f"Partial Dependence: {feat}",
                                "figure": fig_pd,
                                "comment": comment_pd
                            })
                            st.success("PD chart saved to Report tab.")

    ###############################################################################
    # TAB 6: DOWNLOAD
    ###############################################################################
    with tab6:
        st.subheader("Download/Export")

        if st.session_state["filtered_data"] is None or st.session_state["filtered_data"].empty:
            st.info("No data to download.")
        else:
            df_ = st.session_state["filtered_data"]
            if st.button("Download as CSV", key="dl_csv"):
                csv_data = df_.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Confirm CSV Download",
                    data=csv_data,
                    file_name="processed_data.csv",
                    mime="text/csv"
                )

            if st.button("Download as Excel", key="dl_excel"):
                xlsx_data = export_to_excel(df_)
                st.download_button(
                    label="Confirm Excel Download",
                    data=xlsx_data,
                    file_name="processed_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    ###############################################################################
    # TAB 7: REPORT
    ###############################################################################
    with tab7:
        st.subheader("Final Report")

        # Option to add external image
        st.markdown("### Add External Image to Report")
        uploaded_image = st.file_uploader("Upload an image (PNG, JPG, etc.)", type=["png","jpg","jpeg"], key="report_image_upload")
        if uploaded_image is not None:
            img_title = st.text_input("Image Title:", key="report_image_title")
            img_comment = st.text_input("Comment on this image:", key="report_image_comment")
            if st.button("Save Image to Report", key="report_image_save"):
                # convert image to bytes
                image_bytes = uploaded_image.read()
                st.session_state["report_items"].append({
                    "type": "image",
                    "title": img_title or "External Image",
                    "figure": None,  # not used for images
                    "image_bytes": image_bytes,
                    "comment": img_comment
                })
                st.success("Image saved to Report.")

        st.write("---")

        # Show the final report items
        if not st.session_state["report_items"]:
            st.info("No items have been saved to the report yet.")
        else:
            for i, item in enumerate(st.session_state["report_items"], 1):
                the_type = item["type"]
                the_title = item["title"]
                the_comment = item["comment"] or ""
                st.write(f"### {i}. {the_title}")
                if the_type == "figure":
                    # It's a Plotly figure
                    safe_plotly_chart(item["figure"], name=f"report_fig_{i}")
                elif the_type == "image":
                    # It's an external image
                    st.image(item["image_bytes"], use_column_width=True)
                elif the_type == "table":
                    # (Optional) handle table if you want
                    pass

                if the_comment.strip():
                    st.write(f"**Comment:** {the_comment}")

    ###############################################################################
    # FOOTER
    ###############################################################################
    st.write("---")
    st.write("© 2025 MEGA EDA & ML Suite – All-in-One Analysis Tool")
     
 # Add a "Return to Home" button below the footer
    if st.button("Return to Home"):
        # Option A: if you have go_home() function
        go_home()  



def modeling_suite_page():


    import streamlit as st
    # st.set_page_config(layout="wide", page_title="Advanced Regression Analysis Tool")

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import plotly.graph_objects as go
    from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, LabelEncoder, OneHotEncoder
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.linear_model import LogisticRegression, LinearRegression
    from sklearn.svm import SVC, SVR
    from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
    from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree
    from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix,
                                mean_squared_error, r2_score, classification_report, roc_curve, auc, mean_absolute_error)
    from sklearn.feature_selection import SelectKBest, chi2, f_classif
    from sklearn.decomposition import PCA
    from scipy import stats
    import io, base64, time, pickle, os

    # ---------------------------------------------------
    # Custom Constrained Ridge Regression
    # ---------------------------------------------------
    from sklearn.base import BaseEstimator, RegressorMixin

    class ConstrainedRidge(BaseEstimator, RegressorMixin):
        """
        A custom ridge regression that enforces sign constraints on selected coefficients.
        Constraints: dict { feature_index: 'positive'/'negative' }.
        Minimizes MSE + alpha * ||w||^2 using a simple gradient descent approach.
        """
        def __init__(self, alpha=1.0, learning_rate=0.001, max_iter=5000,
                    constraints=None, random_state=42, tol=1e-6):
            self.alpha = alpha
            self.learning_rate = learning_rate
            self.max_iter = max_iter
            self.constraints = constraints if constraints else {}
            self.random_state = random_state
            self.tol = tol
            
        def fit(self, X, y):
            np.random.seed(self.random_state)
            X = np.array(X)
            y = np.array(y)
            n, d = X.shape
            self.coef_ = np.zeros(d)
            self.intercept_ = 0.0
            prev_loss = float('inf')
            for iteration in range(self.max_iter):
                y_pred = self.predict(X)
                error = y_pred - y
                mse = np.mean(error**2)
                l2_reg = self.alpha * np.sum(self.coef_**2)
                current_loss = mse + l2_reg
                if abs(prev_loss - current_loss) < self.tol:
                    break
                prev_loss = current_loss
                grad_w = (2/n)*X.T.dot(error) + 2*self.alpha*self.coef_
                grad_b = (2/n)*np.sum(error)
                lr = self.learning_rate / np.sqrt(iteration + 1) if iteration > 100 else self.learning_rate
                self.coef_ -= lr * grad_w
                self.intercept_ -= lr * grad_b
                for idx, sign_req in self.constraints.items():
                    if sign_req == "positive" and self.coef_[idx] < 0:
                        self.coef_[idx] = 0.0001
                    elif sign_req == "negative" and self.coef_[idx] > 0:
                        self.coef_[idx] = -0.0001
            self.n_iter_ = iteration + 1
            return self

        def predict(self, X):
            return np.array(X).dot(self.coef_) + self.intercept_

    # ---------------------------------------------------
    # Utility: Restore Original Coefficients
    # ---------------------------------------------------
    def restore_original_coeffs_intercept(model, scaler, scaled_columns, original_feature_names):
        """
        Given a fitted linear model that was trained on scaled data,
        restore the coefficients and intercept to the original scale.
        This function assumes that the scaler has attributes scale_ and mean_.
        Restoration is performed only for those features that were scaled.
        """
        if not hasattr(model, "coef_"):
            return None, None
        w_scaled = model.coef_
        b_scaled = model.intercept_
        if scaler is None or scaled_columns is None:
            return w_scaled, b_scaled
        if hasattr(scaler, "scale_") and hasattr(scaler, "mean_"):
            scales = scaler.scale_
            means = scaler.mean_
            w_original = np.copy(w_scaled)
            b_original = b_scaled
            for i, feat in enumerate(original_feature_names):
                if feat in scaled_columns:
                    idx = scaled_columns.index(feat)
                    w_original[i] = w_scaled[i] / scales[idx]
                    b_original -= (w_scaled[i] * means[idx] / scales[idx])
            return w_original, b_original
        else:
            return w_scaled, b_scaled

    # ---------------------------------------------------
    # Utility: Mean Absolute Percentage Error (MAPE)
    # ---------------------------------------------------
    def mean_absolute_percentage_error(y_true, y_pred):
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        mask = y_true != 0
        if not np.any(mask):
            return np.nan
        return np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100

    # ---------------------------------------------------
    # Outlier Functions
    # ---------------------------------------------------
    def remove_outliers_zscore(data, threshold, columns=None):
        if columns is None:
            columns = data.select_dtypes(include=['number']).columns
        original_shape = data.shape[0]
        outlier_info = {}
        df_clean = data.copy()
        for col in columns:
            if col in df_clean.columns:
                # Calculate z-scores on non-null values
                z_scores = np.abs(stats.zscore(df_clean[col].dropna()))
                # Create mask for rows with valid z-scores
                mask = np.abs(stats.zscore(df_clean[col].dropna())) <= threshold
                # Record outliers for reporting
                outliers = df_clean[col].dropna()[~mask]
                outlier_info[col] = {
                    'count': len(outliers),
                    'values': outliers.tolist() if len(outliers) <= 10 else outliers.tolist()[:10] + ['...more...']
                }
                # Remove outliers (retain rows that are NaN or where z-score <= threshold)
                df_clean = df_clean[(np.abs(stats.zscore(df_clean[col].dropna())) <= threshold) | df_clean[col].isna()]
        rows_removed = original_shape - df_clean.shape[0]
        return df_clean, outlier_info, rows_removed

    def remove_outliers_iqr(data, multiplier, columns=None):
        if columns is None:
            columns = data.select_dtypes(include=['number']).columns
        original_shape = data.shape[0]
        outlier_info = {}
        df_clean = data.copy()
        for col in columns:
            if col in df_clean.columns:
                Q1 = df_clean[col].quantile(0.25)
                Q3 = df_clean[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - multiplier * IQR
                upper_bound = Q3 + multiplier * IQR
                outliers = df_clean[col][(df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)]
                outlier_info[col] = {
                    'count': len(outliers),
                    'values': outliers.tolist() if len(outliers) <= 10 else outliers.tolist()[:10] + ['...more...'],
                    'bounds': f"Lower: {lower_bound:.2f}, Upper: {upper_bound:.2f}"
                }
                df_clean = df_clean[~((df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)) | df_clean[col].isna()]
        rows_removed = original_shape - df_clean.shape[0]
        return df_clean, outlier_info, rows_removed

    # ---------------------------------------------------
    # Multicollinearity Analysis Function
    # ---------------------------------------------------
    def plot_multicollinearity(df, threshold=0.8):
        numeric_cols = df.select_dtypes(include=np.number).columns
        if len(numeric_cols) < 2:
            st.write("Not enough numeric features for multicollinearity analysis.")
            return
        corr_matrix = df[numeric_cols].corr().abs()
        # Mask to show only correlations above the threshold (excluding 1.0)
        high_corr = corr_matrix.where((corr_matrix >= threshold) & (corr_matrix < 1))
        fig = px.imshow(high_corr, text_auto=True, color_continuous_scale='Reds', title=f'Multicollinearity (|corr| ≥ {threshold})')
        st.plotly_chart(fig)

    # ---------------------------------------------------
    # Data Profiling Function (Modified)
    # ---------------------------------------------------
    def data_profiling(df):
        st.markdown("### Data Summary")
        st.write(df.describe().T)
        st.markdown("### Unique Values per Column")
        unique_df = pd.DataFrame({
            "Column": df.columns,
            "Unique Values": [", ".join(map(str, df[col].unique())) for col in df.columns]
        })
        st.dataframe(unique_df)
        st.markdown("### Correlation Heatmap (Numeric Columns)")
        numeric_cols = df.select_dtypes(include=np.number).columns
        if len(numeric_cols) > 1:
            corr = df[numeric_cols].corr()
            fig = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', zmin=-1, zmax=1)
            st.plotly_chart(fig)
        else:
            st.write("Not enough numeric columns for correlation analysis.")

    # ---------------------------------------------------
    # Feature Selection Functions
    # ---------------------------------------------------
    def correlation_feature_selection(df, target_col, threshold=0.1):
        numeric_features = df.select_dtypes(include=np.number).columns.drop(target_col, errors='ignore')
        corr_series = df[numeric_features].corrwith(df[target_col]).abs()
        selected = corr_series[corr_series >= threshold].index.tolist()
        return selected, corr_series.sort_values(ascending=False)

    def selectkbest_feature_selection(df, target_col, k=5):
        from sklearn.feature_selection import SelectKBest, f_regression, f_classif
        numeric_features = df.select_dtypes(include=np.number).columns.drop(target_col, errors='ignore')
        X = df[numeric_features]
        y = df[target_col]
        scoring = f_regression if np.issubdtype(y.dtype, np.number) else f_classif
        selector = SelectKBest(scoring, k=min(k, X.shape[1]))
        selector.fit(X, y)
        mask = selector.get_support()
        selected = X.columns[mask].tolist()
        scores = selector.scores_
        score_df = pd.DataFrame({"Feature": X.columns, "Score": scores}).sort_values("Score", ascending=False)
        return selected, score_df

    # ---------------------------------------------------
    # Custom CSS for Styling (as provided)
    # ---------------------------------------------------
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #4682B4;
            text-align: center;
            margin-bottom: 30px;
        }
        .section-header {
            color: #4682B4;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: #f8f9fa;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .card-text {
            color: #555;
            margin-bottom: 15px;
        }
        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
            color: #4682B4;
        }
        .success-box {
            padding: 10px;
            background-color: #d4edda;
            border-color: #c3e6cb;
            color: #155724;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .warning-box {
            padding: 10px;
            background-color: #fff3cd;
            border-color: #ffeeba;
            color: #856404;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .info-box {
            padding: 10px;
            background-color: #d1ecf1;
            border-color: #bee5eb;
            color: #0c5460;
            border-radius: 5px;
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # Session State Initialization
    # ---------------------------------------------------
    if 'progress' not in st.session_state:
        st.session_state.progress = {
            'data_uploaded': False,
            'data_processed': False,
            'features_engineered': False,
            'model_built': False,
            'model_evaluated': False
        }
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'data' not in st.session_state:
        st.session_state.data = None
        st.session_state.X = None
        st.session_state.y = None
        st.session_state.X_train = None
        st.session_state.X_test = None
        st.session_state.y_train = None
        st.session_state.y_test = None
        st.session_state.model = None
        st.session_state.predictions = None
        st.session_state.target_column = None
        st.session_state.feature_columns = None
        st.session_state.numeric_columns = None
        st.session_state.categorical_columns = None
        st.session_state.transformations_applied = []
        st.session_state.outliers_removed = False
        st.session_state.removed_outliers_info = None
        st.session_state.feature_importance = None
        st.session_state.model_type = None
        st.session_state.problem_type = None
        st.session_state.metrics = {}
        st.session_state.tree_fig = None
        st.session_state.scaler = None
        st.session_state.scaled_columns = None

    # ---------------------------------------------------
    # Utility Functions and Navigation Helpers
    # ---------------------------------------------------
    def create_tree_visualization(model, feature_names, class_names=None):
        try:
            fig = plt.figure(figsize=(20, 10))
            if hasattr(model, 'estimators_'):
                tree_to_plot = model.estimators_[0]
            else:
                tree_to_plot = model
            plot_tree(tree_to_plot, feature_names=feature_names, class_names=class_names,
                    filled=True, rounded=True, proportion=True)
            plt.tight_layout()
            return fig
        except Exception as e:
            st.error(f"Error creating tree visualization: {str(e)}")
            return None

    def create_card(title, description, icon, button_text, button_key, disabled=False):
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">{icon}</div>
            <div class="card-title">{title}</div>
            <div class="card-text">{description}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(button_text, key=button_key, disabled=disabled):
            return True
        return False

    def show_progress_bar():
        steps = ['data_uploaded', 'data_processed', 'features_engineered', 'model_built', 'model_evaluated']
        step_names = ['Data Upload', 'Data Processing', 'Feature Engineering', 'Model Building', 'Evaluation']
        completed = sum(st.session_state.progress[step] for step in steps)
        progress_percentage = int((completed / len(steps)) * 100)
        st.markdown(f"""
        <div style="width:100%; background-color:#f1f1f1; border-radius:5px; margin-bottom:20px;">
            <div style="width:{progress_percentage}%; height:10px; background-color:#4682B4; border-radius:5px;"></div>
        </div>
        """, unsafe_allow_html=True)
        cols = st.columns(len(steps))
        for i, (col, step, name) in enumerate(zip(cols, steps, step_names)):
            with col:
                if st.session_state.progress[step]:
                    st.markdown(f'<div style="color:#28a745; font-weight:bold;">✓ {name}</div>', unsafe_allow_html=True)
                elif i == completed:
                    st.markdown(f'<div style="color:#4682B4; font-weight:bold;">→ {name}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="color:#999;">{name}</div>', unsafe_allow_html=True)

    def download_link(object_to_download, download_filename, download_link_text):
        if isinstance(object_to_download, pd.DataFrame):
            object_to_download = object_to_download.to_csv(index=False)
        b64 = base64.b64encode(object_to_download.encode()).decode()
        return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

    # ---------------------------------------------------
    # Pages of the App
    # ---------------------------------------------------
    def home_page():
        st.markdown('<h1 class="main-header">Machine Learning Model Builder</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 1.2rem; margin-bottom: 30px;">Build machine learning models with ease - no coding required!</p>', unsafe_allow_html=True)
        if any(st.session_state.progress.values()):
            show_progress_bar()
        col1, col2 = st.columns(2)
        with col1:
            if create_card("Data Upload", "Upload your dataset and explore its characteristics", "📊", "Start Data Upload", "start_data_upload"):
                st.session_state.page = 'data_upload'
                st.rerun()
            if create_card("Feature Engineering", "Transform and create features to improve model performance", "🔧", "Start Feature Engineering", "start_feature_engineering", disabled=not st.session_state.progress['data_processed']):
                st.session_state.page = 'feature_engineering'
                st.rerun()
        with col2:
            if create_card("Data Processing", "Clean your data and prepare it for modeling", "🧹", "Start Data Processing", "start_data_processing", disabled=not st.session_state.progress['data_uploaded']):
                st.session_state.page = 'data_processing'
                st.rerun()
            if create_card("Model Building", "Train machine learning models on your processed data", "🤖", "Start Model Building", "start_model_building", disabled=not st.session_state.progress['features_engineered']):
                st.session_state.page = 'model_building'
                st.rerun()
        col1, col2 = st.columns(2)
        with col1:
            if create_card("Model Evaluation", "Evaluate your model's performance with detailed metrics", "📈", "Start Evaluation", "start_evaluation", disabled=not st.session_state.progress['model_built']):
                st.session_state.page = 'evaluation'
                st.rerun()
        with col2:
            if create_card("Export Results", "Export your model, predictions, and processed data", "💾", "Start Export", "start_export", disabled=not st.session_state.progress['model_evaluated']):
                st.session_state.page = 'export'
                st.rerun()
        st.markdown('<h2 class="section-header">Or try with an example dataset</h2>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Iris Dataset", key="iris_example"):
                from sklearn import datasets
                data = datasets.load_iris()
                df = pd.DataFrame(data.data, columns=data.feature_names)
                df['target'] = data.target
                st.session_state.data = df
                st.session_state.progress['data_uploaded'] = True
                st.success("Iris dataset loaded successfully!")
                time.sleep(1)
                st.session_state.page = 'data_upload'
                st.rerun()
        with col2:
            if st.button("Wine Dataset", key="wine_example"):
                from sklearn import datasets
                data = datasets.load_wine()
                df = pd.DataFrame(data.data, columns=data.feature_names)
                df['target'] = data.target
                st.session_state.data = df
                st.session_state.progress['data_uploaded'] = True
                st.success("Wine dataset loaded successfully!")
                time.sleep(1)
                st.session_state.page = 'data_upload'
                st.rerun()
        with col3:
            if st.button("Breast Cancer Dataset", key="cancer_example"):
                from sklearn import datasets
                data = datasets.load_breast_cancer()
                df = pd.DataFrame(data.data, columns=data.feature_names)
                df['target'] = data.target
                st.session_state.data = df
                st.session_state.progress['data_uploaded'] = True
                st.success("Breast Cancer dataset loaded successfully!")
                time.sleep(1)
                st.session_state.page = 'data_upload'
                st.rerun()

    def data_upload_page():
        st.markdown('<h1 class="main-header">Data Upload</h1>', unsafe_allow_html=True)
        show_progress_bar()
        if st.session_state.data is None:
            uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
            if uploaded_file is not None:
                try:
                    df = pd.read_csv(uploaded_file)
                    st.session_state.data = df
                    st.session_state.progress['data_uploaded'] = True
                    st.success("Dataset uploaded successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
        if st.session_state.data is not None:
            df = st.session_state.data
            st.markdown('<h2 class="section-header">Dataset Overview</h2>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Rows:** {df.shape[0]}")
                st.write(f"**Columns:** {df.shape[1]}")
                st.write("**Memory Usage:** {:.2f} MB".format(df.memory_usage(deep=True).sum() / 1024**2))
            with col2:
                st.write("**Column Types:**")
                dtypes = pd.DataFrame(df.dtypes.astype(str), columns=['Data Type'])
                st.dataframe(dtypes)
            st.markdown('<h3 class="section-header">Data Preview</h3>', unsafe_allow_html=True)
            st.dataframe(df.head())
            st.markdown('<h3 class="section-header">Missing Values</h3>', unsafe_allow_html=True)
            missing_data = pd.DataFrame(df.isnull().sum(), columns=['Missing Values'])
            missing_data['Percentage (%)'] = (df.isnull().sum() / len(df) * 100).round(2)
            missing_data = missing_data[missing_data['Missing Values'] > 0]
            if not missing_data.empty:
                st.dataframe(missing_data)
                fig = px.bar(missing_data, x=missing_data.index, y='Percentage (%)', title='Missing Values by Column')
                st.plotly_chart(fig)
            else:
                st.write("No missing values found in the dataset.")
            with st.expander("Data Profiling"):
                data_profiling(df)
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back to Home", key="data_upload_back"):
                    st.session_state.page = 'home'
                    st.rerun()
            with col2:
                if st.button("Proceed to Data Processing →", key="data_upload_next"):
                    st.session_state.page = 'data_processing'
                    st.rerun()

    def data_processing_page():
        st.markdown('<h1 class="main-header">Data Processing</h1>', unsafe_allow_html=True)
        show_progress_bar()
        if st.session_state.data is None:
            st.warning("Please upload data first!")
            return
        df = st.session_state.data.copy()
        st.markdown('<h2 class="section-header">Target Variable Selection</h2>', unsafe_allow_html=True)
        target_col = st.selectbox("Select your target variable", df.columns)
        st.session_state.target_column = target_col
        feature_cols = [col for col in df.columns if col != target_col]
        st.markdown('<h2 class="section-header">Feature Selection</h2>', unsafe_allow_html=True)
        technique = st.radio("Select feature selection technique:", ["Manual", "Correlation-based", "SelectKBest", "All features except target"])
        if technique == "Manual":
            selected_features = st.multiselect("Select features to include", feature_cols, default=feature_cols)
        elif technique == "Correlation-based":
            threshold_corr = st.slider("Minimum absolute correlation with target", 0.0, 1.0, 0.1, 0.05)
            selected_features, corr_scores = correlation_feature_selection(df, target_col, threshold_corr)
            st.write("Features selected by correlation:")
            st.dataframe(corr_scores.to_frame("Correlation"))
            with st.expander("Multicollinearity Analysis"):
                st.write("The heatmap below shows features that are highly correlated (|corr| ≥ 0.8) with each other.")
                plot_multicollinearity(df[selected_features], threshold=0.8)
        else:
            selected_features = feature_cols
            st.write("Using all features except the target.")
        st.markdown('<h2 class="section-header">Missing Values Handling</h2>', unsafe_allow_html=True)
        numeric_cols = df[selected_features].select_dtypes(include=np.number).columns.tolist()
        categorical_cols = df[selected_features].select_dtypes(exclude=np.number).columns.tolist()
        if df[selected_features].isnull().sum().sum() > 0:
            st.markdown('<div class="info-box">Missing values detected in selected features</div>', unsafe_allow_html=True)
            if len(numeric_cols) > 0:
                num_impute = st.selectbox("Numeric columns imputation method:", ["Mean", "Median", "Zero", "Drop rows"])
            if len(categorical_cols) > 0:
                cat_impute = st.selectbox("Categorical columns imputation method:", ["Mode", "Constant value", "Drop rows"])
                if cat_impute == "Constant value":
                    constant_val = st.text_input("Enter constant value for missing data", "MISSING")
        else:
            st.markdown('<div class="success-box">No missing values in selected features</div>', unsafe_allow_html=True)
        st.markdown('<h2 class="section-header">Outlier Detection</h2>', unsafe_allow_html=True)
        if len(numeric_cols) > 0:
            outlier_method = st.radio("Outlier detection method:", ["Z-Score", "IQR"])
            if outlier_method == "Z-Score":
                z_threshold = st.slider("Z-Score threshold", 2.0, 5.0, 3.0)
            else:
                iqr_multiplier = st.slider("IQR multiplier", 1.0, 3.0, 1.5)
        else:
            st.write("No numeric columns for outlier detection")
        if st.button("Process Data", key="process_data"):
            try:
                processed_df = df[selected_features + [target_col]].copy()
                for col in numeric_cols:
                    if processed_df[col].isnull().sum() > 0:
                        if num_impute == "Mean":
                            processed_df[col].fillna(processed_df[col].mean(), inplace=True)
                        elif num_impute == "Median":
                            processed_df[col].fillna(processed_df[col].median(), inplace=True)
                        elif num_impute == "Zero":
                            processed_df[col].fillna(0, inplace=True)
                        elif num_impute == "Drop rows":
                            processed_df.dropna(subset=[col], inplace=True)
                for col in categorical_cols:
                    if processed_df[col].isnull().sum() > 0:
                        if cat_impute == "Mode":
                            processed_df[col].fillna(processed_df[col].mode()[0], inplace=True)
                        elif cat_impute == "Constant value":
                            processed_df[col].fillna(constant_val, inplace=True)
                        elif cat_impute == "Drop rows":
                            processed_df.dropna(subset=[col], inplace=True)
                if len(numeric_cols) > 0:
                    if outlier_method == "Z-Score":
                        processed_df, outlier_info, rows_removed = remove_outliers_zscore(processed_df, z_threshold, numeric_cols)
                        st.session_state.removed_outliers_info = {"method": "Z-Score", "info": outlier_info, "rows_removed": rows_removed}
                    else:
                        processed_df, outlier_info, rows_removed = remove_outliers_iqr(processed_df, iqr_multiplier, numeric_cols)
                        st.session_state.removed_outliers_info = {"method": "IQR", "info": outlier_info, "rows_removed": rows_removed}
                    if rows_removed > 0:
                        st.session_state.outliers_removed = True
                        st.info(f"Removed {rows_removed} outlier rows from the dataset.")
                st.session_state.X = processed_df[selected_features]
                st.session_state.y = processed_df[target_col]
                st.session_state.numeric_columns = numeric_cols
                st.session_state.categorical_columns = categorical_cols
                st.session_state.feature_columns = selected_features
                st.session_state.progress['data_processed'] = True
                st.success("Data processing completed successfully!")
                st.write(f"Processed data shape: {processed_df.shape}")
            except Exception as e:
                st.error(f"Error processing data: {str(e)}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Data Upload", key="data_proc_back"):
                st.session_state.page = 'data_upload'
                st.rerun()
        with col2:
            if st.button("Proceed to Feature Engineering →", key="data_proc_next") and st.session_state.progress['data_processed']:
                st.session_state.page = 'feature_engineering'
                st.rerun()

    def feature_engineering_page():
        st.markdown('<h1 class="main-header">Feature Engineering</h1>', unsafe_allow_html=True)
        show_progress_bar()
        if not st.session_state.progress['data_processed']:
            st.warning("Please process data first!")
            if st.button("Go to Data Processing"):
                st.session_state.page = 'data_processing'
                st.rerun()
            return
        X = st.session_state.X.copy()
        numeric_cols = st.session_state.numeric_columns
        categorical_cols = st.session_state.categorical_columns
        st.markdown('<h2 class="section-header">Feature Transformations</h2>', unsafe_allow_html=True)
        with st.expander("Basic Numeric Transformations", expanded=True):
            st.markdown('<div class="info-box">Select columns for basic transformations</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                log_cols = st.multiselect("Log transform (log(x+1))", numeric_cols)
                sqrt_cols = st.multiselect("Square root transform", numeric_cols)
            with col2:
                square_cols = st.multiselect("Square transform", numeric_cols)
                abs_cols = st.multiselect("Absolute value transform", numeric_cols)
        with st.expander("Feature Scaling", expanded=True):
            st.markdown('<div class="info-box">Scale numeric features for better model performance</div>', unsafe_allow_html=True)
            scale_features = st.checkbox("Apply scaling to numeric features")
            if scale_features:
                scaling_method = st.selectbox("Select scaling method", ["StandardScaler (mean=0, std=1)", "MinMaxScaler (0-1 range)", "RobustScaler (robust to outliers)"])
                scale_cols = st.multiselect("Select columns to scale", numeric_cols, default=numeric_cols)
        if len(categorical_cols) > 0:
            with st.expander("Categorical Encoding", expanded=True):
                st.markdown('<div class="info-box">Convert categorical features to numeric format</div>', unsafe_allow_html=True)
                encoding_method = st.selectbox("Select encoding method", ["One-Hot Encoding", "Label Encoding"])
                encode_cols = st.multiselect("Select columns to encode", categorical_cols, default=categorical_cols)
        with st.expander("Advanced Feature Generation"):
            st.markdown('<div class="info-box">Create new features from existing ones</div>', unsafe_allow_html=True)
            create_interactions = st.checkbox("Create interaction features")
            if create_interactions and len(numeric_cols) >= 2:
                interaction_cols = st.multiselect("Select columns for interactions", numeric_cols, default=numeric_cols[:min(2, len(numeric_cols))])
            create_poly = st.checkbox("Create polynomial features")
            if create_poly and len(numeric_cols) > 0:
                poly_degree = st.slider("Polynomial degree", 2, 3, 2)
                poly_cols = st.multiselect("Select columns for polynomial features", numeric_cols, default=numeric_cols[:min(2, len(numeric_cols))])
        with st.expander("Custom Multiple Transformations"):
            st.markdown('<div class="info-box">Apply a custom transformation to selected columns</div>', unsafe_allow_html=True)
            trans_method = st.selectbox("Select transformation method", ["StandardScaler", "MinMaxScaler", "RobustScaler", "Log", "Sqrt", "Square", "Absolute"])
            trans_columns = st.multiselect("Select columns to apply", numeric_cols)
            if st.button("Apply Custom Transformation"):
                df_temp = st.session_state.X.copy()
                if trans_method == "StandardScaler":
                    scaler_custom = StandardScaler()
                    df_temp[trans_columns] = scaler_custom.fit_transform(df_temp[trans_columns])
                    transformation_desc = f"Applied StandardScaler to {trans_columns}"
                    st.session_state.scaler = scaler_custom
                    st.session_state.scaled_columns = trans_columns
                elif trans_method == "MinMaxScaler":
                    scaler_custom = MinMaxScaler()
                    df_temp[trans_columns] = scaler_custom.fit_transform(df_temp[trans_columns])
                    transformation_desc = f"Applied MinMaxScaler to {trans_columns}"
                    st.session_state.scaler = scaler_custom
                    st.session_state.scaled_columns = trans_columns
                elif trans_method == "RobustScaler":
                    scaler_custom = RobustScaler()
                    df_temp[trans_columns] = scaler_custom.fit_transform(df_temp[trans_columns])
                    transformation_desc = f"Applied RobustScaler to {trans_columns}"
                    st.session_state.scaler = scaler_custom
                    st.session_state.scaled_columns = trans_columns
                elif trans_method == "Log":
                    df_temp[trans_columns] = np.log1p(df_temp[trans_columns])
                    transformation_desc = f"Applied Log transform to {trans_columns}"
                elif trans_method == "Sqrt":
                    df_temp[trans_columns] = np.sqrt(np.abs(df_temp[trans_columns]))
                    transformation_desc = f"Applied Sqrt transform to {trans_columns}"
                elif trans_method == "Square":
                    df_temp[trans_columns] = df_temp[trans_columns] ** 2
                    transformation_desc = f"Applied Square transform to {trans_columns}"
                elif trans_method == "Absolute":
                    df_temp[trans_columns] = np.abs(df_temp[trans_columns])
                    transformation_desc = f"Applied Absolute transform to {trans_columns}"
                st.session_state.X = df_temp
                st.session_state.transformations_applied.append(transformation_desc)
                st.success(transformation_desc)
        if st.button("Apply Feature Engineering", key="apply_transformations"):
            try:
                transformations_applied = []
                X_transformed = st.session_state.X.copy()
                for col in log_cols:
                    X_transformed[f"log_{col}"] = np.log1p(X_transformed[col])
                    transformations_applied.append(f"Applied log transform to {col}")
                for col in sqrt_cols:
                    X_transformed[f"sqrt_{col}"] = np.sqrt(np.abs(X_transformed[col]))
                    transformations_applied.append(f"Applied sqrt transform to {col}")
                for col in square_cols:
                    X_transformed[f"square_{col}"] = X_transformed[col] ** 2
                    transformations_applied.append(f"Applied square transform to {col}")
                for col in abs_cols:
                    X_transformed[f"abs_{col}"] = np.abs(X_transformed[col])
                    transformations_applied.append(f"Applied absolute transform to {col}")
                if scale_features and scale_cols:
                    if scaling_method.startswith("StandardScaler"):
                        scaler = StandardScaler()
                        X_transformed[scale_cols] = scaler.fit_transform(X_transformed[scale_cols])
                    elif scaling_method.startswith("MinMaxScaler"):
                        scaler = MinMaxScaler()
                        X_transformed[scale_cols] = scaler.fit_transform(X_transformed[scale_cols])
                    else:
                        scaler = RobustScaler()
                        X_transformed[scale_cols] = scaler.fit_transform(X_transformed[scale_cols])
                    transformations_applied.append(f"Applied {scaling_method.split()[0]} to {len(scale_cols)} features")
                    st.session_state.scaler = scaler
                    st.session_state.scaled_columns = scale_cols
                if len(categorical_cols) > 0 and encode_cols:
                    if encoding_method == "One-Hot Encoding":
                        X_encoded = pd.get_dummies(X_transformed, columns=encode_cols)
                        X_transformed = X_encoded
                        transformations_applied.append(f"Applied one-hot encoding to {len(encode_cols)} features")
                    else:
                        encoders = {}
                        for col in encode_cols:
                            le = LabelEncoder()
                            X_transformed[col] = le.fit_transform(X_transformed[col].astype(str))
                            encoders[col] = le
                        transformations_applied.append(f"Applied label encoding to {len(encode_cols)} features")
                if create_interactions and len(interaction_cols) >= 2:
                    for i in range(len(interaction_cols)):
                        for j in range(i+1, len(interaction_cols)):
                            col1, col2 = interaction_cols[i], interaction_cols[j]
                            X_transformed[f"{col1}_x_{col2}"] = X_transformed[col1] * X_transformed[col2]
                    num_interactions = len(interaction_cols) * (len(interaction_cols) - 1) // 2
                    transformations_applied.append(f"Created {num_interactions} interaction features")
                if create_poly and poly_cols:
                    from sklearn.preprocessing import PolynomialFeatures
                    poly = PolynomialFeatures(degree=poly_degree, include_bias=False)
                    poly_features = poly.fit_transform(X_transformed[poly_cols])
                    feature_names = poly.get_feature_names_out(poly_cols)
                    orig_features_count = len(poly_cols)
                    poly_df = pd.DataFrame(poly_features[:, orig_features_count:], columns=feature_names[orig_features_count:], index=X_transformed.index)
                    X_transformed = pd.concat([X_transformed, poly_df], axis=1)
                    transformations_applied.append(f"Created {poly_df.shape[1]} polynomial features (degree {poly_degree})")
                st.session_state.X = X_transformed
                st.session_state.transformations_applied.extend(transformations_applied)
                st.session_state.progress['features_engineered'] = True
                st.success("Feature engineering completed successfully!")
                st.markdown('<h3 class="section-header">Transformation Summary</h3>', unsafe_allow_html=True)
                for transform in transformations_applied:
                    st.write(f"- {transform}")
                st.markdown('<h3 class="section-header">Transformed Dataset Preview</h3>', unsafe_allow_html=True)
                st.write(f"Original features: {st.session_state.X.shape[1] - len(transformations_applied)}, New features: {st.session_state.X.shape[1]}")
                st.dataframe(st.session_state.X.head())
            except Exception as e:
                st.error(f"Error during feature engineering: {str(e)}")
                import traceback
                st.text(traceback.format_exc())
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Data Processing", key="feat_eng_back"):
                st.session_state.page = 'data_processing'
                st.rerun()
        with col2:
            if st.button("Proceed to Model Building →", key="feat_eng_next") and st.session_state.progress['features_engineered']:
                st.session_state.page = 'model_building'
                st.rerun()

    def model_building_page():
        st.markdown('<h1 class="main-header">Model Building</h1>', unsafe_allow_html=True)
        show_progress_bar()
        if not st.session_state.progress['features_engineered']:
            st.warning("Please complete feature engineering first!")
            if st.button("Go to Feature Engineering"):
                st.session_state.page = 'feature_engineering'
                st.rerun()
            return
        X = st.session_state.X
        y = st.session_state.y
        if y.dtype == 'object' or len(y.unique()) <= 10:
            st.error("This section is for regression models only. Please ensure your target variable is numeric.")
            return
        problem_type = "Regression"
        st.session_state.problem_type = problem_type
        st.markdown('<h2 class="section-header">Model Selection</h2>', unsafe_allow_html=True)
        st.markdown('<div class="info-box">Regression Problem Detected</div>', unsafe_allow_html=True)
        reg_models = ["Random Forest", "Decision Tree", "Linear Regression", "Gradient Boosting",
                    "Support Vector Machine", "K-Nearest Neighbors", "Ridge Regression",
                    "Constrained Ridge Regression", "Bayesian Ridge Regression"]
        model_choice = st.selectbox("Select a model", reg_models)
        st.session_state.model_type = model_choice
        st.markdown('<h2 class="section-header">Model Configuration</h2>', unsafe_allow_html=True)
        random_state = st.number_input("Random seed", 0, 999, 42)
        if model_choice == "Random Forest":
            n_estimators = st.slider("Number of estimators", 10, 500, 100, 10)
            max_depth = st.slider("Maximum depth", 1, 30, 10)
            min_samples_split = st.slider("Minimum samples to split", 2, 20, 2)
            min_samples_leaf = st.slider("Minimum samples in leaf", 1, 20, 1)
        elif model_choice == "Decision Tree":
            max_depth = st.slider("Maximum depth", 1, 30, 10)
            min_samples_split = st.slider("Minimum samples to split", 2, 20, 2)
            min_samples_leaf = st.slider("Minimum samples in leaf", 1, 20, 1)
        elif model_choice == "Linear Regression":
            pass
        elif model_choice == "Gradient Boosting":
            n_estimators = st.slider("Number of estimators", 10, 500, 100, 10)
            max_depth = st.slider("Maximum depth", 1, 30, 10)
            learning_rate = st.slider("Learning rate", 0.01, 0.5, 0.1, 0.01)
            min_samples_split = st.slider("Minimum samples to split", 2, 20, 2)
            min_samples_leaf = st.slider("Minimum samples in leaf", 1, 20, 1)
        elif model_choice == "Support Vector Machine":
            C = st.slider("Regularization strength (C)", 0.1, 10.0, 1.0, 0.1)
            kernel = st.selectbox("Kernel", ["rbf", "linear", "poly", "sigmoid"])
            gamma = st.selectbox("Gamma", ["scale", "auto"]) if kernel in ["rbf", "poly", "sigmoid"] else None
        elif model_choice == "K-Nearest Neighbors":
            n_neighbors = st.slider("Number of neighbors", 1, 20, 5)
            weights = st.selectbox("Weight function", ["uniform", "distance"])
        elif model_choice == "Ridge Regression":
            alpha = st.slider("Alpha (regularization strength)", 0.01, 10.0, 1.0, 0.01)
        elif model_choice == "Constrained Ridge Regression":
            alpha = st.slider("Alpha (regularization strength)", 0.01, 10.0, 1.0, 0.01)
            learning_rate = st.slider("Learning Rate", 0.0001, 0.1, 0.001, 0.0001)
            max_iter = st.slider("Max Iterations", 1000, 10000, 5000, 500)
            st.write("Specify sign constraints for features (optional):")
            constraints = {}
            for i, feature in enumerate(st.session_state.feature_columns):
                constraint = st.selectbox(f"Constraint for {feature}", ["None", "Positive", "Negative"], key=f"constraint_{feature}")
                if constraint == "Positive":
                    constraints[i] = "positive"
                elif constraint == "Negative":
                    constraints[i] = "negative"
        elif model_choice == "Bayesian Ridge Regression":
            alpha_1 = st.slider("Alpha 1", 1e-7, 1e-5, 1e-6, 1e-7)
            alpha_2 = st.slider("Alpha 2", 1e-7, 1e-5, 1e-6, 1e-7)
            lambda_1 = st.slider("Lambda 1", 1e-7, 1e-5, 1e-6, 1e-7)
            lambda_2 = st.slider("Lambda 2", 1e-7, 1e-5, 1e-6, 1e-7)
        st.markdown('<h2 class="section-header">Train-Test Split</h2>', unsafe_allow_html=True)
        test_size = st.slider("Test size (%)", 10, 40, 20) / 100
        if st.button("Train Model", key="train_model_btn"):
            with st.spinner("Training model..."):
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
                if model_choice == "Random Forest":
                    from sklearn.ensemble import RandomForestRegressor
                    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth,
                                                min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                                                random_state=random_state)
                elif model_choice == "Decision Tree":
                    from sklearn.tree import DecisionTreeRegressor
                    model = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split,
                                                min_samples_leaf=min_samples_leaf, random_state=random_state)
                elif model_choice == "Linear Regression":
                    model = LinearRegression()
                elif model_choice == "Gradient Boosting":
                    from sklearn.ensemble import GradientBoostingRegressor
                    model = GradientBoostingRegressor(n_estimators=n_estimators, max_depth=max_depth,
                                                    learning_rate=learning_rate, min_samples_split=min_samples_split,
                                                    min_samples_leaf=min_samples_leaf, random_state=random_state)
                elif model_choice == "Support Vector Machine":
                    if kernel in ["rbf", "poly", "sigmoid"]:
                        model = SVR(C=C, kernel=kernel, gamma=gamma)
                    else:
                        model = SVR(C=C, kernel=kernel)
                elif model_choice == "K-Nearest Neighbors":
                    model = KNeighborsRegressor(n_neighbors=n_neighbors, weights=weights)
                elif model_choice == "Ridge Regression":
                    from sklearn.linear_model import Ridge
                    model = Ridge(alpha=alpha, random_state=random_state)
                elif model_choice == "Constrained Ridge Regression":
                    model = ConstrainedRidge(alpha=alpha, learning_rate=learning_rate, max_iter=max_iter,
                                            constraints=constraints, random_state=random_state)
                elif model_choice == "Bayesian Ridge Regression":
                    from sklearn.linear_model import BayesianRidge
                    model = BayesianRidge(alpha_1=alpha_1, alpha_2=alpha_2, lambda_1=lambda_1, lambda_2=lambda_2,
                                        random_state=random_state)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                st.session_state.model = model
                st.session_state.X_train = X_train
                st.session_state.X_test = X_test
                st.session_state.y_train = y_train
                st.session_state.y_test = y_test
                st.session_state.predictions = y_pred
                st.session_state.progress['model_built'] = True
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)
                rmse = np.sqrt(mse)
                mae = mean_absolute_error(y_test, y_pred)
                mape = mean_absolute_percentage_error(y_test, y_pred)
                st.metric("Mean Squared Error", f"{mse:.4f}")
                st.metric("R² Score", f"{r2:.4f}")
                st.metric("MAE", f"{mae:.4f}")
                st.metric("MAPE (%)", f"{mape:.2f}")
                st.session_state.metrics = {'mse': mse, 'r2': r2, 'rmse': rmse, 'mae': mae, 'mape': mape}
                if hasattr(model, "coef_"):
                    coef_names = list(st.session_state.X.columns)
                    if st.session_state.scaler is not None and st.session_state.scaled_columns is not None:
                        w_orig, b_orig = restore_original_coeffs_intercept(model, st.session_state.scaler,
                                                                        st.session_state.scaled_columns, coef_names)
                    else:
                        w_orig, b_orig = model.coef_, model.intercept_
                    coef_df = pd.DataFrame({
                        "Feature": coef_names,
                        "Coefficient": w_orig,
                        "Absolute Coefficient": np.abs(w_orig)
                    }).sort_values(by="Absolute Coefficient", ascending=False)
                    st.markdown("<h3 class='section-header'>Model Coefficients (Betas) and Equation</h3>", unsafe_allow_html=True)
                    st.dataframe(coef_df)
                    st.write(f"Intercept: {b_orig:.4f}")
                    eq_terms = []
                    for i, feat in enumerate(coef_names):
                        if i >= 5:
                            eq_terms.append("...")
                            break
                        eq_terms.append(f"({w_orig[i]:.4f})*{feat}")
                    equation = f"y = {b_orig:.4f} + " + " + ".join(eq_terms)
                    st.write("**Regression Equation:**")
                    st.code(equation)
                else:
                    st.write("Model does not provide coefficients.")
                st.success("Model training completed successfully!")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Feature Engineering", key="model_back"):
                st.session_state.page = 'feature_engineering'
                st.rerun()
        with col2:
            if st.button("Proceed to Evaluation →", key="model_next") and st.session_state.progress['model_built']:
                st.session_state.page = 'evaluation'
                st.rerun()

    def evaluation_page():
        st.markdown('<h1 class="main-header">Model Evaluation</h1>', unsafe_allow_html=True)
        show_progress_bar()
        if not st.session_state.progress['model_built']:
            st.warning("Please build a model first!")
            if st.button("Go to Model Building"):
                st.session_state.page = 'model_building'
                st.rerun()
            return
        problem_type = st.session_state.problem_type
        model = st.session_state.model
        X_test = st.session_state.X_test
        y_test = st.session_state.y_test
        y_pred = st.session_state.predictions
        st.markdown('<h2 class="section-header">Model Information</h2>', unsafe_allow_html=True)
        st.write(f"**Model Type:** {st.session_state.model_type}")
        st.write(f"**Problem Type:** {problem_type}")
        st.markdown('<h2 class="section-header">Regression Metrics</h2>', unsafe_allow_html=True)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mape = mean_absolute_percentage_error(y_test, y_pred)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Mean Squared Error (MSE)", f"{mse:.4f}")
            st.metric("Root Mean Squared Error (RMSE)", f"{rmse:.4f}")
            st.metric("MAE", f"{mae:.4f}")
        with col2:
            st.metric("R² Score", f"{r2:.4f}")
            st.metric("MAPE (%)", f"{mape:.2f}")
        st.markdown('<h3 class="section-header">Predictions vs Actual Values</h3>', unsafe_allow_html=True)
        fig = px.scatter(x=y_test, y=y_pred, labels=dict(x='Actual Values', y='Predicted Values'), title='Predicted vs Actual Values')
        min_val = min(min(y_test), min(y_pred))
        max_val = max(max(y_test), max(y_pred))
        fig.add_shape(type='line', line=dict(dash='dash', color='red'), x0=min_val, y0=min_val, x1=max_val, y1=max_val)
        st.plotly_chart(fig)
        st.markdown('<h3 class="section-header">Residuals Analysis</h3>', unsafe_allow_html=True)
        residuals = y_test - y_pred
        fig = px.scatter(x=y_pred, y=residuals, labels=dict(x='Predicted Values', y='Residuals'), title='Residuals vs Predicted Values')
        fig.add_hline(y=0, line_dash='dash', line_color='red')
        st.plotly_chart(fig)
        fig = px.histogram(residuals, title='Distribution of Residuals', labels=dict(x='Residuals', y='Count'))
        st.plotly_chart(fig)
        st.markdown('<h2 class="section-header">Cross-Validation</h2>', unsafe_allow_html=True)
        cv_folds = st.slider("Number of cross-validation folds", 2, 10, 5)
        if st.button("Perform Cross-Validation", key="perform_cv"):
            with st.spinner("Running cross-validation..."):
                scoring = 'r2'
                cv_scores = cross_val_score(model, pd.concat([st.session_state.X_train, st.session_state.X_test]),
                                            pd.concat([st.session_state.y_train, st.session_state.y_test]),
                                            cv=cv_folds, scoring=scoring)
                st.markdown('<h3 class="section-header">Cross-Validation Results</h3>', unsafe_allow_html=True)
                cv_df = pd.DataFrame({'Fold': range(1, cv_folds+1), 'Score': cv_scores})
                fig = px.bar(cv_df, x='Fold', y='Score', title=f'Cross-Validation Scores ({scoring})')
                fig.add_hline(y=cv_scores.mean(), line_dash='dash', line_color='red')
                st.plotly_chart(fig)
                st.write(f"**Mean {scoring}:** {cv_scores.mean():.4f}")
                st.write(f"**Standard Deviation:** {cv_scores.std():.4f}")
        st.session_state.progress['model_evaluated'] = True
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Model Building", key="eval_back"):
                st.session_state.page = 'model_building'
                st.rerun()
        with col2:
            if st.button("Proceed to Export →", key="eval_next"):
                st.session_state.page = 'export'
                st.rerun()

    def export_page():
        st.markdown('<h1 class="main-header">Export Results</h1>', unsafe_allow_html=True)
        show_progress_bar()
        if not st.session_state.progress['model_evaluated']:
            st.warning("Please evaluate your model first!")
            if st.button("Go to Evaluation"):
                st.session_state.page = 'evaluation'
                st.rerun()
            return
        st.markdown('<h2 class="section-header">Download Options</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
            Export your model, processed data, and results for future use.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<h3 class="section-header">Processed Data</h3>', unsafe_allow_html=True)
        if st.button("Export Processed Data", key="export_data_btn"):
            processed_data = pd.concat([st.session_state.X, st.session_state.y], axis=1)
            csv = processed_data.to_csv(index=False)
            st.download_button(label="Download CSV", data=csv, file_name="processed_data.csv", mime="text/csv")
        st.markdown('<h3 class="section-header">Predictions</h3>', unsafe_allow_html=True)
        if st.button("Export Predictions", key="export_pred_btn"):
            predictions_df = pd.DataFrame({'Actual': st.session_state.y_test, 'Predicted': st.session_state.predictions})
            csv = predictions_df.to_csv(index=False)
            st.download_button(label="Download Predictions", data=csv, file_name="predictions.csv", mime="text/csv")
        if st.session_state.tree_fig is not None:
            st.markdown('<h3 class="section-header">Tree Visualization</h3>', unsafe_allow_html=True)
            if st.button("Export Tree Visualization", key="export_tree_viz_btn"):
                buf = io.BytesIO()
                st.session_state.tree_fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
                buf.seek(0)
                st.download_button(label="Download Tree Visualization (PNG)", data=buf, file_name="decision_tree.png", mime="image/png")
        st.markdown('<h3 class="section-header">Trained Model</h3>', unsafe_allow_html=True)
        if st.button("Export Model (pickle format)", key="export_model_btn"):
            model_pickle = pickle.dumps(st.session_state.model)
            st.download_button(label="Download Model", data=model_pickle, file_name="trained_model.pkl", mime="application/octet-stream")
        st.markdown('<h3 class="section-header">Model Report</h3>', unsafe_allow_html=True)
        if st.button("Generate Model Report", key="export_report_btn"):
            problem_type = st.session_state.problem_type
            model_type = st.session_state.model_type
            report_content = f"""
            # Machine Learning Model Report

            ## Model Information
            - **Model Type**: {model_type}
            - **Problem Type**: {problem_type}
            - **Date Created**: {time.strftime("%Y-%m-%d %H:%M:%S")}

            ## Dataset Information
            - **Original Features**: {len(st.session_state.feature_columns)}
            - **Engineered Features**: {len(st.session_state.X.columns)}
            - **Total Samples**: {len(st.session_state.X)}
            - **Training Samples**: {len(st.session_state.X_train)}
            - **Testing Samples**: {len(st.session_state.X_test)}

            ## Feature Transformations Applied
            """
            for transform in st.session_state.transformations_applied:
                report_content += f"- {transform}\n"
            report_content += "\n## Model Performance\n"
            y_test = st.session_state.y_test
            y_pred = st.session_state.predictions
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            mape = mean_absolute_percentage_error(y_test, y_pred)
            report_content += f"- **Mean Squared Error (MSE)**: {mse:.4f}\n"
            report_content += f"- **R² Score**: {r2:.4f}\n"
            report_content += f"- **MAE**: {mae:.4f}\n"
            report_content += f"- **MAPE (%)**: {mape:.2f}\n"
            if hasattr(st.session_state.model, 'coef_'):
                report_content += "\n## Model Coefficients (Betas)\n"
                if st.session_state.scaler is not None and st.session_state.scaled_columns is not None:
                    w_orig, b_orig = restore_original_coeffs_intercept(st.session_state.model, st.session_state.scaler,
                                                                        st.session_state.scaled_columns, list(st.session_state.X.columns))
                else:
                    w_orig, b_orig = st.session_state.model.coef_, st.session_state.model.intercept_
                for feat, coef_val in zip(list(st.session_state.X.columns), w_orig):
                    report_content += f"- **{feat}**: {coef_val:.4f}\n"
                report_content += f"- **Intercept**: {b_orig:.4f}\n"
            st.download_button(label="Download Report", data=report_content, file_name="model_report.md", mime="text/markdown")
        st.markdown('<h3 class="section-header">Start New Project</h3>', unsafe_allow_html=True)
        if st.button("Start New Project", key="new_project_btn"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.page = 'home'
            st.rerun()
        if st.button("← Back to Evaluation", key="export_back"):
            st.session_state.page = 'evaluation'
            st.rerun()

    def main():
        pages = {
            'home': home_page,
            'data_upload': data_upload_page,
            'data_processing': data_processing_page,
            'feature_engineering': feature_engineering_page,
            'model_building': model_building_page,
            'evaluation': evaluation_page,
            'export': export_page
        }
        if st.session_state.page in pages:
            pages[st.session_state.page]()
        else:
            home_page()

    if __name__ == "__main__":
        main()


 # Add a "Return to Home" button below the footer
    if st.button("Return to Home"):
        # Option A: if you have go_home() function
        go_home() 
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

elif page == "myEDA":
    # <-- route to your big EDA function
    myEDA()
    
elif page == "modelingSuite":
    modeling_suite_page()

elif "_" in page:
    # Could be subpages like: section1_baseprice, section1_promodepth, ...
    # or the universal action pages: section2_action1, etc.
    if page == "section1_baseprice":
        base_price_estimator_page()
    elif page == "section1_promodepth":
        promo_depth_page()
    elif page == "section1_calendar":
        calendar_comparison_page()
        
    elif page == "section1_market_construct":
        market_construct_page()
        
    # --- NEW SUB-PAGES FOR SECTION 2 ---
    elif page == "section2_module1":
        section2_module1_page()
    elif page == "section2_module2":
        section2_module2_page()
    elif page == "section2_module3":
        section2_module3_page()
        
        
    elif page == "section3_module2":
        section3_module2_page()
    elif page == "section3_module4":
        section3_module4_page()
        

    elif page == "section4_feature_overview":
        Feature_Overview_page()
    elif page == "section4_transform":
        Transform_page()
    elif page == "section4_create":
        Create_page()
    elif page == "section4_select":
        Select_page()

    
    else:
        # fallback
        section_number, action_number = page.replace("section", "").split("_action")
        action_page(section_number, action_number)


# -------------------------------------------------------------------------
# Sidebar for File Uploads (the only one retained)
# -------------------------------------------------------------------------
st.sidebar.header("📂 File Management")

# Initialize session state for file uploads
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = {}

# File upload widget in sidebar
uploaded_files = st.sidebar.file_uploader(
    "Upload your CSV/Excel files:",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)

# Process and store uploaded files
if uploaded_files:
    for file in uploaded_files:
        if file.name not in st.session_state.uploaded_files:
            if file.name.endswith(".csv"):
                st.session_state.uploaded_files[file.name] = pd.read_csv(file)
            elif file.name.endswith(".xlsx"):
                st.session_state.uploaded_files[file.name] = pd.read_excel(file)

# Allow user to select a file to use
if st.session_state.uploaded_files:
    st.sidebar.subheader("Select a File for Analysis")
    selected_file = st.sidebar.selectbox(
        "Choose a file:",
        options=list(st.session_state.uploaded_files.keys()),
    )
    dataframe = st.session_state.uploaded_files[selected_file]
    st.sidebar.success(f"Using file: `{selected_file}`")

    # Also save the selected file's DataFrame to st.session_state["D0"]
    st.session_state["D0"] = dataframe

else:
    dataframe = None
    st.sidebar.warning("Please upload at least one file.")
