--------------------------------------------------------------------------------------------------------------------
-- Django���K�pProject
-- ���K�p�Ƃ���testapp������
-- ���ꎩ�̂���u�����`��؂��Ă��̑�App���J���ł���΂Ǝv��
--------------------------------------------------------------------------------------------------------------------

2018/11/06
:�ŏ��ɊJ������clone�����ہApython���̃C���X�g�[���Ɏ��s����ꍇ�AVS�̃\�����[�V�����G�N�X�v���[�����python����env���폜���Ă���python���̃C���X�g�[�����s���Ƃ��܂������B

2018/11/06
:�u�����`�̊O�ł̕ύX�e�X�g

2018/11/06
:�u�����`�e�X�g�Q

2018/11/07
:������ŊǗ��T�C�g���@�\���Ȃ����B�ȉ���python manage.py shell�Ŏ����B
�@>>> from testapp.models import Choice, Question
�@>>> from django.utils import timezone
�@>>> q = Question(question_text="What's new?", pub_date=timezone.now())
�@>>> q.save()
�@select * from testapp_question;
�@>>> q.id
�@>>> c = Choice(question=q, choice_text="test choice", votes=0)
�@>>> c.save()
�@select * from testapp_choice;
�@
�@���ꂪ���܂�������Admin�֘A�̉����̐ݒ肪���������B���܂������Ȃ����DB�֘A�̉��������������B

2018/11/14 
:��F�؃V�X�e���\�z�ւ̓�
�@https://note.nkmk.me/python-opencv-face-detection-haar-cascade/
�@https://qiita.com/fukuit/items/c6be23a301a97ebf60e8
�@�@>Python��openCV�𗘗p���摜���̊�����ʂ�����@

�@https://blog.aidemy.net/entry/2017/12/17/214715
�@�@>openCV�Ƌ@�B�w�K�ŔT�؍�46�̊环�ʃV�X�e���\�z�̘b

