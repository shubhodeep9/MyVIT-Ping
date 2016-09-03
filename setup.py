from setuptools import setup, find_packages
setup(
    name='MyVIT-Ping',
    version='0.1.0',
    description='A unity app to notify when the server is down.',
    keywords='MyVIT',
    author='Shubhodeep Mukherjee',
    author_email='shubhodeep9@gmail.com',
    url='https://github.com/shubhodeep9/MyVIT-Ping',
    license='Apache License, Version 2.0',
    install_requires=["requests"],
    py_modules=["ping"],
    entry_points={
        'console_scripts': [
            'myvit-ping=ping:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
