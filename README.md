# Cyber Jarvis

Cyber Jarvis enables users to ask questions and get answers on various cybersecurity topics through a text-based conversational interface. This tool operates using a model hosted on the [Hugging Face Hub](https://huggingface.co/).

![Cyber Jarvis](https://th.bing.com/th/id/OIG4.EV_F4G1xQ_Xa32BENOOg?pid=ImgGn)

## Features

- Users can input text to ask a question or send a message.
- The history section allows users to see their previous interactions and ask questions related to the history.
- The settings section enables users to customize different parameters for text generation.

## How to Use

1. **Text Input:** Write a question or message in the text box on the left.
2. **Parameter Settings:** Adjust parameters such as temperature, max new tokens, top-p (nucleus sampling), and repetition penalty using the sliders on the right.
3. **Send:** Click the "Send" button to submit your message and see the response.

## Technologies Used

- [Streamlit](https://streamlit.io/): A Python library used to create web-based applications.
- [Hugging Face Hub](https://huggingface.co/): A platform for sharing and using natural language processing (NLP) models.

## Installation

1. Clone the project files from this repository.
2. Create a virtual environment using the `requirements.txt` file to install the necessary packages.
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application by executing the following command:
    ```bash
    streamlit run app.py
    ```

## Contribution

If you'd like to contribute, please open a pull request or create an issue. Any contributions and feedback are greatly appreciated!
