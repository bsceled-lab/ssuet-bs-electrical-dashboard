import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SSUET Electrical Engineering Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# SSUET ELECTRICAL ENGINEERING FACULTY DATA
# Source: supplied SSUET BS Electrical Engineering PDF
# Note: Qualification, experience and research fields are not
# included in the supplied source, so they are marked accordingly.
# ============================================================

faculty = [
    {
        "Name": "Dr. Muhammad Ibrar ul Haque",
        "Designation": "Professor",
        "Role": "Chairperson",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Dr. Tarique Aziz",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Dr. Manzar Ahmed",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. M. Nadeem Iqbal",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Syed Faisal Hoda",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Fawad Shaukat",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Sheikh Junaid Yawar",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Zafar Ahmed",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Muhammad Javeed",
        "Designation": "Assistant Professor",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Dr. Andaleeb Ali",
        "Designation": "Senior Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Faiza Waqqas",
        "Designation": "Senior Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Aamir Ali",
        "Designation": "Senior Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Jawad Ali Arshad",
        "Designation": "Senior Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Jeffery Ali Rizvi",
        "Designation": "Senior Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Bineesh Fayyaz",
        "Designation": "Senior Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Rabika Tariq",
        "Designation": "Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Muhammad Muzammil",
        "Designation": "Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Muhammad Tanveer",
        "Designation": "Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
    {
        "Name": "Engr. Mr. Syed Faraz Liaquat",
        "Designation": "Junior Lecturer",
        "Role": "",
        "Qualification": "Not provided in source",
        "Experience": "Not provided in source",
        "Specialization": "Not provided in source",
        "Research Interests": "Not provided in source",
    },
]

df = pd.DataFrame(faculty)

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #64748b;
        margin-top: 2px;
        margin-bottom: 25px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 15px;
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        color: white;
        min-height: 125px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.10);
    }

    .metric-number {
        font-size: 34px;
        font-weight: 800;
    }

    .metric-label {
        font-size: 15px;
        opacity: 0.9;
    }

    .faculty-card {
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 12px;
        background: #ffffff;
        box-shadow: 0 3px 12px rgba(15,23,42,0.06);
    }

    .faculty-name {
        font-size: 20px;
        font-weight: 750;
        color: #0f172a;
    }

    .faculty-role {
        color: #2563eb;
        font-weight: 650;
        margin-top: 3px;
    }

    .info-box {
        padding: 18px;
        border-radius: 12px;
        background: #f8fafc;
        border-left: 5px solid #2563eb;
        margin-bottom: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚡ SSUET EED")
st.sidebar.caption("Electrical Engineering Department")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👨‍🏫 Faculty Directory",
        "📊 Faculty Statistics",
        "🏛️ Department Profile",
    ],
)

st.sidebar.divider()
st.sidebar.caption("Faculty information is based on the supplied SSUET program document.")

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">⚡ Electrical Engineering Department</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Sir Syed University of Engineering and Technology (SSUET)</div>',
    unsafe_allow_html=True,
)

# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.subheader("Department Dashboard")

    total = len(df)
    professors = len(df[df["Designation"] == "Professor"])
    associate = len(df[df["Designation"] == "Associate Professor"])
    assistant = len(df[df["Designation"] == "Assistant Professor"])
    senior = len(df[df["Designation"] == "Senior Lecturer"])
    lecturers = len(df[df["Designation"] == "Lecturer"])
    junior = len(df[df["Designation"] == "Junior Lecturer"])

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f'<div class="metric-card"><div class="metric-number">{total}</div>'
            f'<div class="metric-label">Total Faculty</div></div>',
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f'<div class="metric-card"><div class="metric-number">{professors}</div>'
            f'<div class="metric-label">Professor</div></div>',
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f'<div class="metric-card"><div class="metric-number">{assistant}</div>'
            f'<div class="metric-label">Assistant Professors</div></div>',
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            f'<div class="metric-card"><div class="metric-number">{senior}</div>'
            f'<div class="metric-label">Senior Lecturers</div></div>',
            unsafe_allow_html=True,
        )

    st.write("")

    left, right = st.columns([1.2, 1])

    with left:
        st.subheader("Faculty by Designation")

        counts = (
            df["Designation"]
            .value_counts()
            .rename_axis("Designation")
            .reset_index(name="Faculty")
        )

        fig = px.bar(
            counts,
            x="Designation",
            y="Faculty",
            text="Faculty",
            title="Faculty Distribution",
        )
        fig.update_layout(
            xaxis_title="Designation",
            yaxis_title="Number of Faculty",
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Programs")

        programs = [
            "BS Electrical Engineering",
            "BS Renewable Energy System",
            "B.E Tech (Electrical)",
            "MS Electrical Engineering",
        ]

        for program in programs:
            st.markdown(
                f'<div class="info-box">🎓 <b>{program}</b></div>',
                unsafe_allow_html=True,
            )

    st.subheader("Department Overview")

    st.markdown(
        """
        <div class="info-box">
        The Department of Electrical Engineering was established in September 2014
        and its first batch was enrolled in Spring 2015. The department operates
        under the Faculty of Electrical and Computer Engineering (FoECE).
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "The supplied source describes the department's faculty as experienced, "
        "well-qualified and involved in teaching and research activities."
    )


# ============================================================
# FACULTY DIRECTORY
# ============================================================

elif page == "👨‍🏫 Faculty Directory":

    st.subheader("👨‍🏫 Faculty Directory")
    st.caption(f"{len(df)} faculty members listed in the supplied SSUET source.")

    search = st.text_input(
        "🔎 Search faculty",
        placeholder="Search by faculty name...",
    )

    designations = ["All"] + sorted(df["Designation"].unique().tolist())

    designation_filter = st.selectbox(
        "Filter by designation",
        designations,
    )

    filtered = df.copy()

    if search.strip():
        filtered = filtered[
            filtered["Name"].str.contains(
                search.strip(),
                case=False,
                na=False,
            )
        ]

    if designation_filter != "All":
        filtered = filtered[
            filtered["Designation"] == designation_filter
        ]

    st.write(f"**Showing {len(filtered)} faculty member(s)**")

    for _, person in filtered.iterrows():

        role = f" • {person['Role']}" if person["Role"] else ""

        st.markdown(
            f"""
            <div class="faculty-card">
                <div class="faculty-name">👤 {person['Name']}</div>
                <div class="faculty-role">
                    {person['Designation']}{role}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander(f"View profile — {person['Name']}"):
            col1, col2 = st.columns(2)

            with col1:
                st.write("**Designation**")
                st.write(person["Designation"])

                st.write("**Role**")
                st.write(person["Role"] if person["Role"] else "Not specified")

                st.write("**Qualification**")
                st.write(person["Qualification"])

            with col2:
                st.write("**Experience**")
                st.write(person["Experience"])

                st.write("**Specialization**")
                st.write(person["Specialization"])

                st.write("**Research Interests**")
                st.write(person["Research Interests"])


# ============================================================
# STATISTICS
# ============================================================

elif page == "📊 Faculty Statistics":

    st.subheader("📊 Faculty Statistics")

    counts = (
        df["Designation"]
        .value_counts()
        .rename_axis("Designation")
        .reset_index(name="Faculty")
    )

    c1, c2 = st.columns(2)

    with c1:
        fig1 = px.pie(
            counts,
            names="Designation",
            values="Faculty",
            title="Faculty by Designation",
            hole=0.4,
        )
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        fig2 = px.bar(
            counts,
            x="Designation",
            y="Faculty",
            text="Faculty",
            title="Designation Count",
        )
        fig2.update_layout(
            xaxis_title="Designation",
            yaxis_title="Faculty",
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Faculty Data Table")

    display_df = df[
        ["Name", "Designation", "Role"]
    ].copy()

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# DEPARTMENT PROFILE
# ============================================================

elif page == "🏛️ Department Profile":

    st.subheader("🏛️ Department Profile")

    st.markdown(
        """
        ### About the Department

        The Department of Electrical Engineering was established in
        **September 2014**, and the first batch was enrolled in **Spring 2015**.

        The department operates under the **Faculty of Electrical and Computer
        Engineering (FoECE)**.
        """
    )

    st.divider()

    st.subheader("🎓 Academic Programs")

    programs = [
        ("BS Electrical Engineering", "Undergraduate"),
        ("BS Renewable Energy System", "Undergraduate"),
        ("B.E Tech (Electrical)", "Undergraduate"),
        ("MS Electrical Engineering", "Postgraduate"),
    ]

    for name, level in programs:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{name}**")
        with col2:
            st.write(level)

    st.divider()

    st.subheader("🎯 Vision")

    st.write(
        "The department aims to enhance the quality of teaching and research, "
        "provide excellent education, develop professional and entrepreneurial "
        "skills, contribute to the national economy, address market challenges, "
        "and meet international requirements."
    )

    st.subheader("🚀 Mission")

    st.write(
        "The department promotes a practical environment connected with "
        "theoretical knowledge for education and research, with emphasis on "
        "professional excellence, industrial practices, strong foundations, "
        "morals, dignity, and ethical professional practice."
    )

    st.divider()

    st.subheader("🔬 Key Learning Areas")

    areas = [
        "Electrical Power Systems",
        "Electrical Instrumentations",
        "Electrical Power Flow",
        "Electrical Machine Design",
        "Renewable Energy Systems",
        "Embedded Systems",
    ]

    cols = st.columns(3)

    for i, area in enumerate(areas):
        with cols[i % 3]:
            st.markdown(
                f'<div class="info-box">⚡ {area}</div>',
                unsafe_allow_html=True,
            )

    st.caption(
        "Source: supplied BS Electrical Engineering — Sir Syed University of "
        "Engineering and Technology document."
    )
