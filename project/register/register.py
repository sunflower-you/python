from easydict import EasyDict
from typing import Any
import torch
from enum import Enum, IntEnum
import numpy as np


def _register_generic(module_dict, module_name, module):
    if isinstance(module_name, list):
        for module_name_item in module_name:
            assert module_name_item not in module_dict
            module_dict[module_name_item] = module
    else:
        assert module_name not in module_dict
        module_dict[module_name] = module


class Registry(EasyDict):
    """
        注册器：
    """

    def __init__(self, *args, **kwargs):
        super(Registry, self).__init__(*args, **kwargs)

    def register(self, module_name, module=None):
        # used as function call
        if module is not None:
            if isinstance(module, object):
                assert hasattr(module, "__call__")
            _register_generic(self, module_name, module)
            return

        # used as decorator
        def register_fn(fn):
            _register_generic(self, module_name, fn)
            return fn

        return register_fn
    
ACTIVATION_CLASS = Registry()


class Activation:
    def __init__(self) -> None:
        pass

    def __call__(self, x) -> Any:
        raise NotImplementedError()

class Silu(Activation):
    act_type = "silu"
    
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, x) -> torch.Tensor:
        return x * torch.sigmoid(x)
    

class Relu(Activation):
    act_type = "relu"

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, x) -> torch.Tensor:
        return torch.relu(x)


@ACTIVATION_CLASS.register("Relu6")
class Relu6(Activation):
    act_type = "relu6"

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, x) -> torch.Tensor:
        return torch.clamp(x, 0, 6)


@ACTIVATION_CLASS.register("Threshold")
class Threshold(Activation):
    act_type = "Threshold"

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, x) -> torch.Tensor:
        return torch.threshold(x, 2, 0)
    

class ActivationType(str, Enum):
    Silu = "Silu"
    Relu = "Relu"


ACTIVATION_CLASS.register(ActivationType.Silu, Silu)
ACTIVATION_CLASS.register(ActivationType.Relu, Relu)

if __name__ == '__main__':
    # test
    input_tensor = torch.arange(-1, 8)  
    output = ACTIVATION_CLASS["Relu"]()(input_tensor)
    print(output) # tensor([0, 0, 1, 2, 3, 4, 5, 6, 7])

    output1 = ACTIVATION_CLASS["Relu6"]()(input_tensor)
    print(output1) # tensor([0, 0, 1, 2, 3, 4, 5, 6, 6])

    output2 = ACTIVATION_CLASS["Threshold"]()(input_tensor)
    print(output2) # tensor([0, 0, 0, 0, 3, 4, 5, 6, 7])