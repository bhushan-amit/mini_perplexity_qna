from openai import OpenAI

def generate_response(prompt):
    """
    Sends a prompt to GPT-4 and retrieves the response.
    """
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a mini Perplexity app now. We have been given a query to answer. "
                        "To help us, we have searched the web and have got some snippets and content relevant for the query. "
                        "Your task is to deliver a concise and accurate response to a user's query, drawing from the given search results. "
                        "If the query is ambiguous, feel free to inform the user and ask for clarification. "
                        "Your answer must be precise, of high-quality, and written by an expert using an unbiased and journalistic tone."
                    )
                },
                {"role": "user", "content": prompt}
            ],
        )

        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        print(f"Error in GPT-4 API call: {e}")
        return "Sorry, We couldn't process the information at the moment."
