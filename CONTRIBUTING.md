# Contributing

Thank you for contributing. This repository enforces environment protections because deployments may access privileged resources. Please follow these steps when contributing:

1. Branches & PRs
   - Use descriptive branch names: `feature/<short-desc>`, `fix/<short-desc>`, `chore/<short-desc>`.
   - Open a Pull Request targeting the default branch (usually `main` or `master`).
   - Include testing steps and, if relevant, a deployment plan.

2. CI and tests
   - The repository has a CI pipeline (.github/workflows/ci.yml) that runs tests and builds artifacts.
   - Do not modify deployment steps without approval from repository maintainers.

3. Requesting environment access (staging/production)
   - If you need to run protected deployments or access environment secrets, open an issue using the "Environment access request" template (or describe the request in a new issue).
   - Include: reason for access, duration, required resources, and verification steps.
   - Once approved, a maintainer will add you to the required reviewer group or temporarily grant access following least-privilege practices.

4. Security and secrets
   - Never commit secrets or credentials to source control.
   - Use environment secrets or an external secret manager.
   - Follow the procedures in SECURITY.md to report any security issues.

Thank you — follow these guidelines to keep privileged operations safe and auditable.