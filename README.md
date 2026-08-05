# env-resource-privileged-template

Purpose
This repository is a template for projects that need to perform deployments or operations which access privileged resources (cloud credentials, production databases, etc.). It demonstrates safe patterns for managing environment-specific secrets and protections using GitHub Environments and GitHub Actions.

Key features
- Protected environments: `staging` and `production` with recommended protection rules.
- CI workflow that gates deploys on environment protection and required approvals.
- Guidance for least-privilege secrets and resource access.
- Example Docker Compose and Terraform files for reference.
- CONTRIBUTING and SECURITY guidance for requesting and approving elevated access.

Quick start
1. Create a new GitHub repository named `env-resource-privileged-template`.
2. Add the files from this template to the repo root (README.md, LICENSE, CONTRIBUTING.md, SECURITY.md, .github/, infra/, docker-compose.yml, app/).
3. On GitHub, create two Environments: `staging` and `production`. Configure required reviewers and add environment secrets following `.github/ENVIRONMENTS.md`.
4. Add necessary repository secrets (e.g., `TF_BACKEND_KEY`, `CLOUD_CRED`), but prefer environment secrets for production-level credentials.
5. Adjust `.github/workflows/ci.yml` to match your cloud provider and deployment steps.

Repository structure
- README.md
- LICENSE
- CONTRIBUTING.md
- SECURITY.md
- .github/
  - workflows/ci.yml
  - ENVIRONMENTS.md
- docker-compose.yml
- infra/example.tf
- app/
  - Dockerfile
  - main.py
  - requirements.txt
- .gitignore

Notes on security
- Use environment secrets for credentials that should only be available during protected deployments.
- Keep minimal permissions in CI (`permissions` block in workflows) and only grant write access when absolutely necessary.
- Require code review and environment approvals for production deployments.

If you want, I can also prepare a single commit patch (git diff/patch) you can apply locally; say so and I’ll produce it next.