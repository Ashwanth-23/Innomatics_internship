import streamlit as st
import chromadb

# Displaying some fun elements
st.balloons()
st.title('🚀 📺 Enhancing Search Engine Relevance for Video Subtitles 🎦 ')
st.subheader('🔍 Navigating Multilingual Movie Moments 🍿')

# Establishing connection with ChromaDB
client = chromadb.PersistentClient(path=r"C:\Users\ADMIN\Desktop\Data Sicence\innomatics internship\Search enginee\search_engine_db")
client.heartbeat()

# Creating or getting the collection
collection_name = "mydata_collection"
try:
    collection = client.get_collection(name=collection_name)
except ValueError:
    collection = client.create_collection(name=collection_name)

# Querying and displaying results
query_text = st.text_input('Enter your query:')
if st.button('Search'):
    st.snow()
    def similar_title(query_text):
        result = collection.query(
            query_texts=[query_text],
            include=["metadatas", "distances"],
            n_results=10
        )
        ids = result['ids'][0]
        distances = result['distances'][0]
        metadatas = result['metadatas'][0]
        sorted_data = sorted(zip(metadatas, ids, distances), key=lambda x: x[2], reverse=True)
        return sorted_data

    result_data = similar_title(query_text)
    
    st.success('Here are the most relevant subtitle names :')
    for metadata, ids, distance in result_data:
        subtitle_name = metadata['name']
        st.write(subtitle_name)