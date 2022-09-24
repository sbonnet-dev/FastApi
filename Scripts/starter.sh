#!/bin/sh

echo "################################################"
echo "################### API Server #################"
echo "################################################"
echo ""
echo "  * Setting environments variables"

# Loading environments variables
export $(grep -v '^#' "./Environments/dev.env" | xargs)

echo "     ENV: $ENV"
echo "     APISERVICE_PORT: $APISERVICE_PORT"

echo ""
echo "  * Starting server"
cd ./Bin && uvicorn api:app --reload --host 0.0.0.0 --port $APISERVICE_PORT --app-dir ${PWD}