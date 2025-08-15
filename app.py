import streamlit as st
import os
from document_processor import DocumentProcessor
from rag_engine import RAGEngine

# Configure page
st.set_page_config(
    page_title="Research Synthesis Tool",
    page_icon="🔬",
    layout="wide"
)

# Initialize components
@st.cache_resource
def init_components():
    return DocumentProcessor(), RAGEngine()

doc_processor, rag_engine = init_components()

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
                try:
                    all_text = ""
                    for file in uploaded_files:
                        text = doc_processor.process_pdf(file)
                        all_text += f"\n\nDocument: {file.name}\n{text}"
                    
                    # Create vector store
                    vectorstore = doc_processor.create_vector_store(all_text)
                    st.session_state['vectorstore'] = vectorstore
                    st.success(f"Processed {len(uploaded_files)} documents!")
                except Exception as e:
                    st.error(f"Error processing documents: {e}")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🔍 Research Query")
    query = st.text_area(
        "Enter your research question:",
        height=100,
        placeholder="What are the main findings about climate change impacts on agriculture?"
    )
    
    if st.button("Generate Synthesis"):
        if 'vectorstore' in st.session_state and query:
            with st.spinner("Generating research synthesis..."):
                try:
                    response = rag_engine.query_documents(query, st.session_state['vectorstore'])
                    st.session_state['synthesis'] = response['result']
                    st.session_state['sources'] = response.get('source_documents', [])
                except Exception as e:
                    st.error(f"Error generating synthesis: {e}")
        else:
            st.warning("Please upload and process documents first!")

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
            with st.spinner("Transforming writing style..."):
                try:
                    transformed = rag_engine.academic_writing_assistant(
                        st.session_state['synthesis'], 
                        writing_style
                    )
                    st.session_state['transformed'] = transformed
                except Exception as e:
                    st.error(f"Error transforming text: {e}")

# Display results
if 'synthesis' in st.session_state:
    st.header("📊 Research Synthesis")
    st.write(st.session_state['synthesis'])
    
    if 'transformed' in st.session_state:
        st.header("✨ Transformed Output")
        st.write(st.session_state['transformed'])
    
    with st.expander("📚 Source Documents"):
        for i, doc in enumerate(st.session_state.get('sources', [])):
            st.write(f"**Source {i+1}:**")
            st.write(doc.page_content[:500] + "...")
