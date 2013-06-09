Webkit/iPhoneで検索用のキーボードを出す
#######################################
:date: 2010-10-23 04:23
:author: ka2n
:category: general
:tags: iOS, iPhone, Webkit
:slug: webkit-iphone

iPhoneのSafari(webkit)用にウェブページを作る際のtips.

input要素にtype="search"だけ付与しても検索用のキーボードがでない。

.. code-block:: html

    <form>
        <input type="search" placeholder="けんさく" />
    </form>

ちゃんとformタグで囲うと「改行」ではなく「検索」となります。

|image0|

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/iphonesearchkeybord.png
   :target: http://ktmtt.com/diary/wp-content/uploads/iphonesearchkeybord.png
