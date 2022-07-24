from setuptools import setup
with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name='twitter_bot',
    version='1.1.1',
    description='twitter automation',
    url='https://github.com/isichan0501/twitter_bot',
    author='isichan0501',
    author_email='happymail@info',
    license='MIT',
    keywords='twitter bot api',
    packages=[
        "twitter_bot",
    ],
    install_requires=required,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)