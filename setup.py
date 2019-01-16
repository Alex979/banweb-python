from setuptools import setup

setup(name='banweb',
    version='0.1',
    description='Interface with the banner website to access academic information'
    url='https://github.com/Alex979/banweb-python'
    license='MIT'
    packages=['banweb']
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    zip_safe=False)