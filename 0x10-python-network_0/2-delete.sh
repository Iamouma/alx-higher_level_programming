#!/bin/bash
# This script deletes request to the URL passed as the first argument
curl -sX DELETE "$1"
