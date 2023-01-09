# bookRecord

購入したい本や読んだ本の感想などをリスト化し、記録するアプリを制作した。
簡単なブックリストならフレームワークに備わっている技術をそのまま利用すればよい。本作はそれに加えて「WEBAPIを用いて本の表紙を表示する」、「スクレイピング技術を用いて古本の価格を表示する」機能を持っているアプリを制作した。

1.本の表紙を表示する
　bookRecordProject/bookRecordApp/image_search/image_search.pyをview.pyでインポートして使う。
　書籍の表紙をデータベースに登録されているタイトルを元にAPIを通じて自動で取得できるように設計。まず、GoogleBooksAPIでタイトルからisbn番号（書籍の識別番号）を取得し、OpenBDAPIを用いてisbn番号から表紙のURLを取得できるよう設計した。
 
 2.古本の価格を表示する
　bookRecordProject/bookRecordApp/price_searchディレクトリにある二つのファイル(bookoff_price,valuebooks_price)にスクレイピングするプログラムが書かれている。 views.pyでこれらをインポートして利用する。
  古本サイトであるValueBooksとBookOFFをスクレイピングし、価格を表示するウェブサイト。 タイトル、著者、出版社などを入力すると、自動でスクレイピングし二つのサイトから情報を抜き取って表示させる。

利用技術：　
　言語：Python3　フレームワーク：Django　データベース：SQLite3　API：OpenBD、GoogleBooksAPI　その他：Selenium
 
 
