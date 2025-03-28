#!/usr/bin/env bash

set -euxo pipefail

if [ "$(id -u)" -ne 0 ]; then
    echo -e 'Script must be run as root. Use sudo, su, or add "USER root" to your Dockerfile before running this script.'
    exit 1
fi

apt-get update
apt-get install --no-install-recommends -y \
    gcc \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    gir1.2-gtk-4.0 \
    libgirepository1.0-dev
    # Ubuntu 24.04 or later
    # libgirepository-2.0-dev
