from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import inch
from datetime import datetime
import os


def generate_pdf(role: str, roadmap: str) -> str:
    # ─────────────────────────────────────────
    # File Setup
    # ─────────────────────────────────────────
    filename = f"roadmap_{role.replace(' ', '_')}.pdf"
    filepath = os.path.join(os.getcwd(), filename)
    
    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # ─────────────────────────────────────────
    # Colors
    # ─────────────────────────────────────────
    PRIMARY_COLOR = HexColor("#1a1a2e")      # Dark Navy
    ACCENT_COLOR = HexColor("#e94560")       # Red Accent
    HEADER_BG = HexColor("#16213e")          # Header Background
    TEXT_COLOR = HexColor("#333333")         # Body Text
    LINK_COLOR = HexColor("#0066cc")         # Link Color
    
    # ─────────────────────────────────────────
    # Styles
    # ─────────────────────────────────────────
    styles = getSampleStyleSheet()
    
    # Agent branding header style
    brand_style = ParagraphStyle(
        'BrandStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor("#ffffff"),
        backColor=PRIMARY_COLOR,
        alignment=1,  # Center
        spaceAfter=2,
        spaceBefore=2,
        leftIndent=0,
        rightIndent=0,
        fontName='Helvetica-Bold'
    )
    
    # Title style
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontSize=24,
        textColor=PRIMARY_COLOR,
        spaceAfter=6,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        alignment=1
    )
    
    # Heading 1 style
    h1_style = ParagraphStyle(
        'H1Style',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=ACCENT_COLOR,
        spaceAfter=6,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    # Heading 2 style
    h2_style = ParagraphStyle(
        'H2Style',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=PRIMARY_COLOR,
        spaceAfter=4,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    # Body text style
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT_COLOR,
        spaceAfter=4,
        spaceBefore=2,
        leading=16,
        fontName='Helvetica'
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT_COLOR,
        spaceAfter=3,
        spaceBefore=1,
        leftIndent=20,
        leading=15,
        fontName='Helvetica'
    )
    
    # Link style
    link_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=LINK_COLOR,
        spaceAfter=3,
        spaceBefore=1,
        leftIndent=20,
        leading=14,
        fontName='Helvetica'
    )
    
    # Footer style
    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor("#888888"),
        alignment=1,
        spaceAfter=2,
        spaceBefore=10,
        fontName='Helvetica'
    )
    
    # ─────────────────────────────────────────
    # Build PDF Content
    # ─────────────────────────────────────────
    content = []
    
    # --- HEADER BRANDING ---
    content.append(Paragraph(
        "🤖 AI Career Mentor Agent By Kumar Basu Singh",
        brand_style
    ))
    content.append(Spacer(1, 0.1*inch))
    content.append(HRFlowable(
        width="100%",
        thickness=2,
        color=ACCENT_COLOR
    ))
    content.append(Spacer(1, 0.1*inch))
    
    # --- DATE ---
    date_str = datetime.now().strftime("%B %d, %Y")
    content.append(Paragraph(
        f"Generated on: {date_str}",
        footer_style
    ))
    content.append(Spacer(1, 0.2*inch))
    
    # --- TITLE ---
    content.append(Paragraph(
        f"Career Roadmap: {role}",
        title_style
    ))
    content.append(HRFlowable(
        width="100%",
        thickness=1,
        color=ACCENT_COLOR
    ))
    content.append(Spacer(1, 0.2*inch))
    
    # ─────────────────────────────────────────
    # Parse and Add Roadmap Content
    # ─────────────────────────────────────────
    lines = roadmap.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            content.append(Spacer(1, 0.05*inch))
            continue
        
        # Remove markdown symbols for clean PDF
        # H1 Heading (##)
        if line.startswith('## '):
            text = line.replace('## ', '').replace('#', '').strip()
            text = text.replace('🎯', '').replace('📋', '').replace(
                '🛠️', '').replace('🗺️', '').replace(
                '💡', '').replace('⏱️', '').strip()
            content.append(Paragraph(text, h1_style))
            
        # H2 Heading (###)
        elif line.startswith('### '):
            text = line.replace('### ', '').replace('#', '').strip()
            content.append(Paragraph(text, h2_style))
            
        # Main title (#)
        elif line.startswith('# '):
            text = line.replace('# ', '').replace('#', '').strip()
            text = text.replace('🎯', '').strip()
            content.append(Paragraph(text, h1_style))
            
        # Bullet points with links
        elif line.startswith('•') and '→' in line:
            parts = line.split('→')
            skill_text = parts[0].replace('•', '').strip()
            link_text = parts[1].strip() if len(parts) > 1 else ''
            content.append(Paragraph(f"• {skill_text}", bullet_style))
            if link_text:
                content.append(Paragraph(
                    f'   📎 <link href="{link_text}">{link_text}</link>',
                    link_style
                ))
                
        # Regular bullet points (- or •)
        elif line.startswith('-') or line.startswith('•'):
            text = line.lstrip('-•').strip()
            text = text.replace('**', '')
            content.append(Paragraph(f"• {text}", bullet_style))
            
        # Regular text
        else:
            text = line.replace('**', '').replace('*', '')
            content.append(Paragraph(text, body_style))
    
    # ─────────────────────────────────────────
    # Footer
    # ─────────────────────────────────────────
    content.append(Spacer(1, 0.3*inch))
    content.append(HRFlowable(
        width="100%",
        thickness=1,
        color=ACCENT_COLOR
    ))
    content.append(Paragraph(
        "Generated by AI Career Mentor Agent By Kumar Basu Singh | All rights reserved",
        footer_style
    ))
    content.append(Paragraph(
        f"Role: {role} | Date: {date_str}",
        footer_style
    ))
    
    # ─────────────────────────────────────────
    # Build PDF
    # ─────────────────────────────────────────
    doc.build(content)
    
    return filepath