import setuptools


def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(name='qmtask',
                 version='0.1',
                 description='Solution of the QM task',
                 url='http://github.com/pannkotsky/qmtask',
                 author='Valerii Kovalchuk',
                 author_email='kovvalole@gmail.com',
                 license='MIT',
                 packages=['qmtask'],
                 zip_safe=False)
