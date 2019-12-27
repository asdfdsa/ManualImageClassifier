from setuptools import setup

setup(
    entry_points={
        'console_scripts': [
            # main
            'manualLabeler                           = DeepLearningLabeler:main',
        ]
    }
)