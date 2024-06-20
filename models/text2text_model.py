import time

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from config import TEXT_TO_TEXT_GENERATION_MODEL_NAME


if TEXT_TO_TEXT_GENERATION_MODEL_NAME is None:
    raise FileNotFoundError(
        "Environment variable TEXT_TO_TEXT_GENERATION_MODEL_NAME was not found. Please add it to .env file"
    )


print('Starting load "Text to text model"')
_start_time = time.time()

_tokenizer = T5Tokenizer.from_pretrained(TEXT_TO_TEXT_GENERATION_MODEL_NAME)
_model = T5ForConditionalGeneration.from_pretrained(TEXT_TO_TEXT_GENERATION_MODEL_NAME)

_end_time = time.time()
_total_time_in_seconds = _end_time - _start_time
print(f'"Text to text model" was loaded in {round(_total_time_in_seconds, 2)} seconds')


def generate_text(
        input_text: str | list[str],
        encoder_no_repeat_ngram_size: float = 1,
        repetition_penalty: float = 0.5,
        no_repeat_ngram_size: float = 1,
        max_new_tokens: int = 200,
):
    if isinstance(input_text, list):
        input_text = '\n'.join(input_text)

    inputs = _tokenizer(input_text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = _model.generate(**inputs, num_beams=5, **{
            "encoder_no_repeat_ngram_size": encoder_no_repeat_ngram_size,
            "repetition_penalty": repetition_penalty,
            "no_repeat_ngram_size": no_repeat_ngram_size,
            "max_new_tokens": max_new_tokens,
        })
    return _tokenizer.decode(hypotheses[0], skip_special_tokens=True)
