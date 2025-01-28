from setuptools import find_packages,setup
from typing import List
HIPPEN_DOT_E='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of all requirements
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        if HIPPEN_DOT_E in requirments:
            requirments.remove(HIPPEN_DOT_E)    
    return requirments

setup(
    name='mlproject',
    version='0.0.1',
    author="Vivek",
    author_email='22h51a7314@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)