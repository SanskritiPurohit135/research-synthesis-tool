from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config import RESEARCH_SYNTHESIS_PROMPT, ACADEMIC_WRITING_PROMPT
import os

class RAGEngine:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.llm = OpenAI(temperature=0.7, max_tokens=1500)
        
    def load_vector_store(self, persist_directory="./data/chroma_db"):
        """Load existing vector database"""
        if os.path.exists(persist_directory):
            vectorstore = Chroma(
                persist_directory=persist_directory,
                embedding_function=self.embeddings
            )
            return vectorstore
        return None
    
    def query_documents(self, query, vectorstore, num_docs=3):
        """Query documents using RAG"""
        retriever = vectorstore.as_retriever(search_kwargs={"k": num_docs})
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )
        
        response = qa_chain({"query": query})
        return response
    
    def comparative_analysis(self, vectorstore, papers_info):
        """Advanced comparative analysis across multiple papers"""
        
        # Demo comparative analysis - in real implementation this would use RAG
        comparative_results = {
            "methodology_comparison": """
            **Methodology Comparison Across Papers:**
            
            📊 **Research Approaches Used:**
            - **Paper 1**: Longitudinal climate data analysis (50-year dataset)
            - **Paper 2**: Experimental field trials with controlled conditions  
            - **Paper 3**: Economic modeling and statistical analysis
            - **Paper 4**: Remote sensing and satellite imagery analysis
            
            🔬 **Key Methodological Differences:**
            - **Temporal Scope**: Ranges from 5-year studies to 50-year analyses
            - **Geographic Scale**: Local field studies vs. global assessments
            - **Data Sources**: Primary field data vs. secondary climate records
            """,
            
            "findings_comparison": """
            **Cross-Paper Findings Analysis:**
            
            ✅ **Consistent Findings:**
            - All papers agree: Temperature increase negatively impacts crop yields
            - Consensus on 15-25% yield reduction in heat-stressed crops
            - Agreement on adaptation strategy effectiveness
            
            ⚠️ **Conflicting Results:**
            - **Drought Impact**: Paper 1 reports 20% yield loss, Paper 3 shows 35% loss
            - **Adaptation Timeline**: Estimates range from 5-15 years for full implementation
            - **Economic Costs**: Vary significantly by region and methodology
            
            🔍 **Research Gaps Identified:**
            - Limited data on developing country impacts
            - Insufficient long-term adaptation studies
            - Need for interdisciplinary economic-environmental models
            """,
            
            "research_evolution": """
            **Research Evolution Timeline:**
            
            📈 **Methodological Progression:**
            - **2010-2015**: Focus on temperature-yield correlations
            - **2016-2020**: Integration of precipitation and extreme weather
            - **2021-Present**: Holistic adaptation and resilience studies
            
            🧠 **Conceptual Development:**
            - Early work: Simple climate-crop relationships
            - Current research: Complex socio-economic-environmental systems
            - Future direction: AI-driven prediction and adaptation models
            
            💡 **Emerging Themes:**
            - Climate-smart agriculture gaining prominence
            - Interdisciplinary approaches becoming standard
            - Technology integration (IoT, AI, remote sensing)
            """
        }
        
        return comparative_results
    
    def generate_research_gaps(self, vectorstore):
        """Identify research gaps from multiple papers"""
        
        # Demo research gap analysis
        research_gaps = """
        **🔬 Identified Research Gaps:**
        
        **1. Geographic Coverage Gaps:**
        - Limited studies from Sub-Saharan Africa (only 12% of papers)
        - Insufficient data from small island developing states
        - Urban agriculture impacts largely unexplored
        
        **2. Methodological Gaps:**
        - Need for standardized climate impact metrics
        - Lack of long-term longitudinal studies (>20 years)
        - Limited integration of farmer behavioral data
        
        **3. Interdisciplinary Gaps:**
        - Disconnect between climate science and agricultural economics
        - Insufficient social science perspectives
        - Limited policy implementation studies
        
        **4. Technology Integration Gaps:**
        - AI/ML applications in adaptation strategies underexplored
        - IoT sensor data integration needs development
        - Precision agriculture scalability studies needed
        
        **🚀 Suggested Future Research Directions:**
        - Multi-stakeholder participatory research frameworks
        - Real-time climate adaptation monitoring systems  
        - Cross-cultural adaptation strategy effectiveness studies
        """
        
        return research_gaps
    
    def academic_writing_assistant(self, content, style="undergraduate"):
        """Convert content to different academic writing styles"""
        
        # Demo writing style transformations
        styles = {
            "simple": f"**Simple Explanation:**\n\nLet me break this down in easy terms:\n\n{content[:200]}...\n\nBasically, this research shows that climate change makes it harder to grow food, but scientists are working on solutions!",
            
            "undergraduate": f"**Undergraduate Analysis:**\n\nThis research synthesis examines key findings from multiple studies:\n\n{content[:300]}...\n\nThese findings have important implications for agricultural policy and food security planning.",
            
            "graduate": f"**Graduate-Level Analysis:**\n\nA comprehensive meta-analysis of the literature reveals:\n\n{content[:400]}...\n\nThese results contribute to our understanding of complex climate-agriculture interactions and suggest avenues for future interdisciplinary research.",
            
            "proposal": f"**Research Proposal Section:**\n\n**Literature Review Summary:**\nCurrent research demonstrates:\n\n{content[:350]}...\n\n**Research Objectives:** This study aims to address identified gaps through innovative methodological approaches combining quantitative analysis with stakeholder engagement frameworks."
        }
        
        return styles.get(style, content)
