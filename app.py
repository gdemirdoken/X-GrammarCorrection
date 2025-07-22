import streamlit as st
from transformers import pipeline

# --- Page Configuration ---
st.set_page_config(
    page_title="X Grammar Corrector",
    page_icon="⭐",
    layout="wide"
)

# --- Custom CSS for Buttons and Background ---
st.markdown("""
<style>
/* Target the main app view container for a full background image */
[data-testid="stAppViewContainer"] {
    background-color: #FFFFFF;
    background-repeat: no-repeat;
}

/* Set transparency for the main content block */
.main .block-container {
    background-color: rgba(255, 255, 255, 0.95); /* White background with 85% opacity */
    /* You can adjust the last value (0.85) from 0.0 (fully transparent) to 1.0 (fully opaque) */
    border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    padding-top: 2rem;
    padding-right: 1rem;
    padding-left: 1rem;
    padding-bottom: 2rem;
    max-width: 700px; /* Optional: Constrain max width for better readability on wide screens */
    margin: 30px auto; /* Center the whole content block horizontally */
}

/* Style for the main button (e.g., "Correct my sentence") */
div.stButton > button {
    background-color: #0000FF; /* Blue - This should now work! */
    color: white;
    padding: 20px 40px;
    border: none;
    border-radius: 8px; /* Rounded corners */
    font-size: 26px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
    /* Removed width: 20%; */ /* Allow button to take natural width */
}

/* MODIFIED: Add centering to the Streamlit button's wrapper div */
div.stButton {
    display: flex; /* Use flexbox */
    justify-content: center; /* Center horizontally */
    width: 100%; /* Ensure it takes full width of its parent column */
    margin-top: 20px; /* Space above button */
    margin-bottom: 20px; /* Space below button */
}

/* Style for text areas (input/output boxes) */
.stTextArea > div > div > textarea {
    background-color: #FFFFFF; /* white */
    border: 2px solid #0000FF; /* blue border */
    border-radius: 10px;
    padding: 20px;
    font-size: 20px;
    box-shadow: inset 1px 1px 3px rgba(0,0,0,0.1);
    resize: vertical; /* Allow vertical resizing */
}

/* Style for the main container (where your app content sits) */
.main .block-container {
    padding-top: 2rem;
    padding-right: 1rem;
    padding-left: 1rem;
    padding-bottom: 2rem;
    background-color: rgba(255, 255, 255, 0.95); /* Slightly transparent white background for content area */
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Soft shadow for the container */
}

/* Style for titles (h1, h2 etc.) */
h1 {
    color: #FFFFFF; /* Bright blue for the main title */
    text-align: center;
    font-family: 'Calibri', Constantia;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.15);
    margin-top: 0; /* Remove default top margin */
    margin-bottom: 20px; /* Space below title */
}

/* Style for subheaders */
h2, h3, h4 {
    color: #FFFFFF; /* Black for subheaders */
}

/* Style for st.write text */
.stMarkdown p {
    font-size: 1.5em;
    line-height: 1.2;
    color: #555555;
    text-align: center;
    margin-bottom: 5px; /* Space below paragraphs */
}

/* Style for st.warning and st.info alerts */
.stAlert {
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


# --- Page Title and Description ---
st.title("⭐ X Grammar Corrector ⭐")
st.write("Enter an English sentence below to get grammar and spelling corrections.")
st.markdown("---") # Add a separator

# --- Model Loading (Cached for Performance) ---
# Use a model specifically fine-tuned for grammar correction
# 'vennify/t5-base-grammar-correction' is a good option.
# The first time you run this, it will download the model, which might take a few minutes.
@st.cache_resource
def load_grammar_corrector_model():
    """
    Loads a pre-trained text2text-generation pipeline from Hugging Face for grammar correction.
    """
    # For grammar correction, a model specifically fine-tuned for the task works best.
    # 'vennify/t5-base-grammar-correction' is trained on a grammar correction dataset (JFLEG).
    # You might need to add a "grammar:" prefix for this model as per its documentation.
    return pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

# Load the model
with st.spinner("Loading the grammar correction model... This may take a moment the first time."):
    corrector = load_grammar_corrector_model()

# --- User Input ---
user_input = st.text_area(
    "**Your Sentence:**",
    placeholder="Type or paste your sentence here...",
    height=100
)

# --- Correction Button and Logic ---
if st.button("✨ Correct my sentence"):
    if user_input.strip(): # Check if input is not empty or just whitespace
        with st.spinner("Analyzing and correcting your sentence..."):
            try:
                # The 'vennify/t5-base-grammar-correction' model expects a "grammar: " prefix
                # This helps the model understand the task.
                prompt = f"grammar: {user_input}"

                # Generate response
                # You can experiment with max_length to control output length
                # num_beams can improve quality but increases inference time
                result = corrector(prompt, max_length=200, num_beams=5)[0]['generated_text']

                st.subheader("✅ Corrected Sentence:")
                st.info(result) # Use st.info for a visually distinct output
                
                # Optional: Show original and corrected side-by-side for comparison
                st.markdown("---")
                st.subheader("Comparison:")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Original:**")
                    st.write(user_input)
                with col2:
                    st.write("**Corrected:**")
                    st.write(result)


            except Exception as e:
                st.error(f"An error occurred during correction: {e}")
                st.warning("Please try a different sentence or refresh the page.")
    else:
        st.warning("☝️ Please enter a sentence to be corrected.")

st.markdown("---")

# --- 7. Foreground Logo Image (Now at the bottom, centered using st.columns) ---
# Use st.columns to reliably center the image.
logo_col1, logo_col2, logo_col3 = st.columns([1.45, 1, 1]) # Adjust ratios as needed

with logo_col2: # Place the image in the middle column
    st.image("https://myarticulatestorylineprojects.s3.eu-central-1.amazonaws.com/Logo/Transparent/TransparentLogo-FusionLearnX-TransparentLogo-Alternate2.png",
             width=200) # Adjust the width (in pixels) as desired

st.caption("Powered by FusionLearnX")