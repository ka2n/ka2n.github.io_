boto 2.9.5でSNSからSQSに送られてきたメッセージが文字化けする問題
################################################################
:date: 2013-06-15 23:41
:author: ka2n
:category: general
:slug: boto_sqs_sns_invalid_message
:tags: python

AWSの `SQS`_ , `SNS`_ を使ったWebサービスをPythonで作っていたのだけど、
SNSからSQSにメッセージを投げた時にメッセージが文字化けしてしまうことがあった。

.. code-block:: plain

    Python 2.7.2 (default, Oct 11 2012, 20:14:37)
    boto 2.9.5

を使用

.. code-block:: python
    
    from boto import sqs
    # 接続
    conn = sqs.connect_to_region('ap-northeast-q', aws_access_key_id='key', aws_secret_access_key='sec')
    # キューを取得
    queue = conn.get_queue('queue_name')
    # メッセージを取得
    messages = queue.get_messages()

    len(messages) # > 1

    message = messages[0]
    message.get_body()
    """
    中身がこんな感じで化ける

    O*^6\x8bb~'\x1a\xb6*'1\xeb,j\x07\x88w\x7f.....
    """
    
通常の方法で送った時は問題無いのだけどSNSから送ると化ける。 
あとコンソールだと普通に読める。
どうやら通常の文字列がbase64で\ **デコード**\ されてしまっているっぽい。

.. code-block:: python

    import base64
    txt ="""
    {
        "Type" : "Notification",
        "MessageId" : "00000000-0000-0000-0000-000000000000",
        "TopicArn" : "arn:aws:sns:ap-northeast-1:12345:name",
        "Subject" : "Notification name",
        "Message" : "",
        "Timestamp" : "2013-06-15T13:30:26.436Z",
        "SignatureVersion" : "1",
        "Signature" : "",
        "SigningCertURL" : "https://cert",
        "UnsubscribeURL" : "https://unsubscribe"
        }
    """

    # デコードする
    base64.b64decode(txt)

    """
    なんか似た感じ!!

    O*^6\x8bb~'\x1a\xb6*'1\xeb,j\x07\x88wM4\xd3M4\xd3M4\xd3M4\xd3M4\xd3M4\xd3M4\xd3M4\xd1:)\x89\xc0+\x9d\xaa\xe7k\x0b,\x9e\xc6\xa9\x9e\x8a\xed\x85\xe6\xac\xb7]v\xdf\x8egjg\x92\xb9\xb8\xder\xd3h\xb6'\xe2q\xabb\xa2y\xda\x99\xe3\x1e\xb2\xc6\xa0y8\xa6z\xcbZ\x9a\x9d\xb4\xd7}:\xd7\x94\xf5\xdf}6\xeb\x8d\xfae(\xa0\x9d\xabn\xad\xe5^\xae\xc8\xa8\x9fT\xa2\x82v\xad\xba\xb7\x92\x8a\t\xe2\x9e\x00\x9e\xae\xd5\x11.\x1bm\xa6\xcf\xffq\xea\xedR{.n\xc7+\x89\xb7\x94D\xb8m\xb6\x9b?\xfe\xe9\xec\xb9\xbb\x1c\xae&\xde
    """

解決するには、無駄にデコードしてくれちゃってるのを止めさせるんだけどとりあえずの解決方法が見つかった。

`Garbled data when subscribing to SNS topic with SQS?`_

.. code-block:: python

    from boto import sqs
    from boto.sqs.message import RawMessage

    conn = sqs.connect_to_region('ap-northeast-q', aws_access_key_id='key', aws_secret_access_key='sec')
    queue = conn.get_queue('queue_name')

    # MessageではなくRawMessageにする
    queue.set_message_class(RawMessage)

    messages = queue.get_messages()
    message = messages[0]
    message.get_body()
    """
    正しい結果が取得できた

    {
        "Type" : "Notification"
        ....
    }
    """

必ず文字化けした状態でデータが送られてくるのならこれで対処できる。


.. _SQS: http://aws.amazon.com/sqs/
.. _SNS: http://aws.amazon.com/sns/
.. _Garbled data when subscribing to SNS topic with SQS?: https://groups.google.com/forum/?fromgroups#!topic/boto-users/Pv5fUc_RdVU
