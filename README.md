nohup ~/.local/bin/tensorboard --bind_all --logdir cp_autovocoder/logs > tensorboard.out 2>&1 &


python3 train.py --config config_v1.json --input_wavs_dir /home/yehor/iSTFTNet-pytorch/lada_wavs --input_training_file /home/yehor/iSTFTNet-pytorch/training_list.txt --input_validation_file /home/yehor/iSTFTNet-pytorch/validation_list.txt

python3 train.py --config config_v1.json --input_wavs_dir /home/yehor/iSTFTNet-pytorch/lada_wavs --input_training_file /home/yehor/iSTFTNet-pytorch/training_list.txt --input_validation_file /home/yehor/iSTFTNet-pytorch/validation_list.txt --checkpoint_path cp_hifigan/


python3 train.py --config config_v1.json --input_wavs_dir /home/yehor/iSTFTNet-pytorch/lada_wavs --input_training_file /home/yehor/iSTFTNet-pytorch/training_list.txt --input_validation_file /home/yehor/iSTFTNet-pytorch/validation_list.txt


python3 inference.py --checkpoint_file cp_hifigan/g_00005000 --input_wav_file lada_wavs/25530.wav --output_file output.wav

python3 inference_mel.py --checkpoint_file cp_hifigan/g_00035000 --input_mel_file results3/2_0_lada_durscaling1.0_sigma0.8_sigmatext0.666_sigmaf01.0_sigmaenergy1.0_denoised_0.0.mel --output_file output.wav


nohup ~/.local/bin/tensorboard --bind_all --logdir cp_hifigan/logs > tensorboard.out 2>&1 &
