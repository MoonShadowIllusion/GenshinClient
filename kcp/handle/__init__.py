import os.path
from importlib import import_module
from .BaseHandle import BaseHandle
[
    import_module(f'kcp.handle.{i}')
    for i in [i.removesuffix('.py')
              for i in os.listdir(os.path.dirname(__file__))
              if i.startswith('Handler') and i.endswith('.py')
              ]
]

# 应该只有...Rsp
handles = {}
for i in BaseHandle.__subclasses__():
    _type, _funcs = i.getHandles()
    _hand = handles.get(_type, None)
    if _hand:
        for j in _hand:
            _hand.append(j)
    else:
        handles[_type] = [k for k in _funcs]

print(handles)