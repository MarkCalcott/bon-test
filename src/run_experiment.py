import ollama
import json
import os
from tqdm import tqdm
from bon import best_of_n


def prompt(context: str, query: str, model: str = "qwen3.5:9b") -> str:
    """
    Prompts an LLM with a user message given a system context.
    """

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": query},
        ],
        think=False,
    )
    return response.message.content


def log_result(path, **record):
    with open(path, "a", encoding="utf-8") as handler:
        handler.write(json.dumps(record, ensure_ascii=False) + "\n")


def run_experiment(exp_id: int):

    save_file = f"../data/experiment_{exp_id}.jsonl"
    if os.path.exists(save_file):
        raise FileExistsError(f"The file '{save_file}' already exists.")

    with open("../assets/experiments.json") as handler:
        data = json.load(handler)

    experiment = data[exp_id - 1]
    assert exp_id == experiment["id"]

    print(f"Running experiment {experiment["id"]}")
    print(experiment["description"])

    n = experiment["runs"]
    samples = experiment["samples"]
    messages = experiment["messages"]

    for replicate in tqdm(range(n), unit=" samples processed"):
        for sample in samples:
            context = messages[sample["context"]]
            message = messages[sample["user"]]
            if sample["BoN"]:
                query = best_of_n(message)
            else:
                query = message

            response = prompt(context, query)
            log_result(
                save_file,
                name=sample["name"],
                query=query,
                response=response,
                replicate=replicate,
            )

    print()
