import streamlit as st
from workflow import graph

st.set_page_config(
    page_title="Autonomous AI Research Platform",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<h1 style='text-align:center;'>
🚀 Autonomous AI Research Platform
</h1>

<p style='text-align:center;font-size:18px;'>
Multi-Agent AI • RAG • LangGraph • Automated Research Reports
</p>

<hr>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🤖 AI Research Platform")

    st.markdown("---")

    st.info(
        """
### Features

✅ Multi-Agent Workflow

✅ RAG Pipeline

✅ AI Report Generation

✅ Dynamic Charts

✅ PDF Export

✅ Email Delivery

✅ References Tracking
        """
    )

    st.markdown("---")

    st.caption(
        "Powered by Groq, Tavily, LangGraph, ChromaDB and Streamlit"
    )

# -----------------------------
# INPUTS
# -----------------------------

topic = st.text_input(
    "Enter Report Topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

email = st.text_input(
    "Email Report To (Optional)",
    placeholder="example@gmail.com"
)

# -----------------------------
# BUTTON
# -----------------------------

if st.button("🚀 Generate Report"):

    if topic.strip() == "":
        st.warning("Please enter a topic")
        st.stop()

    with st.spinner(
        "Researching, analyzing and generating report..."
    ):

        result = graph.invoke(
            {
                "topic": topic,
                "email": email
            }
        )

    report_text = result["report_text"]
    metrics = result["metrics"]
    chart_paths = result["chart_paths"]
    pdf_path = result["pdf_path"]
    references = result["references"]

    st.success(
        "✅ Research Report Generated Successfully"
    )

    if email.strip():
        st.success(
            f"📧 PDF sent to {email}"
        )

    # -----------------------------
    # METRICS DASHBOARD
    # -----------------------------

    st.subheader("📈 AI Analysis Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🚀 Advantages",
        metrics.get("advantages", 0)
    )

    col2.metric(
        "⚠️ Challenges",
        metrics.get("challenges", 0)
    )

    col3.metric(
        "📈 Future Trends",
        metrics.get("future_trends", 0)
    )

    col4.metric(
        "💹 Market Growth",
        metrics.get("market_growth", 0)
    )

    st.markdown("---")

    # -----------------------------
    # TABS
    # -----------------------------

    tab1, tab2, tab3 = st.tabs(
        [
            "📄 Report",
            "📊 Charts",
            "📚 References"
        ]
    )

    # -----------------------------
    # REPORT TAB
    # -----------------------------

    with tab1:

        st.subheader("Generated Research Report")

        st.markdown(report_text)

    # -----------------------------
    # CHARTS TAB
    # -----------------------------

    with tab2:

        st.subheader("Visual Analytics")

        for chart in chart_paths:

            st.image(
                chart,
                width=800
            )

    # -----------------------------
    # REFERENCES TAB
    # -----------------------------

    with tab3:

        st.subheader("Sources Used")

        for ref in references:

            st.markdown(
                f"- [{ref['title']}]({ref['url']})"
            )

    st.markdown("---")

    # -----------------------------
    # DOWNLOAD PDF
    # -----------------------------

    with open(pdf_path, "rb") as file:

        st.download_button(
            label="📥 Download PDF Report",
            data=file,
            file_name=f"{topic}_report.pdf",
            mime="application/pdf"
        )