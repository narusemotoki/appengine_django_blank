Google App EngineでDjango 1.4を動かすための空プロジェクトです。  
利用しやすいように少し無駄を残しています。

ライセンスはMITライセンスです。Google App Engineなど、サーバ側で利用する分にはライセンス表記の必要もありません。  
自由に使ってください。

app.yamlの
application: appengine-django-blank
この「appengine-django-blank」をGoogle App Engineに登録したアプリケーション名に変更するだけで、デプロイすればGoogle App Engineで動作するようになります。

ローカルで動かす場合は、app.yamlのあるディレクトリで  
    $ dev_appserver.py .  
を実行してください。dev_appserverはGoogle App EngineのSDKに含まれています。  
http://localhost:8888/{message}にアクセスすると、Hello Worldと共にmessageが表示されます。  
messageの部分は任意の文字列に変更してください。


motoki@naru.se  
http://blog.naru.se