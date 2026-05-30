from langgraph.graph import StateGraph, END
from graph.state import RoadmapState
from graph.nodes import analyze_role_node, search_docs_node, generate_roadmap_node


def build_roadmap_graph():
    # Initialize the graph with our state
    graph = StateGraph(RoadmapState)
    
    # ─────────────────────────────────────────
    # Add All Nodes
    # ─────────────────────────────────────────
    graph.add_node("analyze_role", analyze_role_node)
    graph.add_node("search_docs", search_docs_node)
    graph.add_node("generate_roadmap", generate_roadmap_node)
    
    # ─────────────────────────────────────────
    # Connect Nodes With Edges
    # ─────────────────────────────────────────
    graph.set_entry_point("analyze_role")
    graph.add_edge("analyze_role", "search_docs")
    graph.add_edge("search_docs", "generate_roadmap")
    graph.add_edge("generate_roadmap", END)
    
    # ─────────────────────────────────────────
    # Compile and Return Graph
    # ─────────────────────────────────────────
    return graph.compile()