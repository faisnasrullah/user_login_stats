app_name = "user_login_stats"
app_title = "User Login Statistics"
app_publisher = "Fais Nasrullah"
app_description = "Custom app that automatically generates and sends a daily CSV file containing user login statistics via email"
app_email = "faisnasrullah.akn2014@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "user_login_stats",
# 		"logo": "/assets/user_login_stats/logo.png",
# 		"title": "User Login Statistics",
# 		"route": "/user_login_stats",
# 		"has_permission": "user_login_stats.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/user_login_stats/css/user_login_stats.css"
# app_include_js = "/assets/user_login_stats/js/user_login_stats.js"

# include js, css files in header of web template
# web_include_css = "/assets/user_login_stats/css/user_login_stats.css"
# web_include_js = "/assets/user_login_stats/js/user_login_stats.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "user_login_stats/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "user_login_stats/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "user_login_stats.utils.jinja_methods",
# 	"filters": "user_login_stats.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "user_login_stats.install.before_install"
# after_install = "user_login_stats.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "user_login_stats.uninstall.before_uninstall"
# after_uninstall = "user_login_stats.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "user_login_stats.utils.before_app_install"
# after_app_install = "user_login_stats.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "user_login_stats.utils.before_app_uninstall"
# after_app_uninstall = "user_login_stats.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "user_login_stats.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"user_login_stats.tasks.all"
# 	],
# 	"daily": [
# 		"user_login_stats.tasks.daily"
# 	],
# 	"hourly": [
# 		"user_login_stats.tasks.hourly"
# 	],
# 	"weekly": [
# 		"user_login_stats.tasks.weekly"
# 	],
# 	"monthly": [
# 		"user_login_stats.tasks.monthly"
# 	],
# }

scheduled_events = {
    "daily": [
        "user_login_stats.user_login_statistics.utils.daily_login_stats.daily_login_stats"
    ]
}

# Export Fixtures details
fixtures = [
    {"doctype": "Workspace", "filters": [["module", "=", "User Login Statistics"]]},
]

# Testing
# -------

# before_tests = "user_login_stats.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "user_login_stats.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "user_login_stats.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["user_login_stats.utils.before_request"]
# after_request = ["user_login_stats.utils.after_request"]

# Job Events
# ----------
# before_job = ["user_login_stats.utils.before_job"]
# after_job = ["user_login_stats.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"user_login_stats.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

