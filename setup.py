from setuptools import find_packages, setup
setup(
    name="LibreriaMemoriaFCA",
    version="0.0.1",
    author='Jorge Ariel Díaz Matte',
    author_email='jorge.diazma@sansano.usm.cl',
    packages=find_packages(),
    install_requires=['psutil==5.8.0'],
    py_modules=["LibreriaMemoriaFCA"]
)