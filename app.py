import random
from datetime import datetime, timedelta

class Email:
    def __init__(self, sender, subject, content, date, thread_id):
        self.sender = sender
        self.subject = subject
        self.content = content
        self.date = date
        self.thread_id = thread_id

    def __repr__(self):
        return f"""
From: {self.sender}
Subject: {self.subject}
Date: {self.date}
Thread: {self.thread_id}
Content: {self.content}
"""

def fetch_mock_emails():
    senders = ["malik@bedco.com", "team@group1.com", "updates@service.com"]
    subjects = [
        "Urgent: Deadline Tomorrow",
        "Meeting Follow-up",
        "Weekly Update – FYI"
    ]
    contents = [
        "Hey, please confirm the report by tomorrow.",
        "Attached are the meeting notes. Any updates?",
        "Here’s your annual report of product analytics."
    ]
    
    emails = []
    for i in range(3):
        emails.append(
            Email(
                sender=senders[i],
                subject=subjects[i],
                content=contents[i],
                date=datetime.now() - timedelta(hours=random.randint(1, 72)),
                thread_id=f"thread_{i}"
            )
        )
    return emails
emails = fetch_mock_emails()
emails
def categorize_email(email):
    subject = email.subject.lower()
    content = email.content.lower()

    if any(k in subject + content for k in ["urgent", "asap", "immediately", "deadline"]):
        return "Urgent"
    elif any(k in subject + content for k in ["meeting", "schedule", "call"]):
        return "Meetings"
    elif any(k in subject + content for k in ["please review", "need input", "follow up"]):
        return "Action Required"
    elif any(k in subject + content for k in ["newsletter", "update", "digest"]):
        return "FYI / Read Later"
    else:
        return "Low Priority"
for e in emails:
    print(f"Subject: {e.subject}")
    print("Category:", categorize_email(e))
    print("-" * 40)
 from datetime import datetime

def compute_priority(email, category):
    base = 50

    if category == "Urgent":
        base += 40
    elif category == "Action Required":
        base += 30
    elif category == "Meetings":
        base += 20
    elif category == "FYI / Read Later":
        base += 10
    else:
        base -= 10

   
    hours_ago = (datetime.now() - email.date).seconds / 3600
    recency_bonus = (1 / (1 + hours_ago)) * 30

    return int(base + recency_bonus)
emails = [
    Email(
        sender="malik@bedco.com",
        subject="Urgent: Deadline Tomorrow",
        content="Please review the report ASAP.",
        date=datetime.now() - timedelta(minutes=10),
        thread_id="thread_1"
    ),
    Email(
        sender="team@group1.com",
        subject="Action Required: Review Notes",
        content="Please check the meeting notes.",
        date=datetime.now() - timedelta(hours=5),
        thread_id="thread_2"
    ),
    Email(
        sender="updates@service.com",
        subject="Annual report",
        content="Here’s your annual update.",
        date=datetime.now() - timedelta(hours=24),
        thread_id="thread_3"
    )
]
categories = ["Urgent", "Action Required", "FYI / Read Later"]

for email, category in zip(emails, categories):
    score = compute_priority(email, category)
    print(f"Subject: {email.subject}")
    print(f"Category: {category}")
    print(f"Received: {email.date}")
    print(f"Priority Score: {score}")
    print("-" * 40) 
def generate_reply(email, tone="neutral"):
    if "urgent" in email.subject.lower():
        base_reply = "Got it, I’ll handle this immediately."
    elif "meeting" in email.subject.lower():
        base_reply = "Thanks for the update! I’ll review the meeting notes."
    elif "fyi" in email.subject.lower():
        base_reply = "Thanks for sharing this information."
    else:
        base_reply = "Thanks, I’ll look into it soon."

    if tone == "formal":
        base_reply = "Dear {},\n\n{} \n\nBest regards,".format(
            email.sender.split("@")[0].capitalize(), base_reply
        )
    elif tone == "casual":
        base_reply = base_reply + " 👍"

    return base_reply
for email in emails:
    print("Subject:", email.subject)
    print("Neutral Reply: ", generate_reply(email, tone="neutral"))
    print("Formal Reply: ", generate_reply(email, tone="formal"))
    print("Casual Reply: ", generate_reply(email, tone="casual"))
    print("-" * 50)
  def summarize_thread(emails):
    combined_content = " ".join(e.content for e in emails)
    summary = (
        combined_content[:150] + "..."
        if len(combined_content) > 150
           
        else combined_content
    )
    return summary
summarize_thread(emails)
