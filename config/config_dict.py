cfg={'project_name':'PtNet_Syria_size6',
     'root_dir':'',
    'dataset':{'name':'googledamagedv2',
                'args':{'size':6,'city':'allcities','mode':None}},
    'transform_train':{
                'to_tensor':True,
                'hv_flip_together':True,
                # 'v_flip':True,
                # 'h_flip':True,
                # 'resize':[32,32],
                # 'randomcrop':[32,4],#size,padding
                # 'normal':[[],[]]
                },
    #val_transform
    'transform_val':{
                'to_tensor':True,
                'hv_flip_together':False,
                },
    'loader':{
                'name':'googlesize6',
                # 'name':'google',
                # 'name':'googlesize6',
                # 'name':'googlesize6upresample',
                'mode':None,
                'use_samples_percent':1,
                'batch_size':256,#1024
                'num_workers':8,
                'shuffle':True
            },
    'model':{'name':'ptnetsize6',

                'args':{'n_class':2}      
            },
    'train':{
                'name':'google',
                # 'name':'sentinel2',
                'gpu_ids':[0],
                'lr':0.0025,
                'lr_policy':'step',#or 'linear'
                'loadbestmodel_whenbackwateracc':[False,10],
                'step_size':15,
                'gamma':0.5,
                'momentum':0.9,
                'w_decay':5e-4,
                
                'max_epochs':135,
                'loss':'cross_entropy',# or binary_cross_entropy(暂时不支持)
                'tv_loss':100,
                #'load_pretrain':[False, 'SupCon1000v2', 'ckpt_epoch_1000.pth', '/home/hk/python_script/SupContrast-master/SupContrast-master/save/SupCon/HamaandRaqqa_size6v2_models/SupCon_HamaandRaqqa_size6v2_ptnetsize6_lr_0.05_decay_0.0001_bsz_1024_temp_0.07_trial_0_cosine_warm/'],
                'load_pretrain':[False, 'SupCon1000v2', 'ckpt_epoch_1000.pth', ''],
                'load_checkpoint':False,
                #weitght:None or [1,9] or [x,x]  ignore_index=2 or -100(default) ignore_index不能用于binary_cross_entropy
                # [0.51979147, 13.13170347]Hama no enhance
                # 
                
                'loss_fun_args':{'weight':[1, 9],'ignore_index':-100},
                'print_step_interval':100,
                'acc_index':'F1_1'
                # 'acc_index':'precision'
            },
    'v_generalization':[False, 'channels3normalized']
                }