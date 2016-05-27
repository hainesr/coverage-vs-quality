# Is Code Quality Related to Test Coverage?

### Jorge Arturo Wong-Mozqueda, Robert Haines and Caroline Jay

*Data and scripts for our Code Coverage vs Code Quality analysis.*

## Usage

These analysis tools can be run via a [Docker][docker] container, which will simplify the process of installing dependencies.

### With Docker

* You will need Docker installed. Please see the [installation instructions for your platform][dockerdocs] to get started.
* Run the `setup` script. This will download the Docker image (if necessary), startup the container and connect the current directory into the container for saving any outputs. When you exit the container it will be automatically cleaned up.
* If you would rather run the Docker container with your own options you can do so in the usual way - see the `setup` script for more details. The image is [available on the Docker Hub][dockerhub].

### Without Docker

* You will need `Python`, `numpy`, `pandas` and `matplotlib` installed.
* Change into the `scripts` directory.
* Run: `python regression_combined.py`

## Licence

Copyright (c) 2015, 2016 The University of Manchester, UK.

BSD licenced. See LICENCE for details.

[docker]: https://www.docker.com/
[dockerdocs]: https://docs.docker.com/
[dockerhub]: https://hub.docker.com/r/hainesr/quality/
