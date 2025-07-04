from langgraph.graph import StateGraph
from langgraph.graph import END
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from typing import TypedDict
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="your-llm-model", temperature=0) # you can use any model but i suggest Groq, because its API Key is free.

pdf_loader = PyPDFLoader("your-document.pdf")
document = pdf_loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # you can customize the chunk size and chunk overlap
split_document = splitter.split_documents(document)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",  # use an embedding model by huggingface. No API key needed
    model_kwargs={"device": "cpu"},  
)

database = FAISS.from_documents(split_document, embeddings) 
retreiver = database.as_retriever(search_kwargs={"k": 3}) # you can customize k value

class AgentState(TypedDict):
    context: list[Document]
    question: str
    answer: str
  
def retrieve_node (state: AgentState) -> AgentState:
    """Retrieves relevant data (context) from the FAQ document"""
    context = retreiver.invoke(state['question'])
    return {"context" : context}

template = """Answer the question based on the following context:
    {context}

    Question: {question}
    Give short and concise answers.""" #Give your extra instructions here

prompt = ChatPromptTemplate.from_template(template)

def generate_node (state: AgentState) -> AgentState:
    """Generates answer using the retrieved context"""
    question = state["question"]
    context = state["context"]
    context_text = "\n".join(doc.page_content for doc in context)

    answer = (
        prompt
        | llm
        | StrOutputParser()
    ).invoke({
        "context": context_text,
        "question": question
    })

    return {"answer" : answer}
    
workflow = StateGraph(AgentState)
workflow.add_node("retrieve" , retrieve_node)
workflow.add_node("generate" , generate_node)
workflow.add_edge("retrieve" , "generate")
workflow.set_entry_point("retrieve")
workflow.add_edge("generate" , END)
graph = workflow.compile()

print ("Chatbot -- (type 'quit' to exit)")
while True :
    question = input("\033[93;1mYou: \033[0m")
    if question.lower() == "quit":
        break
    result = graph.invoke(
        {"question": question, 
         "context": [], 
         "answer": ""
         })
    print (f"\n\033[92;1mBot:\033[0m {result['answer']}")
