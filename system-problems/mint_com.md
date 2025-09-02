'''
Design mint.com

Hints:
Interviewer feedback was strange - they said my approach of using message broker + webhook for long-waiting expense-report APIs was too complex, and that storing bank-scraped data in blob storage was also too complex.

Despite applying for an SDE ML position with my ML background, there were no ML questions in the interview.

Requirements:
Users can retrieve their transaction history
Users can set budgets for different categories
Key Components:
User Management System:
User authentication and profiles
Preferences and settings storage
Data Integration Layer:
Connects to banks and financial institutions
Securely retrieves transaction data
Handles authentication with financial institutions
Transaction Processing System:
Stores transaction data
Categorizes transactions (food, entertainment, etc.)
Provides search and filtering capabilities
Budget Management System:
Allows users to set budgets for different categories
Tracks spending against budgets
Sends notifications when approaching budget limits
Storage System:
Secure database for user data
Efficient storage for transaction history
API Layer:
Provides interfaces for mobile and web applications
Handles authentication and data requests
Notification System:
Alerts users about budget status, unusual activity, etc.
Supports multiple channels (email, push, SMS)
This design would need to address challenges like data security, real-time updates, scalability for millions of transactions, and ensuring accurate categorization of transactions.

'''