from app import app
from flask import render_template, send_file
from datetime import datetime
import os, tempfile 
import pdfkit 

@app.route('/download_reciept/<filename>')
def download_receipt(filename):
    #Provide Reciept 
    return send_file(filename, as_attachment=True)

@app.route('/success/<filename>')
def payment(filename):
    return render_template('user/payment.html', filename=filename)

@app.route('/success/<filename>/download')
def download_success_recipient(filename):
    #Provide the reciept 
    return send_file(filename, as_attachment=True)


def generate_reciept(reciept_data):
    #Define HTML Template file
    html_template_path = "app/template/user/reciept_template.html"

    #Read HTML content from seperate file 
    with open(html_template_path, "r") as file:
        reciept_content = file.read()

    #Format HTML content with reciept data 
    reciept_content = reciept_content.format(**reciept_data)  

    #Generate file name (unique and time stamped) for receipt 
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%")
    filename = f'reciept_{timestamp}.pdf'

    # Create temporary directory 
    temp_dir = tempfile.mkdtemp()

    #Save HTML content
    temp_html_path = os.path.join(temp_dir, "temp_reciept.html")
    with open(temp_html_path, "w") as temp_file:
        temp_file.write(reciept_content)

    pdf_path = os.path.join(temp_dir, filename)
    pdfkit.from_file(temp_html_path, pdf_path)

    #Clean temporary HTML file
    os.remove(temp_html_path)

    return pdf_path