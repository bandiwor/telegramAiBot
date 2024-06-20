import time
from typing import Literal

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

from config import TRANSLATION_MODEL_NAME

if TRANSLATION_MODEL_NAME is None:
    raise FileNotFoundError(
        "Environment variable TRANSLATION_MODEL_NAME was not found. Please add it to .env file"
    )


print('Starting load "Translation model"')
_start_time = time.time()

_model = T5ForConditionalGeneration.from_pretrained(TRANSLATION_MODEL_NAME)
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_model.to(_device)
_tokenizer = T5Tokenizer.from_pretrained(TRANSLATION_MODEL_NAME)

_end_time = time.time()
_total_time_in_seconds = _end_time - _start_time
print(f'"Translation model" was loaded in {round(_total_time_in_seconds, 2)} seconds')


def translate_text(input_text: str, target_language: Literal['ru'] | Literal['en'] | Literal['zh']):
    prompt = f'translate to {target_language}: {input_text}'
    input_ids = _tokenizer(prompt, return_tensors="pt")

    generated_tokens = _model.generate(**input_ids.to(_device))
    result = _tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return "; ".join(result)
