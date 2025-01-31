import streamlit as st
from ml_app import run_ml_app

def main():
    menu = ['Home', 'Post Analysis']
    choice = st.sidebar.radio("Menu", menu)

    if choice == 'Home':
        st.markdown(
            """
            <h1 style='text-align: center;'>Monitor Public Opinion!</h1>
            <br>
            <h3 style='text-align: justify;'>Sentiment Analysis on Patrick Kluivert Becoming the Coach of Indonesia National Football Team</h3>
            <p style='text-align: justify;'>
                What is the public's reaction to the possibility of Patrick Kluivert becoming the head coach of the Indonesia National Football Team? With our sentiment analysis tool, you can track opinion trends on X in real-time! Does the majority support it? Are there criticisms? All data is summarized and easily understood.
            </p>
            <br>
            <h3 style='text-align: justify;'>Purpose of Sentiment Analysis</h3>
            <p style='text-align: justify;'>By analyzing sentiments, you can:</p>
            <ul>
                <li>Understand public perception of Patrick Kluivert's potential appointment.</li>
                <li>Identify key concerns and support levels among fans.</li>
                <li>Track changes in sentiment over time.</li>
            </ul>
            <p style='text-align: justify;'>By leveraging sentiment analysis, you can gain a clearer picture of public opinion and make informed conclusions.</p>
            <br>
            <p style='text-align: justify;'>
                <strong>Disclaimer:</strong> This tool is only to help analyze and may analyze sentiments incorrectly. Perform further analysis to reduce analysis errors!
            </p>
            <br>
            <p style='text-align: center;'><strong>Stay ahead and discover what people really think!</strong></p>
            """, 
            unsafe_allow_html=True
        )

    elif choice == "Post Analysis":
        run_ml_app()

if __name__ == '__main__':
    main()
