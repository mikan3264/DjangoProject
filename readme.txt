--------------------------------------------------------------------------------------------------------------------
-- Django練習用Project
-- 練習用としてtestappを内包する
-- これ自体からブランチを切ってその他Appを開発できればと思う
--------------------------------------------------------------------------------------------------------------------

2018/11/06
:最初に開発環境をcloneした際、python環境のインストールに失敗する場合、VSのソリューションエクスプローラ上でpython環境のenvを削除してからpython環境のインストールを行うとうまくいく。

2018/11/06
:ブランチの外での変更テスト

2018/11/06
:ブランチテスト２

2018/11/07
:自宅環境で管理サイトが機能しない問題。以下をpython manage.py shellで試す。
　>>> from testapp.models import Choice, Question
　>>> from django.utils import timezone
　>>> q = Question(question_text="What's new?", pub_date=timezone.now())
　>>> q.save()
　select * from testapp_question;
　>>> q.id
　>>> c = Choice(question=q, choice_text="test choice", votes=0)
　>>> c.save()
　select * from testapp_choice;
　
　これがうまくいけばAdmin関連の何かの設定がおかしい。うまくいかなければDB関連の何かがおかしい。

2018/11/14 
:顔認証システム構築への道
　https://note.nkmk.me/python-opencv-face-detection-haar-cascade/
　https://qiita.com/fukuit/items/c6be23a301a97ebf60e8
　　>PythonでopenCVを利用し画像内の顔を識別する方法

　https://blog.aidemy.net/entry/2017/12/17/214715
　　>openCVと機械学習で乃木坂46の顔識別システム構築の話

