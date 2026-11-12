# Verification and release evidence

This is an **Ansible, Docker Compose and NGINX learning lab**. The included GitHub Actions workflow now builds the five Flask services and the NGINX reverse proxy, checks NGINX syntax, and exercises a real HTTP request through the proxy.

## Acceptance checks

1. `docker compose config -q` validates the service specification.
2. `docker compose build` produces the images from the repository Dockerfiles.
3. `docker compose up -d --no-build` starts the six services.
4. `docker compose exec -T nginx nginx -t` validates the running proxy configuration.
5. `curl -fsS http://127.0.0.1/` confirms the proxy returns the Flask page identifying the serving container.
6. Job cleanup collects bounded logs and tears down the containers even on failure.

The CI test **does not** establish production readiness, five-node HA, TLS, durable logging, or even distribution of requests under load. Those require separate load tests and failure-injection evidence.

## Evidence to capture after a passing run

- GitHub Actions run URL and commit SHA
- `docker compose ps` with services healthy/running
- A sanitized browser or CLI view of the Flask page
- Request-distribution test over 100+ requests showing distinct upstream hosts
- One failed-app scenario and request behavior under failure
- A screenshot of the architecture diagram and the relevant source tree

Redact any public IP addresses, authorization headers, SSH keys, account identifiers and private logs. Never commit `.env`, real credentials, or internal client configurations.