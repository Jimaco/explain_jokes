import streamlit as st
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Title of the app
st.title("Joke Explainer")

# Text box for the user to enter a joke
joke = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke:
        try:
            # Sending the joke to the OpenAI API for explanation
            #response = openai.ChatCompletion.create(
            #    model="gpt-40-mini",  # Replace with the correct model if necessary
            #    messages=[
            #        {"role": "user", "content": f"Explain this joke: {joke}"}
            #    ]
            #)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"Explain this joke: {joke}"}
                ]
            )


            # Print the response from the model
            #explanation = response['choices'][0]['message']['content']
            explanation = response.choices[0].message.content
            st.subheader("Explanation")
            st.write(explanation)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a joke before submitting.")
