import streamlit as st

st.title("🔬 Research Synthesis Tool Test")
st.write("If you can see this, Streamlit is working!")

# Test imports
try:
    from document_processor import DocumentProcessor
    st.success("✅ Document processor imported successfully")
except Exception as e:
    st.error(f"❌ Document processor error: {e}")

try:
    from rag_engine import RAGEngine  
    st.success("✅ RAG engine imported successfully")
except Exception as e:
    st.error(f"❌ RAG engine error: {e}")

try:
    from config import OPENAI_API_KEY
    if OPENAI_API_KEY:
        st.success("✅ API key loaded successfully")
    else:
        st.error("❌ API key is missing")
except Exception as e:
    st.error(f"❌ Config error: {e}")
