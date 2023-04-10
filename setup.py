from setuptools import setup, find_packages

from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:     #it is implying that which type of file is input and which type of file it will return
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]  #replacing the extra line and space of the requirements.txt file

        # -e . will be ignored 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="RegressionProject",
    version="0.0.1",
    author="Arunavo",
    author_email="arunavobasu.ds@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
    
    )