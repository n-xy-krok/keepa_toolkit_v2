from . import __version__ as app_version

app_name = "keepa_toolkit_v2"
app_title = "Keepa Toolkit V2"
app_publisher = "N_XY"
app_description = "Keepa Toolkit Frappe App Reworked"
app_email = "kubliy.n@ikrok.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/keepa_toolkit_v2/css/keepa_toolkit_v2.css"
# app_include_js = "/assets/keepa_toolkit_v2/js/keepa_toolkit_v2.js"

# include js, css files in header of web template
# web_include_css = "/assets/keepa_toolkit_v2/css/keepa_toolkit_v2.css"
# web_include_js = "/assets/keepa_toolkit_v2/js/keepa_toolkit_v2.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "keepa_toolkit_v2/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "keepa_toolkit_v2.utils.jinja_methods",
#	"filters": "keepa_toolkit_v2.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "keepa_toolkit_v2.install.before_install"
after_install = "keepa_toolkit_v2.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "keepa_toolkit_v2.uninstall.before_uninstall"
after_uninstall = "keepa_toolkit_v2.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "keepa_toolkit_v2.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    'cron':{
        '* * * * *': 
            [
            "keepa_toolkit_v2.tasks.keepa_product_retriever",
            "keepa_toolkit_v2.tasks.keepa_category_retriever"
            ]
    },
#	"all": [
#		"keepa_toolkit_v2.tasks.all"
#	],
#	"daily": [
#		"keepa_toolkit_v2.tasks.daily"
#	],
#	"hourly": [
#		"keepa_toolkit_v2.tasks.hourly"
#	],
#	"weekly": [
#		"keepa_toolkit_v2.tasks.weekly"
#	],
#	"monthly": [
#		"keepa_toolkit_v2.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "keepa_toolkit_v2.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "keepa_toolkit_v2.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "keepa_toolkit_v2.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["keepa_toolkit_v2.utils.before_request"]
# after_request = ["keepa_toolkit_v2.utils.after_request"]

# Job Events
# ----------
# before_job = ["keepa_toolkit_v2.utils.before_job"]
# after_job = ["keepa_toolkit_v2.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"keepa_toolkit_v2.auth.validate"
# ]
