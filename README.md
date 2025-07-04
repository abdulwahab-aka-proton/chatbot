
# FAQ assistance Chat-bot 
Hi! This is a bot which answers user questions by consulting an FAQ document. It is made using *Langgraph* , *RAG* (Retrieval Augmented Generation) and simple *Python*.

**Example**: A document containing Frequently Asked Questions (and their answers) about an online Hackathon is provided to the chat-bot. Chat-bot then processes this information and helps users with their queries by getting relevant data from the document.

Note:  This is not just for FAQ documents. Any kind of readable document can be passed to the bot. i.e. Lecture notes, Resumes, Manuals etc.

## How to use this Chat-bot?
**1. Install Python**
Check if Python is installed on your system by running  the following  command on Windows Command Prompt / Terminal or Powershell 
```
python --version
```
If it shows a Python version then you can skip this section.

If Python is not installed on your system then follow the steps below to download the official Python installer from the [Python.org](https://www.python.org/) site:

1.  Open your browser and navigate to the [downloads page for Windows](https://www.python.org/downloads/windows/) on Python.org.
2.  Under the _Python Releases for Windows_ heading, click the link for the _Latest Python 3 Release - Python 3.x.z_.
3.  Scroll to the bottom and select either _Windows installer (64-bit)_ or _Windows installer (32-bit)_.
4. Once you have downloaded the Installer go ahead and run it. It will install Python on your system.


**2. Python Packages Needed**

Once Python is installed on your system, run the following commands in terminal to install all Python packages required to run this chat-bot.

 - `pip install langgraph`
 - `pip install langchain-core`
 - `pip install langchain-groq`
 - `pip install langchain-huggingface`
 - `pip install langchain-community`
 - `pip install langchain-text-splitters`
 - `pip install python-dotenv`
 
**3. API KEY**
You will need an API Key to access a Large Language Model (LLM). You can use any API Key provider. But i suggest either Groq or Huggingface since both are free.

Once you have generated the API Key, copy it and keep it safe.

**4. Implementation**

 1. Create a folder
 2. Inside the folder, create an `.env` file and create an `app.py` file.
 3. Inside the `.env` file, enter your API Key.
	For Example: 
	
> GROQ_API_KEY="your-api-key"

 4. Copy the code from `chatbot.py` inside this repository.
 5. Paste the code copied into `app.py`.
 6. Save and Run!
