from setuptools import setup, find_packages

setup(
    name="security-ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "pefile>=2023.2.7",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "security-ai=security_ai.cli:main",
        ],
    },
    author="Falconmx1",
    description="Herramienta de ciberseguridad potenciada por IA",
    license="GPL-3.0",
)
