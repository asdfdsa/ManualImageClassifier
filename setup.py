from setuptools import setup

setup(
	name="manualLabeler",
    version="0.0.1",
    description="Manual image classifier for purposes such as deep learning",

    author="Bin Wang",
    author_email="alexwang911217@gmail.com",
    url="https://https://github.com/asdfdsa/ManualImageClassifier",

    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],

    install_requires=["numpy", "matplotlib"],

    entry_points={
        'console_scripts': [
            # main
            'manualLabeler                           = DeepLearningLabeler:main',
        ]
    }
)