import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Akshit Sandeep Bane | Data Professional",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOBAL CUSTOM CSS (Professional Slate & Emerald Theme) ---
st.markdown("""
    <style>
    /* Professional Slate Background */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    
    /* Clean gradient for Name */
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #10B981 0%, #0EA5E9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1rem;
        display: inline-block;
    }
    .subtitle {
        font-size: 1.35rem;
        color: #94A3B8; 
        font-weight: 500;
        margin-bottom: 1.5rem;
        letter-spacing: 0.5px;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #F1F5F9; 
        margin-top: 2.5rem;
        margin-bottom: 1.2rem;
        position: relative;
        padding-bottom: 0.6rem;
        border-bottom: 2px solid #1E293B;
    }
    .section-header::after {
        content: "";
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 80px;
        height: 2px;
        background: #10B981;
    }
    
    .job-title {
        font-weight: bold;
        font-size: 1.35rem;
        color: #10B981;
    }
    
    .company-date {
        color: #64748B;
        font-weight: 500;
        text-align: right;
        line-height: 1.4;
    }
    
    /* Education Layout */
    .edu-container {
        margin-bottom: 1rem;
    }
    .edu-degree {
        font-size: 1.25rem;
        font-weight: 700;
        color: #F8FAFC;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.3;
    }
    .edu-uni {
        font-size: 1.05rem;
        color: #94A3B8;
        margin: 4px 0 0 0 !important;
        padding: 0 !important;
        line-height: 1.3;
    }
    .gpa-text {
        font-size: 0.95rem;
        color: #10B981;
        font-weight: 600;
        margin: 4px 0 0 0 !important;
        padding: 0 !important;
        line-height: 1.3;
    }
    
    /* Sidebar Links */
    .sidebar-link-container {
        margin-bottom: 12px;
        font-size: 1rem;
    }
    .sidebar-link-container a {
        color: #E2E8F0 !important;
        text-decoration: none !important;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .sidebar-link-container a:hover {
        color: #10B981 !important;
    }
    
    /* Skills Badges */
    .skill-category {
        font-size: 1.15rem;
        font-weight: 600;
        color: #F1F5F9;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .badge-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 1.5rem;
    }
    .skill-badge {
        background-color: #1E293B; 
        color: #E2E8F0; 
        padding: 10px 16px;
        border-radius: 4px; 
        font-size: 0.95rem;
        font-weight: 500;
        border-left: 4px solid #334155; 
        transition: all 0.2s ease;
    }
    .skill-badge:hover {
        background-color: #0F172A;
        border-left: 4px solid #10B981; 
        color: #FFFFFF;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    /* Project Badges */
    .proj-badge {
        background: #1E293B;
        color: #38BDF8;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid #38BDF8;
        margin-right: 8px;
        margin-bottom: 10px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CONTACT INFO ---
with st.sidebar:
    st.markdown("### 📍Frankfurt am Main, Germany")
    st.write("---")
    
    st.markdown("""
        <div class="sidebar-link-container">
            <span>🔗</span> <a href="https://www.linkedin.com/in/akshit-bane-944399215/" target="_blank">LinkedIn</a>
        </div>
        <div class="sidebar-link-container">
            <span>💻</span> <a href="https://github.com/Akshit-Bane" target="_blank">GitHub</a>
        </div>
        <div class="sidebar-link-container" style="margin-top: 15px;">
            <span>📧</span> <span style="font-weight:500; color:#E2E8F0;">Email:</span>
            <div style="color: #94A3B8; font-size: 0.95rem; margin-top: 4px;">akshitbane2001@gmail.com</div>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN HERO SECTION ---
st.markdown('<div class="main-title">Akshit Sandeep Bane</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Data Professional | Analytics & AI Enthusiast | Master’s Student</div>', unsafe_allow_html=True)

st.markdown("""
**Transforming raw datasets into intelligent, forward-looking insights.** I am a results-oriented data professional and Master’s student with two years of experience translating complex information into clear visualisations and strategic business outcomes. While my foundation is strongly rooted in Power BI, SQL, and robust pipeline engineering, I am currently eagerly learning and integrating Artificial Intelligence and Machine Learning into my analytical workflows. I thrive at the intersection of traditional data analytics, modern predictive AI tools, and real-world business impact.
""")

st.write("---")

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["📋 Experience & Background", "🛠️ Technical Skills", "💻 Portfolio Projects"])

# ==========================================
# TAB 1: EXPERIENCE & BACKGROUND
# ==========================================
with tab1:
    st.markdown('<div class="section-header">Professional Experience</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<span class="job-title">Software Specialist</span>', unsafe_allow_html=True)
        st.markdown("**eClinicalWorks**")
        st.markdown("""
        * **Advanced Analytics & Power BI:** Built and maintained dynamic Power BI dashboards to monitor service KPIs and billing performance. Conducted deep-dive analysis to provide account managers with real-time visibility, empowering them to act on anomalies and drive strategic business decision-making.
        * **Data Management & Quality:** Managed and validated contract-linked billing datasets for 200+ US medical practices, ensuring data quality and SLA compliance that directly supported client retention and revenue operations.
        * **Database Validation:** Conducted structured SQL-based data validation routines on patient safety and insurance datasets, achieving a 93% data accuracy rate.
        * **Process Optimisation:** Documented data flows, validation standards, and service processes to improve operational consistency and drastically reduce onboarding time across cross-functional teams.
        * **Governance & Security:** Coordinated access and role management within internal platforms, upholding data governance standards that ensured regulatory compliance and operational trust across the business.
        """)
    with col2:
        st.markdown('<div class="company-date">Mumbai, India<br>Jul 2022 – Aug 2024</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">Academic Background</div>', unsafe_allow_html=True)
    
    # Entry 1: Master's Degree
    edu1_col1, edu1_col2 = st.columns([3, 1])
    with edu1_col1:
        st.markdown("""
            <div class="edu-container">
                <p class="edu-degree">Master of Science in High Integrity Systems</p>
                <p class="edu-uni">Frankfurt University of Applied Sciences</p>
                <p style="color: #94A3B8; font-size: 0.95rem; margin-top: 4px;">Currently pursuing advanced studies to deepen expertise in data systems, analytics, and machine learning architectures.</p>
            </div>
        """, unsafe_allow_html=True)
    with edu1_col2:
        st.markdown('<div class="company-date">Frankfurt am Main, Germany<br>Present</div>', unsafe_allow_html=True)

    st.write("") # Small spacer

    # Entry 2: Bachelor's Degree
    edu2_col1, edu2_col2 = st.columns([3, 1])
    with edu2_col1:
        st.markdown("""
            <div class="edu-container">
                <p class="edu-degree">Bachelor of Science in Information Technology</p>
                <p class="edu-uni">University of Mumbai</p>
                <p class="gpa-text">Grade: 1.0 (German Scale equivalent)</p>
            </div>
        """, unsafe_allow_html=True)
    with edu2_col2:
        st.markdown('<div class="company-date">Mumbai, India<br>2019 – 2022</div>', unsafe_allow_html=True)

    # Entry 3: Languages
    st.markdown('<div class="section-header">Languages</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div class="skill-badge">🗣️ English (IELTS 7.0)</div>
            <div class="skill-badge">🗣️ German (A2.1, actively improving)</div>
        </div>
    """, unsafe_allow_html=True)


# ==========================================
# TAB 2: TECHNICAL SKILLS (4 Columns)
# ==========================================
with tab2:
    st.markdown('<div class="section-header">Core Competencies & Tech Stack</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Section 1: Analytics & Databases
    with col1:
        st.markdown('<div class="skill-category">📊 Analytics & DBs</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <div class="skill-badge">Power BI (DAX)</div>
                <div class="skill-badge">Tableau</div>
                <div class="skill-badge">SQL & MySQL</div>
                <div class="skill-badge">Snowflake</div>
                <div class="skill-badge">Excel (Power Query)</div>
                <div class="skill-badge">KPI Dashboards</div>
            </div>
        """, unsafe_allow_html=True)

    # Section 2: Python & Machine Learning
    with col2:
        st.markdown('<div class="skill-category">🧠 Python & ML</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <div class="skill-badge">Python (Pandas, NumPy)</div>
                <div class="skill-badge">Scikit-Learn</div>
                <div class="skill-badge">Random Forest & XGBoost</div>
                <div class="skill-badge">Data Validation</div>
                <div class="skill-badge">Anomaly Detection</div>
            </div>
        """, unsafe_allow_html=True)

    # Section 3: AI, Automation & Cloud Infra
    with col3:
        st.markdown('<div class="skill-category">☁️ AI & Cloud Infra</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <div class="skill-badge">Prompt Engineering</div>
                <div class="skill-badge">LLM Integration</div>
                <div class="skill-badge">AI-Assisted Automation</div>
                <div class="skill-badge">AWS / Cloud Infra</div>
                <div class="skill-badge">GCP (Google Cloud Platform)</div>
                <div class="skill-badge">Docker / Containers</div>
            </div>
        """, unsafe_allow_html=True)

    # Section 4: Tools & Workflows
    with col4:
        st.markdown('<div class="skill-category">🛠️ Tools & Workflows</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="badge-container">
                <div class="skill-badge">JIRA & Confluence</div>
                <div class="skill-badge">Git & GitHub</div>
                <div class="skill-badge">Agile Methodologies</div>
                <div class="skill-badge">IAM Concepts</div>
                <div class="skill-badge">Microsoft Suite</div>
                <div class="skill-badge">Process Optimisation</div>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 3: PROJECTS PORTFOLIO
# ==========================================
with tab3:
    st.markdown('<div class="section-header">Featured Architectures</div>', unsafe_allow_html=True)
    
    # Project 1
    with st.container():
        st.markdown("### 🏡 Boston House Price Prediction")
        st.markdown("""
            <div>
                <span class="proj-badge">Python</span>
                <span class="proj-badge">Jupyter Notebook</span>
                <span class="proj-badge">Scikit-Learn</span>
                <span class="proj-badge">Random Forest</span>
                <span class="proj-badge">XGBoost</span>
                <span class="proj-badge">Statsmodels</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        **Overview:** An end-to-end Machine Learning pipeline predicting Boston housing prices based on structural and neighborhood features.
        * **Robust Preprocessing:** Handled outliers using the IQR capping method, conducted multicollinearity checks using VIF, and applied One-Hot Encoding and StandardScaler.
        * **Feature Transformation:** Applied a log transformation to the target variable (MEDV) to correct non-normal distribution.
        * **Model Evaluation:** Evaluated algorithms including Ridge/Lasso, Decision Trees, SVR, and Ensemble methods. The **Random Forest Regressor** achieved an **R-squared of 0.802** and an RMSE of 0.20.
        """)
        st.write("---")

    # Project 2
    with st.container():
        st.markdown("### 🌿 PlantCo Performance Profitability Tracker")
        st.markdown("""
            <div>
                <span class="proj-badge">Power BI</span>
                <span class="proj-badge">Power Query</span>
                <span class="proj-badge">DAX</span>
                <span class="proj-badge">Star Schema</span>
                <span class="proj-badge">Data Visualization</span>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        **Overview:** A comprehensive Power BI dashboard designed to identify sales growth opportunities and geographical pain points.
        * **Data Modeling:** Architected a robust Star Schema connecting Fact tables (2,440+ transactions) with Dimension tables (Accounts and Product Hierarchies).
        * **Time Intelligence:** Created custom DAX measures to compare Year-to-Date (YTD) versus Prior Year-to-Date (PYTD) performance dynamically.
        * **Actionable Insights:** Designed interactive scatter charts to segment accounts based on profitability, directly guiding executive sales strategies.
        """)
