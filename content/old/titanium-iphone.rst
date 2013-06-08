Titanium/iPhone 指定できるフォント
##################################
:date: 2010-12-17 00:16
:author: ka2n
:category: general
:slug: titanium-iphone

| Appcelerator
TitaniumでiPhone(iOS)向けアプリケーションを開発する際、ラベルなどに使用できるフォントの一覧。
|  mobilesdk v1.4.1.1くらいの情報です。

指定方法

| [code]
|  var new\_label = Ti. UI.createLabel({
|  color:"#000",
|  text:"テキスト",
|  font:{ fontWeight: "bold", fontSize: 20, fontFamily: 'Helvetica Neue'
},
|  textAlign:center,
|  width:'auto'
|  });
|  [/code]

フォントによってはfontWeightの指定が効かないものもある。

使用可能なフォント

-  AmericanTypewriter
-  AmericanTypewriter-Bold
-  AppleGothic
-  ArialMT
-  Arial-BoldMT
-  Arial-BoldItalicMT
-  Arial-ItalicMT
-  ArialRoundedMTBold
-  ArialUnicodeMS
-  Courier
-  Courier-BoldOblique
-  Courier-Oblique
-  Courier-Bold
-  CourierNewPS-BoldMT
-  CourierNewPS-ItalicMT
-  CourierNewPS-BoldItalicMT
-  CourierNewPSMT
-  DBLCDTempBlack
-  Georgia-Bold
-  Georgia
-  Georgia-BoldItalic
-  Georgia-Italic
-  Helvetica-Oblique
-  Helvetica-BoldOblique
-  Helvetica
-  Helvetica-Bold
-  HelveticaNeue
-  HelveticaNeue-Bold
-  HiraKakuProN-W3
-  HiraKakuProN-W6
-  MarkerFelt-Thin
-  STHeitiJ-Medium
-  STHeitiJ-Light
-  STHeitiK-Medium
-  STHeitiK-Light
-  STHeitiSC-Medium
-  STHeitiSC-Light
-  STHeitiTC-Light
-  STHeitiTC-Medium
-  TimesNewRomanPSMT
-  TimesNewRomanPS-BoldMT
-  TimesNewRomanPS-BoldItalicMT
-  TimesNewRomanPS-ItalicMT
-  TrebuchetMS-Italic
-  TrebuchetMS
-  Trebuchet-BoldItalic
-  TrebuchetMS-Bold
-  Verdana-Bold
-  Verdana-BoldItalic
-  Verdana
-  Verdana-Italic
-  Zapfino

| 別途フォントファイルを用意すればこのリストに無いものも使用できるみたいです。
| 
http://developer.appcelerator.com/blog/2010/04/adding-custom-fonts-to-ipad.html
