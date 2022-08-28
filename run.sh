#!/bin/bash
clear
export FLASK_DEBUG=1
export FLASK_APP=server_app/server.py
flask run
