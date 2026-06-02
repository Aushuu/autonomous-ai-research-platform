from typing import TypedDict

from agents.researcher import ResearchAgent
from agents.analyzer import AnalyzerAgent
from agents.metrics_agent import MetricsAgent
from agents.chart_agent import ChartAgent
from agents.report_agent import ReportAgent
from agents.email_agent import EmailAgent
from agents.data_extractor import DataExtractorAgent

from rag.vector_store import VectorStore
from rag.rag_agent import RAGAgent

from langgraph.graph import StateGraph, END


class ReportState(TypedDict):

    topic: str
    research_data: list
    report_text: str
    statistics: dict
    metrics: dict
    chart_paths: list
    pdf_path: str
    email: str
    references: list


research_agent = ResearchAgent()
analyzer_agent = AnalyzerAgent()
metrics_agent = MetricsAgent()
chart_agent = ChartAgent()
report_agent = ReportAgent()
email_agent = EmailAgent()
data_extractor_agent = DataExtractorAgent()
vector_store = VectorStore()
rag_agent = RAGAgent()


def research_node(state):

    research_data = research_agent.research(
        state["topic"]
    )

    return {
        "research_data": research_data
    }


def analyzer_node(state):

    documents = []

    for item in state["research_data"]:
        documents.append(item["content"])

    vector_store.build_vector_db(documents)

    rag_context = rag_agent.get_context(state["topic"])

    report_text = analyzer_agent.analyze(
        state["topic"],
        state["research_data"],
        rag_context
    )

    return {
        "report_text": report_text
    }


def metrics_node(state):

    metrics = metrics_agent.extract_metrics(
        state["report_text"]
    )

    return {
        "metrics": metrics
    }
def statistics_node(state):

    statistics = data_extractor.extract_data(
        state["report_text"]
    )

    return {
        "statistics": statistics
    }


def chart_node(state):

    chart_paths = chart_agent.generate_charts(
        state["topic"],
        state["metrics"]
    )

    return {
        "chart_paths": chart_paths
    }


def references_node(state):

    references = []

    for item in state["research_data"]:

        references.append(
            {
                "title": item.get("title", ""),
                "url": item.get("url", "")
            }
        )

    return {
        "references": references
    }


def pdf_node(state):

    pdf_path = report_agent.generate_pdf(
        state["topic"],
        state["report_text"],
        state["chart_paths"],
        state["metrics"],
        state["references"]
    )

    return {
        "pdf_path": pdf_path
    }


def email_node(state):

    email = state.get("email", "")

    if email:

        email_agent.send_report(
            email,
            state["pdf_path"]
        )

    return {
        "email": email
    }


workflow = StateGraph(
    ReportState
)

workflow.add_node(
    "research",
    research_node
)

workflow.add_node(
    "analyze",
    analyzer_node
)

workflow.add_node(
    "extract_metrics",
    metrics_node
)

workflow.add_node(
    "chart",
    chart_node
)

workflow.add_node(
    "collect_references",
    references_node
)

workflow.add_node(
    "pdf",
    pdf_node
)

workflow.add_node(
    "send_email",
    email_node
)

workflow.set_entry_point(
    "research"
)

workflow.add_edge(
    "research",
    "analyze"
)

workflow.add_edge(
    "analyze",
    "extract_metrics"
)

workflow.add_edge(
    "extract_metrics",
    "chart"
)

workflow.add_edge("chart", "collect_references")
workflow.add_edge("collect_references", "pdf")

workflow.add_edge(
    "pdf",
    "send_email"
)

workflow.add_edge(
    "send_email",
    END
)

graph = workflow.compile()