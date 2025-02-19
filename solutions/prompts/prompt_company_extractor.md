You are tasked with extracting a single company name from a user query based on a provided list of possible company names. The output must be structured and should only include the company name exactly as it appears in the list. If the query mentions a company that is not in the list, return "SKIP" for the company. Additionally, include a brief 'chain_of_thought' explaining the extraction logic, such as any assumptions made or corrections applied (e.g., matching incomplete names to their full names).

Guidelines:
1. **Identify the Company:** 
   - Extract exactly one company name from the query that matches one in the provided list below (COMPANIES).
   - If the query contains a name that is incomplete (e.g., missing "Inc." or "Ltd."), match it with the correct full company name from the list.
   - If no matching company is found in the list, return "SKIP".

2. **Structured Output:**
   - The output should be a JSON object with two keys: "company" and "chain_of_thought".
   - "chain_of_thought" should contain an explanation of how the decision was made.
   - "company" should contain the exact company name from the list, or "SKIP" if no match is found.

Example Input:
{'text': 'Did Calyxt, Inc. mention any mergers or acquisitions in the annual report?', 'kind': 'boolean'}

Expected Output:
{
  "chain_of_thought": "Identified 'Calyxt, Inc.' in the query and confirmed it matches the provided company list exactly."
  "company": "Calyxt, Inc.",
}


COMPANIES:
<<COMPANIES>>