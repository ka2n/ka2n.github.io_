iOS7がWebspeech Synthesis APIをサポートしたので試す
################################################################
:date: 2013-09-20 07:50
:author: ka2n
:category: general
:slug: ios7_webspeech_test
:tags: iOS, HTML

iOS7のSafariからWebspeech APIのSynthesis API(text to speech)をサポートしたようなので試してみる.

.. code-block:: javascript

   var s = new SpeechSynthesisUtterance("Hello");
   speech.rate = 1;             // スピード
   speech.volume = 1;           // 音量
   speech.pitch = 1;            // ピッチ
   speech.text = 'Helloooo';    // 内容
   speech.lang = 'ja-JP';       // 言語

   speechSynthesis.speak(s);

SpeechSynthesisUtteranceのlangが空だった場合は端末の言語に合せてくれる模様。

テストページを作りました。
`iOS7 webspeech test(iOS7で見て下さい) <files/ios7_webspeech_test.html>`_

注意が必要なのは、ボタンを押すなどのユーザーによる操作の後にしか動作しない点
なかなか面白いAPIですね。口を動かすのが面倒な時に使ってみてはいかがでしょうか。
