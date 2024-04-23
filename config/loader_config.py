#%%
import os
import numpy as np
import config.config_dict


'''
dataname格式:
    name_arg1-xxx_arg2-xxx_arg3.......
    xxx必须为数字
'''
class DataConfig():
    def __init__(self):
        self.root_dir='data/samples/'
        self.name=config.config_dict.cfg['dataset']['name']

        self.args=config.config_dict.cfg['dataset']['args']
        self.info={}
        
        #例如'sentinel2_size-6','sentinel2_size-4','sentinel2_size-2':

        eval('self.'+self.name)(**self.args)


    
    def googledamagedv2(self,size,city,mode):
        # city='Raqqa'
        if mode is None:
            if city=='allcities':
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}/val.pth'
            else:
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}/cities/{city}/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}/cities/{city}/val.pth'
        else:
            if city=='allcities':
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}/val.pth'
            else:
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}/cities/{city}/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}/cities/{city}/val.pth'
    def googledamagedv3(self,size,city,mode):
        # city='Hama'
        if mode is None:
            if city=='allcities':
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}_mt/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}_mt/val.pth'
            else:
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}_mt/cities/{city}/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}_mt/cities/{city}/val.pth'
        else:
            if city=='allcities':
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}_mt/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}_mt/val.pth'
            else:
                self.info['train_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}_mt/cities/{city}/train.pth'
                self.info['test_dir']=f'data/samples/Syria_samples/split_size{size}_{mode}_mt/cities/{city}/val.pth'
    def Udamagedv2(self,size,city,mode):
        self.info['train_dir']=f'data/samples/Ukraine_samples/split/cities/{city}/train.pth'
        self.info['test_dir']=f'data/samples/Ukraine_samples/split/cities/{city}/val.pth'
    def Udamagedv3crossval(self,size,city,mode):
        self.info['train_dir']=f'data/samples/Ukraine_samples/split_mt/cities/{city}/cross_val/{mode}/train.pth'
        self.info['test_dir']=f'data/samples/Ukraine_samples/split_coordv2_v3/cities/{city}/cross_val/{mode}/val.pth'
    def Udamagedv3(self,size,city,mode):
        self.info['train_dir']=f'data/samples/Ukraine_samples/split_mt/cities/{city}/train.pth'
        self.info['test_dir']=f'data/samples/Ukraine_samples/split_mt/cities/{city}/val.pth'

  
# %%
