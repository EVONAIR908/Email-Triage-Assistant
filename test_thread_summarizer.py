def summarize_thread(emails):
    combined_content = " ".join(e.content for e in emails)
    summary = (
        combined_content[:150] + "..."
        if len(combined_content) > 150
           
        else combined_content
    )
    return summary
