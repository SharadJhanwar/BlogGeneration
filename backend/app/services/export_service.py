import os
import re
from typing import Literal
from docx import Document
from io import BytesIO
from htmldocx import HtmlToDocx
from bs4 import BeautifulSoup
from xhtml2pdf import pisa

async def export_blog(content: str, title: str, format: Literal["pdf", "docx", "md", "html"]):
    try:
        if format == "md":
            return content, "text/markdown", f"{title}.md"
        
        elif format == "html":
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>{title}</title>
                <style>
                    body {{ font-family: sans-serif; line-height: 1.6; padding: 40px; max-width: 900px; margin: auto; color: #333; }}
                    h1 {{ color: #111; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
                    img {{ max-width: 100%; height: auto; border-radius: 8px; margin: 20px 0; }}
                    p {{ margin-bottom: 15px; }}
                </style>
            </head>
            <body>
                <h1>{title}</h1>
                {content}
            </body>
            </html>
            """
            return html_content, "text/html", f"{title}.html"
        
        elif format == "docx":
            doc = Document()
            # Set a more modern font
            style = doc.styles['Normal']
            font = style.font
            font.name = 'Calibri'
            
            new_parser = HtmlToDocx()
            # Wrap content in a body to ensure it's treated as HTML
            full_html = f"<html><body><h1>{title}</h1>{content}</body></html>"
            new_parser.add_html_to_document(full_html, doc)
            
            file_stream = BytesIO()
            doc.save(file_stream)
            file_stream.seek(0)
            return file_stream.getvalue(), "application/vnd.openxmlformats-officedocument.wordprocessingml.document", f"{title}.docx"
        
        elif format == "pdf":
            # Use xhtml2pdf for rich rendering
            html_content = f"""
            <html>
            <head>
                <style>
                    @page {{
                        size: a4 portrait;
                        @frame content_frame {{
                            left: 50pt; width: 492pt; top: 50pt; height: 742pt;
                        }}
                    }}
                    body {{ font-family: Helvetica, Arial, sans-serif; font-size: 12pt; line-height: 1.5; }}
                    h1 {{ font-size: 24pt; text-align: center; color: #333; margin-bottom: 20pt; }}
                    h2 {{ font-size: 18pt; color: #444; margin-top: 15pt; border-bottom: 1pt solid #ccc; }}
                    img {{ max-width: 100%; height: auto; display: block; margin: 10pt auto; }}
                    b, strong {{ font-weight: bold; }}
                    i, em {{ font-style: italic; }}
                </style>
            </head>
            <body>
                <h1>{title}</h1>
                {content}
            </body>
            </html>
            """
            
            # Simple cleanup for xhtml2pdf
            soup = BeautifulSoup(html_content, 'html.parser')
            # Flatten figure tags
            for figure in soup.find_all('figure'):
                img = figure.find('img')
                if img:
                    figure.replace_with(img)
            
            result = BytesIO()
            pisa_status = pisa.CreatePDF(str(soup), dest=result)
            
            if pisa_status.err:
                raise Exception("Error rendering PDF with xhtml2pdf")
                
            return result.getvalue(), "application/pdf", f"{title}.pdf"
        
        else:
            raise ValueError(f"Unsupported format: {format}")

    except Exception as e:
        print(f"Export Error [{format}]: {e}")
        import traceback
        traceback.print_exc()
        raise e
