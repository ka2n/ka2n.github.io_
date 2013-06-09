Titanium mobileでHTTP通信
#########################
:date: 2011-01-14 10:37
:author: ka2n
:category: general
:tags: iPhone, titanium
:slug: titanium-mobile-http

下書きのまま忘れていましたので、少し古いかもしれませんが公開させていただきます

TitaniumでHTTPClientを使った通信、HTTPリクエストを送ってJSONでレスポンスもらったりしてみる。

https://code.google.com/p/titanium-mobile-doc-ja/wiki/guides_network_httpclient

.. code-block:: javascript

    // オフラインなら処理しないようにしたほうがいいですよね！
    if(Titanium.Network.online == false){
        // エラー表示
        return;
    }

    // オブジェクトを生成します。
    var xhr = Titanium.Network.createHTTPClient();

    // 第一引数はHTTP Method(GETかPOSTがほとんどだと思いますが)
    // 第二引数はURIです。

    xhr.open('GET','http://search.twitter.com/search.json?q=%23titanium');

    // レスポンスを受け取るイベント
    xhr.onload = function(){
    alert(this.responseText);
    /*
    // これと同義
    xhr.onreadystatechange = function(){
        if(this.readyState == xhr.DONE){
            alert(this.responseText);
        }
    };
    */
    };

    // エラー発生時のイベント
    xhr.onerror = function(error){
    // errorにはエラー事由の文字列オブジェクトが入ってくる。
    };

    // リクエスト送信します。(引数としてJSON値を入れるとパラメータ化される)
    xhr.send();
    /*
    xhr.send({
        q : 'querystring',
        param_name : 'param_value'
    });
    */


ええと、この中の、

.. code-block:: javascript

    // リクエスト送信します。(引数としてJSON値を入れるとパラメータ化される)
    xhr.send();

という所。それが当たり前なのかもしれませんが、

.. code-block:: javascript

    xhr.open('GET','http://search.twitter.com/search.json?q=%23titanium');

とGETでリクエストすると指定してあったとしても、

.. code-block:: javascript

    var param = {
    book : '1',
    name:'hoge',
    kind:'hage'
    }
    xhr.send(param);

としてJSONを渡してしまうとリクエストは **勝手** にPOSTになるので注意。

iPhone Simulatorが行っている通信をキャプチャする楽な方法がないものか…今はWireSharkを使っています
