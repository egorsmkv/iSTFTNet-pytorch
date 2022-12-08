with open('./radtts/filelists/olha_ukrainian_train_filelist.txt') as x:
    for z in x:
        # this is as ugly as it is effective, lol
        print(z.strip().split('|')[0].split('/')[-1].replace('.wav',''))
