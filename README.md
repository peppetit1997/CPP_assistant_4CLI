# CPP_assistant_4CLI

This project implements a simple Command Line Interface (CLI) chat application that interacts with the OpenAI API to provide assistance with C++ programming queries.

## Prerequisites

- Python 3.x
- curses library (usually comes pre-installed with Python)

## Installation

1. Clone this repository to your local machine:

```
git clone <repository_url>
```

2. Navigate to the project directory:

```
cd <project_directory>
```

3. Install required Python packages:

```
pip install -r requirements.txt
```

## Usage

To start the C++ Helper CLI Chat application, run the following command:

```
python <path_to_main_script>
```

Once the application is running, follow the on-screen instructions to prompt the AI about C++ and receive assistance.

### Note:

- Press "Q" or "q" at any time to quit the application.

## Configuration

Before running the application, ensure you have an OpenAI API key. You can obtain one from the [OpenAI website](https://openai.com/).

Once you have obtained your API key, create a file named `apikey.py` in the project directory and define a variable `openaiApikey` containing your API key:

```python
openaiApikey = "YOUR_API_KEY_HERE"
```

## Features

- Queries the OpenAI GPT-3 model for assistance with C++ programming.
- Persists chat history and index to local storage for faster response times.
- Provides a simple and intuitive interface using the curses library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README further based on your project's specific details and requirements.
