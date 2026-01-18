import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_groq_response_with_verification(query):
    """
    Get response with chain of verification to reduce hallucinations and bias.
    Returns a dict with: answer, confidence, has_bias, verification_notes, requires_refinement
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Please set it in your .env file.")
    
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3, groq_api_key=api_key)
    
    # Step 1: Initial response
    initial_prompt = PromptTemplate(
        input_variables=["query"],
        template="""Answer the following query factually and concisely. 
Be objective and avoid speculation.
Query: {query}

Provide a direct, factual answer:"""
    )
    initial_response = llm.invoke(initial_prompt.format(query=query))
    initial_text = initial_response.content if hasattr(initial_response, 'content') else str(initial_response)
    
    # Step 2: Verification - Check for accuracy and bias
    verification_prompt = PromptTemplate(
        input_variables=["query", "response"],
        template="""Evaluate the following response for accuracy, bias, and hallucinations.

Original Query: {query}
Response: {response}

Please evaluate:
1. Is this factually accurate? (Yes/No)
2. Does it contain any bias or one-sided perspective? (Yes/No)
3. Are there any unsupported or speculative claims? (Yes/No)
4. Confidence level (Low/Medium/High)
5. Any issues that need correction?

Format your response as:
Accuracy: [Yes/No]
Bias: [Yes/No]
Unsupported Claims: [Yes/No]
Confidence: [Low/Medium/High]
Issues: [list any problems or say "None"]"""
    )
    verification_response = llm.invoke(verification_prompt.format(query=query, response=initial_text))
    verification_text = verification_response.content if hasattr(verification_response, 'content') else str(verification_response)
    
    # Step 3: Extract verification metrics
    confidence = "Medium"
    if "Confidence: High" in verification_text:
        confidence = "High"
    elif "Confidence: Low" in verification_text:
        confidence = "Low"
    
    has_bias = "Bias: Yes" in verification_text
    has_errors = "Accuracy: No" in verification_text or "Unsupported Claims: Yes" in verification_text
    requires_refinement = has_errors or has_bias or confidence == "Low"
    
    # Step 4: If issues found, generate refined response
    if requires_refinement:
        refine_prompt = PromptTemplate(
            input_variables=["query", "original_response", "issues"],
            template="""Based on the verification feedback, provide an improved response.

Query: {query}
Previous Response: {original_response}

Issues Found: {issues}

Please provide a corrected, factual, and unbiased response.
Focus on accuracy, objectivity, and remove any biased or speculative language."""
        )
        refined_response = llm.invoke(refine_prompt.format(
            query=query, 
            original_response=initial_text,
            issues=verification_text
        ))
        final_text = refined_response.content if hasattr(refined_response, 'content') else str(refined_response)
    else:
        final_text = initial_text
    
    return {
        "answer": final_text,
        "confidence": confidence,
        "has_bias": has_bias,
        "verification_notes": verification_text,
        "requires_refinement": requires_refinement
    }

# ==================== Streamlit UI ====================
st.set_page_config(page_title="LangChain ChatBot", page_icon=":earth_americas:", layout="wide")

st.header("LangChain ChatBot - Powered by Groq")
st.markdown("*With Chain of Verification for Accuracy & Bias Reduction*")

# Check if API key is configured
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.warning("⚠️ Please configure your Groq API key in the .env file to use this chatbot.")
    st.info("Add GROQ_API_KEY=your_actual_key to your .env file")
    st.stop()

# Input section
st.subheader("Ask a Question")
input_query = st.text_input("Enter your query here:", key="input", placeholder="e.g., What is the capital of France?")

submit = st.button("Submit", use_container_width=True)

if submit and input_query:
    try:
        with st.spinner("Processing with chain of verification..."):
            result = get_groq_response_with_verification(input_query)
        
        # Display main answer
        st.subheader("Answer")
        st.write(result["answer"])
        
        # Display verification metrics in columns
        st.subheader("Verification Metrics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            confidence_color = "🟢" if result["confidence"] == "High" else "🟡" if result["confidence"] == "Medium" else "🔴"
            st.metric("Confidence Level", f"{confidence_color} {result['confidence']}")
        
        with col2:
            bias_indicator = "✅ No Bias" if not result["has_bias"] else "⚠️ Possible Bias"
            st.metric("Bias Check", bias_indicator)
        
        with col3:
            refinement_indicator = "✅ Original" if not result["requires_refinement"] else "🔄 Refined"
            st.metric("Response Type", refinement_indicator)
        
        # Expandable verification details
        with st.expander("📋 View Verification Details"):
            st.write("**Verification Analysis:**")
            st.text(result["verification_notes"])
            if result["requires_refinement"]:
                st.info("ℹ️ This response was automatically refined based on verification findings to improve accuracy and reduce bias.")
        
        # Additional info
        st.divider()
        st.caption("💡 **How it works:** Your query goes through a 4-step verification chain: (1) Generate response, (2) Verify accuracy & bias, (3) Assess confidence, (4) Refine if needed.")
        
    except ValueError as e:
        st.error(f"Configuration Error: {e}")
    except Exception as e:
        st.error(f"Error: {type(e).__name__}: {str(e)}")
        st.info("Please check that your Groq API key is valid and set in the .env file")
