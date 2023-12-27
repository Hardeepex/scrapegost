# Lambda function to normalize dates to a standard format
normalize_date = lambda raw_date: raw_date.strip().replace('/', '-')

# Lambda function to normalize text to lower case
normalize_text = lambda raw_text: raw_text.lower()

# Lambda function to normalize numbers to integers
normalize_number = lambda raw_number: int(raw_number)
