# ProfilePal - The chatbot for your profile


Welcome to ProfilePal, the smart chatbot designed to enhance your professional presence! Imagine having a personal assistant that knows everything about your achievements, skills, and experiences, ready to answer any question about your profile at any time.

With ProfilePal, your portfolio website transforms into an interactive experience. Leveraging the power of Llama3 and Streamlit, ProfilePal offers instant, accurate responses based on your detailed resume and portfolio, all stored securely in a vector database. Whether you're showcasing your projects, detailing your work history, or highlighting your unique talents, ProfilePal ensures visitors get the information they need effortlessly.

## Key Features

- **Instant Answers**: Visitors can interact with ProfilePal to quickly learn about your background, projects, and expertise.
- **Smart Retrieval**: Using advanced Retrieval-Augmented Generation (RAG), ProfilePal fetches the most relevant information from your stored documents.
- **Seamless Integration**: Easily integrates into your existing static portfolio website, adding a dynamic chat feature without any hassle.
- **Continuous Learning**: ProfilePal adapts and improves over time, ensuring it always provides the best answers.

## Installation

To integrate ProfilePal into your portfolio, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/s-suryakiran/ProfilePal.git
    ```

2. Navigate to the project directory:
    ```sh
    cd profilepal
    ```

3. Install the necessary dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your environment variables for Llama3 and vector database:
    - Create a `.streamlit` directory in the project root:
      ```sh
      mkdir .streamlit
      ```

    - Create a `secrets.toml` file in the `.streamlit` directory and add your secrets:
      ```toml
      # .streamlit/secrets.toml
      NVIDIA_API_KEY = "YOUR_NVIDIA_API_KEY"
      PINECONE_API_KEY = "YOUR_PINECONE_API_KEY"
      INDEX_NAME = "YOUR_PINECONE_INDEX_NAME"
      ```

5. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

Integrate the chat feature into your static portfolio website by embedding the provided chat widget code snippet. Customize the appearance and behavior to match your site’s design and functionality.

## Contributing

I welcome contributions to enhance ProfilePal! Feel free to fork the repository, create a branch, and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Make your profile stand out with ProfilePal – the ultimate chatbot companion that turns your static portfolio into an engaging, interactive showcase of your professional journey.
