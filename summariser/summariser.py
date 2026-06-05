import json
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def summarise_documents(filepath):
    with open(filepath, "r") as f:
        documents = json.load(f)
    
    for document in documents:
        title = document["title"]
        description = document.get("description", "No description available")
        
        prompt = f"Summarise this AI policy document in 2 sentences for a general audience: {title}. {description}"
        
        response = client.models.generate_content(
            model="gemini-1.5-flash-8b",
            contents=prompt
        )
        document["summary"] = response.text
        
        print(f"Summarised: {title}")
    
    with open(filepath, "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved summaries to {filepath}")

summarise_documents("data/govuk.json")