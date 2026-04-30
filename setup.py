# setup.py - Installation configuration for BitNet
# Fork of microsoft/BitNet with additional features and improvements

from setuptools import setup, find_packages
import os
import sys

# Ensure we're running on a supported Python version
if sys.version_info < (3, 8):
    sys.exit("Python 3.8 or higher is required.")

# Read the README for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Read requirements from requirements.txt if it exists
def read_requirements(filename="requirements.txt"):
    req_path = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(req_path):
        with open(req_path, "r", encoding="utf-8") as f:
            return [
                line.strip()
                for line in f
                if line.strip() and not line.startswith("#")
            ]
    return []

setup(
    name="bitnet",
    version="0.1.0",
    author="BitNet Contributors",
    description="A fork of microsoft/BitNet — efficient 1-bit LLM inference framework",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/BitNet",
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*"]),
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "isort>=5.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
        "cuda": [
            "torch>=2.0.0+cu118",
        ],
        "cpu": [
            "torch>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bitnet-run=bitnet.run_inference:main",
            "bitnet-setup=bitnet.setup_env:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="llm bitnet quantization inference 1-bit transformer",
    include_package_data=True,
    zip_safe=False,
)
