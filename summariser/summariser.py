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
        
        prompt = f"Summarise this AI policy document in 2 sentences for a general audience: {title}. {description}"
        
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        document["summary"] = response.choices[0].message.content
        
        print(f"Summarised: {title}")
    
    with open(filepath, "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved summaries to {filepath}")

summarise_documents("data/govuk.json")
summarise_documents("data/us.json")
summarise_documents("data/eu.json")