## Data dictionary
Target  | Description   | Data Type
--|--|--
less_than_a_year    | indicates if the customer has a tenure less than 12 months and has churned. Engineered from the original churn and tenure columns | int64
Categorical Features   | Description |    Data Type
--|--|--
senior_citizen|    indicates if the customer is a senior citizen    |int64
dependents|        indicates if the customer has dependents    |int64
phone_service|    indicates if the customer has phone service with Telco    | int64
multiple_lines |    indicates if the customer with phone service has multiple lines    | int64
online_security|    indicates if the customer has online security services |    int 64
online_backup|    indicates if the customer has online backup services |    int64
device_protection    | indicates if the customer has device protection services |    int64
tech_support |  indicates if the customer has tech support services |    int64
streaming_tv |    indicates if the customer has tv streaming services |    int64
streaming_movies |    indicates if the customer has movie streaming services |    int64
payment_type    | indicates the type of payment method a customer is using | int64
internet_service_type |    indicates which internet service (if any) the customer has |    int64
gender    |   indicates the the customers' gender identity |    uint8
contract_type |     indicates the type of contract the customer has with Telco |    int64
auto_bill_pay |    indicates if the customer is enrolled in auto bill pay or not |    int64

Continuous Features | Description | Data Type
--|--|--
monthly_charges | how much a customer pays per month in dollars| float64
total_charges   | how much a customer has paid over the course of their tenure | float64
tenure          | how many months the customer has been with the company| int64

Other   | Description   | Data Type
--|--|--
churn   | indicates whether or not a customer churned | int64
customer_id | customer id number                       | object