Ti: ローカルにキャッシュした画像もRetinaで表示する
##################################################
:date: 2011-10-31 19:20
:author: ka2n
:category: general
:tags: titanium
:slug: ti-retina

Titanium mobile
1.7.3の現時点では、ImageViewにhiresプロパティが存在し、iPhone4や4Sなどの高解像度機種においてはこれを有効にしておくことで綺麗に表示することができます。

.. code-block:: javascript

    var image = Ti.UI.createImageView({
        image: 'http://hogehoge/image.jpg' /* 160x160pxのJPG */
        hires: true,
        width: 80,
        height: 80
    });
  

ローカルファイルだと使えない
============================

ただ、1つ落とし穴があって、これがリモートのファイルであれば良いんですが、キャッシュしたローカルファイルだとhiresが効かない。
ローカルファイルは"@2x"の命名規則で高解像度用画像かどうかを判別しているようです。
ローカルのファイルでhiresを使用しても、画像が80x80pxのImageViewにあわせてリサイズされ、160x160pxにスケールアップされる。画像はボケます。
せっかく画像自体が大きのにもったいない。

解決法1
--------

大きいImageViewを作成して、それを2DMatrixで半分の大きさにする。

.. code-block:: javascript

    var image = Ti.UI.createImageView({
        image: './hogehoge/image.jpg' /* ローカルにある160x160pxのJPG */
        width: 80 * 2,
        height: 80 * 2,
        top: -(80*2) /* 描画位置がずれるので修正 */,
        transform: Ti.UI.create2DMatrix().scale(0.5)
    });

一応これで、目的は達成です。ただこれはパフォーマンスが悪かった。

解決法2
-------

.. code-block:: javascript

    var imageWrap = Ti.UI.createView({
        width: 80,
        height: 80
    })
    var image = Ti.UI.createImageView({
        image: './hogehoge/image.jpg' /* ローカルにある160x160pxのJPG */
        top: 0,
        left: 0,
        right: 0,
        bottom: 0
    });
    imageWrap.add(image);

ImageViewには直接サイズを指定せずに、UIViewに内包させます。これでOKですた。

TitaniumのImageViewでリモートURLの画像を永続的にキャッシュする
https://gist.github.com/930962

リモートにある画像をアプリの領域へ保存してくれます。
貧弱な3G回線を考えると、できるだけリモートのものはローカルに置いておきたい。このキャッシュを使ったときに上の表示方法が役立ちました。
