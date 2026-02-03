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
