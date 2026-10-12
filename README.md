# Ansible + Docker: Flask Application Behind NGINX

Infrastructure automation lab demonstrating how **Ansible roles**, **Docker Compose**, and **NGINX** can be combined to deploy and reverse-proxy five Flask application containers.

> **Validation status:** Repository code inspected and documented. This documentation does not claim that the deployment has passed a fresh end-to-end run.

## Architecture

```text
Client :80
    |
NGINX load-balancer container
    |
Docker bridge network (app_net)
    +-- app1 (Flask)
    +-- app2 (Flask)
    +-- app3 (Flask)
    +-- app4 (Flask)
    +-- app5 (Flask)
```

## Repository structure

- `docker-compose.yaml`: five application services, one NGINX service, and an isolated Docker bridge network.
- `dockerfiles/app/`: Flask application and its Dockerfile.
- `dockerfiles/nginx/`: NGINX configuration and image definition.
- `ansible/playbook.yaml`: host-group-targeted automation using `flask_app` and `nginx` roles.
- `ansible/inventory/`: inventory file (edit before using in your own environment).
- `ansible/roles/`: role tasks for automation.

## Run locally with Docker Compose

Install a supported Docker Engine and Docker Compose plugin, then run:

```bash
docker compose config
docker compose up --build -d
docker compose ps
curl -i http://localhost/
docker compose logs --tail=100 nginx
docker compose down
```

**Important:** The Compose file binds NGINX to host port 80. Ensure that port is free, and avoid exposing the demonstration deployment to the public Internet.

## Run the Ansible workflow

Inspect role tasks, inventory, SSH connectivity, and host privileges **before execution**. The playbook targets the `nginxlb` inventory group and uses privilege escalation.

```bash
ansible-inventory -i ansible/inventory/hosts.ini --graph
ansible -i ansible/inventory/hosts.ini nginxlb -m ping
ansible-playbook -i ansible/inventory/hosts.ini ansible/playbook.yaml --syntax-check
ansible-playbook -i ansible/inventory/hosts.ini ansible/playbook.yaml --check
# Run only on a lab target you control:
ansible-playbook -i ansible/inventory/hosts.ini ansible/playbook.yaml
```

## What this project demonstrates

**Configuration management:** reusable Ansible roles and inventory scoping.

**Container operations:** multiple independently named application containers connected through a Compose network.

**Traffic routing:** one public-facing NGINX container serving the application tier.

**Operational validation:** configuration inspection, request smoke tests, and targeted container logs.

## Production-readiness gaps

The sample is a lab, not a production-ready web stack. Add health checks, TLS termination, persistent logging, image pinning, resource limits, secret management, CI tests, and controlled deployment/rollback processes. Confirm NGINX upstream configuration and test actual balancing under load before claiming high availability.

## Next improvements

- Idempotence testing with Molecule or a clean lab VM
- GitHub Actions linting and container-build checks
- Monitoring, image vulnerability scanning, and load-test evidence
- Architecture screenshot and sanitized test results

*Portfolio theme: configuration management, containers, Linux operations, reverse proxying and deployment automation.*
