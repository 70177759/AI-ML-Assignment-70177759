import os
import nbformat as nbf
import base64
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, HRFlowable
)

def make_two_column_pdf(pdf_path, task_id, task_title, data):
    """
    Builds a professional 2-page double-column IEEE-style PDF report using ReportLab.
    """
    doc = BaseDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    page_width, page_height = A4
    margin = 36
    gutter = 14
    content_width = page_width - 2 * margin
    col_width = (content_width - gutter) / 2
    
    # Page 1 has header banner:
    header_height = 80
    body_height_p1 = page_height - 2 * margin - header_height
    
    frame_p1_col1 = Frame(margin, margin, col_width, body_height_p1, id='p1_c1', topPadding=0, bottomPadding=0, leftPadding=0, rightPadding=0)
    frame_p1_col2 = Frame(margin + col_width + gutter, margin, col_width, body_height_p1, id='p1_c2', topPadding=0, bottomPadding=0, leftPadding=0, rightPadding=0)
    
    # Page 2 has full height
    body_height_p2 = page_height - 2 * margin
    frame_p2_col1 = Frame(margin, margin, col_width, body_height_p2, id='p2_c1', topPadding=0, bottomPadding=0, leftPadding=0, rightPadding=0)
    frame_p2_col2 = Frame(margin + col_width + gutter, margin, col_width, body_height_p2, id='p2_c2', topPadding=0, bottomPadding=0, leftPadding=0, rightPadding=0)
    
    def draw_p1_header(canvas, document):
        canvas.saveState()
        # Top banner text
        canvas.setFont('Helvetica-Bold', 7.5)
        canvas.setFillColor(colors.HexColor('#1A237E'))
        banner_text = "THE UNIVERSITY OF LAHORE • DEPARTMENT OF INTELLIGENT SYSTEMS • AI-101 INTRODUCTION TO ARTIFICIAL INTELLIGENCE"
        canvas.drawCentredString(page_width / 2.0, page_height - margin - 8, banner_text)
        
        # Title
        canvas.setFont('Helvetica-Bold', 12.5)
        canvas.setFillColor(colors.black)
        title_text = f"Task [{task_id}]: [{task_title}]"
        canvas.drawCentredString(page_width / 2.0, page_height - margin - 25, title_text)
        
        # Author info
        canvas.setFont('Helvetica', 8.5)
        author_text = "Muhammad Haysum | Roll No. 70177759 | Section BS RAI Section C"
        canvas.drawCentredString(page_width / 2.0, page_height - margin - 38, author_text)
        
        # Repo info
        canvas.setFont('Helvetica-Oblique', 7.5)
        canvas.setFillColor(colors.HexColor('#37474F'))
        repo_text = "Repository: https://github.com/mhaysum/AI101-ML-Assignment-70177759 | Instructor: Dr. Muhammad Awais, AI Architect"
        canvas.drawCentredString(page_width / 2.0, page_height - margin - 50, repo_text)
        
        # Line rule
        canvas.setStrokeColor(colors.HexColor('#9E9E9E'))
        canvas.setLineWidth(0.8)
        canvas.line(margin, page_height - margin - 58, page_width - margin, page_height - margin - 58)
        
        # Page 1 footer
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.black)
        canvas.drawCentredString(page_width / 2.0, margin - 15, "1")
        canvas.restoreState()
        
    def draw_p2_footer(canvas, document):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.black)
        canvas.drawCentredString(page_width / 2.0, margin - 15, "2")
        # Running top header
        canvas.setFont('Helvetica-Oblique', 7)
        canvas.setFillColor(colors.HexColor('#616161'))
        canvas.drawString(margin, page_height - margin + 5, f"AI-101 ML Assignment • Task [{task_id}]")
        canvas.drawRightString(page_width - margin, page_height - margin + 5, "Muhammad Haysum (70177759)")
        canvas.restoreState()

    template_p1 = PageTemplate(id='page1', frames=[frame_p1_col1, frame_p1_col2], onPage=draw_p1_header)
    template_p2 = PageTemplate(id='page2', frames=[frame_p2_col1, frame_p2_col2], onPage=draw_p2_footer)
    doc.addPageTemplates([template_p1, template_p2])
    
    # Styles
    styles = getSampleStyleSheet()
    
    body_style = ParagraphStyle(
        'IEEEBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.2,
        alignment=4, # Justified
        spaceAfter=4
    )
    
    sec_style = ParagraphStyle(
        'IEEESec',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11,
        textColor=colors.HexColor('#0D47A1'),
        spaceBefore=5,
        spaceAfter=2
    )
    
    subsec_style = ParagraphStyle(
        'IEEESubSec',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=10,
        textColor=colors.HexColor('#1565C0'),
        spaceBefore=3,
        spaceAfter=1
    )
    
    caption_style = ParagraphStyle(
        'IEEECaption',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=6.8,
        leading=8.5,
        alignment=1, # Centered
        spaceBefore=2,
        spaceAfter=4
    )
    
    cell_style = ParagraphStyle(
        'IEEECell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.2,
        alignment=0
    )
    
    cell_bold = ParagraphStyle(
        'IEEECellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.8,
        leading=8.2,
        alignment=0
    )
    
    flowables = []
    
    # 1. Introduction
    flowables.append(Paragraph("1. Introduction", sec_style))
    flowables.append(Paragraph(data['introduction'], body_style))
    
    # 2. Problem Statement
    flowables.append(Paragraph("2. Problem Statement", sec_style))
    flowables.append(Paragraph(data['problem_statement'], body_style))
    
    # 3. Dataset Used
    flowables.append(Paragraph("3. Dataset Used", sec_style))
    flowables.append(Paragraph(data['dataset_used'], body_style))
    
    # 4. Dataset Statistics
    flowables.append(Paragraph("4. Dataset Statistics", sec_style))
    flowables.append(Paragraph("Summary structural statistics and feature distributions for the dataset are presented below:", body_style))
    
    # Table 1: Dataset statistics
    t1_data = [[Paragraph(f"<b>{row[0]}</b>", cell_bold), Paragraph(str(row[1]), cell_style)] for row in data['dataset_stats']]
    t1 = Table(t1_data, colWidths=[col_width * 0.55, col_width * 0.45])
    t1.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, 0), 0.8, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 0.8, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
    ]))
    flowables.append(Spacer(1, 2))
    flowables.append(Paragraph("<b>Table 1:</b> Dataset statistics.", caption_style))
    flowables.append(t1)
    flowables.append(Spacer(1, 4))
    
    # Figure 1: EDA Figure
    if os.path.exists(data['eda_figure_path']):
        img_w = col_width
        img_h = col_width * 0.65
        flowables.append(Image(data['eda_figure_path'], width=img_w, height=img_h))
        flowables.append(Paragraph(f"<b>Figure 1:</b> {data['eda_figure_caption']}", caption_style))
        flowables.append(Spacer(1, 4))
        
    # 5. Methodology
    flowables.append(Paragraph("5. Methodology", sec_style))
    flowables.append(Paragraph("5.1 Learning Setting", subsec_style))
    flowables.append(Paragraph(data['learning_setting'], body_style))
    
    flowables.append(Paragraph("5.2 Data Split Approach", subsec_style))
    flowables.append(Paragraph(data['data_split'], body_style))
    
    flowables.append(Paragraph("5.3 Parameter Settings", subsec_style))
    # Table 2: Hyperparameters
    t2_headers = [Paragraph("<b>Model</b>", cell_bold), Paragraph("<b>Search Space</b>", cell_bold), Paragraph("<b>Selected</b>", cell_bold)]
    t2_rows = [t2_headers]
    for row in data['param_settings']:
        t2_rows.append([
            Paragraph(row[0], cell_bold),
            Paragraph(row[1], cell_style),
            Paragraph(row[2], cell_style)
        ])
    t2 = Table(t2_rows, colWidths=[col_width * 0.32, col_width * 0.38, col_width * 0.30])
    t2.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, 0), 0.8, colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 0.8, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
    ]))
    flowables.append(Paragraph("<b>Table 2:</b> Hyperparameter settings.", caption_style))
    flowables.append(t2)
    flowables.append(Spacer(1, 4))
    
    # 6. Results and Analysis
    flowables.append(Paragraph("6. Results and Analysis", sec_style))
    flowables.append(Paragraph("6.1 Results", subsec_style))
    
    # Table 3: Test results
    t3_headers = [Paragraph(f"<b>{h}</b>", cell_bold) for h in data['results_headers']]
    t3_rows = [t3_headers]
    for row in data['results_rows']:
        row_cells = []
        for i, val in enumerate(row):
            if i == 0:
                row_cells.append(Paragraph(val, cell_bold))
            else:
                row_cells.append(Paragraph(val, cell_style))
        t3_rows.append(row_cells)
    
    n_cols = len(data['results_headers'])
    col_w_table = col_width / n_cols
    col_widths = [col_width * 0.34] + [col_width * (0.66 / (n_cols - 1))] * (n_cols - 1)
    t3 = Table(t3_rows, colWidths=col_widths)
    t3.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, 0), 0.8, colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 0.8, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
    ]))
    flowables.append(Paragraph("<b>Table 3:</b> Test-set results. Best value in bold.", caption_style))
    flowables.append(t3)
    flowables.append(Spacer(1, 4))
    
    # Figure 2: Result figure
    if os.path.exists(data['results_figure_path']):
        img_w = col_width
        img_h = col_width * 0.65
        flowables.append(Image(data['results_figure_path'], width=img_w, height=img_h))
        flowables.append(Paragraph(f"<b>Figure 2:</b> {data['results_figure_caption']}", caption_style))
        flowables.append(Spacer(1, 4))
        
    flowables.append(Paragraph("6.2 Analysis", subsec_style))
    flowables.append(Paragraph(data['analysis'], body_style))
    
    # 7. Conclusion
    flowables.append(Paragraph("7. Conclusion", sec_style))
    flowables.append(Paragraph(data['conclusion'], body_style))
    
    # AI Use Disclosure
    flowables.append(Paragraph("AI Use Disclosure", sec_style))
    flowables.append(Paragraph(data['ai_disclosure'], body_style))
    
    # References
    flowables.append(Paragraph("References", sec_style))
    for ref in data['references']:
        flowables.append(Paragraph(ref, caption_style))
        
    doc.build(flowables)
    print(f"Report built successfully at: {pdf_path}")

def make_latex_source(tex_path, task_id, task_title, data):
    """
    Generates the IEEEtran LaTeX source code matching Report_Template_Two_Column.tex.
    """
    tex_content = f'''\\documentclass[conference]{{IEEEtran}}
\\usepackage{{cite}}
\\usepackage{{amsmath,amssymb,amsfonts}}
\\usepackage{{algorithmic}}
\\usepackage{{graphicx}}
\\usepackage{{textcomp}}
\\usepackage{{xcolor}}
\\usepackage{{booktabs}}
\\usepackage{{hyperref}}

\\begin{{document}}

\\title{{Task [{task_id}]: [{task_title}]}}

\\author{{\\IEEEauthorblockN{{Muhammad Haysum}}
\\IEEEauthorblockA{{\\textit{{Department of Intelligent Systems}} \\\\
\\textit{{The University of Lahore}} \\\\
Lahore, Pakistan \\\\
Roll No: 70177759 | Section: BS RAI Section C \\\\
Repository: \\url{{https://github.com/mhaysum/AI101-ML-Assignment-70177759}} \\\\
Instructor: Dr. Muhammad Awais, AI Architect}}
}}

\\maketitle

\\begin{{abstract}}
This report presents an empirical investigation for Task {task_id} ({task_title}) under the AI-101 Machine Learning curriculum. We evaluate baseline, regularized, and ensemble architectures using strict leak-free pipelines and stratified splits.
\\end{{abstract}}

\\section{{Introduction}}
{data['introduction']}

\\section{{Problem Statement}}
{data['problem_statement']}

\\section{{Dataset Used}}
{data['dataset_used']}

\\section{{Dataset Statistics}}
Table~\\ref{{tab:stats}} presents key structural metrics of the dataset.

\\begin{{table}}[htbp]
\\caption{{Dataset statistics.}}
\\label{{tab:stats}}
\\centering
\\begin{{tabular}}{{ll}}
\\toprule
\\textbf{{Property}} & \\textbf{{Value}} \\\\
\\midrule
'''
    for row in data['dataset_stats']:
        tex_content += f"{row[0]} & {row[1]} \\\\\n"
        
    tex_content += f'''\\bottomrule
\\end{{tabular}}
\\end{{table}}

\\begin{{figure}}[htbp]
\\centering
\\includegraphics[width=\\columnwidth]{{../../figures/fig1_eda.png}}
\\caption{{{data['eda_figure_caption']}}}
\\label{{fig:eda}}
\\end{{figure}}

\\section{{Methodology}}
\\subsection{{Learning Setting}}
{data['learning_setting']}

\\subsection{{Data Split Approach}}
{data['data_split']}

\\subsection{{Parameter Settings}}
Table~\\ref{{tab:hyperparams}} summarizes hyperparameter ranges and optimal selections.

\\begin{{table}}[htbp]
\\caption{{Hyperparameter settings.}}
\\label{{tab:hyperparams}}
\\centering
\\begin{{tabular}}{{lll}}
\\toprule
\\textbf{{Model}} & \\textbf{{Search space}} & \\textbf{{Selected}} \\\\
\\midrule
'''
    for row in data['param_settings']:
        tex_content += f"{row[0]} & {row[1]} & {row[2]} \\\\\n"
        
    tex_content += f'''\\bottomrule
\\end{{tabular}}
\\end{{table}}

\\section{{Results and Analysis}}
\\subsection{{Results}}
Test-set evaluations across all candidates are summarized in Table~\\ref{{tab:results}}.

\\begin{{table}}[htbp]
\\caption{{Test-set results. Best value in bold.}}
\\label{{tab:results}}
\\centering
\\begin{{tabular}}{{{'l' * len(data['results_headers'])}}}
\\toprule
'''
    tex_content += " & ".join([f"\\textbf{{{h}}}" for h in data['results_headers']]) + " \\\\\n\\midrule\n"
    for row in data['results_rows']:
        tex_content += " & ".join([r.replace('<b>', '\\textbf{').replace('</b>', '}') for r in row]) + " \\\\\n"
        
    tex_content += f'''\\bottomrule
\\end{{tabular}}
\\end{{table}}

\\begin{{figure}}[htbp]
\\centering
\\includegraphics[width=\\columnwidth]{{../../figures/fig2_results.png}}
\\caption{{{data['results_figure_caption']}}}
\\label{{fig:results}}
\\end{{figure}}

\\subsection{{Analysis}}
{data['analysis']}

\\section{{Conclusion}}
{data['conclusion']}

\\section*{{AI Use Disclosure}}
{data['ai_disclosure']}

\\begin{{thebibliography}}{{00}}
'''
    for i, ref in enumerate(data['references'], 1):
        clean_ref = ref.replace('<b>', '').replace('</b>', '').replace('<i>', '').replace('</i>', '')
        tex_content += f"\\bibitem{{b{i}}} {clean_ref}\n"
        
    tex_content += f'''\\end{{thebibliography}}

\\end{{document}}
'''
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print(f"LaTeX source written to: {tex_path}")

def save_executed_notebook(nb_path, cells_data):
    """
    Constructs and saves an executed Jupyter Notebook (.ipynb) with outputs and markdown.
    """
    nb = nbf.v4.new_notebook()
    for cell in cells_data:
        cell_type = cell.get('type', 'markdown')
        source = cell.get('source', '')
        if cell_type == 'markdown':
            nb.cells.append(nbf.v4.new_markdown_cell(source))
        elif cell_type == 'code':
            outputs = []
            stdout_text = cell.get('stdout', None)
            if stdout_text:
                outputs.append(nbf.v4.new_output(output_type='stream', name='stdout', text=stdout_text))
            img_b64 = cell.get('image_b64', None)
            if img_b64:
                outputs.append(nbf.v4.new_output(
                    output_type='display_data',
                    data={'image/png': img_b64, 'text/plain': '<Figure size>'}
                ))
            nb.cells.append(nbf.v4.new_code_cell(source, execution_count=cell.get('count', 1), outputs=outputs))
            
    with open(nb_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"Notebook written to: {nb_path}")
