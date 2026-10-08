import streamlit as st
import pandas as pd
import json
from datetime import datetime

st.set_page_config(page_title="AI Technical SEO & Schema Automation", page_icon="🔎", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.2rem; max-width: 1400px;}
[data-testid="stSidebar"] {background: #f7f9fc;}
.metric-card {padding: 18px; border: 1px solid #e5e7eb; border-radius: 14px; background: white;}
.issue {padding: 12px 16px; border-radius: 10px; border: 1px solid #e5e7eb; margin: 8px 0;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

pages = ["Dashboard","Site Audit","AI SEO","Schema Automation","Crawl Issues","Recommendations","Reports","Settings"]
with st.sidebar:
    st.title("🔎 SEO Automation")
    st.caption("AI + Technical SEO + Schema")
    for p in pages:
        if st.button(p, use_container_width=True, type="primary" if st.session_state.page == p else "secondary"):
            st.session_state.page = p
    st.divider()
    st.success("System ready")
    st.caption("Prototype data layer • v1.0")

def score_card(label, value, delta=""):
    st.markdown(f'<div class="metric-card"><b>{label}</b><h2>{value}</h2><small>{delta}</small></div>', unsafe_allow_html=True)

if st.session_state.page == "Dashboard":
    st.title("AI Technical SEO & Schema Automation")
    st.caption("One console for crawling, technical SEO intelligence, structured data and AI-powered recommendations.")
    cols = st.columns(5)
    for c, (l,v,d) in zip(cols, [
        ("SEO Health","87/100","+6 this week"),
        ("Schema Coverage","78%","+12%"),
        ("Indexability","91%","+4%"),
        ("Critical Issues","7","-9 resolved"),
        ("AI Opportunities","23","+8 detected")]):
        with c: score_card(l,v,d)
    st.subheader("SEO Health Overview")
    chart = pd.DataFrame({"Category":["Crawl","Indexability","Schema","Metadata","Links"],
                          "Score":[94,91,78,86,82]}).set_index("Category")
    st.bar_chart(chart)
    st.subheader("Priority Actions")
    for x in ["Fix 4 pages with missing canonical tags","Add Product schema to 6 product URLs",
              "Resolve 3 broken internal links","Improve 8 pages with duplicate meta titles"]:
        st.markdown(f'<div class="issue">⚠️ {x}</div>', unsafe_allow_html=True)

elif st.session_state.page == "Site Audit":
    st.title("🕷️ Site Audit")
    url = st.text_input("Website URL", "https://example.com")
    if st.button("Run Technical Audit", type="primary"):
        st.success(f"Audit completed for {url}")
        data = pd.DataFrame([
            ["Pages crawled",120,"Healthy"],["200 responses",108,"Healthy"],
            ["4xx/5xx errors",7,"Critical"],["Missing canonicals",4,"Warning"],
            ["Duplicate titles",8,"Warning"],["Missing meta descriptions",11,"Warning"],
            ["Broken internal links",3,"Critical"],["XML sitemap",1,"Healthy"]
        ], columns=["Check","Count","Status"])
        st.dataframe(data, use_container_width=True, hide_index=True)
    else:
        st.info("Enter a website and run the audit. Connect a crawler/API in production for live crawling.")

elif st.session_state.page == "AI SEO":
    st.title("🤖 AI SEO Intelligence")
    content = st.text_area("Paste page content or an audit finding", height=180)
    if st.button("Generate AI Recommendations", type="primary"):
        st.subheader("AI Recommendations")
        recs = [
            "Prioritize pages with indexability and canonical conflicts before content optimization.",
            "Rewrite duplicate title tags around unique search intent and primary entities.",
            "Strengthen internal links from high-authority pages to underlinked commercial pages.",
            "Add structured data only where the visible page content supports the properties."
        ]
        for r in recs: st.markdown("• " + r)
        st.download_button("Download recommendations", "\n".join(recs), "ai_seo_recommendations.txt")

elif st.session_state.page == "Schema Automation":
    st.title("🧩 Schema Automation")
    st.caption("Generate production-ready JSON-LD from page information.")
    url = st.text_input("Page URL", "https://example.com/product/example")
    schema_type = st.selectbox("Schema type", ["Product","Organization","LocalBusiness","Article","Service","FAQPage","BreadcrumbList","WebSite","WebPage","Person","Event"])
    name = st.text_input("Entity / page name", "Example Product")
    description = st.text_area("Description", "A useful description of the page or entity.")
    if st.button("Generate JSON-LD", type="primary"):
        if schema_type == "Product":
            obj = {"@context":"https://schema.org","@type":"Product","name":name,"description":description,"url":url}
        elif schema_type == "Organization":
            obj = {"@context":"https://schema.org","@type":"Organization","name":name,"description":description,"url":url}
        elif schema_type == "Article":
            obj = {"@context":"https://schema.org","@type":"Article","headline":name,"description":description,"url":url}
        else:
            obj = {"@context":"https://schema.org","@type":schema_type,"name":name,"description":description,"url":url}
        pretty = json.dumps(obj, indent=2)
        st.code(pretty, language="json")
        st.download_button("Download schema.json", pretty, "schema.json", "application/json")
        st.success("Schema generated. Validate against the page's visible content before deployment.")

elif st.session_state.page == "Crawl Issues":
    st.title("🚨 Crawl Issues")
    df = pd.DataFrame([
        ["ERR-001","Broken internal link","/services","/contact-us","Critical","Open"],
        ["ERR-002","Missing canonical","/products/a","","High","Open"],
        ["ERR-003","Duplicate title","/blog/a","","Medium","Open"],
        ["ERR-004","4xx response","/old-page","","Critical","Resolved"],
        ["ERR-005","Thin content","/service-b","","Medium","Open"]
    ], columns=["ID","Issue","Source","Target","Priority","Status"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button("Export crawl issues CSV", df.to_csv(index=False), "crawl_issues.csv", "text/csv")

elif st.session_state.page == "Recommendations":
    st.title("💡 Recommendations")
    df = pd.DataFrame([
        ["Canonical cleanup","Technical","High","4 pages","Add self-referencing canonicals"],
        ["Schema expansion","Structured Data","High","6 pages","Deploy Product schema"],
        ["Internal linking","Content","Medium","12 pages","Add contextual links"],
        ["Metadata cleanup","On-page","Medium","8 pages","Rewrite duplicate titles"]
    ], columns=["Opportunity","Area","Priority","Affected Pages","Recommended Action"])
    st.dataframe(df, use_container_width=True, hide_index=True)

elif st.session_state.page == "Reports":
    st.title("📊 Reports & Exports")
    st.write("Generate audit and schema reports for SEO teams, clients or management.")
    report = {
        "generated_at": datetime.now().isoformat(),
        "technical_seo_score": 87,
        "schema_coverage": 78,
        "indexability": 91,
        "critical_issues": 7,
        "ai_opportunities": 23
    }
    st.json(report)
    st.download_button("Download SEO report JSON", json.dumps(report, indent=2), "seo_report.json", "application/json")

else:
    st.title("⚙️ Settings")
    st.checkbox("Enable scheduled crawling", value=True)
    st.checkbox("Enable AI recommendations", value=True)
    st.checkbox("Enable automatic schema suggestions", value=True)
    st.selectbox("Currency", ["ZAR (R)","USD ($)","EUR (€)"])
    st.info("Production connectors can be added for Google Search Console, GA4, a crawler and Looker Studio.")
