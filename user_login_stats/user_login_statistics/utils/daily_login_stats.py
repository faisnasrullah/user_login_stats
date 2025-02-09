import frappe
import csv
from frappe.utils import getdate, nowdate


def get_user_login_stats():
    """Query for getting data user login stats"""
    users = frappe.db.sql("""
        SELECT 
            first_name, 
            last_name, 
            COUNT(login.name) AS login_attempts
        FROM 
            `tabUser` AS user
        LEFT JOIN 
            `tabActivity Log` AS login 
        ON 
            user.name = login.user AND login.operation = 'Login'
        GROUP BY 
            user.name
    """, as_dict=True)

    return users


def generate_csv(data):
    """Generate a CSV file from user login data."""
    file_name = f"user_login_stats_{getdate(nowdate())}.csv"
    file_path = frappe.get_site_path("public", "files", file_name)

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Login Attempts"])
        for user in data:
            writer.writerow([user["first_name"], user["last_name"], user["login_attempts"]])

    return file_path


def send_email_with_csv(file_path):
    """Send an email with the CSV file attached."""
    recipients = []

    setup = frappe.get_doc("Setup Email Recipient")
    list_email_recipient = setup.email_recipient

    for data in list_email_recipient:
        recipients.append(data.email_address)

    email_args = {
        "recipients": recipients or ["zcode88@gmail.com"],
        "subject": "Daily User Login Statistics",
        "message": "Please find attached the daily user login statistics.",
        "attachments": [{
            "fname": file_path.split("/")[-1],
            "fcontent": open(file_path, "rb").read()
        }]
    }

    frappe.sendmail(**email_args)


@frappe.whitelist()
def daily_login_stats():
    """Main function to fetch data, generate CSV, and send email."""
    try:
        # get data user login statistics
        user_data = get_user_login_stats()
        
        # create file CSV
        csv_file_path = generate_csv(user_data)
        
        # send email with file CSV
        send_email_with_csv(csv_file_path)
        
        frappe.log_error("Daily login stats email sent successfully.")
    except Exception as e:
        # Log error if failed to send email
        frappe.log_error(f"Failed to send daily login stats: {str(e)}")