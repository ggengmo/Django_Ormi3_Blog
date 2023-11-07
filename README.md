# Django_Ormi3_Blog
- Cooking Blog
## 목차
[1. 목표와 기능](#1-목표와-기능)
[2. 개발 기술 및 환경](#2-개발-기술-및-환경)
[3. 프로젝트 구조와 일정](#3-프로젝트-구조와-일정)
[4. UI](#4-UI)
[5. 기능](#5-기능)
[6. 개발 이슈](#6-개발-이슈)
[7. 개발하면서 느낀점](#7-개발하면서-느낀점)

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
|<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/8a552aee-624d-4812-9ec6-eb8c4c52ec60" width="100%">비밀번호 변경|

## 5. 기능
### 5.1 Main
<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/7b01080a-e24f-435e-a47d-5f248f81ba9c" width="100%"><br>
- 메인페이지에서 블로그 이동, 회원가입, 로그인을 구현하였고 로그인을 하면 로그아웃 버튼이 생깁니다.

### 5.2 Accounts
<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/b3762c5a-4af5-4cd2-8526-f68ade3a6f55" width="100%"><br>
- 회원가입과 로그인 기능입니다.

<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/4f314fc5-0cd0-4cef-b9df-10a21d1d2452" width="100%"><br>
- 로그인 한 사용자의 프로필을 수정할 수 있습니다.

<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/18d6039b-df6e-48d3-9a99-818443fefd0d" width="100%"><br>
-사용자의 프로필 페이지에서 비밀번호 변경을 할 수 있습니다.

### 5.3 Blog
<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/aaf1334d-4a13-4e0a-8e35-4cc08913e001" width="100%"><br>
- 로그인을 하지 않은 사용자면 글작성을 누를 시 로그인페이지로 이동 후 글작성을 할 수 있습니다.

<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/366672ee-7ae2-40a7-b322-900ecfb2e666" width="100%"><br>
- 글 상세 페이지에서 수정하기를 하려면 로그인을 해야 하고 작성한 작성자가 아니라면 오류페이지가 나옵니다.

- 오류페이지는 밑에 있습니다.

<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/ec552d69-f69c-4a88-9767-6b091e1e0059" width="100%"><br>
- 글 상세 페이지에서 삭제하기를 하려면 로그인을 해야 하고 작성한 작성자가 아니라면 오류페이지가 나옵니다.

<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/33d1843b-9046-4221-96bc-650fd14e9674" width="100%"><br>
- 삭제되거나 없는 페이지의 접속하려고 할 때 404 오류와 수정 및 삭제 시 권한이 없을 때 403 오류가 나옵니다.

<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/4630c37c-8f61-4ad5-9527-cba77be209d3" width="100%"><br>
- 글의 조회수가 나옵니다.

<img src="https://github.com/ggengmo/Django_Ormi3_Blog/assets/142369113/f0aeb729-dc99-42a6-bb77-0b6223119665" width="100%"><br>
- 댓글을 작성할 수 있고 댓글 옆에 대댓글 아이콘을 누르면 대댓글을 입력할 수 있는 폼이 나옵니다.
## 6. 개발 이슈
### 6.1 글을 조회 할 때 조회수가 1이 늘어야하는데 2로 올라가는 현상이 발생했습니다.

```python
def get(self, request, *args, **kwargs):
    try:
        self.object = self.get_object()
    except Http404:
        return render(request, 'blog/404.html', status=404)
    return super().get(request, *args, **kwargs)
```

기존 코드에서 ```self.object = self.get_object()``` 한번 올라간 후 ```return super().get(request, *args, **kwargs)``` 여기서 한 번 더 올라가는 걸 알게 되어서 해당 코드를

```python
def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    if self.object is None:
        return render(request, 'blog/404.html', status=404)
    context = self.get_context_data(object=self.object)
    return self.render_to_response(context)
```

수정 후 조회수가 1씩 올라가게 수정했습니다.
### 6.2 댓글작성 오류

```python
def post(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.author = request.user
        comment.save()
        return redirect('blog:post_detail', pk=self.get_object().pk)
    else:
        return self.get(request, *args, **kwargs)

```

기존 코드에서 댓글 작성 시 PostDetailView에서 ```object```가 없는데 호출해서 오류가 생겨 

```python
def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = request.user
        comment.save()
        return redirect('blog:post_detail', pk=self.object.pk)
    else:
        return self.get(request, *args, **kwargs)

```

```object```를 먼저 설정하고 ```get_object()```를 호출하도록 수정했습니다.

### 6.3 user의 프로필이 안 만들어지는 현상
User의 인스턴스가 생성되면 Profile의 인스턴스가 생성이 안 되는 오류가 생겨 시그널을 사용해서 User의 인스턴스가 생성될 때 연결된 Profile 인스턴스가 자동으로 생성되게 했습니다.

```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    Profile.objects.get_or_create(user=instance)
```

그리고 User의 인스턴스가 수정될 때마다 Profile 인스턴스도 같이 수정되도록 해당 코드를 추가했습니다.

```python
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```

## 7. 개발하면서 느낀점
- 처음 프로젝트의 구조를 기획하면서부터 간단한 블로그라도 생각보다 개발할 것이 많다는 생각이 들기도 하였지만 일단은 요구사항부터 개발 후 생각했던 것을 개발하려고 했습니다. 하지만 초반에 어쩌다 보니 DB가 꼬여 전부 지우고 다시 시작하는 바람에 급하게 개발을 하면서 시간을 쓰기도 하고 UI부터 추가하고 싶은 기능을 추가하다 보니 시간이 촉박했습니다. 그러다 보니 기능은 다 구현을 하였지만 아쉬운 마음이 크기도 하고 좀 더 신경을 썼다면 여유로웠을 거 같다는 생각이 들기도 하지만 이러한 경험으로 마감기한이 정해진 프로젝트를 진행하면서 제가 추가로 개발하고 싶은 것을 개발하는 건 물론 좋지만 마감 기한 안에 개발할 수 있게 파악을 하여 기획을 하는 것이 좀 더 좋은 기획이라는 것을 느꼈습니다.
 
- Django를 배우면서 처음으로 해본 프로젝트이기도 하고 모르는 것들이 많아 찾아보기도 하고 공부를 하면서 하였는데 그러다 보니 많은 사람들의 코드를 보았는데 그러면서 느낀 점이 정말 기본기가 탄탄하고 얼마나 잘 숙지하냐가 정말 중요하단 것을 느꼈습니다. 다른 사람들의 코드가 어떻게 구성되어 있는지를 보며 기본적인 원리를 잘 이해하고 숙지하는 것이 얼마나 중요한지 깨달았습니다. 특히 오류 해결 과정에서 어떻게 더 효과적이고 효율적인 코드를 작성할 수 있는지 고민을 하게 되었고 좀 더 노력해야겠다는 생각이 들었습니다.
