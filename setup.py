from setuptools import setup, find_packages

setup(
    name="context-switcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        'console_scripts': [
            'context-switcher=context_switcher.generate_summary:main',
        ],
    },
    author="Jonathan Wong",
    author_email="hello@jonton.dev",
    description="A tool for generating AI-enhanced git commit summaries",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jonton11/context-switcher-assistant",
    python_requires=">=3.11",
) 