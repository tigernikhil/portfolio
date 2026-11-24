#!/bin/bash
set -euo pipefail

# Preflight environment verification
verify_docker() {
    if ! command -v docker &> /dev/null; then
        echo "Docker is not installed. Please install Docker and try again."
        exit 1
    fi
}

verify_pnpm() {
    if ! command -v pnpm &> /dev/null; then
        echo "pnpm is not installed. Please install pnpm and try again."
        exit 1
    fi
}

verify_node_version() {
    if ! command -v node &> /dev/null; then
        echo "Node.js is not installed. Please install Node.js and try again."
        exit 1
    fi
    node_major=$(node -v | cut -d'.' -f1 | tr -d 'v')
    if [ "$node_major" -lt 20 ]; then
        echo "Node.js version 20+ is required. Current version is $node_version"
        exit 1
    fi
}

verify_smtp_credentials() {
    if [ -z "${SMTP_USER+x}" ] || [ -z "${SMTP_PASSWORD+x}" ]; then
        echo "SMTP credentials are not set. Please set SMTP_USER and SMTP_PASSWORD and try again."
        exit 1
    fi
}

verify_jwt_secret() {
    if [ -z "${JWT_SECRET+x}" ]; then
        echo "JWT_SECRET is not set. Please set JWT_SECRET and try again."
        exit 1
    fi
}

verify_docker
verify_pnpm
verify_node_version
verify_smtp_credentials
verify_jwt_secret

# Monorepo build step
pnpm install
pnpm build
pnpm test

# Health check polling loop
poll_health() {
    local service_name=$1
    local port=$2
    local url="http://localhost:$port/health"
    local max_retries=10
    local retry_count=0
    while [ $retry_count -lt $max_retries ]; do
        if curl -s -o /dev/null -w "%{http_code}" $url | grep -q 200; then
            echo "$service_name is healthy"
            return 0
        else
            echo "$service_name is not healthy, retrying in 5 seconds..."
            sleep 5
            retry_count=$((retry_count + 1))
        fi
    done
    echo "$service_name is not healthy after $max_retries retries"
    return 1
}

poll_health "flight-tracker" 8080
poll_health "cleartax" 5000

# Zero-downtime cutover and automated rollback on failure
# Placeholder for zero-downtime cutover and rollback logic
# This would typically involve deploying to a staging environment first
# and then promoting to production if all checks pass
# Automated rollback logic would involve reverting to the previous version if the deployment fails