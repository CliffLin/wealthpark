export GITROOT=$(git rev-parse --show-toplevel)
PYTHON=python3

setup_environment() {
    . "$GITROOT/.env/bin/activate"
    export PYTHONPATH="$GITROOT:$PYTHONPARK"

    if [ ! -e "$GITROOT/runtime" ]; then
        mkdir "$GITROOT/runtime"
    fi
}
if [ ! -e "$GITROOT/.env" ]; then
    if "$PYTHON" -m venv "$GITROOT/.env"; then
        . "$GITROOT/.env/bin/activate"
    else
        echo "Unable to create python3 env" 1>&2
        false
    fi
else
    setup_environment
fi
