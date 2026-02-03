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

