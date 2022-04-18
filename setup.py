from setuptools import setup, find_packages

setup(
    name='ai_art',
    version='0.0.1',
    description='',
    author='Lukas Deutz',
    url='git@github.com:LukasDeutz/ai-art.git',
    packages=find_packages(where='ai_art', include = ['optimizers']),
    # install_requires=[
    #     'numpy==1.19.5',
    #     'matplotlib==3.3.3',
    #     'pandas==1.1.4',
    #     'tensorflow==2.4.1',
    #     'jupyter==1.0.0',
    #     'tqdm==4.54.0',
    #     'scipy==1.6.0',
    #     'scikit-image==0.17.2'
    # ],
)
