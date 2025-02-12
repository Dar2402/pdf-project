from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_pdf(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    elements = []

    table_data = [["Field", "Value"]] 
    for key, value in data.items():
        table_data.append([key.replace("_", " ").title(), value])

    # Create Table with Styles
    table = Table(table_data, colWidths=[200, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), 
        ('FONTSIZE', (0, 0), (-1, -1), 12),  
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10), 
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)
    return buffer
