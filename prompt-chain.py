# prompt-chain.py code floww

def run_prompt_chain(customer_query):
    results = []

    # Step 1: Interpret intent
    intent = f"The customer seems to be asking about: {customer_query.strip()}."
    results.append(intent)

    # Step 2: Map to possible categories
    possible_categories = []
    categories = [
        "Account Opening", "Billing Issue", "Account Access", "Transaction Inquiry",
        "Card Services", "Account Statement", "Loan Inquiry", "General Information"
    ]

    query_lower = customer_query.lower()
    if "open" in query_lower or "new account" in query_lower:
        possible_categories.append("Account Opening")
    if "bill" in query_lower or "charge" in query_lower or "payment" in query_lower:
        possible_categories.append("Billing Issue")
    if "login" in query_lower or "password" in query_lower or "access" in query_lower:
        possible_categories.append("Account Access")
    if "transaction" in query_lower or "money" in query_lower or "transfer" in query_lower:
        possible_categories.append("Transaction Inquiry")
    if "card" in query_lower or "debit" in query_lower or "credit" in query_lower:
        possible_categories.append("Card Services")
    if "statement" in query_lower:
        possible_categories.append("Account Statement")
    if "loan" in query_lower:
        possible_categories.append("Loan Inquiry")
    if not possible_categories:
        possible_categories.append("General Information")

    results.append(possible_categories)

    # Step 3: Choose most appropriate category
    chosen_category = possible_categories[0]
    results.append(chosen_category)

    # Step 4: Extract additional details (simple keyword-based example)
    import re
    details = re.findall(r"\b\d+\b", customer_query)
    if details:
        extracted = f"Possible numeric details found: {details}"
    else:
        extracted = "No extra details provided."
    results.append(extracted)

    # Step 5: Generate short response
    response = f"Thank you for contacting us. It seems your issue relates to {chosen_category}. Our team will assist you shortly."
    results.append(response)

    return results


# Example test
if __name__ == "__main__":
    user_query = "Hi, I lost my debit card and need a replacement."
    outputs = run_prompt_chain(user_query)
    for i, step in enumerate(outputs, 1):
        print(f"Step {i} Output: {step}\n")
