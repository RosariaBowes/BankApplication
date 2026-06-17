from app import app
from flask import render_template, send_file
from datetime import datetime
import os, tempfile 

@app.route('/download_receipt/<filename>')
def download_receipt(filename):
    #Provide Receipt 
    return send_file(filename, as_attachment=True)

@app.route('/success/<filename>')
def payment(filename):
    return render_template('user/payment.html', filename=filename)

@app.route('/success/<filename>/download')
def download_success_recipient(filename):
    #Provide the receipt 
    return send_file(filename, as_attachment=True)


def generate_receipt(receipt_data):
    #Define HTML Template file
    html_template_path = "app/templates/user/receipt_template.html"

    #Read HTML content from seperate file 
    with open(html_template_path, "r") as file:
        receipt_content = file.read()

    #Format HTML content with receipt data 
    receipt_content = receipt_content.format(**receipt_data)  

    #Generate file name (unique and time stamped) for receipt 
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'receipt_{timestamp}.pdf'

    # Create temporary directory 
    temp_dir = tempfile.mkdtemp()

    #Save HTML content
    temp_html_path = os.path.join(temp_dir, "temp_receipt.html")
    with open(temp_html_path, "w") as temp_file:
        temp_file.write(receipt_content)

    return temp_html_path
