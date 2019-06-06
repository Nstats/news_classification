#!/usr/bin/env bash
python news_classification.py \
  --task_name=News \
  --do_train=true \
  --do_eval=true \
  --do_predict=true \
  --data_dir=./data/news \
  --vocab_file=./data/pretrained_model/chinese_base/vocab.txt \
  --bert_config_file=./data/pretrained_model/chinese_base/bert_config.json \
  --init_checkpoint=./data/pretrained_model/chinese_base/bert_model.ckpt \
  --max_seq_length=300 \
  --train_batch_size=2 \
  --learning_rate=2e-5 \
  --num_train_epochs=5 \
  --output_dir=./data/news/outputs

:<<annotation
annotation
