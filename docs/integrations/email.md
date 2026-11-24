# Email Templates for Transactional Emails

## Overview
Transactional emails are sent in response to user actions, such as password reset, tool completion, and more. This section details the email templates used for these purposes.

## Password Reset Email Template
### Purpose
Used when a user requests a password reset.

### Template
```plaintext
<!DOCTYPE html>
<html>
<head>
    <title>Password Reset</title>
</head>
<body>
    <h1>Password Reset</h1>
    <p>Dear [User Name],</p>
    <p>Thank you for using our service. You have requested a password reset for your account.</p>
    <p>To reset your password, please click the link below:</p>
    <p><a href="[Reset URL]">Reset Password</a></p>
    <p>If you did not request this, please ignore this email and your account will remain secure.</p>
    <p>Best regards,</p>
    <p>[Platform Name] Team</p>
</body>
</html>
```

### Variables
- `[User Name]`: The username of the user who requested the password reset.
- `[Reset URL]`: The URL to reset the password.

## Tool Completion Notification Email Template
### Purpose
Used when a user completes a tool.

### Template
```plaintext
<!DOCTYPE html>
<html>
<head>
    <title>Tool Completion Notification</title>
</head>
<body>
    <h1>Tool Completion Notification</h1>
    <p>Dear [User Name],</p>
    <p>Thank you for using our service. You have successfully completed the [Tool Name] tool.</p>
    <p>Here are the details of your completion:</p>
    <ul>
        <li>[Tool Details]</li>
    </ul>
    <p>For further information, please contact our support team.</p>
    <p>Best regards,</p>
    <p>[Platform Name] Team</p>
</body>
</html>
```

### Variables
- `[User Name]`: The username of the user who completed the tool.
- `[Tool Name]`: The name of the tool.
- `[Tool Details]`: The details of the tool completion.

## Verification Email Template
### Purpose
Used when a user needs to verify their email address.

### Template
```plaintext
<!DOCTYPE html>
<html>
<head>
    <title>Email Verification</title>
</head>
<body>
    <h1>Email Verification</h1>
    <p>Dear [User Name],</p>
    <p>To verify your email address, please click the link below:</p>
    <p><a href="[Verification URL]">Verify Email</a></p>
    <p>If you did not request this, please ignore this email and your account will remain secure.</p>
    <p>Best regards,</p>
    <p>[Platform Name] Team</p>
</body>
</html>
```

### Variables
- `[User Name]`: The username of the user who needs to verify their email.
- `[Verification URL]`: The URL to verify the email address.

## Production-Ready Considerations
- Ensure all URLs are properly formatted and accessible.
- Use HTTPS for all links to ensure security.
- Include placeholders for variables that will be dynamically populated during the email sending process.
- Test the templates thoroughly in different environments to ensure they work as expected.

## Conclusion
These templates are designed to provide clear and informative content to users while ensuring security and user experience. They are essential for maintaining a robust and user-friendly Personal Technology Platform.
