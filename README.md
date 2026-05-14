# aidlc-workflows

> Fork of [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows)

A collection of AI-driven development lifecycle (AIDLC) workflows designed to streamline software development processes using AI assistance.

## Overview

This project provides reusable workflow templates and automation scripts for integrating AI capabilities into the software development lifecycle, including code review, testing, documentation generation, and deployment pipelines.

## Features

- 🤖 AI-assisted code review workflows
- 📝 Automated documentation generation
- 🧪 Intelligent test generation and validation
- 🚀 CI/CD pipeline integrations
- 🔒 Security scanning with Bandit and Checkov

## Prerequisites

- Python 3.10+
- AWS CLI configured with appropriate permissions
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/aidlc-workflows.git
cd aidlc-workflows

# Install dependencies using uv
uv sync

# Or using pip
pip install -e .
```

## Usage

```bash
# Run a workflow
python -m aidlc_workflows run --workflow <workflow-name>

# List available workflows
python -m aidlc_workflows list
```

## Project Structure

```
aidlc-workflows/
├── .github/              # GitHub Actions workflows and templates
│   ├── ISSUE_TEMPLATE/   # Issue templates
│   └── CODEOWNERS        # Code ownership definitions
├── src/                  # Source code
│   └── aidlc_workflows/  # Main package
├── tests/                # Test suite
├── docs/                 # Documentation
├── .bandit               # Bandit security scanner config
├── .checkov.yaml         # Checkov IaC scanner config
└── README.md
```

## Security

This project uses:
- **Bandit** for Python security linting
- **Checkov** for infrastructure-as-code security scanning

Run security checks locally:

```bash
# Bandit
bandit -c .bandit -r src/

# Checkov
checkov --config-file .checkov.yaml
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original project: [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows)
- AWS Labs team for the foundational work
