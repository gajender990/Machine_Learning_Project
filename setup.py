from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
## filepath returns a list 
def getrequirements(file_path:str)->List[str] :
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml_project',
    version='0.1.1',
    author='gajender',
    author_email='kunwar.gajender34@gmail.com',
    install_requires = getrequirements('requirements.txt')
)