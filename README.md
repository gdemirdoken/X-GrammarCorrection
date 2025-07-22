# X-GrammarCorrection
X-grammar correction service
FusionLearnX Grammar Corrector ✍️
Overview
FusionLearnX Grammar Corrector is a sleek and intuitive web application built with Streamlit and powered by Hugging Face Transformers. It allows users to input English sentences and receive instant grammar and spelling corrections, along with a side-by-side comparison of the original and corrected text.

This application is designed for anyone looking for quick and effective text refinement, from students and writers to professionals.

Features
Instant Grammar & Spelling Correction: Utilizes a fine-tuned T5 model (vennify/t5-base-grammar-correction) for accurate and context-aware corrections.

User-Friendly Interface: Clean and responsive design built with Streamlit.

Side-by-Side Comparison: Easily view the original sentence alongside its corrected version to understand the changes.

Dynamic Button State: The "Correct my sentence" button visually indicates its active state after submission.

Custom Styling: Features a custom aesthetic with a unique background, themed buttons, and text areas.

Responsive Design: Optimized for a smooth experience across various devices (desktop, tablet, mobile).

Live Demo
Experience the FusionLearnX Grammar Corrector live:
[Your Deployed App URL Here]

(Remember to replace https://your-app-name.streamlit.app/ with the actual URL after deploying your app to Streamlit Community Cloud.)

Technologies Used
Streamlit: For building the interactive web application.

Hugging Face Transformers: For leveraging powerful pre-trained language models.

Specifically, vennify/t5-base-grammar-correction for the core correction logic.

Python: The primary programming language.

CSS: For custom styling and visual enhancements.

Getting Started (Local Setup)
To run this application on your local machine, follow these steps:

Clone the Repository:

git clone https://github.com/your-username/streamlit-grammar-corrector.git
cd streamlit-grammar-corrector

(Replace your-username/streamlit-grammar-corrector.git with your actual GitHub repository URL)

Create a Virtual Environment (Recommended):

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install Dependencies:
The application requires streamlit and transformers. You can install them using the requirements.txt file.

pip install -r requirements.txt

(Ensure your requirements.txt contains streamlit and transformers)

Run the Application:

streamlit run app.py

Your browser should automatically open a new tab with the app (usually at http://localhost:8501). If not, copy the "Local URL" from your terminal and paste it into your browser.

Deployment (Streamlit Community Cloud)
This app can be easily deployed for free using Streamlit Community Cloud.

Push to GitHub: Ensure your app.py and requirements.txt files are pushed to a public GitHub repository.

Sign Up/Log In: Go to share.streamlit.io and sign in with your GitHub account.

Deploy New App: Click "New app," select your repository, branch (main or master), and the main file path (app.py).

Click "Deploy!": Streamlit will handle the rest, and your app will be live in minutes.

Usage
Enter Text: Type or paste the English sentence you want to correct into the provided text area.

Click "Correct my sentence": The application will process your input.

View Correction: The corrected sentence will appear below, along with a side-by-side comparison highlighting the changes.

Customization
Feel free to customize the app's appearance and functionality:

Styling: Modify the CSS within the <style> tags in app.py to change colors, fonts, button styles, and background.

Model: Experiment with other text-to-text generation models from the Hugging Face Model Hub by changing the model parameter in pipeline().

Layout: Adjust st.set_page_config(layout="centered") to "wide" for a broader app layout.

Content: Add more Streamlit components (st.sidebar, st.expander, etc.) to enhance your app.

Contributing
Contributions are welcome! If you have suggestions for improvements or find any issues, please open an issue or submit a pull request on the GitHub repository.

License
This project is open-source and available under the MIT License. (You might need to create a LICENSE file in your repo if you want to explicitly define this.)

Contact
For questions or feedback, please contact [Your Name/Email/LinkedIn/Website].
