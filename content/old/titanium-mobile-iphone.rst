Titanium mobileでiPhoneの電話用のスピーカー(レシーバー)から音を鳴らす
#####################################################################
:date: 2012-02-07 00:49
:author: ka2n
:category: general
:tags: iOS, titanium
:slug: titanium-mobile-iphone

Titanium
mobileで音声ファイルを再生したい時はTi.Media.sound周りなどを使いますが、大きな音が出るスピーカーではなく電話の時に使う小さいスピーカー(本当はレシーバーというそうです)から音を出したいときってありますよね。きっと。探しみたら簡単にできる様なのでここに書いておきます。

.. code-block:: javascript

    var player = Ti.Media.createSound({
     url: 'sound.caf'
     });

    player.play(); // スピーカーから音がなる

    // 現在のオーディオセッションのルートを変える
    Ti.Media.setAudioSessionMode(Ti.Media.AUDIO_SESSION_MODE_PLAY_AND_RECORD);

    player.play(); // レシーバーから音がなる

    // 元のルートに変える

    Ti.Media.setAudioSessionMode(Titanium.Media.AUDIO_SESSION_MODE_PLAYBACK);

    player.play(); // スピーカーから音がなる
