from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from graph.state import RoadmapState
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize LLM and Tavily
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# ─────────────────────────────────────────
# NODE 1: Analyze Role & Extract Skills
# ─────────────────────────────────────────
def analyze_role_node(state: RoadmapState) -> dict:
    prompt = f"""
    You are an expert career counselor.
    The user wants to become a: {state['role']}
    
    Your task is to list the TOP 10 most important skills needed to become a {state['role']}.
    
    Rules:
    - Return ONLY a numbered list of skills
    - No extra explanation
    - Each skill on a new line
    - Format: 1. Skill Name
    
    Example:
    1. Python Programming
    2. Machine Learning
    3. Data Analysis
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Parse skills from response
    lines = response.content.strip().split('\n')
    skills = []
    for line in lines:
        line = line.strip()
        if line and line[0].isdigit():
            skill = line.split('.', 1)[-1].strip()
            if skill:
                skills.append(skill)
    
    return {"skills": skills}


# ─────────────────────────────────────────
# NODE 2: Search Documentation Links
# ─────────────────────────────────────────
def search_docs_node(state: RoadmapState) -> dict:
    documentation_links = {}
    
    for skill in state['skills']:
        try:
            results = tavily.search(
                query=f"{skill} official documentation site",
                max_results=1
            )
            
            if results and results.get('results'):
                url = results['results'][0]['url']
                documentation_links[skill] = url
            else:
                documentation_links[skill] = f"https://www.google.com/search?q={skill}+documentation"
                
        except Exception:
            documentation_links[skill] = f"https://www.google.com/search?q={skill}+documentation"
    
    return {"documentation_links": documentation_links}


# ─────────────────────────────────────────
# NODE 3: Generate Full Roadmap
# ─────────────────────────────────────────
def generate_roadmap_node(state: RoadmapState) -> dict:
    skills_with_links = ""
    for skill, link in state['documentation_links'].items():
        skills_with_links += f"- {skill}: {link}\n"
    
    prompt = f"""
    You are an expert career mentor. Generate a detailed, structured roadmap for someone who wants to become a {state['role']}.

    Skills needed (with documentation links):
    {skills_with_links}

    Create a comprehensive roadmap with this EXACT structure:

    # 🎯 Career Roadmap: {state['role']}

    ## 📋 Overview
    Write 2-3 lines about this role and its importance.

    ## 🛠️ Skills Required
    List each skill as a bullet point with its documentation link.
    Format: • Skill Name → Documentation Link

    ### Phase 1: Foundation (Month 1-2)
    - List what to learn in bullet points
    - Be specific and detailed

    ### Phase 2: Core Skills (Month 3-4)
    - List what to learn in bullet points
    - Be specific and detailed

    ### Phase 3: Advanced Skills (Month 5-6)
    - List what to learn in bullet points
    - Be specific and detailed

    ### Phase 4: Projects & Portfolio (Month 7-8)
    - List project ideas
    - What to build to showcase skills

    ### Phase 5: Job Ready (Month 9-10)
    - Interview preparation
    - Resume tips
    - Where to apply

    ## 💡 Pro Tips
    - 3-4 important tips for success in this role

    ## ⏱️ Estimated Timeline
    Write total estimated time to become job ready.

    Make it detailed, motivating and easy to understand for a beginner.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "roadmap": response.content,
        "is_complete": True
    }