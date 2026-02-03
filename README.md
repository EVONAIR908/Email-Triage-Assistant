# Email-Triage-Assistant
Overview
->Modern inboxes are overwhelming. Important messages get buried under long threads, CC clutter, and low-priority emails.
->The Email Triage Assistant acts like a smart email secretary:
1. Summarizes long email threads
2. Identifies what’s urgent or actionable
3. Categorizes emails automatically
4. Suggests context-aware replies
5. Helps users respond faster with confidence

Key Features
->Email Thread Compression
Removes quoted text, signatures, and repetition
Preserves decisions, deadlines, and action items
Produces concise, readable summaries

-> Context Awareness
Understands full conversation history
Avoids redundant or incorrect replies
Tracks unresolved questions and pending tasks

-> Automatic Categorization
Emails are classified into:
1. Urgent
2. Action Required
3. Meetings
4. FYI / Read Later
5.Low Priority / Spam

-> Priority Scoring
Each email is assigned a priority score based on:
Keywords (ASAP, deadline, urgent)
Sender importance
Due dates and mentions
Thread activity

-> Smart Reply Generation
Generates reply drafts using AI
Matches tone (formal / neutral / casual)
User can edit, send, or discard suggestions

-> Inbox Dashboard
Summarized email view
Category-based filters
Priority sorting
Suggested replies in one place

-> How It Works
1.User connects their email account
2.Emails are fetched and grouped by thread
3.Threads are compressed into summaries
4.Emails are categorized and prioritized
5.AI generates suggested replies
6.User reviews and sends responses
 
Tech Stack
->Backend
1. Python
2. FastAPI

-> AI & NLP
1.LLM API (OpenAI / Claude / Gemini)
Thread summarization
Intent & urgency classification
Structured outputs with schemas

->Email Integration
Gmail API (primary)

->UI
Streamlit (for fast MVP dashboard)

Storage

SQLite / PostgreSQL

Optional vector database (FAISS / Chroma) for context memory

 WORK IN PROGRESS
