
import openai

from data_load import load_system_prompt

with open("../openai_api_key.txt", "r") as f:
    api_key = f.read()

# openai.api_key = api_key

GPT_model = "gpt-3.5-turbo"

RANDOM_SEED = 123

client = openai.Client(api_key=api_key)

def get_model_response(message, gpt_model=GPT_model, random_seed=RANDOM_SEED):
    completion = client.chat.completions.create(
    model=gpt_model,
    seed=random_seed,
    messages=message,
    )
    return completion.choices[0].message.content

def get_message_with_example(game_question, game_examples, system_prompt_file='new_system_prompt.txt'):
    messages = []
    
    messages.append({"role": "system", "content":load_system_prompt(system_prompt_file)})

    # some examples
    for example in game_examples:
        messages.append({"role": "user", "content": f"Name: {example.name}\nDescription: {example.description}"})
        messages.append({"role": "assistant", "content": example.code})

    # final prompt
    messages.append({"role": "user", "content": f"Name: {game_question.name}\nDescription: {game_question.description}"})
    return messages


def get_response(message_fn, game_question, game_examples):
    return get_model_response(message_fn(game_question, game_examples))