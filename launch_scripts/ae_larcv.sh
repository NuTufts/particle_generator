#!/bin/bash
CUDA_LAUNCH_BLOCKING=0 CUDA_VISIBLE_DEVICES=0,1 python train.py \
--gpu 1 \
--dataset 64 \
--batch_size 256 \
--num_epochs 1000 \
--sample_size 16 \
--shuffle True \
--drop_last True \
--num_workers 8 \
--model ae \
--n_layers 3 \
--l_dim 384 \
--ae_lr 1e-4 \
--ae_opt adam \
--loss_fn mse \
--beta 0.5 \
--data_root /media/hdd1/kai/particle_generator/larcv_data/train/ \
--save_root /media/hdd1/kai/particle_generator/experiments/
