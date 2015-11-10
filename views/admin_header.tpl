% title = setdefault('title', '')
% logged = setdefault('logged', False)
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="content-type" content="text/html;chatset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{ title }}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/style.css" />
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <nav class="navbar navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-menu">
            <span class="sr-only">메뉴 열기</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/a">꿀단지<sup>관리 모드</sup></a>
        </div>  <!-- navbar-header -->
        <div class="collapse navbar-collapse navbar-right" id="navbar-menu">
          <ul class="nav navbar-nav">
            <li><a href="/a/book_list">작품 목록</a></li>
            <li class="hidden-xs"><a href="/a/new_book">새 작품 등록</a></li>
            <li><a href="/a/backup">DB 백업</a></li>
            <li><a href="/keywords">로그아웃</a></li>
          </ul>
          <!-- <form class="nav navbar-form navbar-right" role="search">
            <div class="form-group">
              <input type="text" class="form-control input-sm" placeholder="제목 검색">
            </div>
          </form> -->
        </div>  <!-- collapse -->
      </div>  <!-- container -->
    </nav>
    <div class="container">
