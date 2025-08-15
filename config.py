import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Prompt Templates
RESEARCH_SYNTHESIS_PROMPT = """
You are an expert research analyst. Based on the following research document excerpts, provide a comprehensive synthesis.

Context: {context}

User Query: {query}

Provide a detailed analysis that includes:
1. Key findings and insights
2. Methodologies used
3. Implications and significance
4. Areas for future research

Response:
"""

ACADEMIC_WRITING_PROMPT = """
Convert the following research synthesis into {writing_style} style:

Original Content: {content}

Writing Styles:
- "simple": Explain like I'm 5 (ELI5)
- "undergraduate": University student level
- "graduate": Advanced academic level
- "proposal": Research proposal format

Style: {writing_style}

Response:
"""

# Advanced Comparative Analysis Prompts
COMPARATIVE_ANALYSIS_PROMPT = """
You are an expert research analyst performing comparative analysis across multiple research papers.

Based on the following documents about {topic}, provide a comprehensive comparative analysis:

Documents: {context}

Please analyze:
1. Methodological approaches used across papers
2. Consistent findings vs conflicting results  
3. Research evolution and trends
4. Identified knowledge gaps

Provide structured, detailed analysis:
"""

RESEARCH_GAPS_PROMPT = """
Based on your analysis of multiple research papers on {topic}, identify:

1. Geographic or demographic gaps in research coverage
2. Methodological limitations or gaps  
3. Interdisciplinary connections that need development
4. Future research directions that would advance the field

Context: {context}

Provide actionable research gap analysis:
"""
