..
    This file is part of bdc-odc
    Copyright 2020 INPE.

    bdc-odc is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Creating Docker Images for the ODC Environment
========================================================


This subsection presents the steps necessary for the preparation of the basic ODC environment. This process will be performed with the `Docker <https://docs.docker.com/get-docker/>`_.


.. note::

    The following commands have been tested on Linux. If you are using Microsoft Windows, be aware of possible changes in the form of the command.

The first step is to acquire the codes that will be used. Do this using  ``git clone`` command in the Brazil data Cube `bdc-odc <https://github.com/brazil-data-cube/bdc-odc>`_. The complete command is shown below::

    git clone https://github.com/brazil-data-cube/bdc-odc.git


After the download, access the directory that was created::

    cd bdc-odc


Inside the directory, run the ``build-docker.sh`` script, which will generate the ``ODC-Core`` images and also the ``Jupyter-Notebook``::

    ./build-docker.sh

After the end of the above command, two new images should be available in your Docker environment. To check these images, use the command ``docker images``, as shown below::

    docker images


This command should list two new images, as shown below::

    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    local/odc-jupyter   1.7                 684c49022dd4        About an hour ago   1.93GB
    local/odc           1.7                 72408270a63b        About an hour ago   1.63GB