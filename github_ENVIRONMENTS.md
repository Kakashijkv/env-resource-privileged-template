# GitHub Environments — recommended configuration

This file explains how to configure the `staging` and `production` environments in the GitHub repository settings to safely protect access to privileged resources.

1. Create environments
   - Settings -> Environments -> New environment
   - Create `staging` and `production`

2. Protection rules (recommended)
   - Required reviewers: add one or more team members who must approve deployments.
   - Wait timer: optionally set a deployment branch restriction or wait timer (e.g., 5 min) for production to give time for last-minute cancellations.
   - Deployment branches: restrict which branches can deploy to the environment (e.g., `main` -> production, `develop` or feature branches -> staging).

3. Secrets
   - Use environment secrets for credentials that should only be available during deployments to that environment (e.g., `PROD_CLOUD_SERVICE_ACCOUNT`).
   - Do NOT store long-lived credentials in repository secrets if they should only be used during protected deploys.

4. Least privilege & ephemeral credentials
   - Prefer short-lived or OIDC-provisioned credentials.
   - Configure your cloud IAM so CI service accounts only have the required roles (e.g., deploy role, not full admin).

5. Reviewer workflows
   - Use issues or the built-in environment reviewer approval to document why the deploy is needed.
   - Keep an audit log of approvals and the associated deployment runs.

6. Example mapping
   - `main` branch -> `production` environment (requires 2 reviewers)
   - `develop` branch -> `staging` environment (requires 1 reviewer)

7. Emergency access
   - Define a documented process (issue + approval) for emergency deploys that includes temporary elevations and rotation of credentials afterward.

Links
- GitHub Environments docs: https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment