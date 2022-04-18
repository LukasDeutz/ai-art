from setuptools import setup

setup(
    name='ai-art',
    version='0.0.1',
    description='',
    author='Lukas Deutz',
    url='git@github.com:LukasDeutz/ai-art.git',
    py_modules=['callback', 'loss_functions', 'normalize', 'reconstruct_content', 'reconstruct_style', 'transfer_style'],
    packages=['optimizers'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
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
