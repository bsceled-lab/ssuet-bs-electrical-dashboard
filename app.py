import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SSUET Electrical Engineering",
    page_icon="⚡",
    layout="wide",
)

FACULTY = [
    {
        "Name": "Dr. Muhammad Ibrar ul Haque",
        "Designation": "Professor",
        "Role": "Chairperson",
        "Qualification": "Ph.D. Electronic Engineering — SSUET; M.S. Telecommunication — SSUET; B.E. Electronic Engineering — NEDUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electronic Engineering, Telecommunication",
        "Research": "Academic leadership and engineering research. Specific current research profile should be verified from the official university source.",
    },
    {
        "Name": "Dr. Tarique Aziz",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "Ph.D. Electrical Engineering — Zhejiang University, China; M.Sc. Electrical Engineering — COMSATS University Islamabad; B.E. Electrical Engineering — Q.U.E.S.T., Nawabshah",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electrical Engineering",
        "Research": "Electrical engineering research and teaching. Specific current research profile should be verified from the official university source.",
    },
    {
        "Name": "Dr. Manzar Ahmed",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "M.S. Telecommunication — Asian Institute of Technology, Thailand; B.E. Electrical Engineering — UET Lahore",
        "Experience": "Not published in the available official source.",
        "Expertise": "Telecommunication, Electrical Engineering",
        "Research": "Telecommunication and electrical engineering teaching/research.",
    },
    {
        "Name": "Engr. M. Nadeem Iqbal",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "M.S. Electronic Engineering — SSUET; M.A. Islamic Studies — University of Karachi; PGD Computer & IT — University of Karachi; B.E. Electrical Engineering — NEDUET; B.Sc. Physics — University of Karachi",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electronic Engineering, Electrical Engineering, Computer & IT",
        "Research": "Electrical/electronic engineering research activity.",
    },
    {
        "Name": "Engr. Syed Faisal Hoda",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "M.E. Electrical Engineering, specialization in Telecommunication — NEDUET; B.E. Electrical Engineering — NEDUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Telecommunication, Electrical Engineering",
        "Research": "Telecommunication and electrical engineering research activity.",
    },
    {
        "Name": "Engr. Fawad Shaukat",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "M.S. Communication & Signal Processing — Imperial College London, UK; B.E. Electrical Engineering — NEDUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Communication, Signal Processing",
        "Research": "Signal Processing & Deep Learning research cluster activity.",
    },
    {
        "Name": "Engr. Sheikh Junaid Yawar",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "M.E. Energy — NEDUET; B.E. Electrical Engineering — NEDUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Energy, Electrical Engineering",
        "Research": "Power & Energy System research activity.",
    },
    {
        "Name": "Engr. Zafar Ahmed",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "M.S. Power Electronics — NEDUET; B.E. Electrical Engineering — NEDUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Power Electronics, Electrical Engineering",
        "Research": "Power & Energy System research activity.",
    },
    {
        "Name": "Engr. Muhammad Javeed",
        "Designation": "Assistant Professor",
        "Role": "Faculty Member",
        "Qualification": "M.S. Electrical Telecommunication — SSUET; B.S. Electronic Engineering — SSUET; B.Sc. Physics & Mathematics — University of Karachi",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electrical Telecommunication, Electronic Engineering",
        "Research": "Electrical/electronic engineering research activity.",
    },
    {
        "Name": "Dr. Andaleeb Ali",
        "Designation": "Senior Lecturer",
        "Role": "Faculty Member",
        "Qualification": "Not published in the available source material.",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electrical Engineering",
        "Research": "Teaching and academic activity.",
    },
    {
        "Name": "Engr. Faiza Waqqas",
        "Designation": "Senior Lecturer",
        "Role": "Faculty Member",
        "Qualification": "M.S. Telecommunication — SSUET; B.S. Electronic Engineering — SSUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Telecommunication, Electronic Engineering",
        "Research": "Telecommunication and electronic engineering academic activity.",
    },
    {
        "Name": "Engr. Aamir Ali",
        "Designation": "Senior Lecturer",
        "Role": "Faculty Member",
        "Qualification": "M.E. Power System Engineering — NEDUET; B.E. Electrical Engineering — NEDUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Power Systems, Electrical Engineering",
        "Research": "Power system academic/research activity.",
    },
    {
        "Name": "Engr. Jawad Ali Arshad",
        "Designation": "Senior Lecturer",
        "Role": "Faculty Member",
        "Qualification": "M.E. Telecommunication — Hamdard University; B.S. Electronic Engineering — SSUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Telecommunication, Electronic Engineering",
        "Research": "Telecommunication/electronic engineering academic activity.",
    },
    {
        "Name": "Engr. Jeffery Ali Rizvi",
        "Designation": "Senior Lecturer",
        "Role": "Faculty Member",
        "Qualification": "M.E. Electrical Engineering — University of Windsor, Canada; B.S. Electronic Engineering — SSUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electrical Engineering, Electronic Engineering",
        "Research": "Electrical/electronic engineering academic activity.",
    },
    {
        "Name": "Bineesh Fayyaz",
        "Designation": "Senior Lecturer",
        "Role": "Faculty Member",
        "Qualification": "Not published in the available source material.",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electrical Engineering",
        "Research": "Teaching and academic activity.",
    },
    {
        "Name": "Engr. Rabika Tariq",
        "Designation": "Lecturer",
        "Role": "Faculty Member",
        "Qualification": "M.S. Electronic Engineering — SSUET; MBA Finance — University of Karachi; B.S. Electronic Engineering — SSUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electronic Engineering, Engineering Management",
        "Research": "Electronic engineering academic activity.",
    },
    {
        "Name": "Engr. Muhammad Muzammil",
        "Designation": "Lecturer",
        "Role": "Faculty Member",
        "Qualification": "M.S. Electrical Engineering — Bahria University; B.S. Electrical Engineering — FAST-NUCES",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electrical Engineering",
        "Research": "Power/electrical engineering research activity.",
    },
    {
        "Name": "Engr. Muhammad Tanveer",
        "Designation": "Lecturer",
        "Role": "Faculty Member",
        "Qualification": "M.E. Industrial Control Automation — Hamdard University; B.S. Electronic Engineering — SSUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Industrial Control, Automation, Electronic Engineering",
        "Research": "Control, automation and electronic engineering academic activity.",
    },
    {
        "Name": "Engr. Mr. Syed Faraz Liaquat",
        "Designation": "Junior Lecturer",
        "Role": "Faculty Member",
        "Qualification": "B.S. Electronic Engineering — SSUET; M.S. Engineering Management — enrolled at SSUET",
        "Experience": "Not published in the available official source.",
        "Expertise": "Electronic Engineering, Engineering Management",
        "Research": "Teaching and academic activity.",
    },
]

df = pd.DataFrame(FACULTY)

st.markdown("""
<style>
.main {background:#f6f8fb;}
.hero {
    padding: 2rem 2.2rem;
    border-radius: 22px;
    background: linear-gradient(135deg,#0b1f3a,#145da0);
    color:white;
    margin-bottom:1.5rem;
}
.hero h1 {font-size:2.5rem;margin-bottom:.3rem;}
.hero p {font-size:1.05rem;opacity:.92;}
.metric-card {
    background:white;
    padding:1.15rem;
    border-radius:16px;
    border:1px solid #e5e7eb;
    box-shadow:0 4px 16px rgba(0,0,0,.05);
}
.profile-card {
    background:white;
    padding:1.2rem;
    border-radius:18px;
    border:1px solid #e5e7eb;
    margin-bottom:1rem;
}
.section-card {
    background:white;
    padding:1.4rem;
    border-radius:18px;
    border:1px solid #e5e7eb;
    margin-bottom:1.2rem;
}
.badge {
    display:inline-block;
    padding:.35rem .7rem;
    border-radius:999px;
    background:#e8f1fb;
    color:#145da0;
    font-weight:600;
    margin-bottom:.7rem;
}
.small-note {color:#6b7280;font-size:.88rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>⚡ SSUET Electrical Engineering</h1>
<p>Faculty Directory & Academic Department Dashboard</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Overview", "👨‍🏫 Faculty Profiles", "📊 Analytics", "🏛️ Department"]
)

st.sidebar.markdown("---")
st.sidebar.info("Sir Syed University of Engineering & Technology\n\nFaculty information is presented from the available SSUET source material.")

if page == "🏠 Overview":
    c1, c2, c3, c4, c5 = st.columns(5)
    metrics = [
        ("Total Faculty", len(df)),
        ("Professor", int((df["Designation"] == "Professor").sum())),
        ("Assistant Professor", int((df["Designation"] == "Assistant Professor").sum())),
        ("Senior Lecturer", int((df["Designation"] == "Senior Lecturer").sum())),
        ("Lecturer / Junior", int(df["Designation"].isin(["Lecturer", "Junior Lecturer"]).sum())),
    ]
    for col, (label, value) in zip([c1,c2,c3,c4,c5], metrics):
        with col:
            st.markdown(
                f'<div class="metric-card"><div class="small-note">{label}</div><h2>{value}</h2></div>',
                unsafe_allow_html=True
            )

    st.markdown("### Faculty Distribution")
    counts = df["Designation"].value_counts().reset_index()
    counts.columns = ["Designation", "Faculty"]
    fig = px.bar(
        counts,
        x="Designation",
        y="Faculty",
        text="Faculty",
        title="Faculty by Academic Rank",
    )
    fig.update_layout(template="plotly_white", height=420)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="section-card">
        <h3>🎓 Academic Programs</h3>
        <ul>
        <li>BS Electrical Engineering</li>
        <li>BS Renewable Energy System</li>
        <li>B.E Tech (Electrical)</li>
        <li>MS Electrical Engineering</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-card">
        <h3>📅 Department History</h3>
        <p><strong>Established:</strong> September 2014</p>
        <p><strong>First Batch:</strong> Spring 2015</p>
        <p><strong>Faculty:</strong> Electrical Engineering Department, FoECE</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "👨‍🏫 Faculty Profiles":
    st.markdown("## 👨‍🏫 Faculty Profiles")
    st.caption("Select a faculty member's tab to view qualification, experience, expertise and academic information.")

    search = st.text_input("🔎 Search faculty by name", "")
    rank_options = ["All"] + sorted(df["Designation"].unique().tolist())
    rank = st.selectbox("Filter by academic rank", rank_options)

    filtered = df.copy()
    if search.strip():
        filtered = filtered[filtered["Name"].str.contains(search.strip(), case=False, na=False)]
    if rank != "All":
        filtered = filtered[filtered["Designation"] == rank]

    if filtered.empty:
        st.warning("No faculty member matches your search/filter.")
    else:
        tabs = st.tabs(filtered["Name"].tolist())
        for tab, (_, person) in zip(tabs, filtered.iterrows()):
            with tab:
                st.markdown(
                    f'<div class="profile-card"><span class="badge">{person["Designation"]}</span><h2>{person["Name"]}</h2><p class="small-note">{person["Role"]}</p></div>',
                    unsafe_allow_html=True
                )

                a, b = st.columns(2)
                with a:
                    st.markdown("### 🎓 Qualification")
                    st.info(person["Qualification"])
                with b:
                    st.markdown("### ⏱️ Professional Experience")
                    st.info(person["Experience"])

                c, d = st.columns(2)
                with c:
                    st.markdown("### 🔬 Expertise")
                    st.success(person["Expertise"])
                with d:
                    st.markdown("### 📚 Research / Academic Activity")
                    st.write(person["Research"])

                st.markdown("---")
                st.caption(
                    "Accuracy note: Experience years and some individual profile details were not published in the available source material, so they are not invented here."
                )

elif page == "📊 Analytics":
    st.markdown("## 📊 Faculty Analytics")

    left, right = st.columns(2)
    with left:
        counts = df["Designation"].value_counts().reset_index()
        counts.columns = ["Designation", "Faculty"]
        pie = px.pie(
            counts,
            names="Designation",
            values="Faculty",
            title="Faculty Composition",
            hole=.45,
        )
        pie.update_layout(template="plotly_white")
        st.plotly_chart(pie, use_container_width=True)

    with right:
        qualification_known = (~df["Qualification"].str.contains("Not published", case=False, na=False)).sum()
        qualification_missing = len(df) - qualification_known
        qdf = pd.DataFrame({
            "Status": ["Qualification available", "Qualification not available"],
            "Faculty": [qualification_known, qualification_missing],
        })
        qfig = px.bar(
            qdf,
            x="Status",
            y="Faculty",
            text="Faculty",
            title="Qualification Data Coverage",
        )
        qfig.update_layout(template="plotly_white")
        st.plotly_chart(qfig, use_container_width=True)

    st.markdown("### Faculty Directory")
    st.dataframe(
        df[["Name", "Designation", "Qualification", "Expertise"]],
        use_container_width=True,
        hide_index=True,
    )

elif page == "🏛️ Department":
    st.markdown("## 🏛️ Department Information")

    st.markdown("""
    <div class="section-card">
    <h3>About the Department</h3>
    <p>
    The Electrical Engineering Department at SSUET was established in September 2014,
    with its first batch starting in Spring 2015. The department operates under the
    Faculty of Electrical & Computer Engineering (FoECE).
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="section-card">
        <h3>🎓 Programs</h3>
        <ul>
        <li>BS Electrical Engineering</li>
        <li>BS Renewable Energy System</li>
        <li>B.E Tech (Electrical)</li>
        <li>MS Electrical Engineering</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-card">
        <h3>⚙️ Key Learning Areas</h3>
        <ul>
        <li>Electrical Power Systems</li>
        <li>Electrical Instrumentation</li>
        <li>Electrical Power Flow</li>
        <li>Electrical Machine Design</li>
        <li>Renewable Energy Systems</li>
        <li>Embedded Systems</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h3>🔬 Research Areas Mentioned in SSUET Material</h3>
    <ul>
    <li>Signal Processing & Deep Learning</li>
    <li>Power & Energy Systems</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.success("Tip: Use the Faculty Profiles page to open each faculty member's detailed tab.")
