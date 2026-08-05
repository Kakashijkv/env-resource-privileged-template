# Security Policy

Reporting a Vulnerability
If you discover a security vulnerability, please report it privately to the repository maintainers or the organization’s security contact. Do not open a public issue.

Security best practices used here
- Environment secrets (GitHub Environments) are used for credentials required to access privileged resources (production DBs, cloud service accounts).
- Repository secrets should be used for less-sensitive values; use environment secrets for production credentials.
- Least privilege: CI jobs and service accounts used by CI should have only the permissions they need.
- Reviewers and environment approvals: Production deployments require explicit approval by designated reviewers.

Rotation & revocation
- Rotate credentials on regular schedule.
- If a credential compromise is suspected, revoke and rotate immediately, and notify stakeholders.

Contact
Provide maintainer or organization contact information here.