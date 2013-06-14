Firefoxを自家ビルドしようとしてみた -> できなかった
###################################################
:date: 2010-08-29 11:03
:author: ka2n
:category: general
:tags: Firefox
:slug: firefox

Firefox4のbeta4が出たのでいれてみてナカナカ快適だなーとか思ったけど、アドオンの問題とかあってベータ版を使い続けるのは辛い。のでFirefox3に戻してみたんだけど、ちょっと重いのが気になったので、遊びがてら自家ビルドしてみた。

| Firefox 3.x Intel Mac build - KNCN Wiki
| http://wiki.kncn.net/index.php?Firefox%203.x%20Intel%20Mac%20build#vc6383e5

ここを参考にする。

Firefox3.6.8のMac, SnowLeopard, 64bit向けにビルド。

libIDLとGLibを入れます。
finkを使っています。

.. code-block:: console

    $ fink selfupdate
    $ fink update-all

(久しぶりやったらいろいろたまってて時間かかった…orz)

.. code-block:: console

    $ fink install libidl2
    $ fink install glib

んで
http://releases.mozilla.org/pub/mozilla.org/firefox/releases/
からfirefox-3.6.8.source.tar.bz2をダウンロード、展開する。

解凍したディレクトリの/browser/config/mozconfigを編集。

.. code-block:: config

    # This file specifies the build flags for Firefox.?? You can use it by adding:
    # . $topsrcdir/browser/config/mozconfig
    # to the top of your mozconfig file.

    CC="gcc-4.2 -arch x86_64"
    CXX="g++-4.2 -arch x86_64"
    HOST_CC="gcc-4.2"
    HOST_CXX="g++-4.2"
    RANLIB=ranlib
    AR=ar
    AS=$CC
    LD=ld
    STRIP="strip -x -S"
    CROSS_COMPILE=1
    mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox.obj
    mk_add_options MOZ_MAKE_FLAGS="-s -j4"
    ac_add_options --target=x86_64-apple-darwin10.4.0
    ac_add_options --enable-macos-target=10.6
    ac_add_options --with-macos-sdk=/Developer/SDKs/MacOSX10.6.sdk
    ac_add_options --enable-application=browser
    ac_add_options --enable-optimize="-O3 -march=core2 -msse3 -pipe"
    ac_add_options --disable-debug
    ac_add_options --disable-tests
    ac_add_options --disable-mochitest
    ac_add_options --disable-crashreporter
    ac_add_options --enable-extensions=default
    ac_add_options --enable-svg
    ac_add_options --enable-strip
    ac_add_options --enable-libxul
    ac_add_options --enable-static-libs
    ac_add_options --enable-canvas
    ac_add_options --enable-pthreads
    ac_add_options --enable-prebinding
    ac_add_options --enable-update-packaging
    ac_add_options --disable-pedantic
    ac_add_options --disable-libIDLtest
    ac_add_options --disable-glibtest

    # for distribution;
    export BUILD_OFFICIAL=1
    export MOZILLA_OFFICIAL=1
    export MOZ_OFFICIAL_BRANDING=1
    mk_add_options BUILD_OFFICIAL=1
    mk_add_options MOZILLA_OFFICIAL=1
    mk_add_options MOZ_OFFICIAL_BRANDING=1
    ac_add_options --enable-official-branding
    ac_add_options --with-branding=other-licenses/branding/firefox


よく分からないけど、-O3 -marc=core2で最適化してくれるんかな…と。

.. code-block:: console

   $ make -f client.mk build

でビルド。

.. code-block:: console

    configure: error: --enable-application=APP was not specified and is required.

とか怒られちゃったのでググって解決。

mozconfigを解凍したディレクトリのトップにコピーしておけば良いみたい。

.. code-block:: console

   $ cd 解凍したディレクトリ
   $ cp browser/config/mozconfig .

んでもっかいビルドしてみる。

.. code-block:: console

    _method_declaration in host_xpidl_java.o
    _method_declaration in host_xpidl_java.o
    ld: symbol(s) not found
    collect2: ld returned 1 exit status
    make[7]: *** [host_xpidl] Error 1
    make[6]: *** [export] Error 2
    make[5]: *** [export] Error 2
    make[4]: *** [export] Error 2
    make[3]: *** [export_tier_xpcom] Error 2
    make[2]: *** [tier_xpcom] Error 2
    make[1]: *** [default] Error 2
    make: *** [build] Error 2

と出て、エラー。。

ここで時間切れになったので諦めた。
また時間あるときにやってみよう。
