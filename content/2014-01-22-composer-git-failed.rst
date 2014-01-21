composerで'Failed to execute git checkout'が出るときの対処法
==============================================================
:date: 2014-01-22
:author: ka2n
:slug: composer-failed-to-execute-git-checkout-error
:category: dev
:tags: php, composer

composerの依存ライブラリでgitのレポジトリからチェックアウトするものがあったのだけど(phpunit)
たまたまその時上手くチェックアウトできない状態だったため下のようなエラーが出でしまった。

.. code-block:: bash

      - Installing phpunit/phpunit (3.7.x-dev 50880d1)
        Cloning 50880d1f546fec2b55fe6903ee7d5aef3fa70b76

      [RuntimeException]
      Failed to execute git checkout '50880d1f546fec2b55fe6903ee7d5aef3fa70b76' && git reset --hard '50880d1f546fec2b55fe6903ee7d5aef3fa70b76'

      error: You have local changes to 'phpunit'; cannot switch branches.


対処

.. code-block:: bash

    php composer.phar install --prefer-dist


``--prefer-dist`` はソースコードをチェックアウトしてくるのじゃなくて、アーカイブから取得してくれる。githubだったらタグがついてるやつ。
普段からつけた方が良いな。
