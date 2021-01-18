from setuptools import setup, find_packages

setup(
    name='shop_faunadb',
    version='1.0.0',
    description='Showcase FaunaDB usage with python driver',

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(),

    install_requires=['flask-restx==0.2.0', 'faunadb==4.0.1'],
)
