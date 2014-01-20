composerで'Failed to execute git checkout'
==========================================
:date: 2014-01-20
:author: ka2n
:status: draft


.. code-block:: bash

      - Installing phpunit/phpunit (3.7.x-dev 50880d1)
        Cloning 50880d1f546fec2b55fe6903ee7d5aef3fa70b76

      [RuntimeException]
      Failed to execute git checkout '50880d1f546fec2b55fe6903ee7d5aef3fa70b76' && git reset --hard '50880d1f546fec2b55fe6903ee7d5aef3fa70b76'

      error: You have local changes to 'phpunit'; cannot switch branches.

.. code-block:: bash

    php composer.phar install --prefer-dist
