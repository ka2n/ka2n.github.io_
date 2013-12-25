datetime.datetimeをYYYY-MM-DDTHH:MM:SS文字列にする
==================================================
:date: 2013-12-25 13:15
:author: ka2n

何も考えないで作ると、高精度のdatetime.datetimeオブジェクトになっている
余計な情報を削りたかった

.. code-block:: python
    
    import datetime
    now = datetime.datetime.now()
    print(now.isoforat())
    # => '2013-12-25T13:06:27.574037'
    # YYYY-MM-DDTHH:MM:SS.mmmmmm の形式になっている
    # マイクロ秒が余分

.. code-block:: python

    import datetime
    now = datetime.datetime.now().replace(microsecond=0, tzinfo=None)
    # マイクロ秒に0を指定する。ついでにタイムゾーンも無しにする
    print(now.isoforat())
    # => 2013-12-25T13:06:27

Pythonのdatetimeオブジェクトはタイムゾーンとか考える事が多くて苦手意識持ってたんだけど、
他の言語でもそれなりに面倒なので諦めた。
