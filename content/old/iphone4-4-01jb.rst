iPhone4 4.01JBでテザリング有効化
################################
:date: 2010-08-05 23:10
:author: ka2n
:category: general
:tags: iPhone, iPhone4, JailBreak
:slug: iphone4-4-01jb

メモ

WiMaxあるし、マクドナルドやスタバでネットつながるのでそんなに必要でもないけど、緊急時に便利なので。

#. CommCenterによる.mobileconfigの署名チェックを回避するパッチをインストール

   Cydia > More Package Sources > iPhone-Notes.de
   又は
   Search > iPhone-Notes.deと入力 > iPhone-Notes.de
   でレポジトリを追加。

#. 追加したレポジトリからasCommCenterPatchをインストールする。

   これで自由にmobileconfigを入れられます。
   一応リブートしとく。

#. mobileconfigをインストール

   BenMのやつをtype-mask: 55にしたもの。
   jp\_softbank\_iphonepacket\_usims.mobileconfig

   .. code-block:: xml

       <?xml version="1.0" encoding="UTF-8"?>
       <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
       "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
       <plist version="1.0">
           <dict>
               <key>PayloadContent</key>
               <array>
                   <dict>
                       <key>PayloadContent</key>
                       <array>
                           <dict>
                               <key>DefaultsData</key>
                               <dict>
                                   <key>apns</key>
                                   <array>
                                       <dict>
                                           <key>apn</key>
                                           <string>smile.world</string>
                                           <key>password</key>
                                           <string>so2t3k3m2a</string>
                                           <key>type-mask</key>
                                           <integer>55</integer>
                                           <key>username</key>
                                           <string>dna1trop</string>
                                       </dict>
                                   </array>
                               </dict>
                               <key>DefaultsDomainName</key>
                               <string>com.apple.managedCarrier</string>
                           </dict>
                       </array>
                       <key>PayloadDescription</key>
                       <string>Provides customization of carrier Access Point Name.</string>
                       <key>PayloadDisplayName</key>
                       <string>Advanced Settings</string>
                       <key>PayloadIdentifier</key>
                       <string>jp.softbankusims.profile.apn</string>
                       <key>PayloadOrganization</key>
                       <string>Softbank iPhone Packet Flat usim Japan</string>
                       <key>PayloadType</key>
                       <string>com.apple.apn.managed</string>
                       <key>PayloadUUID</key>
                       <string>AA4E4364-57EA-4EFE-91EA-D33EEBD81446</string>
                       <key>PayloadVersion</key>
                       <integer>1</integer>
                   </dict>
               </array>
               <key>PayloadDescription</key>
               <string>Softbank iPhone Packet Flat usim Japan - BenM.at</string>
               <key>PayloadDisplayName</key>
               <string>JP Softbank iPhone Packet Flat usim</string>
               <key>PayloadIdentifier</key>
               <string>jp.softbankusims.profile</string>
               <key>PayloadOrganization</key>
               <string>Softbank iPhone Packet Flat usim Japan</string>
               <key>PayloadType</key>
               <string>Configuration</string>
               <key>PayloadUUID</key>
               <string>A882C0D6-1D18-42EC-9013-3F466A0A4291</string>
               <key>PayloadVersion</key>
               <integer>1</integer>
           </dict>
       </plist>



#. /var/Managed Preferences/mobile/com.apple.managedCarrier.plist

   apnやpasswordと並列の場所に以下を追記する。自分はiFileを使いました。

   .. code-block:: xml

       <key>type-mask</key>
       <integer>55</integer>

#. /var/mobile/Library/Preferences/com.apple.MobileInternetSharing.plist

   .. code-block:: xml

       <key>State</key>
       <integer>1022</integer>

   となっていることを確認。なっていなければ編集して1022にする。

#. /System/Library/Carrier Bundles/Softbank\_jp.bundle/carrier.plist
    type-mask を 7 から 55 に変更
    これはやらなくてもできましたが、念のため
#. リセット > ネットワークの設定をリセット

**at your own riskで！**

|image0|

.. |image0| image:: http://ktmtt.com/diary/wp-content/uploads/1000000789.png
   :target: http://ktmtt.com/diary/wp-content/uploads/1000000789.png
