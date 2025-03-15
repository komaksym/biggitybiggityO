
DATA_PATH="train_set.json"        
OUTPUT_PATH="output_model/"     
MODEL_PATH="deepseek-ai/deepseek-coder-6.7b-instruct"

export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128

deepspeed finetune_deepseekcoder.py \
            --model_name_or_path "$MODEL_PATH" \
                --data_path "$DATA_PATH" \
                    --output_dir "$OUTPUT_PATH" \
                        --num_train_epochs 3 \
                            --model_max_length 1024 \
                                --per_device_train_batch_size 4 \
                                    --per_device_eval_batch_size 1 \
                                        --gradient_accumulation_steps 16 \
                                            --evaluation_strategy "no" \
                                                --save_strategy "steps" \
                                                    --save_steps 100 \
                                                        --save_total_limit 100 \
                                                            --learning_rate 2e-5 \
                                                                --warmup_steps 10 \
                                                                    --logging_steps 1 \
                                                                        --lr_scheduler_type "cosine" \
                                                                            --gradient_checkpointing True \
                                                                                --report_to "tensorboard" \
                                                                                    --deepspeed configs/ds_config_zero3.json \
                                                                                        --bf16 True
