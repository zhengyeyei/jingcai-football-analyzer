from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="jingcai-football-analyzer",
    version="0.1.0",
    author="zhengyeyei",
    author_email="zhengyeyei@example.com",
    description="一套完整的竞彩足球分析与预测系统",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhengyeyei/jingcai-football-analyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "jingcai-crawler=scripts.run_crawler:main",
            "jingcai-train=scripts.train_model:main",
            "jingcai-predict=scripts.generate_predictions:main",
        ],
    },
)
