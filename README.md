# 🐰 RABBIT - Resourceful Academic Book-Based Interactive Tutor

Welcome to RABBIT, your personal academic assistant! This interactive tool leverages advanced AI capabilities to help you with your studies by providing detailed explanations and answers to your academic questions.

This repo is mostly a modification of [Dropbox-ai-chat](https://github.com/pathway-labs/dropbox-ai-chat/tree/main)

#Demo
when you ask a question within the context of books 
<img src="assets/run1.gif" alt="Image" width="600"/>

when you ask a query or question out of context
<img src="assets/run2.gif" alt="Image" width="600"/>




## Table of Contents

1. Project Description
2. End User
3. Industry Impact
4. Business Value
5. Utilization of LLM App
6. Technical Implementation
7. Installation and Setup
8. Usage Instructions
9. Contributing
10. License

## Project Description

RABBIT is designed to assist students, educators, and academic professionals by providing instant, detailed answers to their academic inquiries. It enhances the learning experience through interactive and personalized support, making it a valuable tool in the education industry.

### End User

- Students at various educational levels (middle school to university)
- Educators seeking to provide additional support to their students
- Academic professionals needing quick and reliable information

### Industry Impact

RABBIT can transform the education industry by offering a scalable solution for academic assistance, enhancing the quality of learning and providing immediate support to users.

### Business Value

Integrating RABBIT into educational institutions, online learning platforms, and tutoring services can increase enrollment, retention rates, and customer satisfaction by offering a unique and interactive learning experience.

### Utilization of LLM App

RABBIT utilizes a Large Language Model (LLM) to process user queries and generate accurate responses in real-time, making it a powerful tool for academic support.

### Technical Implementation

- **Pathway**:Used for storing and retriving data fast and efficiently.
- **Streamlit**: Used for the front-end, creating an interactive web application.


## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repository/rabbit.git
    ```
2. **Open RABBIT**
  
   ```bash
    cd rabbit
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**:
    Create a `.env` file in the root directory with the following content:
    ```
    PORT=127.0.0.1
    PORT=8080
    OPENAI_API_TOKEN="PUT YOUR OPENAI API KEY HERE"
    EMBEDDER_LOCATOR=text-embedding-ada-002
    EMBEDDING_DIMENSION=1536
    MODEL_LOCATOR=gpt-3.5-turbo
    MAX_TOKENS=200
    TEMPERATURE=0.05
    DROPBOX_LOCAL_FOLDER_PATH="ADD DROPBOX PATH HERE"
    
    ```
5. **Run backend(Pathway)
    ```bash
    python main.py
    ```
      
6. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage Instructions

1. Open your web browser and navigate to `http://localhost:8501`.
2. Enter your academic question or doubt in the text input box.
3. Click 'Enter' to submit your query.
4. RABBIT will provide a detailed answer based on your query.

### Sidebar Instructions

1. Enter your question or doubt in the text input box below.
2. Click 'Enter'.
3. The RABBIT will provide a detailed answer based on your query.

## Contributing

We welcome contributions to enhance RABBIT! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
