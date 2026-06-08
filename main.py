from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

app = FastAPI(title="The AI Agent Millionaire PDF Engine")

# Sample Data: Aap is list ko pure 100 ideas tak extend kar sakte hain
IDEAS_DATA = [
    {"id": 1, "title": "Autonomous SEO Discovery Engine", "desc": "Ek aisa system jo internet se daily naye AI tools track karta hai, unka automatic sitemap banata hai, aur Google Search Console me index karwata hai. E.g., 80+ pages auto-index daily for AdSense income."},
    {"id": 2, "title": "AI Local Appointment Bot (SANOL Style)", "desc": "Local salons, clinics, ya gyms ke liye ek WhatsApp bot jo customers se chat karke unka time-slot khud book karta hai. Owner se monthly subscription (₹1500/month) charge karein."},
    {"id": 3, "title": "Automated Micro-SaaS Wrapping", "desc": "Ek single-page utility tool (jaise background remover ya invoice generator) banakar Stripe/Razorpay se connect karna aur monthly access bechna."},
    {"id": 4, "title": "Autonomous API Reselling", "desc": "Bade AI LLM frameworks ki API ka wrapper banakar chote automatic features local developers ko custom price par rent karna."},
    {"id": 5, "title": "Auto-Review & Reputation Responder", "desc": "Google My Business par local shops ke reviews ka AI se instant automatic reply dena taaki unki local ranking top par aa jaye."},
    # ... Aap isi tarah pure 100 ideas is list me add kar sakte hain
]

@app.get("/")
def home():
    return {"status": "Active", "message": "Welcome to The AI Agent Millionaire PDF Generator. Go to /generate-pdf to download your book."}

@app.get("/generate-pdf")
def generate_pdf():
    pdf_filename = "The_AI_Agent_Millionaire_100_Ideas.pdf"
    
    # Document setup
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()

    # Custom Styling
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=26, leading=30, textColor=colors.HexColor("#1A365D"), alignment=1, spaceAfter=10)
    subtitle_style = ParagraphStyle('SubTitle', parent=styles['Normal'], fontSize=12, leading=16, textColor=colors.HexColor("#4A5568"), alignment=1, spaceAfter=25)
    idea_title_style = ParagraphStyle('IdeaTitle', parent=styles['Heading2'], fontSize=14, leading=18, textColor=colors.HexColor("#2B6CB0"), spaceBefore=12, spaceAfter=6)
    desc_style = ParagraphStyle('Desc', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#2D3748"), spaceAfter=12)

    # Title & Header
    story.append(Paragraph("<b>The AI Agent Millionaire</b>", title_style))
    story.append(Paragraph("100 Smart Ways to Build Automatic Systems Using Mobile & AI Agents (2026 Edition)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E0"), spaceAfter=20))

    # Generating 100 Ideas (Looping data multiple times for demonstration if list is short)
    count = 1
    for _ in range(20): # Is loop ko aap dynamic bana sakte hain jab pure 100 unique items hon
        for item in IDEAS_DATA:
            if count > 100:
                break
            story.append(Paragraph(f"<b>Idea #{count}: {item['title']}</b>", idea_title_style))
            story.append(Paragraph(item['desc'], desc_style))
            count += 1

    doc.build(story)
    
    return FileResponse(path=pdf_filename, filename=pdf_filename, media_type='application/pdf')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.py", host="0.0.0.0", port=8000, reload=True)
