#!/bin/sh

###
### start.sh
###
### Local development server docker-entrypoint-initdb.d script.
###

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

# Migrate the database.
python manage.py migrate

# Launch the application server.
python manage.py runserver_plus 0.0.0.0:8000
