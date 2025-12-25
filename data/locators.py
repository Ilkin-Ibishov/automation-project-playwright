# Signup Form (Step 1 - on /login page)
SIGNUP_NAME = "[data-qa='signup-name']"
SIGNUP_EMAIL = "[data-qa='signup-email']"
SIGNUP_BUTTON = "[data-qa='signup-button']"

# Login Form (on /login page)
LOGIN_EMAIL = "[data-qa='login-email']"
LOGIN_PASSWORD = "[data-qa='login-password']"
LOGIN_BUTTON = "[data-qa='login-button']"

# Registration Form (Step 2 - on /signup page)
# Use text-based selector (works better in Playwright than XPath)
REGISTRATION_TITLE = "h2:has-text('Enter Account Information')"

# Error Messages
EMAIL_EXISTS_ERROR = "p:has-text('Email Address already exist!')"