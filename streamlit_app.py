import streamlit as st

# Inject custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
        background-color: #f0f2f6; /* Light grey background for a clean look */
    }

    h1 {
        font-size: 2.5rem;
        color: #007bff; /* Bootstrap primary blue */
        animation: fadeIn 2s ease-in-out;
        display: flex;
        align-items: center;
    }

    h1 i {
        margin-right: 10px;
    }

    p {
        font-size: 1.2rem;
        color: #333;
        animation: slideIn 2s ease-in-out;
    }

    .highlight {
        background-color: #ffeb3b; /* Material yellow */
        padding: 0.2em;
        border-radius: 0.2em;
        color: #d32f2f; /* Material red */
        font-weight: bold;
    }

    .highlight-blue {
        background-color: #bbdefb; /* Light blue */
        padding: 0.2em;
        border-radius: 0.2em;
        color: #0d47a1; /* Dark blue */
        font-weight: bold;
    }

    .highlight-box {
        display: inline-block;
        background-color: #d32f2f; /* Bootstrap primary blue */
        color: white;
        padding: 0.5em;
        border-radius: 0.5em;
        animation: bounce 2s infinite;
        font-weight: bold;
    }

    .icon-box {
        display: inline-block;
        background-color: #e3f2fd; /* Light blue background */
        padding: 1em;
        border-radius: 50%;
        margin-right: 10px;
        color: #1976d2; /* Medium blue */
    }

    .content-box {
        background-color: #ffffff; /* White background for content */
        padding: 2em;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from {
            transform: translateX(-100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-30px);
        }
        60% {
            transform: translateY(-15px);
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit content
st.markdown('<h1><i class="fas fa-heartbeat"></i>Health Insurance Predictor</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="content-box">
    <div class="icon-box">
        <i class="fas fa-user-md"></i>
    </div>
    <div style="display: inline-block; vertical-align: top;">
        <p>Predict your health insurance premium with our advanced algorithm.</p>
    </div>
</div>
""", unsafe_allow_html=True)

