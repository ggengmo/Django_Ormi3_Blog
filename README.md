# Django_Ormi3_Blog
- Cooking Blog
## 목차
1. 목표와 기능
2. 개발 기술 및 환경
3. 프로젝트 구조와 일정
4. UI
5. 기능
6. 개발 이슈
7. 개발하면서 느낀점

## 1. 목표와 기능
### 1.1 목표
- 많은 사용자들이 쉽게 레시피 및 요리 팁을 볼 수 있는 Blog
### 1.2 기능
- 검색기능과 태그를 통해 쉽게 찾고싶은 레시피를 찾을 수 있는 기능
- 댓글로 소통할 수 있는 기능
## 2. 개발 기술 및 환경
### 2.1 개발 기술
#### FE
<div>
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</div>

#### BE
<div>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

### 2.2 개발 환경
<div>
    <img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>

## 3. 프로젝트 구조와 개발 일정
### 3.1 프로젝트 Directory 구조

```
📦Django_Ormi3_Blog
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂blog
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂cookingblog
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂main
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┣ 📂accounts
 ┃ ┃ ┗ 📂profile_img
 ┃ ┗ 📂blog
 ┃ ┃ ┗ 📂images
 ┣ 📂static
 ┃ ┣ 📂assets
 ┃ ┣ 📂css
 ┃ ┃ ┣ 📜form.css
 ┃ ┃ ┣ 📜form2.css
 ┃ ┃ ┣ 📜form3.css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂css2
 ┃ ┃ ┣ 📜style.css
 ┃ ┃ ┗ 📜style.css.map
 ┃ ┣ 📂css3
 ┃ ┃ ┣ 📜mdb.min.css
 ┃ ┃ ┣ 📜mdb.min.css.map
 ┃ ┃ ┣ 📜mdb.rtl.min.css
 ┃ ┃ ┣ 📜mdb.rtl.min.css.map
 ┃ ┃ ┗ 📜style.css
 ┃ ┣ 📂css4
 ┃ ┃ ┣ 📜change_password.css
 ┃ ┃ ┣ 📜profile.css
 ┃ ┃ ┗ 📜profile_update.css
 ┃ ┣ 📂fonts
 ┃ ┃ ┣ 📂material-icon
 ┃ ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┗ 📂fonts
 ┃ ┣ 📂images
 ┃ ┃ ┣ 📜signin-image.jpg
 ┃ ┃ ┗ 📜signup-image.jpg
 ┃ ┣ 📂img
 ┃ ┃ ┗ 📜mdb-favicon.ico
 ┃ ┣ 📂js
 ┃ ┃ ┣ 📜main.js
 ┃ ┃ ┗ 📜scripts.js
 ┃ ┣ 📂js2
 ┃ ┃ ┣ 📜mdb.min.js
 ┃ ┃ ┗ 📜mdb.min.js.map
 ┃ ┣ 📂js3
 ┃ ┃ ┗ 📜profile_update.js
 ┃ ┣ 📂vendor
 ┃ ┃ ┗ 📂jquery
 ┃ ┃ ┃ ┣ 📜jquery-ui.min.js
 ┃ ┃ ┃ ┗ 📜jquery.min.js
 ┃ ┣ 📜index.html
 ┃ ┣ 📜main.html
 ┃ ┣ 📜post.html
 ┃ ┗ 📜sign.html
 ┣ 📂templates
 ┃ ┣ 📂accounts
 ┃ ┃ ┣ 📜change_password.html
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┣ 📜form2.html
 ┃ ┃ ┣ 📜profile.html
 ┃ ┃ ┗ 📜profile_update.html
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📜403.html
 ┃ ┃ ┣ 📜404.html
 ┃ ┃ ┣ 📜comment_confirm_delete.html
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┣ 📜form2.html
 ┃ ┃ ┣ 📜form3.html
 ┃ ┃ ┣ 📜post_confirm_delete.html
 ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┗ 📜post_list.html
 ┃ ┣ 📂main
 ┃ ┃ ┗ 📜index.html
 ┃ ┗ 📜base.html
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┗ 📜README.md
```

### 3.2 프로젝트 URL 구조
|app: accounts |views 함수 이름|html 파일이름   |
|:------------|:------------|:------------|
|'signup/'     |signup        |signup.html   |
|'login/'      |login         |login.html    |
|'logout/'     |logout        |N/A|
|'profile/'    |profile       |profile.html  |
|'change_password/'|change_password|change_password.html|
|'profile_update/'|profile_update|profile_update.html|

|app: blog  |views 함수 이름  |html 파일이름   |
|:-------------|:--------------|:------------|
|''|post_list|post_list.html|
|'<int:pk>/'|post_detail|post_detail.html|
|'write/'|post_write|form.html|
|'<int:pk>/edit/'|post_edit|form2.html|
|'<int:pk>/delete/'|post_delete|post_confirm_delete.html|
|'search/'|post_search|post_search.html|
|'<int:pk>/comment_new/'|comment_new|comment_new.html|
|'<int:post_pk>/comment/<int:pk>/edit'|comment_edit|form3.html|
|'<int:post_pk>/comment/<int:pk>/delete'|comment_delete|comment_confirm_delete.html|

|app: blog|Error|html 파일이름|
|:--------|:------------|:---------|
|404|404(없는 페이지)|404.html|
|403|403(권한 없는 페이지)|403.html|

|app: main |views 함수 이름|html 파일이름|
|:--------|:------------|:---------|
|'/'       |index         |index.html|

### 3.3 개발 일정
<div>
  <img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/74e052d7-0a5c-4aba-b352-0e3372eef7d6" width="100%">
  <img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/b9b4c832-9d98-4f3b-8f78-fa52f90a0731" width="100%">
</div>

### 3.4 기능
<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/0527f45a-9957-4419-b910-016dc38d3079" width="100%">

### 3.5 ERD(Entity-Relationship Diagram)
<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/418cfd17-4ed6-421f-8ed8-a4120ed14022" width="100%">

## 4. UI
|Main||
|-|-|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/b0880df8-6a3d-465e-8846-5f3492707cb2" width="100%">기본 메인|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/8dded94c-7919-41d0-bd60-078b51750884" width="100%">로그인(logout으로 변경) 시 메인|

|Blog||
|-|-|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/90bb13fc-a90d-4ee4-bdbc-2992977af61b" width="100%">기본 글 목록|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/c331dfe0-042f-407a-a616-0c8dab157979" width="100%">로그인 시(navbar변경) 글 목록|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/be0ea8f3-f07a-48e5-8cf8-931561f78fd1" width="100%">타이틀 검색|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/248b837c-2e1f-4976-9097-7a8ad8e5f51d" width="100%">태그 검색, 클릭|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/651267c5-f152-46c3-9a00-1bf8d3bf6f06" width="100%">글 상세|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/f2efd4b5-5cc5-4a17-a93d-2c110c5b2eb3" width="100%">댓글 및 대댓글 작성|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/c6fb7cff-6a88-4e5d-b7e5-74141ac8f50c" width="100%">댓글 없을 시|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/fe9a6834-a3ff-4adb-a4a8-ccabe30ccfd7" width="100%">댓글 수정|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/cc948919-f9fb-4b97-b528-d33e4df1166e" width="100%">댓글 삭제|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/94e1c79f-6f14-41a9-9be0-cd886200c032" width="100%">글 작성|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/2d577962-c091-4d3a-ab36-45ebdcd23cc8" width="100%">글 삭제|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/549b8834-ae0d-43a8-b9ab-1f26404f9c5a" width="100%">글 수정|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/870d79a0-64ea-47d9-be91-aed52637a278" width="100%">수정, 삭제 권환 없을 시|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/54cc337d-a9d3-42aa-8a13-df01c69536f1" width="100%">없는 페이지를 접속할 시|

|Accounts||
|-|-|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/99fe1798-fcaa-483c-8b39-489c52b97b72" width="100%">회원가입|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/6a279613-d55c-4090-88f0-eb7534a1a44f" width="100%">로그인|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/a50b5efa-4918-4beb-9882-96263126ba73" width="100%">프로필|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/661e0dcf-0dd1-44a4-9185-658917e72ede" width="100%">프로필 수정|
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/661e0dcf-0dd1-44a4-9185-658917e72ede" width="100%">비밀번호 변경|

## 5. 기능
### 5.1 Main

### 5.2 Accounts

### 5.3 Blog
