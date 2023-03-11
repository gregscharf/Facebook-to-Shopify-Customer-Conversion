# Facebook to Shopify Customer Conversion
Converts a csv file containing Facebook leads into a format that can be imported into Shopify to create new customers

Occasionally Shopify adds new fields to the customer object.  The header line in the script will need to be updated when that occurs, otherwise the csv file output will not import into Shopify.

Usage:
```bash
./facebook_to_shopify_customer_converstion.py facebook_leads.csv shopify_customers.csv
```

