import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SSUET Electrical Engineering", page_icon="⚡", layout="wide")

faculty = [
("Dr. Muhammad Ibrar ul Haque","Professor","Chairperson",
"Ph.D. Electronic Engineering (SSUET)\nM.S. Telecommunication (SSUET)\nB.E. Electronic Engineering (NEDUET)",
"Not published in the available source.","Electrical Engineering","Department teaching, research and research-cluster activities."),
("Dr. Tarique Aziz","Assistant Professor","",
"Ph.D. Electrical Engineering (Zhejiang University, China)\nM.Sc. Electrical Engineering (COMSATS University, Islamabad)\nB.E. Electrical Engineering (Q.U.E.S.T., Nawabshah)",
"Not published in the available source.","Electrical Engineering","Not published in the available source."),
("Dr. Manzar Ahmed","Assistant Professor","",
"M.S. Telecommunication (Asian Institute of Technology, Thailand)\nB.E. Electrical Engineering (UET Lahore)",
"Not published in the available source.","Telecommunication / Electrical Engineering","Not published in the available source."),
("Engr. M. Nadeem Iqbal","Assistant Professor","",
"M.S. Electronic Engineering (SSUET)\nM.A. Islamic Studies (University of Karachi)\nPGD Computer & IT (University of Karachi)\nB.E. Electrical Engineering (NEDUET)\nB.Sc. Physics (University of Karachi)",
"Not published in the available source.","Electrical / Electronic Engineering","SSUET newsletter documents participation in a PSQCA standards meeting."),
("Engr. Syed Faisal Hoda","Assistant Professor","",
"M.E. Electrical Engineering, specialization in Telecommunication (NEDUET)\nB.E. Electrical Engineering (NEDUET)",
"Not published in the available source.","Electrical Engineering / Telecommunication","Not published in the available source."),
("Engr. Fawad Shaukat","Assistant Professor","",
"M.S. Communication & Signal Processing (Imperial College London, UK)\nB.E. Electrical Engineering (NEDUET)",
"Not published in the available source.","Communication & Signal Processing","SSUET documents Signal Processing & Deep Learning as an ELED research-cluster area."),
("Engr. Sheikh Junaid Yawar","Assistant Professor","",
"M.E. Energy (NEDUET)\nB.E. Electrical Engineering (NEDUET)",
"Not published in the available source.","Energy / Electrical Engineering","Not published in the available source."),
("Engr. Zafar Ahmed","Assistant Professor","",
"M.S. Power Electronics (NEDUET)\nB.E. Electrical Engineering (NEDUET)",
"Not published in the available source.","Power Electronics","SSUET documents participation in the Power & Energy System research cluster."),
("Engr. Muhammad Javeed","Assistant Professor","",
"M.S. Electrical Telecommunication (SSUET)\nB.S. Electronic Engineering (SSUET)\nB.Sc. Physics & Mathematics (University of Karachi)",
"Not published in the available source.","Electrical Telecommunication","Not published in the available source."),
("Dr. Andaleeb Ali","Senior Lecturer","",
"Not provided in available official source material.","Not published in the available source.","Electrical Engineering","Not published in the available source."),
("Engr. Faiza Waqqas","Senior Lecturer","",
"M.S. Telecommunication (SSUET)\nB.S. Electronic Engineering (SSUET)",
"Not published in the available source.","Telecommunication / Electronic Engineering","Not published in the available source."),
("Engr. Aamir Ali","Senior Lecturer","",
"B.E. Electrical Engineering (NEDUET)\nM.E. Power System Engineering (NEDUET)",
"Not published in the available source.","Power System Engineering","Not published in the available source."),
("Engr. Jawad Ali Arshad","Senior Lecturer","",
"M.E. Telecommunication (Hamdard University)\nB.S. Electronic Engineering (SSUET)",
"Not published in the available source.","Telecommunication / Electronic Engineering","SSUET documents research-cluster participation."),
("Engr. Jeffery Ali Rizvi","Senior Lecturer","",
"M.E. Electrical Engineering (University of Windsor, Canada)\nB.S. Electronic Engineering (SSUET)",
"Not published in the available source.","Electrical Engineering","SSUET documents research-cluster participation."),
("Bineesh Fayyaz","Senior Lecturer","",
"Not provided in available official source material.","Not published in the available source.","Electrical Engineering","Not published in the available source."),
("Engr. Rabika Tariq","Lecturer","",
"M.S. Electronic Engineering (SSUET)\nM.B.A. Finance (University of Karachi)\nB.S. Electronic Engineering (SSUET)",
"Not published in the available source.","Electronic Engineering","Not published in the available source."),
("Engr. Muhammad Muzammil","Lecturer","",
"M.S. Electrical Engineering (Bahria University)\nB.S. Electrical Engineering (FAST-NUCES)",
"Not published in the available source.","Electrical Engineering","SSUET newsletter documents research-cluster participation."),
("Engr. Muhammad Tanveer","Lecturer","",
"M.E. Industrial Control Automation (Hamdard University)\nB.S. Electronic Engineering (SSUET)",
"Not published in the available source.","Industrial Control & Automation","Not published in the available source."),
("Engr. Mr. Syed Faraz Liaquat","Junior Lecturer","",
"B.S. Electronic Engineering (SSUET)\nM.S. Engineering Management — enrolled (SSUET)",
"Not published in the available source.","Electronic Engineering / Engineering Management","SSUET departmental activity records participation in faculty activities."),
]
df = pd.DataFrame(faculty, columns=["Name","Designation","Role","Qualification","Experience","Expertise","Research"])

st.markdown("""<style>
.stApp{background:#f5f7fb}.hero{background:linear-gradient(135deg,#071a33,#0f4c81,#168aad);padding:32px 38px;border-radius:22px;color:white;margin-bottom:25px;box-shadow:0 12px 30px #071a3330}.hero h1{margin:0;font-size:38px}.hero p{font-size:17px;opacity:.9}.metric{background:white;border:1px solid #e2e8f0;border-radius:17px;padding:20px;box-shadow:0 5px 18px #0f172a10}.value{font-size:30px;font-weight:800;color:#0f4c81}.label{color:#64748b}.card{background:white;border:1px solid #e2e8f0;border-radius:18px;padding:20px;margin-bottom:14px;box-shadow:0 5px 18px #0f172a0d}.title{font-size:24px;font-weight:800;color:#0f172a}.blue{color:#0f4c81;font-weight:700}.section{font-weight:800;color:#0f4c81;margin-bottom:8px}
</style>""", unsafe_allow_html=True)

st.sidebar.markdown("## ⚡ SSUET")
st.sidebar.caption("Electrical Engineering Faculty Dashboard")
page=st.sidebar.radio("MENU",["🏠 Overview","👨‍🏫 Faculty Profiles","📊 Analytics","🏛️ Department"])

st.markdown('<div class="hero"><h1>⚡ Electrical Engineering Department</h1><p>Sir Syed University of Engineering and Technology · Professional Faculty Information Dashboard</p></div>',unsafe_allow_html=True)

if page=="🏠 Overview":
    st.subheader("Department at a Glance")
    vals=[("Total Faculty",len(df)),("Professor",(df.Designation=="Professor").sum()),("Assistant Professor",(df.Designation=="Assistant Professor").sum()),("Senior Lecturer",(df.Designation=="Senior Lecturer").sum()),("Lecturer / Junior",((df.Designation=="Lecturer")|(df.Designation=="Junior Lecturer")).sum())]
    cs=st.columns(5)
    for c,(label,val) in zip(cs,vals):
        c.markdown(f'<div class="metric"><div class="value">{val}</div><div class="label">{label}</div></div>',unsafe_allow_html=True)
    st.write("")
    a,b=st.columns([1.2,1])
    with a:
        counts=df.Designation.value_counts().reset_index(); counts.columns=["Designation","Faculty"]
        st.plotly_chart(px.bar(counts,x="Designation",y="Faculty",text="Faculty",title="Faculty by Academic Rank"),use_container_width=True)
    with b:
        st.subheader("Academic Programs")
        for x in ["BS Electrical Engineering","BS Renewable Energy System","B.E Tech (Electrical)","MS Electrical Engineering"]:
            st.markdown(f'<div class="card">🎓 <b>{x}</b></div>',unsafe_allow_html=True)
    st.info("The department was established in September 2014 and the first batch was enrolled in Spring 2015.")

elif page=="👨‍🏫 Faculty Profiles":
    st.subheader("👨‍🏫 Faculty Profiles")
    x,y=st.columns([2,1])
    search=x.text_input("🔎 Search faculty",placeholder="Type a name...")
    rank=y.selectbox("Academic rank",["All"]+sorted(df.Designation.unique()))
    f=df.copy()
    if search: f=f[f.Name.str.contains(search,case=False,na=False)]
    if rank!="All": f=f[f.Designation==rank]
    names=f.Name.tolist()
    if names:
        tabs=st.tabs(names)
        for tab,(_,p) in zip(tabs,f.iterrows()):
            with tab:
                st.markdown(f'<div class="card"><div class="title">👤 {p.Name}</div><div class="blue">{p.Designation}{" · "+p.Role if p.Role else ""}</div></div>',unsafe_allow_html=True)
                c1,c2=st.columns(2)
                with c1:
                    st.markdown(f'<div class="card"><div class="section">🎓 Qualification</div>{p.Qualification.replace(chr(10),"<br>")}</div>',unsafe_allow_html=True)
                with c2:
                    st.markdown(f'<div class="card"><div class="section">⏱️ Professional Experience</div>{p.Experience}</div>',unsafe_allow_html=True)
                c3,c4=st.columns(2)
                with c3: st.markdown(f'<div class="card"><div class="section">🔬 Expertise</div>{p.Expertise}</div>',unsafe_allow_html=True)
                with c4: st.markdown(f'<div class="card"><div class="section">📚 Research / Academic Activity</div>{p.Research}</div>',unsafe_allow_html=True)
                st.caption("Missing experience is intentionally not estimated; add verified information from an official CV/profile.")
    else: st.warning("No matching faculty member.")

elif page=="📊 Analytics":
    st.subheader("📊 Faculty Analytics")
    counts=df.Designation.value_counts().reset_index(); counts.columns=["Designation","Faculty"]
    c1,c2=st.columns(2)
    with c1: st.plotly_chart(px.pie(counts,names="Designation",values="Faculty,hole=.45".split(",")[0],title="Faculty Composition",hole=.45),use_container_width=True)
    with c2: st.plotly_chart(px.bar(counts,x="Designation",y="Faculty",text="Faculty",title="Academic Rank Distribution"),use_container_width=True)
    known=~df.Qualification.str.startswith("Not provided")
    a,b=st.columns(2); a.metric("Profiles with qualification data",int(known.sum())); b.metric("Profiles needing official data",int((~known).sum()))
    st.dataframe(df[["Name","Designation","Role","Qualification","Experience","Expertise"]],use_container_width=True,hide_index=True)

else:
    st.subheader("🏛️ Department Profile")
    st.markdown("**Established:** September 2014  
**First batch:** Spring 2015  
**Faculty:** Faculty of Electrical and Computer Engineering (FoECE)")
    st.markdown("### 🎓 Programs")
    st.write("• BS Electrical Engineering\n• BS Renewable Energy System\n• B.E Tech (Electrical)\n• MS Electrical Engineering")
    st.markdown("### 🔬 Key Learning Areas")
    st.write("Electrical Power Systems · Electrical Instrumentations · Electrical Power Flow · Electrical Machine Design · Renewable Energy Systems · Embedded Systems")
    st.markdown("### 🎯 Vision")
    st.write("The department aims to enhance teaching and research, provide excellent education, develop professional and entrepreneurial skills, contribute to the national economy and meet international requirements.")
    st.markdown("### 🚀 Mission")
    st.write("The department promotes a practical environment connected with theoretical knowledge, excellence in education and industrial practices, strong foundations for future challenges, and ethical professional practice.")

st.divider()
st.caption("SSUET Electrical Engineering Faculty Dashboard · Verify information against the latest official university records.")
