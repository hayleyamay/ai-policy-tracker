# AI Policy Tracker 🌍

Hi! This is a little project I built to keep track of what's happening 
in AI policy across the UK, US, and EU — specifically aimed at reasearchers, students, and the general public. It's clear, easy to read and most importantly not geared towards 
lawyers or politicians.

🔗 **Check it out live:** https://hayleyamay.github.io/ai-policy-tracker/

## What it actually does

Every day, it automatically:
- Pulls the latest AI-related policy papers from GOV.UK
- Grabs new AI bills going through US Congress
- Checks the EU AI Act implementation page for updates
- Uses an AI model to write a quick, plain-English summary of each one
- Updates a little website with everything, so anyone can browse it

No manual updates, no paywalls — it just quietly runs itself every morning.

## Why I built this

I'm doing an MS in Computer Science (AI/ML), and I'm especially interested 
in AI safety, ethics, and governance. I wanted a project that combined 
those interests with real software skills — web scraping, APIs, automation, 
and deploying something genuinely useful and public.

I also just think people should be able to easily see what's happening 
in AI policy without needing a law degree.

## How it's built

- **Scrapers** (`scraper/`) — three different approaches depending on 
  what each government site allows: a clean JSON API for GOV.UK, an 
  authenticated API for US Congress, and HTML scraping for the EU AI Act 
  Tracker
- **Summariser** (`summariser/`) — sends each document to the Groq API 
  (LLaMA 3.1) and asks for a short, human-readable summary
- **Automation** (`.github/workflows/`) — GitHub Actions runs the whole 
  pipeline every day automatically
- **Website** (`index.html`) — a simple page that reads the data and 
  displays it, hosted free on GitHub Pages

## Built with

Python, BeautifulSoup, the Groq API, GitHub Actions, and plain HTML/CSS/JS — 
nothing fancy, just things that work.

## A bit about me

I'm Hayley — an MS Computer Science student focused on AI safety, ethics, 
and governance. This is one of a few projects I'm building as I dig deeper 
into this industry and my future career!