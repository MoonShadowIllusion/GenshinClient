DEVICE = "7a3ea24ed3f172dc882af6721541a5173399a5fc1655361916696"

# 8个字节

CLIENT_SEED: bytes = b'xukexuke'

# 发送数据时，此值加一
client_sequence_id = 'client_sequence_id'


def init():  # 初始化
    global _global_dict
    _global_dict = {
        "client_sequence_id": 1
    }


def set_value(key, value):
    # 定义一个全局变量
    _global_dict[key] = value


def get_value(key):
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _global_dict[key]
    except:
        print('读取' + key + '失败\r\n')
