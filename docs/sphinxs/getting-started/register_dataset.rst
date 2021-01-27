..
    This file is part of bdc-odc
    Copyright 2020 INPE.

    bdc-odc is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Registering Datasets in the ODC Database
==========================================

After the process of downloading and creating the files with the description of the datasets has been completed, they can be inserted into the ``ODC-Core`` metadata database. To add all the data described in the previous step, the following command can be used::

    find ~/products/CB4_64_16D_STK_1/datasets/*.yaml \
         -exec datacube -vvv dataset add -p CB4_64_16D_STK_1 {} \;


If necessary, individual additions can be made using the ``datacube dataset add`` command. For more information, consult the `ODC documentation <https://datacube-core.readthedocs.io/en/latest/>`_.
