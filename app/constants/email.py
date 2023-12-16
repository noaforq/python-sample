PASSWORD_RESET = {
    "subject": "[TechFUL - パスワード変更受付]",
    "template_name": "password_reset.txt",
}

EMAIL_UPDATE = {
    "subject": "[TechFUL - メールアドレス変更確認]",
    "template_name": "email_update.txt",
}

SUB_EMAIL_UPDATE = {
    "subject": "[TechFUL - サブメールアドレス変更確認]",
    "template_name": "sub_email_update.txt",
}

SIGNUP = {
    "subject": "TechFUL - ユーザー登録",
    "template_name": "signup.txt",
}

INVITATION_SCHOOL_USER = {
    "subject": "TechFUL - 学校アカウント新規登録",
    "template_name": "invitation_school_user.txt",
}

COMPANY_USER_SIGNUP = {
    "subject": "[TechFUL] - 企業アカウント登録",
    "template_name": "company_user_signup.txt",
}

"""
企業からユーザー
"""
CHAT_FROM_COMPANY_TO_USER = {
    "subject": "[TechFUL] - {company_name}から新しいメッセージが届いています。",
    "template_name": "chat/chat_from_company_to_user.txt",
}

"""
ユーザーから企業
"""
CHAT_FROM_USER_TO_COMPANY = {
    "subject": "[TechFUL] - {user_account_name}様から新しいメッセージが届いています。",
    "template_name": "chat/chat_from_user_to_org.txt",
}

"""
学校からユーザー
"""
CHAT_FROM_SCHOOL_TO_USER = {
    "subject": "[TechFUL] - {school_manager_name}様から新しいメッセージが届いています。",
    "template_name": "chat/chat_from_school_to_user.txt",
}

"""
ユーザーから学校
"""
CHAT_FROM_USER_TO_SCHOOL = {
    "subject": "[TechFUL] - {user_account_name}様から新しいメッセージが届いています。",
    "template_name": "chat/chat_from_user_to_org.txt",
}

"""
444（エージェント）からユーザー
"""
CHAT_FROM_AGENT_TO_USER = {
    "subject": "[TechFUL] - TechFULキャリアアドバイザーから新しいメッセージが届いています。",
    "template_name": "chat/chat_from_agent_to_user.txt",
}

"""
ユーザーから444（エージェント）
"""
CHAT_FROM_USER_TO_AGENT = {
    "subject": "[TechFUL] - {user_account_name}様から新しいメッセージが届いています。",
    "template_name": "chat/chat_from_user_to_agent.txt",
}

"""
444（自社求人）からユーザー
"""
CHAT_FROM_444_TO_USER = {
    "subject": "[TechFUL] - 444株式会社から新しいメッセージが届いています。",
    "template_name": "chat/chat_from_444_to_user.txt",
}

"""
ユーザーから444（自社求人）
"""
CHAT_FROM_USER_TO_444 = {
    "subject": "[TechFUL] - {user_account_name}様から新しいメッセージが届いています。",
    "template_name": "chat/chat_from_user_to_444.txt",
}

"""
スカウト通知(スカウトプラン)
"""
SCOUT_NOTICE = {
    "subject": "[TechFUL] - {company_name}からスカウトがきています！。",
    "template_name": "scout/scout_notice.txt",
}

"""
選考ステップ変更（スカウトプラン）スカウト承諾(応募)
"""
SCOUT_ACCEPT = {
    "subject": "[TechFUL] {user_account_name}様が選考ステップを変更しました。",
    "template_name": "scout/scout_accept.txt",
}

"""
選考ステップ変更（スカウトプラン）スカウト辞退
"""
SCOUT_DECLINE = {
    "subject": "[TechFUL] {user_account_name}様が選考ステップを変更しました。",
    "template_name": "scout/scout_decline.txt",
}

"""
求人応募通知（直接採用（＝スカウトプラン））応募しました(ユーザー側)　
"""
SCOUT_JOB_APPLICATION_TO_USER = {
    "subject": "[TechFUL] {company_name}の求人 '{job_title}'に応募しました。",
    "template_name": "scout/scout_job_application_to_user.txt",
}

"""
求人応募通知（直接採用（＝スカウトプラン））スカウトプラン(企業側)
"""
SCOUT_JOB_APPLICATION_TO_COMPANY = {
    "subject": "[TechFUL] {user_account_name}様が求人に応募しました。",
    "template_name": "scout/scout_job_application_to_company.txt",
}

"""
選考ステップ変更（スカウトプラン）企業担当者による変更
"""
SCOUT_SELECTION_STEPS_CHANGED_COMPANY_REPRESENTATIVE = {
    "subject": "[TechFUL] {company_name}の選考ステップが変更されました。",
    "template_name": "scout/scout_selection_steps_changed_company_representative.txt",
}

"""
選考ステップ変更（スカウトプラン）スタッフによる変更
"""
SCOUT_SELECTION_STEPS_CHANGED_COMPANY_STAFF = {
    "subject": "スタッフによりステータスが変更されました。",
    "template_name": "scout/scout_selection_steps_changed_staff.txt",
}

"""
規約同意前エージェントチャット
"""
AGENT_TERMS_BEFORE_ACCEPTANCE = {
    "subject": "[TechFUL] エージェントからメッセージが届きました！",
    "template_name": "agent/agent_terms_before_acceptance.txt",
}

"""
規約同意
"""
AGENT_TERMS_AFTER_ACCEPTANCE = {
    "subject": "[TechFUL] {user_account_name}様が規約を承諾しました。",
    "template_name": "agent/agent_terms_after_acceptance.txt",
}

"""
選考ステップ 人材紹介プラン　444からユーザ
"""
AGENT_RECRUITMENT_444_TO_USER = {
    "subject": "[TechFUL] 444株式会社から{company_name}への求人の紹介があります！",
    "template_name": "agent/agent_recruitment_444_to_user.txt",
}

"""
選考ステップ 人材紹介プラン ユーザーから企業
"""
AGENT_RECRUITMENT_USER_TO_COMPANY = {
    "subject": "[TechFUL] {user_account_name}様に{company_name}様の求人を紹介しました。",
    "template_name": "agent/agent_recruitment_user_to_company.txt",
}

"""
選考ステップ変更 人材紹介プラン スカウト承諾
"""
AGENT_SCOUT_ACCEPT = {
    "subject": "[TechFUL] {user_account_name}様の選考ステップが変更されました。",
    "template_name": "agent/agent_scout_accept.txt",
}

"""
選考ステップ変更 人材紹介プラン スカウト辞退
"""
AGENT_SCOUT_DECLINE = {
    "subject": "[TechFUL] {user_account_name}様の選考ステップが変更されました。",
    "template_name": "agent/agent_scout_decline.txt",
}

"""
求人応募通知 人材紹介求人直接応募 ユーザー
"""
AGENT_JOB_APPLICATION_NOTICE_TO_USER = {
    "subject": "[TechFUL] {company_name}の求人 '{job_title}'に応募しました。",
    "template_name": "agent/agent_job_application_notice_to_user.txt",
}

"""
求人応募通知 人材紹介求人直接応募 444
"""
AGENT_JOB_APPLICATION_NOTICE_TO_444 = {
    "subject": "[TechFUL] {user_account_name}様が{company_name}様の求人に応募しました。",
    "template_name": "agent/agent_job_application_notice_to_444.txt",
}

"""
人材紹介プラン　エージェントによる変更（各ステップ) ユーザー
"""
AGENT_SELECTION_STEPS_CHANGED_TO_USER = {
    "subject": "[TechFUL] {company_name}の選考ステップが変更されました。",
    "template_name": "agent/agent_selection_steps_changed_to_user.txt",
}

"""
人材紹介プラン　エージェントによる変更（各ステップ) 444
"""
AGENT_SELECTION_STEPS_CHANGED_TO_444 = {
    "subject": "[TechFUL] {user_account_name}の選考ステップが変更されました。",
    "template_name": "agent/agent_selection_steps_changed_to_444.txt",
}

"""
人材紹介プラン　エージェントによる変更（各ステップ) スタッフ
"""
AGENT_SELECTION_STEPS_CHANGED_TO_STAFF = {
    "subject": "スタッフによりステータスが変更されました。",
    "template_name": "agent/agent_selection_steps_changed_to_staff.txt",
}


"""
スタッフが問題の公開情報を更新した時の社内通知
"""
UPDATE_QUESTIONS_PUBLISH = {
    "subject": "[TechFUL] 問題の公開情報を更新しました。",
    "template_name": "content/update_questions_publish.txt",
}
