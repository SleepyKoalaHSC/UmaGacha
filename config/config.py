import configparser
import os

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "config.ini")

conf = configparser.ConfigParser()

conf.read(cfgpath, encoding="utf-8")

# 调用get方法获取配置的数据(获取的数据默认为字符串类型)
# 训练参数
epochs = int(conf.get('train_params', 'epochs'))
lr = float(conf.get('train_params', 'lr'))
vocab_size = int(conf.get('train_params', 'vocab_size'))
train_batch_size = int(conf.get('train_params', 'train_batch_size'))
eval_batch_size = int(conf.get('train_params', 'eval_batch_size'))
save_steps = int(conf.get('train_params', 'save_steps'))
logging_steps = int(conf.get('train_params', 'logging_steps'))

# 存储文件路径
pretrained_model_path = conf.get('file_path', 'pretrained_model_path')
output_model_path = conf.get('file_path', 'output_model_path')
logging_dir = conf.get('file_path', 'logging_dir')
train_set_path = conf.get('file_path', 'train_set_path')
test_set_path = conf.get('file_path', 'test_set_path')
