"""
@Auth: David Gao
@File: make_pipeline_container.py
@Editor: LazyVim
@Email: 582435572@qq.com
"""

from kfp.components import func_to_container_op  # this will put this function running in certain container 
from typing import NamedTuple
from collections import namedtuple 

# define your pipeline step functions
def add_operation(a:int, b:int) -> NamedTuple('result_tuple', [('add_result', int)]):
    result_tuple = namedtuple(typename='data_result', field_names=['add_result'])
    
    return result_tuple(a+b)

# set image which function need to use
image_use =  'python3.8'

# create pipeline operation
add_op = func_to_container_op(add_operation, base_image=image_use)

# create pipeline
@dsl.pipeline(
    name='test pipeline',
    description='test kubeflow pipeline'
)
def model_pipeline_main(i: int, j: int):
    add_op_result = add_op(i, j)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        model_pipeline_main,
        package_path=''  # yaml saved location
    )

