from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fpdf import FPDF
import os

app = FastAPI(title="The AI Agent Millionaire - Super Premium Volume")

# 📂 PURE 100 COMPLETELY DISTINCT SUBJECTS ENGINE
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
        title = f"Autonomous {ind} System"
        tools = "Make.com, OpenAI Assistants API, Twilio WhatsApp API, Google Workspace"
        desc = f"System Runbook Topic #{num}: Architectural framework execution modules for automated {ind} processing workflows. Handles secure transactional hooks autonomously."
        flow = "User Sync -> Incoming Webhook Node -> OpenAI Inference Kernel -> Ledger Database"
        steps = "1. Deploy cloud infrastructure parameters mappings. 2. Mount source training logs context variables. 3. Monitor webhook execution loops."
        command = "mkdir agent-core && cd ai-agent-core\\npip install openai twilio fastapi uvicorn requests"
        money = "Monthly Platform Subscription Retainer: Invoice target storefronts Rs. 3,000 to Rs. 6,000/month."
        diff, cap = "Medium", "Tools Only"
    elif (i % 4) == 1:
        ind = media_subjects[(i // 4) % len(media_subjects)]
        title = f"Automated {ind} Traffic Factory"
        tools = "Python Scrapy, Gemini Pro API, ElevenLabs Audio, Social Media REST APIs"
        desc = f"System Runbook Topic #{num}: Machine-driven content scaling loop engineered to render and distribute premium {ind} dynamic assets without manual inputs."
        flow = "Source Scraper Engine -> Parser Unit -> LLM Context Compilation -> Automated REST Dispatch"
        steps = "1. Setup asynchronous processing workers layers. 2. Establish baseline conversion variables schemas. 3. Stream platform pushes."
        command = "pip install scrapy requests beautifulsoup4 soundfile\\npython production_worker.py"
        money = "Ad-Network Arbitrage: Secure automatic high-playback programmatic payouts sequentially."
        diff, cap = "Low", "Zero Capital"
    elif (i % 4) == 2:
        ind = saas_subjects[(i // 4) % len(saas_subjects)]
        title = f"Premium {ind} Utility SaaS"
        tools = "Next.js, Tailwind CSS, FastAPI Backend, Supabase Core, Stripe API Hooks"
        desc = f"System Runbook Topic #{num}: High-converting user interface portal mapped explicitly for programmatic {ind} adjustments with credits paywall limits blocks."
        flow = "Client Document Upload -> FastAPI Route Handler -> Token Optimization Array -> Stripe Return"
        steps = "1. Render minimalist interface structures canvas layouts. 2. Link payment gateway confirmation tokens. 3. Output files."
        command = "npm install @stripe/stripe-js pdf-parse openai dotenv\\nnpm run production-build"
        money = "Pay-Per-Use Transactional Tokens: Charge consumers Rs. 49 to Rs. 149 per compile cycle instantly."
        diff, cap = "High", "Minimal SaaS Fee"
    else:
        ind = infra_subjects[(i // 4) % len(infra_subjects)]
        title = f"Enterprise {ind} Operations Monitor"
        tools = "Python Scrapy Core, PostgreSQL Relational DB, Redis Cache, Resend Mail API"
        desc = f"System Runbook Topic #{num}: Non-intrusive background cloud micro-daemon application built to inspect architecture components logs for {ind} irregularities."
        flow = "Scheduler Daemon -> Query Scan Sequence -> Memory Cache Check -> Resend Webhook Transmission"
        steps = "1. Initialize target monitoring script patterns sequences. 2. Map data parameters to SQL storage schemas. 3. Launch alert pipelines."
        command = "pip install scrapy supabase resend redis psycopg2-binary\\npython micro_daemon.py"
        money = "B2B Technical Retention Contract: Charge modern tech founders and platforms Rs. 5,000 to Rs. 12,000/month."
        diff, cap = "High", "Server Cost Only"

    FINAL_100_BLUEPRINTS.append({
        "number": num, "category": cat, "title": title, "tools": tools,
        "desc": desc, "flow": flow, "steps": steps, "command": command, "money": money,
        "difficulty": diff, "capital": cap
    })

# Supplementary data schemas
TOOL_DIRECTORY = [
    {"name": "FastAPI Framework", "use": "High-speed Python APIs creation", "url": "https://fastapi.tiangolo.com"},
    {"name": "Make Automation", "use": "Visual backend logic & webhooks flow", "url": "https://www.make.com"},
    {"name": "OpenAI Platform", "use": "Large Language Models & Agent API", "url": "https://platform.openai.com"},
    {"name": "Supabase Database", "use": "PostgreSQL storage & Vector search layers", "url": "https://supabase.com"},
    {"name": "Twilio Gateway", "use": "WhatsApp Business and SMS APIs router", "url": "https://www.twilio.com"},
    {"name": "Resend Infrastructure", "use": "B2B Email marketing delivery node", "url": "https://resend.com"}
]

class SuperPremiumEbook(FPDF):
    def __init__(self):
        super().__init__()
        self.current_section_tag = "AUTONOMOUS CORE REFERENCE"

    def set_section_tag(self, tag):
        self.current_section_tag = tag

    def header(self):
        if self.page_no() > 5:
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(100, 116, 139)
            self.cell(120, 10, f"THE AI AGENT MILLIONAIRE  |  MODULE: {self.current_section_tag}", 0, 0, "L")
            self.set_font("Helvetica", "B", 7.5)
            self.set_text_color(37, 99, 235)
            self.cell(0, 10, "2026 DEPLOYMENT MANUAL CODES STANDARD", 0, 0, "R")
            self.set_draw_color(226, 232, 240)
            self.line(15, 22, 200, 22)
            self.ln(12)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("Helvetica", "B", 7.5)
            self.set_text_color(148, 163, 184)
            self.cell(110, 10, "[ RUNBOOK AUTHENTICATION ACCESS STATUS: VERIFIED SEED MODEL ]", 0, 0, "L")
            self.set_font("Helvetica", "I", 8)
            self.cell(0, 10, f"System Page Reference Index: {self.page_no()}", 0, 0, "R")

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
            <p class="text-slate-400 text-sm mb-8 leading-relaxed">Full Scale 100 Topics Complete Edition. Optimized code visualization panels and vector structural alignment blocks.</p>
            <a href="/generate-pdf" class="block w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-4 px-6 rounded-2xl transition duration-200">
                Download Full 100 Subject Book ↓
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
    
    # 📘 PAGE 1: DYNAMIC SOLID DARK COVER
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
    pdf.cell(0, 10, "100 INTERACTIVE SUBJECT BLUEPRINTS FEATURING CODE CHANNELS RUNBOOKS", 0, 1, "C")
    
    pdf.set_y(240)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 10, "2026 ULTIMATE PRODUCTION WORKFLOW  |  BY MANTU PATRA", 0, 1, "C")

    # 📘 PAGE 2: FULL COMPREHENSIVE TEXT INTRODUCTION
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "INTRODUCTION: THE PRINCIPLES OF AUTONOMY", 0, 1, "L")
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

    add_intro_block("A. THE STRATEGIC OVERVIEW", 
                    "AI systems automation ke is daur me sabse badi tactical flaw hai simple wrappers "
                    "bana kar chor dena. Is premium manual guide ka complete objectives aapko backend systems aur "
                    "continuous micro-daemons pipelines deploy karna sikhana hai jo production parameters par "
                    "bina kisi human touch ke 24/7 autonomous machines ki tarah compute karein.")
    
    add_intro_block("B. SYSTEM PREREQUISITES MAPPING", 
                    "Sabhie 100 technical concepts ko deploy karne ke liye heavy equipment configuration data "
                    "ki zaroorat nahi hai. Aap apne mobile standard terminal app (Termux Client) ka use karke, "
                    "isolated python runtimes, safe proxy layers rotation, aur cloud webhooks platforms integration "
                    "ke zariye high-performance nodes create kar sakte hain seamlessly.")

    # 📘 PAGE 3-5: INTERACTIVE LINKS INDEX DIRECTORY
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "SYSTEM INDEX & COMPLETE SUBJECTS DIRECTORY", 0, 1, "L")
    
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

    # 📘 INDIVIDUAL EXPLICIT DEEP TOPIC BLUEPRINTS RUNBOOKS
    last_cat = None
    for blueprint in FINAL_100_BLUEPRINTS:
        if blueprint['category'] != last_cat:
            last_cat = blueprint['category']
            pdf.set_section_tag(last_cat)
            
            pdf.add_page()
            pdf.set_fill_color(30, 41, 59)
            pdf.rect(0, 0, 215, 280, "F")
            pdf.set_y(120)
            pdf.set_font("Helvetica", "B", 20)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 10, last_cat, 0, 1, "C")
            pdf.ln(4)
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(59, 130, 246)
            pdf.cell(0, 10, "PRODUCTION RUNBOOKS INBOUND DEPLOYMENT MATRIX", 0, 1, "C")
            
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
        pdf.cell(0, 6, f"Tier Metrics: {blueprint['difficulty']}  |  Costing: {blueprint['capital']}", 0, 1, "R")
        
        # Solid Accent Indicator Shapes (Graphic Border Blocks Mapping)
        current_y = pdf.get_y()
        pdf.set_fill_color(37, 99, 235)
        pdf.rect(15, current_y + 2, 4, 12, "F")
        
        pdf.set_x(23)
        pdf.set_font("Helvetica", "B", 15)
        pdf.set_text_color(15, 23, 42)
        pdf.multi_cell(0, 10, blueprint['title'], 0, "L")
        pdf.ln(4)
        
        def format_section(heading, text_data, color_rgb=(51, 65, 85), font_type="", is_code_bg=False):
            pdf.set_x(15)
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(37, 99, 235)
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
            else:
                pdf.set_x(15)
                pdf.set_font("Helvetica", font_type, 10.5)
                pdf.set_text_color(*color_rgb)
                pdf.multi_cell(0, 6, text_data, 0, "J")
                pdf.ln(3)

        format_section("A. EXPERT SUBJECT MATERIAL & SPECIFICATION:", blueprint['desc'])
        format_section("B. DATA PROCESSING FLUID ARCHITECTURE NETWORK MAP:", f"  [ {blueprint['flow']} ]", color_rgb=(100, 116, 139), font_type="B")
        format_section("C. MANDATORY AUTOMATION DEPLOYMENT SYSTEM TOOLS:", blueprint['tools'], color_rgb=(15, 23, 42), font_type="I")
        format_section("D. STEP-BY-STEP TERMINAL RUNBOOK EXECUTION WORKFLOW:", blueprint['steps'])
        format_section("E. ISOLATED TERMINAL ENGINE DEPENDENCY INITIALIZATION CODES:", blueprint['command'], is_code_bg=True)
        
        # Solid Value Monetization Boxes
        pdf.ln(1)
        curr_y = pdf.get_y()
        pdf.set_fill_color(240, 253, 244)
        pdf.set_draw_color(167, 243, 208)
        pdf.rect(15, curr_y, 180, 25, "FD")
        
        pdf.set_y(curr_y + 3)
        pdf.set_x(20)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(20, 83, 45)
        pdf.cell(0, 5, "MONETIZATION BLUEPRINT & VALUE CAPTURE STRATEGY:", 0, 1, "L")
        
        pdf.set_x(20)
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(22, 101, 52)
        pdf.cell(0, 6, blueprint['money'], 0, 1, "L")

    # 📘 FINAL CHAPTER: APPENDIX ARCHITECTURE REFERENCE PLATFORMS
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "APPENDIX: TECH PLATFORM INTEGRATION PORTALS", 0, 1, "L")
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
