# Smart ATS System

## Overview

This application leverages the power of generative AI to help you craft a resume that aligns perfectly with your target job descriptions. It offers actionable insights to enhance your resume's effectiveness and increase your chances of landing your dream job. It will give advice on how to increase your chances of success with your CV.

## Table of Contents
- [Disclaimer](#disclaimer)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Environment Setup](#environment-setup)
  - [API Key](#api-key)
  - [Running the Application](#running-the-application)
- [Key Features](#key-features)
- [Usage](#usage)
- [Contributing](#contributing)
  - [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
  - [Code Contributions](#code-contributions)

## Disclaimer

The accuracy of the generated responses is dependent on the quality of the input data and the capabilities of the underlying generative AI model. It's recommended to use this application as a guide and to carefully review its suggestions before making any final changes to your resume.

## Getting Started

### Prerequisites

- Python (>=3.9)
- Other prerequisites are mentioned in requirements.txt

### Environment Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Deepak-porwal04/smart-ats-system.git
   cd smart-ats-system

2. **Create a virtual environment:**
    ```bash
    conda create -p venv python==3.9
    ```
    ```bash
    conda activate venv/
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **create a .env file in project root, and write:**
```bash
API_KEY = 'your_api_key_here'
```

### API Key

- visit https://makersuite.google.com/

- Click on *Get API key*

- Now click on *Create API key in new project*

- Copy the API Key and keep it secure


### Running the Application

- After having the [Environment Setup](#environment-setup). Run the following command:
```bash
streamlit run app.py
```

## Key Features
- **Resume Summary**: Provides a comprehensive overview of your resume's strengths and weaknesses in relation to a specific job description.
- **Percentage Match**: Evaluates the compatibility of your resume with a job description, offering a percentage score and key reasons for the assessment.
- **Improvement Tips**: Recommends specific ways to strengthen your resume and make it more appealing to potential employers.
- **Missing Keyword Identification**: Pinpoints essential keywords that are absent from your resume but are crucial for the job role, suggesting additions to enhance its relevance.

## Usage
- Open the application in your browser.
- Paste the job description in the provided text area.
- Upload your resume in PDF format.
- Choose the desired analysis:
   - "Resume Summary" to get a general evaluation.
   - "Check the percentage match" to assess compatibility.
   - "Tips to improve the resume" to receive specific suggestions.
   - "Check the missing Keywords" to identify important keywords to include.
- Click the corresponding button to generate the AI-powered response.

## Contributing

Contributions are most welcomed. If you're interested in improving this project, here's how you can get involved:

### Bug Reports and Feature Requests

If you come across any issues or have ideas for new features, please let me know by [opening an issue](https://github.com/Deepak-porwal04/smart-ats-system/issues). Provide detailed information about the problem or your feature request, and we'll do our best to address it.

### Code Contributions

If you'd like to contribute code to this project, follow these simple steps:

1. **Fork the Repository:**
   - Click on the "Fork" button at the top right of the [project repository](https://github.com/Deepak-porwal04/smart-ats-system) page.

2. **Clone Your Fork:**
   - Clone your forked repository to your local machine.
     ```bash
     git clone https://github.com/Deepak-porwal04/smart-ats-system.git
     cd smart-ats-system
     ```

3. **Create a Branch:**
   - Create a new branch for your changes.
     ```bash
     git checkout -b feature-or-fix-branch
     ```

4. **Make Changes:**
   - Make your code changes and improvements.

5. **Commit Changes:**
   - Commit your changes with a descriptive commit message.
     ```bash
     git add .
     git commit -m "Your descriptive commit message"
     ```

6. **Push Changes:**
   - Push your changes to your fork on GitHub.
     ```bash
     git push origin feature-or-fix-branch
     ```

7. **Submit a Pull Request:**
   - Open a pull request (PR) against the main repository.
   - Provide a clear title and description for your PR.

Let me review your contributions and work with you to integrate them into the project.

