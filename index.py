import streamlit as st

# Paste your HTML as a multi-line string
html_code = """
<!DOCTYPE html>
<html>

<body>
    <h1 style="color: rgb(0, 92, 128);width:100%;text-align:center">
        Demo: Embedding Google Forms on a Website
    </h1>

    <p style="width:100%;text-align:center">
        How to embed Google Forms 
        on any website?
    </p>


    <!-- Specify the <iframe> given by the
        the Google Forms embed page -->
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdQXR125YOsMT8LKqaak75XjFG0ODK4otMnt3q_SITGqq1xwQ/viewform?embedded=true" 
        width="550" height="600" 
        frameborder="0" marginheight="0"
        marginwidth="0"
        style="width:100%;text-align:center">
        Loading…
    </iframe>
</body>

</html>
"""
st.html(html_code)
st.iframe("https://docs.google.com/forms/d/e/1FAIpQLSdQXR125YOsMT8LKqaak75XjFG0ODK4otMnt3q_SITGqq1xwQ/viewform?embedded=true") 

