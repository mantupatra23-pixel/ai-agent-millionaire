from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fpdf import FPDF
import os

app = FastAPI(title="The AI Agent Millionaire - Super Premium Edition")

# 📂 PURE 100 COMPLETELY DISTINCT TECHNICAL SUBJECTS DATA MATRIX
FINAL_100_BLUEPRINTS = []
categories = ["LOCAL BUSINESS AUTOMATION", "HYPER-TRAFFIC MEDIA SYSTEMS", "MICRO-SAAS DEVELOPMENT", "DATA & INFRASTRUCTURE OPERATORS"]

subjects = [
    "Salon Slot Booking", "Gym Lead Follow-up", "Real Estate Matcher", "Restaurant Review Booster",
    "Kirana Ledger Bot", "Dentist Recall Engine", "Boutique Inventory Agent", "Car Wash Scheduler",
    "Cafe Order Automator", "Hotel Concierge Bot", "Pharmacy Prescription Reminder", "Diagnostic Lab Booking",
    "Coaching Institute Doubt Solver", "Spa Wellness Advisor", "Bakery Pre-order Bot", "Catering Lead Qualification",
    "Dry Cleaning Pickup Bot", "Pet Grooming Organizer", "Jewelry Shop Showroom Guide", "Law Firm Case Intake",
    "Accounting Client Collector", "Interior Design Moodboard Bot", "Packers & Movers Estimator", "Solar Panel Lead Agent",
    "Electrician Dispatch Coordinator"
]

media_subjects = [
    "Audio-Podcast Curator", "Pinterest Viral Traffic", "Reddit Storyteller Channel", "YouTube Shorts Engine",
    "Automated Newsletter Writer", "X/Twitter Trend Viral Bot", "Instagram Aesthetic Curator", "LinkedIn Ghostwriter Bot",
    "Medium Article Programmatic Factory", "Substack Niche Digest Builder", "TikTok Faceless Meme Factory", "Spotify Ambient Playlist Curator",
    "Daily Tech News Summarizer", "Stock Market Automated Alert Reel", "Crypto Sentiment Live Broadcaster", "Product Hunt Launch Informer",
    "HackerNews Trend Analyzer", "E-book Auto-Publisher Bot", "Meme Marketing Automatic Router", "AI Video Translation Pipeline",
    "Real-time Sports Commentary Generator", "Gaming Clips Automatic Editor", "SaaS Feature Explainer Bot", "Startup Pitch Audio Synthesizer",
    "Local Event Dynamic Broadcast Engine"
]

saas_subjects = [
    "Resume Customizer Portal", "Dynamic Invoice Tax Planner", "AI Cover Letter Architect", "Cold Email Hyper-Personalizer",
    "Pitch Deck Slide Copy Generator", "SQL Query Natural Language Tool", "SEO Meta Description Bulk Optimizer", "Code Error Instant Explainer",
    "Sitemap XML Auto-Validator", "API Documentation Auto-Generator", "Micro-CRM for Solo Founders", "No-Code Component Customizer",
    "UI/UX Accessibility Checker Bot", "Social Media Bio Dynamic Generator", "Regex Pattern English Translator", "JSON Schema Auto-Sanitizer",
    "Markdown to HTML Clean Converter", "E-commerce Product Copy Multiplier", "Job Description Post Architect", "Competitor Ad Copy Analyzer",
    "Affiliate Link Auto-Cloaker", "Terms & Conditions Micro-Generator", "Privacy Policy Customizer Bot", "User Feedback Sentiment Aggregator",
    "Changelog Automated Draft Tool"
]

infra_subjects = [
    "Competitor Pricing Watchdog", "Programmatic SEO Content Factory", "Broken Link Auto-Repair Daemon", "Server Log Anomaly Detector",
    "S3 Bucket Cost Optimization Sentinel", "SSL Certificate Expiry Auto-Renewer", "Database Slow Query Optimizer", "API Rate Limit Monitoring Agent",
    "Uptime Alert Slack Webhook Router", "Docker Container Auto-Scale Watcher", "GitHub Repo PR Auto-Reviewer", "Cloudflare Rule Dynamic Adjuster",
    "Phishing Link Domain Scraper", "Google Search Console Indexing Daemon", "Proxy Rotation Automated Manager", "Stripe Dispute Evidence Collector",
    "Backlink Growth Monitoring Daemon", "Pinterest Image Metadata Optimizer", "YouTube Video Description Auto-Updater", "Multi-Cloud Backup Sync Worker",
    "Redis Cache Eviction Monitor", "Webflow to Static HTML Exporter", "Shopify Stock Level Reorder Agent", "Google Map Citation Audit Engine",
    "Automated Trademark Infringement Finder"
]

for i in range(100):
    num = i + 1
    cat = categories[i % 4]
    
    if (i % 4) == 0:
        ind = subjects[(i // 4) % len(subjects)]
        title = f"Autonomous {ind} Framework"
        tools = "Make.com, OpenAI Assistants API, Twilio WhatsApp API, Google Workspace"
        desc = f"System Schema #{num}: Ek conversational AI agent architecture framework jo local {ind} workflows ko handle karta hai. Yeh processing metadata analytics parameters auto-parse karke database layer update karta hai."
        flow = "User Chat -> Twilio Webhook -> Make Pipeline -> OpenAI Core -> Ledger Update"
        steps = "1. Setup cloud channel webhooks for input streaming. 2. Mount knowledge base criteria to vector memory index. 3. Hook output streams securely."
        command = "mkdir ai-agent-core && cd ai-agent-core\\npip install openai twilio fastapi uvicorn requests\\npython main.py"
        money = "Monthly Retainer: Charge Rs. 3,000 to Rs. 6,000/month securely from client store."
        guardrail = "Set Max-Tokens logic to prevent runaway recursion loops in OpenAI Assistants calls."
        diff, cap = "Medium", "Tools Only"
    elif (i % 4) == 1:
        ind = media_subjects[(i // 4) % len(media_subjects)]
        title = f"Automated {ind} Matrix"
        tools = "Python Scrapy, Gemini Pro API, ElevenLabs Voice, Platform REST APIs"
        desc = f"System Schema #{num}: High-fidelity dynamic content rendering engine jo automated {ind} media operations deploy karta hai without human processing layers."
        flow = "Scraper Daemon -> Tokenizer Layer -> LLM Content Variant Gen -> REST API Dispatch"
        steps = "1. Launch celery worker loops on cloud servers. 2. Implement target media transformation structures. 3. Monitor analytics index parameters."
        command = "pip install requests beautifulsoup4 soundfile analytics-sdk\\nscrapy crawl media_pipeline"
        money = "Traffic Revenue Arbitrage: Capitalize programmatic traffic payouts directly via dashboard metrics."
        guardrail = "Use concurrent request limits and proxy rotation to avoid temporary IP blocks from source sites."
        diff, cap = "Low", "Zero Capital"
    elif (i % 4) == 2:
        ind = saas_subjects[(i // 4) % len(saas_subjects)]
        title = f"Premium {ind} Micro-SaaS Portal"
        tools = "Next.js, Tailwind CSS, FastAPI Backend, Supabase Engine, Stripe Gateway"
        desc = f"System Schema #{num}: Single-utility user portal framework engineered around {ind} optimization blocks. Features embedded dynamic credit balance management ledger tools."
        flow = "Client Form Upload -> FastAPI API Endpoint -> AI Asset Compiler Layer -> Stripe Hook Return"
        steps = "1. Configure React frontend forms layout blueprints. 2. Mount authorization keys to target endpoints variables. 3. Route response files."
        command = "npm install @stripe/stripe-js pdf-parse openai dotenv\\nnpm run dev"
        money = "Pay-Per-Generation: Invoice users Rs. 49 to Rs. 149 per transaction directly via token stripe integration."
        guardrail = "Implement absolute request timeouts on FastAPI router nodes to safeguard background database execution pools."
        diff, cap = "High", "Minimal SaaS Fee"
    else:
        ind = infra_subjects[(i // 4) % len(infra_subjects)]
        title = f"Enterprise {ind} Guardian Daemon"
        tools = "Python Scrapy, PostgreSQL Server, Redis Cache, Resend Mail API, AWS EC2"
        desc = f"System Schema #{num}: Persistent cloud daemon application engineered to monitor technical performance parameters for {ind} anomalies autonomously."
        flow = "Cron Thread Trigger -> Active Scanner Node -> Redis Memory Cache Filter -> Resend Mailer Out"
        steps = "1. Deploy background daemon processes loops. 2. Hook tracking parameters schemas to relational DB structures. 3. Run alert webhooks."
        command = "pip install scrapy supabase resend redis psycopg2-binary\\npython daemon_worker.py"
        money = "B2B Infrastructure Retainer: Bill software systems clients Rs. 5,000 to Rs. 12,000/month seamlessly."
        guardrail = "Set standard database connection pool pooling thresholds to minimize heavy operational overhead loops."
        diff, cap = "High", "Server Cost Only"

    FINAL_100_BLUEPRINTS.append({
        "number": num, "category": cat, "title": title, "tools": tools,
        "desc": desc, "flow": flow, "steps": steps, "command": command, "money": money,
        "difficulty": diff, "capital": cap, "guardrail": guardrail
    })

TOOL_DIRECTORY = [
    {"name": "FastAPI Framework", "use": "High-speed Python APIs creation", "url": "https://fastapi.tiangolo.com"},
    {"name": "Make Automation", "use": "Visual backend logic & webhooks flow", "url": "https://www.make.com"},
    {"name": "OpenAI Platform", "use": "Large Language Models & Agent API", "url": "https://platform.openai.com"},
    {"name": "Supabase Database", "use": "PostgreSQL storage & Vector search layers", "url": "https://supabase.com"},
    {"name": "Twilio Gateway", "use": "WhatsApp Business and SMS APIs router", "url": "https://www.twilio.com"},
    {"name": "Resend Infrastructure", "use": "B2B Email marketing delivery node", "url": "https://resend.com"}
]

# Custom Context-Aware FPDF Subclass for Super-Premium Books
class SuperPremiumEbook(FPDF):
    def __init__(self):
        super().__init__()
        self.current_section_tag = "PRODUCTION ENGINE REFERENCE"

    def set_section_tag(self, tag):
        self.current_section_tag = tag

    def header(self):
        # Dynamically hides header tracking bar on Cover, Intro, and Index Directory
        if self.page_no() > 5:
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(100, 116, 139)
            # Left Header context updates in real-time depending on book progress
            self.cell(120, 10, f"THE AI AGENT MILLIONAIRE  |  SECTION: {self.current_section_tag}", 0, 0, "L")
            self.set_font("Helvetica", "B", 7.5)
            self.set_text_color(37, 99, 235)
            self.cell(0, 10, "2026 PRODUCTION RUNBOOK STANDARD", 0, 0, "R")
            self.set_draw_color(226, 232, 240)
            self.line(15, 22, 200, 22)
            self.ln(12)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("Helvetica", "B", 7.5)
            self.set_text_color(148, 163, 184)
            self.cell(100, 10, "[ RUNBOOK KEY STATUS: GOLD VERIFIED PRODUCTION STANDARDS ]", 0, 0, "L")
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 10, f"System Page Reference: {self.page_no()}", 0, 0, "R")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>The AI Agent Millionaire - Book Portal</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    </head>
    <body class="bg-slate-950 text-white font-sans antialiased flex items-center justify-center min-h-screen">
        <div class="max-w-md p-10 bg-slate-900 border border-slate-800 rounded-3xl text-center shadow-2xl relative overflow-hidden">
            <div class="absolute -top-10 -right-10 w-32 h-32 bg-blue-600/10 rounded-full blur-2xl"></div>
            <h1 class="text-3xl font-black mb-4">The AI Agent Millionaire</h1>
            <p class="text-slate-400 text-sm mb-8 leading-relaxed">Super-Premium Full Scale Edition. Featuring context-aware dynamic page headers, clean tabular appendices, and multi-line code execution systems.</p>
            <a href="/generate-pdf" class="block w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-4 px-6 rounded-2xl transition duration-200 shadow-xl shadow-blue-600/20">
                Download Super Premium Book ↓
            </a>
        </div>
    </body>
    </html>
    """

@app.get("/generate-pdf")
def export_premium_pdf():
    target_pdf = "The_AI_Agent_Millionaire_Ultimate.pdf"
    pdf = SuperPremiumEbook()
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # 📘 1. MAIN FRONT COVER PAGE
    pdf.add_page()
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(0, 0, 215, 280, "F")
    
    pdf.set_fill_color(30, 41, 59)
    pdf.rect(15, 80, 180, 75, "F")
    
    pdf.set_y(95)
    pdf.set_font("Helvetica", "B", 25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, "THE AI AGENT MILLIONAIRE", 0, 1, "C")
    
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(59, 130, 246)
    pdf.cell(0, 10, "100 INTERACTIVE BLUEPRINTS WITH MULTI-LINE RUNBOOKS & CODE TERMINALS", 0, 1, "C")
    
    pdf.set_y(240)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 10, "2026 ULTIMATE PRODUCTION WORKFLOW  |  BY MANTU PATRA", 0, 1, "C")

    # 📘 2. EXPANDED PRE-TEXT INTRODUCTION CHAPTER
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "INTRODUCTION: THE ARCHITECTURE OF AUTONOMY", 0, 1, "L")
    pdf.set_fill_color(37, 99, 235)
    pdf.rect(15, pdf.get_y() + 2, 40, 2, "F")
    pdf.ln(12)
    
    def add_intro_block(title, content):
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(37, 99, 235)
        pdf.cell(0, 6, title, 0, 1, "L")
        pdf.ln(1)
        pdf.set_font("Helvetica", "", 10.5)
        pdf.set_text_color(51, 65, 85)
        pdf.multi_cell(0, 6, content, 0, "J")
        pdf.ln(4)

    add_intro_block("A. THE CORE PHILOSOPHY", 
                    "AI ke is advanced daur me sabse badi galti hai wahi purane template systems banana jo "
                    "poori market copy kar rahi hai. Is book ka purpose aapko fully autonomous workflows aur "
                    "background network micro-daemons build karna sikhana hai jo production cloud clusters par "
                    "bina kisi human click ke 24/7 self-running machine ki tarah operate karein.")
    
    add_intro_block("B. SYSTEM REQUIREMENTS MATRIX", 
                    "Sabhie 100 systems ko test aur deploy karne ke liye aapko heavy computers nahi chahiye. "
                    "Aap apne mobile me Termux Linux terminal client setup karke, standard Python environment binaries, "
                    "aur cloud webhook routers (jaise Make or Resend API keys) ka use karke in pipelines ko locally initializes kar sakte hain.")

    add_intro_block("C. THE RUNBOOK BLUEPRINT METHODOLOGY", 
                    "Har ek single blueprint sheet ko humne strictly functional layers me standardise kiya hai: "
                    "System Logic description, data flowchart mapping brackets, tech dependency criteria tools stack, "
                    "step-by-step shell execution guides, operational safety limit warnings, aur ultimate value pricing modules.")

    # 📘 3. CLICKABLE INDEX DIRECTORY
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "SYSTEM INDEX & DIRECTORY", 0, 1, "L")
    
    pdf.set_fill_color(37, 99, 235)
    pdf.rect(15, pdf.get_y() + 2, 30, 2, "F")
    pdf.ln(10)
    
    links_map = {}
    for blueprint in FINAL_100_BLUEPRINTS:
        links_map[blueprint['number']] = pdf.add_link()

    index_count = 0
    for blueprint in FINAL_100_BLUEPRINTS:
        if index_count > 0 and index_count % 22 == 0:
            pdf.add_page()
            pdf.ln(10)
            
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(37, 99, 235)
        pdf.cell(22, 7, f"TOPIC #{blueprint['number']:03d} ->", 0, 0, "L", link=links_map[blueprint['number']])
        
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(15, 23, 42)
        short_title = blueprint['title'][:48] + "..." if len(blueprint['title']) > 48 else blueprint['title']
        pdf.cell(0, 7, short_title, 0, 1, "L", link=links_map[blueprint['number']])
        index_count += 1

    # 📘 4. INDIVIDUAL TOPICS RUNBOOKS GENERATION WITH CONTEXT ACCESS
    last_cat = None
    for blueprint in FINAL_100_BLUEPRINTS:
        if blueprint['category'] != last_cat:
            last_cat = blueprint['category']
            # Updating our header tracking mechanism instantly before loading section page
            pdf.set_section_tag(last_cat)
            
            pdf.add_page()
            pdf.set_fill_color(30, 41, 59)
            pdf.rect(0, 0, 215, 280, "F")
            pdf.set_y(120)
            pdf.set_font("Helvetica", "B", 20)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 10, last_cat, 0, 1, "C")
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(59, 130, 246)
            pdf.cell(0, 10, "PRODUCTION RUNBOOKS INBOUND MAPPING", 0, 1, "C")
            
        pdf.add_page()
        pdf.set_link(links_map[blueprint['number']], y=0)
        
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(100, 116, 139)
        pdf.cell(0, 5, blueprint['category'], 0, 1, "L")
        
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(37, 99, 235)
        pdf.cell(0, 6, f"SYSTEM RUNBOOK TOPIC #{blueprint['number']:03d}", 0, 0, "L")
        
        pdf.set_x(140)
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(0, 6, f"Complexity: {blueprint['difficulty']}  |  Capital: {blueprint['capital']}", 0, 1, "R")
        
        # Thick Modern Left Border Accent Block
        current_y = pdf.get_y()
        pdf.set_fill_color(37, 99, 235)
        pdf.rect(15, current_y + 2, 4, 12, "F")
        
        pdf.set_x(23)
        pdf.set_font("Helvetica", "B", 16)
        pdf.set_text_color(15, 23, 42)
        pdf.multi_cell(0, 10, blueprint['title'], 0, "L")
        pdf.ln(4)
        
        def format_section(heading, text_data, color_rgb=(51, 65, 85), font_type="", is_code_bg=False, is_warning=False):
            pdf.set_x(15)
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(225, 29, 72) if is_warning else pdf.set_text_color(37, 99, 235)
            pdf.cell(0, 6, heading, 0, 1, "L")
            pdf.ln(1)
            
            if is_code_bg:
                lines = text_data.split('\\n')
                box_height = (len(lines) * 6) + 6
                box_y = pdf.get_y()
                
                pdf.set_fill_color(15, 23, 42)
                pdf.rect(15, box_y, 180, box_height, "F")
                
                pdf.set_y(box_y + 3)
                pdf.set_font("Courier", "B", 9.5)
                pdf.set_text_color(248, 250, 252)
                
                for line in lines:
                    pdf.set_x(20)
                    pdf.cell(0, 6, line, 0, 1, "L")
                pdf.set_x(15)
                pdf.ln(5)
            elif is_warning:
                w_y = pdf.get_y()
                pdf.set_fill_color(254, 242, 242)
                pdf.rect(15, w_y, 180, 12, "F")
                pdf.set_y(w_y + 3)
                pdf.set_x(20)
                pdf.set_font("Helvetica", "I", 10)
                pdf.set_text_color(153, 27, 27)
                pdf.cell(0, 6, text_data, 0, 1, "L")
                pdf.set_x(15)
                pdf.ln(4)
            else:
                pdf.set_x(15)
                pdf.set_font("Helvetica", font_type, 10.5)
                pdf.set_text_color(*color_rgb)
                pdf.multi_cell(0, 6, text_data, 0, "J")
                pdf.ln(3)

        format_section("1. DETAILED OPERATIONAL SPECIFICATION:", blueprint['desc'])
        format_section("2. DATA FLOW ARCHITECTURE FLUID MAP:", f"  [ {blueprint['flow']} ]", color_rgb=(100, 116, 139), font_type="B")
        format_section("3. REQUIRED AUTOMATION TECHNOLOGY TOOLS SYSTEM:", blueprint['tools'], color_rgb=(15, 23, 42), font_type="I")
        format_section("4. STEP-BY-STEP TERMINAL SETUP IMPLEMENTATION GUIDE:", blueprint['steps'])
        format_section("5. SYSTEM LIMITS & OPERATIONAL GUARDRAILS:", blueprint['guardrail'], is_warning=True)
        format_section("6. TERMINAL ENGINE INITIALIZATION COMMANDS (RUNFLOW):", blueprint['command'], is_code_bg=True)
        
        # 💰 Monetization Block Container
        pdf.ln(1)
        curr_y = pdf.get_y()
        pdf.set_fill_color(240, 253, 244)
        pdf.set_draw_color(167, 243, 208)
        pdf.rect(15, curr_y, 180, 25, "FD")
        
        pdf.set_y(curr_y + 3)
        pdf.set_x(20)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(20, 83, 45)
        pdf.cell(0, 5, "MONETIZATION MODEL & STRATEGIC VALUE CAPTURE:", 0, 1, "L")
        
        pdf.set_x(20)
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(22, 101, 52)
        pdf.cell(0, 6, blueprint['money'], 0, 1, "L")

    # 📘 5. APPENDIX: CORE ECOSYSTEM PLATFORMS DIRECTORY
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "APPENDIX: TECH PLATFORM INTEGRATION LINKS", 0, 1, "L")
    pdf.set_fill_color(37, 99, 235)
    pdf.rect(15, pdf.get_y() + 2, 45, 2, "F")
    pdf.ln(12)

    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_fill_color(15, 23, 42)
    pdf.cell(45, 8, " Platform Name", 1, 0, "L", True)
    pdf.cell(75, 8, " Primary Core Functional Utility", 1, 0, "L", True)
    pdf.cell(60, 8, " Secure Dashboard Access Link", 1, 1, "L", True)

    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    for tool in TOOL_DIRECTORY:
        pdf.cell(45, 8, f" {tool['name']}", 1, 0, "L")
        pdf.cell(75, 8, f" {tool['use']}", 1, 0, "L")
        pdf.set_text_color(37, 99, 235)
        pdf.cell(60, 8, " Open Portal Website ->", 1, 1, "C", link=tool['url'])
        pdf.set_text_color(51, 65, 85)

    pdf.output(target_pdf)
    return FileResponse(path=target_pdf, filename=target_pdf, media_type='application/pdf')
