![example workflow](https://github.com/thephysicsriot/megafauna/actions/workflows/python-app.yml/badge.svg)

# Megafauna
The backend of an organizational tool for table top games

# Run Megafauna with Docker

`docker build -t megafauna .`

`docker run --rm -p 5000:5000 megafauna`

# Unit tests

Simply run `pytest`

Or for test debugging with pdb `pytest --pdb -s`
