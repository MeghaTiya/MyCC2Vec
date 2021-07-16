# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:04:52 2021

@author: Dell
"""

run lmg_cc2ftr.py -train -train_data train.pkl -dictionary_data dict.pkl -no-cuda -device -1


run lmg_cc2ftr.py -predict -pred_data test.pkl -dictionary_data dict.pkl -load_model snapshot/2021-07-16_14-49-22/epoch_50.pt  -name output.pkl


run lmg_eval.py -train_data smalltrain.pkl -test_data test.pkl -train_cc2ftr_data train_cc2ftr.pkl -test_cc2ftr_data test_cc2ftr.pkl 


#debugfile('G:/CMI/CC2Vec-master-VVcpu/CC2Vec-master/lmg/lmg_cc2ftr.py', wdir='G:/CMI/CC2Vec-master-VVcpu/CC2Vec-master/lmg')