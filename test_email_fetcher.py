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
    senders = ["boss@company.com", "team@startup.com", "newsletter@service.com"]
    subjects = [
        "Urgent: Deadline Tomorrow",
        "Meeting Follow-up",
        "Weekly Update – FYI"
    ]
    contents = [
        "Hey, please confirm the report by tomorrow.",
        "Attached are the meeting notes. Any updates?",
        "Here’s your weekly digest of product analytics."
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

