# Copyright 2023-present Daniel Han-Chen & the MAI team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    "INT_TO_FLOAT_MAPPER",
    "FLOAT_TO_INT_MAPPER",
]

__INT_TO_FLOAT_MAPPER = \
{
    "mai/mistral-7b-bnb-4bit" : (
        "mai/mistral-7b",
        "mistralai/Mistral-7B-v0.1",
    ),
    "mai/llama-2-7b-bnb-4bit" : (
        "mai/llama-2-7b",
        "meta-llama/Llama-2-7b-hf",
    ),
    "mai/llama-2-13b-bnb-4bit" : (
        "mai/llama-2-13b",
        "meta-llama/Llama-2-13b-hf",
    ),
    "mai/codellama-34b-bnb-4bit" : (
        "codellama/CodeLlama-34b-hf",
    ),
    "mai/zephyr-sft-bnb-4bit" : (
        "mai/zephyr-sft",
        "HuggingFaceH4/mistral-7b-sft-beta",
    ),
    "mai/tinyllama-bnb-4bit" : (
        "mai/tinyllama",
        "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
    ),
    "mai/tinyllama-chat-bnb-4bit" : (
        "mai/tinyllama-chat",
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    ),
    "mai/mistral-7b-instruct-v0.1-bnb-4bit" : (
        "mai/mistral-7b-instruct-v0.1",
        "mistralai/Mistral-7B-Instruct-v0.1",
    ),
    "mai/mistral-7b-instruct-v0.2-bnb-4bit" : (
        "mai/mistral-7b-instruct-v0.2",
        "mistralai/Mistral-7B-Instruct-v0.2",
    ),
    "mai/llama-2-7b-chat-bnb-4bit" : (
        "mai/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "mai/llama-2-7b-chat-bnb-4bit" : (
        "mai/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "mai/codellama-7b-bnb-4bit" : (
        "mai/codellama-7b",
        "codellama/CodeLlama-7b-hf",
    ),
    "mai/codellama-13b-bnb-4bit" : (
        "codellama/CodeLlama-13b-hf",
    ),
    "mai/yi-6b-bnb-4bit" : (
        "mai/yi-6b",
        "01-ai/Yi-6B",
    ),
    "mai/solar-10.7b-bnb-4bit" : (
        "upstage/SOLAR-10.7B-v1.0",
    ),
    "mai/gemma-7b-bnb-4bit" : (
        "mai/gemma-7b",
        "google/gemma-7b",
    ),
    "mai/gemma-2b-bnb-4bit" : (
        "mai/gemma-2b",
        "google/gemma-2b",
    ),
    "mai/gemma-7b-it-bnb-4bit" : (
        "mai/gemma-7b-it",
        "google/gemma-7b-it",
    ),
    "mai/gemma-2b-bnb-4bit" : (
        "mai/gemma-2b-it",
        "google/gemma-2b-it",
    ),
    "mai/mistral-7b-v0.2-bnb-4bit" : (
        "mai/mistral-7b-v0.2",
        "alpindale/Mistral-7B-v0.2-hf",
    ),
    "mai/gemma-1.1-2b-it-bnb-4bit" : (
        "mai/gemma-1.1-2b-it",
        "google/gemma-1.1-2b-it",
    ),
    "mai/gemma-1.1-7b-it-bnb-4bit" : (
        "mai/gemma-1.1-7b-it",
        "google/gemma-1.1-7b-it",
    ),
    "mai/Starling-LM-7B-beta-bnb-4bit" : (
        "mai/Starling-LM-7B-beta",
        "Nexusflow/Starling-LM-7B-beta",
    ),
    "mai/Hermes-2-Pro-Mistral-7B-bnb-4bit" : (
        "mai/Hermes-2-Pro-Mistral-7B",
        "NousResearch/Hermes-2-Pro-Mistral-7B",
    ),
    "mai/OpenHermes-2.5-Mistral-7B-bnb-4bit" : (
        "mai/OpenHermes-2.5-Mistral-7B",
        "teknium/OpenHermes-2.5-Mistral-7B",
    ),
    "mai/codegemma-2b-bnb-4bit" : (
        "mai/codegemma-2b",
        "google/codegemma-2b",
    ),
    "mai/codegemma-7b-bnb-4bit" : (
        "mai/codegemma-7b",
        "google/codegemma-7b",
    ),
    "mai/codegemma-7b-it-bnb-4bit" : (
        "mai/codegemma-7b-it",
        "google/codegemma-7b-it",
    ),
    "mai/llama-3-8b-bnb-4bit" : (
        "mai/llama-3-8b",
        "meta-llama/Meta-Llama-3-8B",
    ),
    "mai/llama-3-8b-Instruct-bnb-4bit" : (
        "mai/llama-3-8b-Instruct",
        "meta-llama/Meta-Llama-3-8B-Instruct",
    ),
    "mai/llama-3-70b-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B",
    ),
    "mai/llama-3-70b-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B-Instruct",
    ),
    "mai/Phi-3-mini-4k-instruct-bnb-4bit" : (
        "mai/Phi-3-mini-4k-instruct",
        "microsoft/Phi-3-mini-4k-instruct",
    ),
    "mai/mistral-7b-v0.3-bnb-4bit" : (
        "mai/mistral-7b-v0.3",
        "mistralai/Mistral-7B-v0.3",
    ),
    "mai/mistral-7b-instruct-v0.3-bnb-4bit" : (
        "mai/mistral-7b-instruct-v0.3",
        "mistralai/Mistral-7B-Instruct-v0.3",
    ),
    "mai/Phi-3-medium-4k-instruct-bnb-4bit" : (
        "mai/Phi-3-medium-4k-instruct",
        "microsoft/Phi-3-medium-4k-instruct",
    ),
    "mai/Qwen2-0.5B-bnb-4bit" : (
        "mai/Qwen2-0.5B",
        "Qwen/Qwen2-0.5B",
    ),
    "mai/Qwen2-0.5B-Instruct-bnb-4bit" : (
        "mai/Qwen2-0.5B-Instruct",
        "Qwen/Qwen2-0.5B-Instruct",
    ),
    "mai/Qwen2-1.5B-bnb-4bit" : (
        "mai/Qwen2-1.5B",
        "Qwen/Qwen2-1.5B",
    ),
    "mai/Qwen2-1.5B-Instruct-bnb-4bit" : (
        "mai/Qwen2-1.5B-Instruct",
        "Qwen/Qwen2-1.5B-Instruct",
    ),
    "mai/Qwen2-7B-bnb-4bit" : (
        "mai/Qwen2-7B",
        "Qwen/Qwen2-7B",
    ),
    "mai/Qwen2-7B-Instruct-bnb-4bit" : (
        "mai/Qwen2-7B-Instruct",
        "Qwen/Qwen2-7B-Instruct",
    ),
    "mai/Qwen2-70B-bnb-4bit" : (
        "Qwen/Qwen2-70B",
    ),
    "mai/Qwen2-70B-Instruct-bnb-4bit" : (
        "Qwen/Qwen2-70B-Instruct",
    ),
    "mistralai/Codestral-22B-v0.1" : (
        "mistral-community/Codestral-22B-v0.1",
    ),
    "mai/gemma-2-9b-bnb-4bit" : (
        "mai/gemma-2-9b",
        "google/gemma-2-9b",
    ),
    "mai/gemma-2-27b-bnb-4bit" : (
        "mai/gemma-2-27b",
        "google/gemma-2-27b",
    ),
    "mai/gemma-2-9b-it-bnb-4bit" : (
        "mai/gemma-2-9b-it",
        "google/gemma-2-9b-it",
    ),
    "mai/gemma-2-27b-it-bnb-4bit" : (
        "mai/gemma-2-27b-it",
        "google/gemma-2-27b-it",
    ),
    "mai/Phi-3-mini-4k-instruct-v0-bnb-4bit" : ( # Old Phi pre July
        "mai/Phi-3-mini-4k-instruct-v0",
    ),
    "mai/Mistral-Nemo-Instruct-2407-bnb-4bit" : ( # New 12b Mistral models
        "mai/Mistral-Nemo-Instruct-2407",
        "mistralai/Mistral-Nemo-Instruct-2407",
    ),
    "mai/Mistral-Nemo-Base-2407-bnb-4bit" : ( # New 12b Mistral models
        "mai/Mistral-Nemo-Base-2407",
        "mistralai/Mistral-Nemo-Base-2407",
    ),
    "mai/Meta-Llama-3.1-8B-bnb-4bit" : (
        "mai/Meta-Llama-3.1-8B",
        "meta-llama/Meta-Llama-3.1-8B",
    ),
    "mai/Meta-Llama-3.1-8B-Instruct-bnb-4bit" : (
        "mai/Meta-Llama-3.1-8B-Instruct",
        "meta-llama/Meta-Llama-3.1-8B-Instruct",
    ),
    "mai/Meta-Llama-3.1-70B-bnb-4bit" : (
        "mai/Meta-Llama-3.1-70B",
        "meta-llama/Meta-Llama-3.1-70B",
    ),
    "mai/Meta-Llama-3.1-405B-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-405B",
    ),
    "mai/Meta-Llama-3.1-405B-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-405B-Instruct",
    ),
    "mai/Meta-Llama-3.1-70B-Instruct-bnb-4bit" : (
        "mai/Meta-Llama-3.1-70B-Instruct",
        "meta-llama/Meta-Llama-3.1-70B-Instruct",
    ),
    "mai/Mistral-Large-Instruct-2407-bnb-4bit" : (
        "mistralai/Mistral-Large-Instruct-2407",
    ),
    "mai/gemma-2-2b-bnb-4bit" : (
        "mai/gemma-2-2b",
        "google/gemma-2-2b",
    ),
    "mai/gemma-2-2b-it-bnb-4bit" : (
        "mai/gemma-2-2b-it",
        "google/gemma-2-2b-it",
    ),
    "mai/Phi-3.5-mini-instruct-bnb-4bit" : (
        "mai/Phi-3.5-mini-instruct",
        "microsoft/Phi-3.5-mini-instruct",
    ),
    "mai/c4ai-command-r-08-2024-bnb-4bit" : (
        "CohereForAI/c4ai-command-r-08-2024",
    ),
    "mai/c4ai-command-r-plus-08-2024-bnb-4bit" : (
        "CohereForAI/c4ai-command-r-plus-08-2024",
    ),
    "mai/Llama-3.1-Storm-8B-bnb-4bit" : (
        "mai/Llama-3.1-Storm-8B",
        "akjindal53244/Llama-3.1-Storm-8B",
    ),
    "mai/Hermes-3-Llama-3.1-8B-bnb-4bit" : (
        "mai/Hermes-3-Llama-3.1-8B",
        "NousResearch/Hermes-3-Llama-3.1-8B",
    ),
    "mai/Hermes-3-Llama-3.1-70B-bnb-4bit" : (
        "mai/Hermes-3-Llama-3.1-70B",
        "NousResearch/Hermes-3-Llama-3.1-70B",
    ),
    "mai/Hermes-3-Llama-3.1-405B-bnb-4bit" : (
        "NousResearch/Hermes-3-Llama-3.1-405B",
    ),
    "mai/SmolLM-135M-bnb-4bit" : (
        "mai/SmolLM-135M",
        "HuggingFaceTB/SmolLM-135M",
    ),
    "mai/SmolLM-360M-bnb-4bit" : (
        "mai/SmolLM-360M",
        "HuggingFaceTB/SmolLM-360M",
    ),
    "mai/SmolLM-1.7B-bnb-4bit" : (
        "mai/SmolLM-1.7B",
        "HuggingFaceTB/SmolLM-1.7B",
    ),
    "mai/SmolLM-135M-Instruct-bnb-4bit" : (
        "mai/SmolLM-135M-Instruct",
        "HuggingFaceTB/SmolLM-135M-Instruct",
    ),
    "mai/SmolLM-360M-Instruct-bnb-4bit" : (
        "mai/SmolLM-360M-Instruct",
        "HuggingFaceTB/SmolLM-360M-Instruct",
    ),
    "mai/SmolLM-1.7B-Instruct-bnb-4bit" : (
        "mai/SmolLM-1.7B-Instruct",
        "HuggingFaceTB/SmolLM-1.7B-Instruct",
    ),
    "mai/Mistral-Small-Instruct-2409-bnb-4bit" : (
        "mai/Mistral-Small-Instruct-2409",
        "mistralai/Mistral-Small-Instruct-2409",
    ),
    "mai/Qwen2.5-0.5B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-0.5B-Instruct",
        "Qwen/Qwen2.5-0.5B-Instruct",
    ),
    "mai/Qwen2.5-1.5B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-1.5B-Instruct",
        "Qwen/Qwen2.5-1.5B-Instruct",
    ),
    "mai/Qwen2.5-3B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-3B-Instruct",
        "Qwen/Qwen2.5-3B-Instruct",
    ),
    "mai/Qwen2.5-7B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-7B-Instruct",
        "Qwen/Qwen2.5-7B-Instruct",
    ),
    "mai/Qwen2.5-14B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-14B-Instruct",
        "Qwen/Qwen2.5-14B-Instruct",
    ),
    "mai/Qwen2.5-32B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-32B-Instruct",
        "Qwen/Qwen2.5-32B-Instruct",
    ),
    "mai/Qwen2.5-72B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-72B-Instruct",
        "Qwen/Qwen2.5-72B-Instruct",
    ),
    "mai/Qwen2.5-0.5B-bnb-4bit" : (
        "mai/Qwen2.5-0.5B",
        "Qwen/Qwen2.5-0.5B",
    ),
    "mai/Qwen2.5-1.5B-bnb-4bit" : (
        "mai/Qwen2.5-1.5B",
        "Qwen/Qwen2.5-1.5B",
    ),
    "mai/Qwen2.5-3B-bnb-4bit" : (
        "mai/Qwen2.5-3B",
        "Qwen/Qwen2.5-3B",
    ),
    "mai/Qwen2.5-7B-bnb-4bit" : (
        "mai/Qwen2.5-7B",
        "Qwen/Qwen2.5-7B",
    ),
    "mai/Qwen2.5-14B-bnb-4bit" : (
        "mai/Qwen2.5-14B",
        "Qwen/Qwen2.5-14B",
    ),
    "mai/Qwen2.5-32B-bnb-4bit" : (
        "mai/Qwen2.5-32B",
        "Qwen/Qwen2.5-32B",
    ),
    "mai/Qwen2.5-72B-bnb-4bit" : (
        "mai/Qwen2.5-72B",
        "Qwen/Qwen2.5-72B",
    ),
    "mai/Qwen2.5-Math-1.5B-bnb-4bit" : (
        "mai/Qwen2.5-Math-1.5B",
        "Qwen/Qwen2.5-Math-1.5B",
    ),
    "mai/Qwen2.5-Math-7B-bnb-4bit" : (
        "mai/Qwen2.5-Math-7B",
        "Qwen/Qwen2.5-Math-7B",
    ),
    "mai/Qwen2.5-Math-72B-bnb-4bit" : (
        "mai/Qwen2.5-Math-72B",
        "Qwen/Qwen2.5-Math-72B",
    ),
    "mai/Qwen2.5-Math-1.5B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-Math-1.5B-Instruct",
        "Qwen/Qwen2.5-Math-1.5B-Instruct",
    ),
    "mai/Qwen2.5-Math-7B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-Math-7B-Instruct",
        "Qwen/Qwen2.5-Math-7B-Instruct",
    ),
    "mai/Qwen2.5-Math-72B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-Math-72B-Instruct",
        "Qwen/Qwen2.5-Math-72B-Instruct",
    ),
    "mai/Qwen2.5-Coder-1.5B-bnb-4bit" : (
        "mai/Qwen2.5-Coder-1.5B",
        "Qwen/Qwen2.5-Coder-1.5B",
    ),
    "mai/Qwen2.5-Coder-7B-bnb-4bit" : (
        "mai/Qwen2.5-Coder-7B",
        "Qwen/Qwen2.5-Coder-7B",
    ),
    "mai/Qwen2.5-Coder-1.5B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-Coder-Instruct-1.5B",
        "Qwen/Qwen2.5-Coder-Instruct-1.5B",
    ),
    "mai/Qwen2.5-Coder-7B-Instruct-bnb-4bit" : (
        "mai/Qwen2.5-Coder-7B-Instruct",
        "Qwen/Qwen2.5-Coder-7B-Instruct",
    ),
}

INT_TO_FLOAT_MAPPER  = {}
FLOAT_TO_INT_MAPPER  = {}
MAP_TO_MAI_16bit = {}

for key, values in __INT_TO_FLOAT_MAPPER.items():
    INT_TO_FLOAT_MAPPER[key] = values[0]

    for value in values:
        FLOAT_TO_INT_MAPPER[value] = key
    pass

    # Map to MAI version for 16bit versions
    if len(values) == 2:
        if values[0].startswith("mai"):
            MAP_TO_MAI_16bit[values[1]] = values[0]
            MAP_TO_MAI_16bit[values[1].lower()] = values[0]
        pass
    pass

    # Get lowercased
    lowered_key = key.lower()
    INT_TO_FLOAT_MAPPER[lowered_key] = values[0].lower()

    for value in values:
        FLOAT_TO_INT_MAPPER[value.lower()] = lowered_key
    pass
pass
