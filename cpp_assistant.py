import curses
from curses import wrapper



import openai
from apikey import openaiApikey
openai.api_key = openaiApikey

import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to a simple c++ helper CLI chat")
    while True:
        stdscr.addstr("Please prompt the AI aout c++: ")
        curses.echo()
        prompt = stdscr.getstr().decode("utf-8")
        curses.noecho()
        if (str(prompt) == "Q" or str(prompt) == "q"):
            curses.nocbreak()
            curses.echo()
            curses.endwin()
            stdscr.refresh()
            return
        else:
            stdscr.addstr(query(prompt))
            stdscr.refresh()

def query(prompt):
    # check if storage already exists
    PERSIST_DIR = "./storage"
    if not os.path.exists(PERSIST_DIR):
        # load the documents and create the index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    # Either way we can now query the index
    query_engine = index.as_chat_engine()
    response = query_engine.chat(prompt)
    return(str(response))
if __name__ == "__main__":
    wrapper(main)
