// Copyright (c) 2025, Fais Nasrullah and contributors
// For license information, please see license.txt

frappe.ui.form.on("Setup Email Recipient", {
	refresh: function(frm) {
        // Add custom button in toolbar
        if (frm.doc.email_recipient) {
            frm.add_custom_button(__("Test Send Email"), function() {
                // call method for executing script
                frappe.call({
                    method: "user_login_stats.user_login_statistics.utils.daily_login_stats.daily_login_stats",
                    callback: function(r) {
                        if (r.exc) {
                            frappe.msgprint(__("Failed to send email. Please check the error log."));
                        } else {
                            frappe.msgprint(__("Email sent successfully!"));
                        }
                    }
                });
            });
        }
    }
});
