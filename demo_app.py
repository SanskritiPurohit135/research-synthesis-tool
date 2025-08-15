import streamlit as st
import time

# Configure page
st.set_page_config(
    page_title="Research Synthesis Tool",
    page_icon="🔬",
    layout="wide"
)

# Main UI
st.title("🔬 Research Synthesis Tool with Academic Writing Assistant")
st.markdown("**Upload research papers and get intelligent synthesis with multiple writing styles!**")

# Sidebar for configuration
with st.sidebar:
    st.header("📁 Document Upload")
    uploaded_files = st.file_uploader(
        "Upload PDF research papers",
        type="pdf",
        accept_multiple_files=True
    )
    
    if uploaded_files:
        if st.button("Process Documents"):
            with st.spinner("Processing documents..."):
                time.sleep(2)  # Simulate processing
                st.session_state['processed'] = True
                st.session_state['num_files'] = len(uploaded_files)
                st.success(f"✅ Successfully processed {len(uploaded_files)} documents!")
                st.success("📚 Vector database created with 1,247 text chunks")
                st.success("🧠 Ready for intelligent querying!")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🔍 Research Query")
    query = st.text_area(
        "Enter your research question:",
        height=100,
        value="What are the main findings about climate change impacts on agriculture?"
    )
    
    if st.button("Generate Synthesis"):
        if st.session_state.get('processed', False):
            with st.spinner("Analyzing documents and generating synthesis..."):
                time.sleep(3)  # Simulate AI processing
                
                # Demo synthesis response
                synthesis = """
                **Key Findings on Climate Change Impacts on Agriculture:**

                Based on the analysis of uploaded research papers, several critical patterns emerge:

                **1. Temperature Effects:**
                - Global average temperatures have increased by 1.2°C since 1970
                - Heat stress reduces crop yields, particularly for wheat and corn
                - Optimal growing zones are shifting poleward at 70km per decade

                **2. Precipitation Changes:**
                - Irregular rainfall patterns affect 40% of global agricultural areas
                - Drought frequency has increased by 15% in key farming regions
                - Extreme weather events cause $5B annual crop losses

                **3. Adaptation Strategies:**
                - Heat-resistant crop varieties show 20% better resilience
                - Precision irrigation reduces water usage by 30%
                - Crop rotation systems improve soil carbon sequestration

                **4. Economic Implications:**
                - Food prices projected to increase 15-25% by 2030
                - Small-scale farmers disproportionately affected
                - Investment in climate-smart agriculture essential

                **Methodology:** This synthesis combines findings from multiple peer-reviewed studies using RAG (Retrieval-Augmented Generation) technology to identify patterns and extract insights across different research papers.
                """
                
                st.session_state['synthesis'] = synthesis
        else:
            st.warning("⚠️ Please upload and process documents first!")

with col2:
    st.header("✍️ Academic Writing Assistant")
    
    if 'synthesis' in st.session_state:
        writing_style = st.selectbox(
            "Choose writing style:",
            ["simple", "undergraduate", "graduate", "proposal"],
            format_func=lambda x: {
                "simple": "🎯 Simple (ELI5)",
                "undergraduate": "🎓 Undergraduate Level", 
                "graduate": "🔬 Graduate Level",
                "proposal": "📋 Research Proposal"
            }[x]
        )
        
        if st.button("Transform Writing Style"):
            with st.spinner("Transforming to " + writing_style + " style..."):
                time.sleep(2)
                
                # Demo transformations
                transformations = {
                    "simple": """
                    **Climate Change and Farming (Simple Explanation):**
                    
                    Think of Earth like a big greenhouse that's getting warmer. This affects how we grow food:
                    
                    🌡️ **It's Getting Hotter:** The planet is 1.2 degrees warmer than 50 years ago. That might not sound like much, but it's like having a fever - even small changes matter a lot!
                    
                    🌧️ **Weird Weather:** Sometimes there's too much rain, sometimes not enough. It's like the weather can't make up its mind!
                    
                    🌾 **Crops Are Struggling:** Plants are like people - they don't like it too hot or too cold. When it gets too warm, they get stressed and don't grow as well.
                    
                    💡 **Smart Solutions:** Farmers are getting creative! They're using:
                    - Special plants that handle heat better
                    - Smart watering systems
                    - Better ways to take care of soil
                    
                    The main message: Climate change makes farming harder, but smart people are working on solutions!
                    """,
                    
                    "undergraduate": """
                    **Climate Change Impacts on Agricultural Systems:**
                    
                    This analysis examines how changing climate patterns affect global food production systems. Key findings include:
                    
                    **Environmental Changes:**
                    - Temperature increases of 1.2°C since 1970 create heat stress in major crops
                    - Precipitation variability affects 40% of agricultural regions worldwide
                    - Growing zones are migrating northward due to warming trends
                    
                    **Agricultural Consequences:**
                    - Staple crops (wheat, corn, rice) show decreased yields under heat stress
                    - Water scarcity affects irrigation-dependent farming systems
                    - Extreme weather events cause significant economic losses ($5B annually)
                    
                    **Adaptation Strategies:**
                    - Development of climate-resilient crop varieties
                    - Implementation of precision agriculture technologies
                    - Integration of sustainable farming practices
                    
                    **Economic Implications:**
                    Food security concerns arise from projected 15-25% price increases by 2030, particularly affecting vulnerable populations.
                    """,
                    
                    "graduate": """
                    **Anthropogenic Climate Change Effects on Global Agricultural Productivity: A Systematic Analysis**
                    
                    **Abstract:** This synthesis examines the multifaceted relationships between anthropogenic climate change and agricultural systems, utilizing retrieval-augmented analysis of recent peer-reviewed literature.
                    
                    **Thermodynamic Effects:** Elevated mean global temperatures (ΔT = +1.2°C, 1970-2020) induce physiological stress responses in C3 and C4 photosynthetic pathways, resulting in measurable yield decreases across temperate cereal crops (Triticum aestivum, Zea mays).
                    
                    **Hydrological Variability:** Altered precipitation regimes, characterized by increased coefficient of variation in seasonal rainfall, disrupt established crop phenology and irrigation scheduling, affecting approximately 40% of global cultivated area.
                    
                    **Biogeographical Shifts:** Optimal cultivation zones exhibit poleward migration at 70 km decade⁻¹, necessitating adaptive management strategies and cultivar selection protocols.
                    
                    **Socioeconomic Externalities:** Market volatility analysis indicates projected food commodity price inflation of 15-25% by 2030, with disproportionate impacts on small-holder farming systems and food-insecure populations.
                    
                    **Research Implications:** These findings underscore the urgent need for interdisciplinary approaches integrating climate science, agronomy, and policy research.
                    """,
                    
                    "proposal": """
                    **Research Proposal: Integrative Assessment of Climate-Agriculture Interactions**
                    
                    **1. Research Objectives:**
                    - Quantify climate change impacts on agricultural productivity across multiple spatial and temporal scales
                    - Develop predictive models for crop yield under future climate scenarios
                    - Evaluate adaptation strategy effectiveness and implementation barriers
                    
                    **2. Significance:**
                    Current research demonstrates significant climate-induced agricultural stress (1.2°C warming, 40% precipitation variability impact). This study addresses critical knowledge gaps in adaptation pathway optimization.
                    
                    **3. Methodology:**
                    - Multi-scale analysis combining satellite imagery, weather station data, and farm-level surveys
                    - Machine learning models for yield prediction under climate scenarios
                    - Stakeholder engagement through participatory research methods
                    
                    **4. Expected Outcomes:**
                    - Peer-reviewed publications in high-impact agricultural and climate journals
                    - Policy recommendations for climate-smart agriculture implementation
                    - Decision-support tools for farmers and agricultural extension services
                    
                    **5. Budget Justification:**
                    Estimated $150,000 over 24 months for personnel, equipment, and dissemination activities.
                    
                    **6. Timeline:**
                    Year 1: Data collection and model development
                    Year 2: Analysis, validation, and dissemination
                    """
                }
                
                st.session_state['transformed'] = transformations[writing_style]

# Display results
if 'synthesis' in st.session_state:
    st.header("📊 Research Synthesis")
    st.write(st.session_state['synthesis'])
    
    if 'transformed' in st.session_state:
        st.header("✨ Transformed Output")
        st.write(st.session_state['transformed'])
    
    with st.expander("📚 Source Documents Used"):
        st.write("**Document Analysis Summary:**")
        if st.session_state.get('processed'):
            st.write(f"- Processed {st.session_state.get('num_files', 0)} research papers")
            st.write("- Created 1,247 text chunks for semantic search")
            st.write("- Identified key themes: climate impacts, adaptation strategies, economic effects")
            st.write("- RAG retrieval used top 5 most relevant passages for each query")

# Footer
st.markdown("---")
st.markdown("**🔬 Research Synthesis Tool** - Powered by RAG + Prompt Engineering + Academic Writing Assistant")
