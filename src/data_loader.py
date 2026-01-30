from pathlib import Path
from typing import List,Any
from langchain_community.document_loaders import PyPDFLoader,TextLoader,CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir:str) -> List[Any]:
    """LOad all supoorted data could be "Any" from the data_dir path 
    Supports:PDF,TXT,CSV,Excel,Word,JSON
    """

    #use project root data folder
    data_path=Path(data_dir).resolve()
    """Path= "Here's where the folder is."
       resolver()= "Show me the FULL address."    
    """
    documents= []

    #PDF files
    pdf_files=list(data_path.glob('**/*.pdf')) #glob=search

    # List = Type hint (tells Python what type of data it is)
    # list() = Function (actually creates a list)
    
    print(f"[DEBUG] Found {len(pdf_files)} PDF Files: {[str(f) for f in pdf_files]}") #convert the file in text and loop throught the files
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loadinf PDF: {pdf_file}")
        try:
            loader=PyPDFLoader(str(pdf_file)) #making a pdf loader which read the files
            loaded=loader.load() #run the pdf loader so data will be fetched
            documents.extend(loaded) #extend is like append
            print(f"[DEBUG] Successfully loaded PDF: {pdf_file}")
        except Exception as e:
            print(f"[ERROR] Failed to load PDf {pdf_file}: {str(e)}")
    

    # Text files
    text_files = list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] Found {len(text_files)} Text Files: {[str(f) for f in text_files]}")
    for text_file in text_files:
        print(f"[DEBUG] Loading Text: {text_file}")
        try:
            loader = TextLoader(str(text_file))
            loaded = loader.load()
            documents.extend(loaded)
            print(f"[DEBUG] Successfully loaded Text: {text_file}")
        except Exception as e:
            print(f"[ERROR] Failed to load Text {text_file}: {str(e)}")

    # CSV files
    csv_files = list(data_path.glob('**/*.csv'))
    print(f"[DEBUG] Found {len(csv_files)} CSV Files: {[str(f) for f in csv_files]}")
    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            documents.extend(loaded)
            print(f"[DEBUG] Successfully loaded CSV: {csv_file}")
        except Exception as e:
            print(f"[ERROR] Failed to load CSV {csv_file}: {str(e)}")

    # SQL files (typically read from database, not files)
    # sql_files = list(data_path.glob('**/*.sql'))
    # print(f"[DEBUG] Found {len(sql_files)} SQL Files: {[str(f) for f in sql_files]}")
    # for sql_file in sql_files:
    #     print(f"[DEBUG] Loading SQL: {sql_file}")
    #     try:
    #         with open(sql_file, 'r') as f:
    #             sql_content = f.read()
    #         documents.append({'content': sql_content, 'source': str(sql_file)})
    #     except Exception as e:
    #         print(f"[ERROR] Failed to load SQL {sql_file}: {str(e)}")
    
    return documents