#!/bin/bash
CUDA_VISIBLE_DEVICES=0,1 python train.py \
--gpu 0 \
--dataset 256 \
--batch_size 250 \
--num_epochs 1000 \
--sample_size 16 \
--shuffle True \
--drop_last True \
--num_workers 8 \
--model conv_ae \
--depth 32 \
--n_layers 5 \
--l_dim 102 \
--ae_lr 1e-4 \
--ae_opt adam \
--loss_fn mse \
--beta 0.5 \
--data_root /media/hdd1/kai/particle_generator/larcv_data/train/ \
--save_root /media/hdd1/kai/particle_generator/experiments/
