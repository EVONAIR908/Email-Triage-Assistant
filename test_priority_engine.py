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
