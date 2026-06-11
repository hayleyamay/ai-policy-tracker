import json
import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def summarise_documents(filepath):
    with open(filepath, "r") as f:
        documents = json.load(f)
    
    for document in documents:
        title = document["title"]
        description = document.get("description", "No description available")
        
        prompt = f"Write a 2 sentence plain English summary of this AI policy document. Only write the summary, nothing else. If you have limited information, summarise based on the title alone. Title: {title}. Description: {description}"
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response.choices[0].message.content

        bad_phrases = ["I'm ready", "I cannot", "you did not provide", "Please share", "I'm unable"]
        if any(phrase in summary for phrase in bad_phrases):
            summary = f"This document covers AI policy related to: {title}"

        document["summary"] = summary
        
        print(f"Summarised: {title}")
    
    with open(filepath, "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved summaries to {filepath}")

summarise_documents("data/govuk.json")
summarise_documents("data/us.json")
summarise_documents("data/eu.json")