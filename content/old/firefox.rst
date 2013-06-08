Firefoxを自家ビルドしようとしてみた
###################################
:date: 2010-08-29 11:03
:author: ka2n
:category: general
:tags: Firefox
:slug: firefox

| Firefox4のbeta4が出たのでいれてみてナカナカ快適だなーとか思ったけど、アドオンの問題とかあってベータ版を使い続けるのは辛い。のでFirefox3に戻してみたんだけど、ちょっと重いのが気になったので、遊びがてら自家ビルドしてみた。
|  Firefox 3.x Intel Mac build - KNCN Wiki
| 
http://wiki.kncn.net/index.php?Firefox%203.x%20Intel%20Mac%20build#vc6383e5

ここを参考にする。

Firefox3.6.8のMac, SnowLeopard, 64bit向けにビルド。

| libIDLとGLibを入れます。
|  finkを使っています。

| [code]
|  # fink selfupdate
|  # fink update-all
|  (久しぶりやったらいろいろたまってて時間かかった…orz)

# fink install libidl2

# fink install glib

[/code]

| んで
|  http://releases.mozilla.org/pub/mozilla.org/firefox/releases/
|  からfirefox-3.6.8.source.tar.bz2をダウンロード、解凍。

解凍したディレクトリ/browser/config/mozconfigを編集。

| [code]
|  # This file specifies the build flags for Firefox.?? You can use it
by adding:
|  #?? . $topsrcdir/browser/config/mozconfig
|  # to the top of your mozconfig file.

| CC="gcc-4.2 -arch x86\_64"
|  CXX="g++-4.2 -arch x86\_64"
|  HOST\_CC="gcc-4.2"
|  HOST\_CXX="g++-4.2"
|  RANLIB=ranlib
|  AR=ar
|  AS=$CC
|  LD=ld
|  STRIP="strip -x -S"
|  CROSS\_COMPILE=1
|  mk\_add\_options MOZ\_OBJDIR=@TOPSRCDIR@/firefox.obj
|  mk\_add\_options MOZ\_MAKE\_FLAGS="-s -j4"
|  ac\_add\_options --target=x86\_64-apple-darwin10.4.0
|  ac\_add\_options --enable-macos-target=10.6
|  ac\_add\_options --with-macos-sdk=/Developer/SDKs/MacOSX10.6.sdk
|  ac\_add\_options --enable-application=browser
|  ac\_add\_options --enable-optimize="-O3 -march=core2 -msse3 -pipe"
|  ac\_add\_options --disable-debug
|  ac\_add\_options --disable-tests
|  ac\_add\_options --disable-mochitest
|  ac\_add\_options --disable-crashreporter
|  ac\_add\_options --enable-extensions=default
|  ac\_add\_options --enable-svg
|  ac\_add\_options --enable-strip
|  ac\_add\_options --enable-libxul
|  ac\_add\_options --enable-static-libs
|  ac\_add\_options --enable-canvas
|  ac\_add\_options --enable-pthreads
|  ac\_add\_options --enable-prebinding
|  ac\_add\_options --enable-update-packaging
|  ac\_add\_options --disable-pedantic
|  ac\_add\_options --disable-libIDLtest
|  ac\_add\_options --disable-glibtest

| # for distribution;
|  export BUILD\_OFFICIAL=1
|  export MOZILLA\_OFFICIAL=1
|  export MOZ\_OFFICIAL\_BRANDING=1
|  mk\_add\_options BUILD\_OFFICIAL=1
|  mk\_add\_options MOZILLA\_OFFICIAL=1
|  mk\_add\_options MOZ\_OFFICIAL\_BRANDING=1
|  ac\_add\_options --enable-official-branding
|  ac\_add\_options --with-branding=other-licenses/branding/firefox
|  [/code]

よく分からないけど、-O3 -marc=core2で最適化してくれるんかな…と。

| [code]
|  # make -f client.mk build
|  [/code]

でビルド。

| したら
|  [code]
|  configure: error: --enable-application=APP was not specified and is
required.
|  [/code]

とか怒られちゃったのでググって解決。

| mozconfigを解凍したディレクトリのトップにコピーしておけば良いみたい。
|  [code]
|  # cd 解凍したディレクトリ
|  # copy browser/config/mozconfig .
|  [/code]

んでもっかいビルドしてみる。

| [code]
|  \_method\_declaration in host\_xpidl\_java.o
|  \_method\_declaration in host\_xpidl\_java.o
|  ld: symbol(s) not found
|  collect2: ld returned 1 exit status
|  make[7]: \*\*\* [host\_xpidl] Error 1
|  make[6]: \*\*\* [export] Error 2
|  make[5]: \*\*\* [export] Error 2
|  make[4]: \*\*\* [export] Error 2
|  make[3]: \*\*\* [export\_tier\_xpcom] Error 2
|  make[2]: \*\*\* [tier\_xpcom] Error 2
|  make[1]: \*\*\* [default] Error 2
|  make: \*\*\* [build] Error 2
|  [/code]

と出て、エラー。。

| ここで時間切れになったので諦めた。
|  また時間あるときにやってみよう。
