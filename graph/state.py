from typing import Optional, List
from typing_extensions import TypedDict


class RoadmapState(TypedDict):
    # User input
    role: str
    
    # Agent outputs
    skills: List[str]
    documentation_links: dict
    roadmap: str
    pdf_path: Optional[str]
    
    # Status tracking
    error: Optional[str]
    is_complete: bool