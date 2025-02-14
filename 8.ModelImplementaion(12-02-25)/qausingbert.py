import torch
from transformers import (
    BertForQuestionAnswering,
    BertTokenizerFast,
)
from scipy.special import softmax
import plotly.express as px
import pandas as pd
import numpy as np

model_name="deepset/bert-base-cased-squad2"

tokenizer=BertTokenizerFast.from_pretrained(model_name)
model=BertForQuestionAnswering.from_pretrained(model_name)


def predict_answers(context,question):
    inputs=tokenizer(question,context,return_tensors='pt')
    with torch.no_grad():
        output=model(**inputs)
    start_score,end_score=softmax(output.start_logits)[0],softmax(output.end_logits)[0]
    start_idx = np.argmax(start_score)
    end_idx = np.argmax(end_score)
    confidence_score = (start_score[start_idx] + end_score[end_idx]) /2
    answer_ids = inputs.input_ids[0][start_idx: end_idx + 1]
    answer_tokens = tokenizer.convert_ids_to_tokens(answer_ids)
    answer = tokenizer.convert_tokens_to_string(answer_tokens)

    if answer != tokenizer.cls_token:
        return answer, confidence_score
    return None, confidence_score


context = """Subhash Chandra Bose passed through quarters inhabited by Englishmen and also met a
 large number of them in the tram cars. The British using these cars were purposely rude and offensive to Indians in various ways. The sensitive mind of Subhash revolted against such insulting and rude behavior of the British.
 On many occasions, there was an exchange of hot words between him and misbehaving British.
   Majority of the students of the Presidency College, where he studied, were free thinkers. 
   The college continued to be a storm centre and was looked upon by the British Government "as a hotbed of sedition, rendezvous of revolutionaries" and was frequently searched by the police.
 The first two years of his life were greatly influenced by the group, which styled itself as the neo-Vivekananda group and Subhash developed intellectually during this period. The group generally
   followed the teachings of Rama Krishna and Vivekananda with special emphasis on social service as
 means of spiritual development and was non-aligned to a revolutionary group. 
 The shock of the Great World War roused his political consciousness. He graduated at the age of 22 and enrolled himself for the postgraduate with experimental psychology as a special subject. 
His father, however, wanted him to go to England to appear for the Indian Civil Services. 
In spite of his mental reservations, Subhash took it as a challenge. In England, 
he was greatly impressed with the freedom allowed to students at Cambridge. Every student behaved in a dignified manner. Notwithstanding his preoccupation with his studies,
 he displayed his public spirit and fearlessness throughout his stay in England. He and K. L. Gouba were selected by the Indian Majlis, to represent the British Government the difficulties the Indian students encountered for admission to the University Officers' Training Corps. Though he took a harsh view of the British high handedness and racial arrogance, 
 he did admire their qualities which exacted him. He himself behaved there in a dignified way and was of the view that Indians who go abroad, must consider themselves to be unofficial ambassadors of the country, who should uphold their country's prestige. 
 He was quite serious in purpose and disliked anybody wasting time on trivialities."""
questions = [
    "Who were selected by the Indian Majlis?",
    "Majority of the students of the Presidency College were?",
    "Whose teachings did the group generally follow?",
    "Subhash Chandra's father wanted him to go to England and appear for what?",
    "At what age did Subhash enroll for his postgraduation?",
    " what is apple?"
]

for question in questions:
    print(f"Question:{question}")
    print(f"Ans:{predict_answers(context,question)[0]}")
    print(f"confidence_score:{int(predict_answers(context,question)[1]*100)}","%")
    print()


