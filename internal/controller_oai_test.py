import controller_oai
api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJzdXBvcm5vLmNoYXVkaHVyeUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZX0sImh0dHBzOi8vYXBpLm9wZW5haS5jb20vYXV0aCI6eyJwb2lkIjoib3JnLU9RM1l0SWRBVmQyaVZuRDlOeTZaWFZBSyIsInVzZXJfaWQiOiJ1c2VyLTQxYnFKcVd5RThIZUdrcGN0N0dHZ3RjdCJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIwNTQ4NDAyODg5ODQ2Mjg2NjIiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzA2MDA2Mjg3LCJleHAiOjE3MDY4NzAyODcsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.wzJ021DCDOOtiVd7XLXAN_9caeIEX8xZkp-LTzDb7uq1zK_lV5db-sSdmZwsV8T-EZWTELslaNGId2uQPNx01ANMJDz6sSF5hRJgO8RLiwJqSweDYeWoSUec8uiLdZA0NyxC_5P9sOHmwGQe4tZEFbssoQ2eHynh7zUNa1WcA27wPs-RsOjToKYuR6ZzynYHMoN8TXCX4xGUWnp8t9HSXKf6Mr_zaFExwYK2LWl8krQpxwSG22n_VOnsw-99aNikDB-m7Wrjp1oEZpjLik6d79cd-nb8XkRP7HfXer30IyajnrzQoj24E6MX1vTwjoNKV0uytbFjPIHMcOMt6z7acA"
controller = OpenAI_API_Controller(api_key) 
model_name = "legal-text-converter"
prompt = "Portfolio:\"Supreme Court Judge\"\nContext:\"Preamble of Constitution\"\nTextBody:\"WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC, REPUBLIC and to secure to all its citizens:-JUSTICE, social, economic and political;LIBERTY of thought, expression, belief, faith and worship;EQUALITY of status and of opportunity; and to promote among them allFRATERNITY assuring the dignity of the individual and the unity and integrity of the nation;IN OURthis twenty-sixth day of November 1949, do HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION.\""
max_tokens = 4000
temperature = 0.5
n = 1

generated_completions = controller.oai_prompt(model_name, prompt, max_tokens=max_tokens, temperature=temperature, n=n)

for i, text in enumerate(generated_completions):
    print(f"Completion {i+1}: {text}")