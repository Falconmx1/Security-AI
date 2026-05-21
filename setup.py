from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="security-ai",
    version="0.1.0",
    author="Falconmx1",
    author_email="tu-email@ejemplo.com",
    description="Herramienta de ciberseguridad potenciada por IA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Falconmx1/Security-AI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "pefile>=2023.2.7",
        "colorama>=0.4.6",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "security-ai=security_ai.cli:main",
        ],
    },
)
