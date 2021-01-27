..
    This file is part of bdc-odc
    Copyright 2020 INPE.

    bdc-odc is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Configuring the ODC-Core
=========================

The link that has been made between the ``ODC-Core`` and ``PostgreSQL`` containers is not enough for the correct functioning of the ``ODC-Core``. It will be necessary to create the database schema with the ODC model. To do this, we will use the command line program called ``datacube-cli``, available in the ``ODC-Core`` container::

    docker exec -it bdc-odc-core datacube system init


To check if the above command has created the tables of the ODC schema, use the following command::

    docker exec -it bdc-odc-pg psql -U opendatacube -d opendatacube -c "\dt agdc.*"


The following tables should be presented as a result::

                   List of relations
     Schema |       Name       | Type  |   Owner
    --------+------------------+-------+------------
     agdc   | dataset          | table | agdc_admin
     agdc   | dataset_location | table | agdc_admin
     agdc   | dataset_source   | table | agdc_admin
     agdc   | dataset_type     | table | agdc_admin
     agdc   | metadata_type    | table | agdc_admin
    (5 rows)


.. note::

    Another way to check if everything is right is to list the products registered in the system. No returns will be displayed as no data has been entered, but no errors should be shown either::

        docker exec -it bdc-odc-core datacube product list
