% title = setdefault('title', '')
% logged = setdefault('logged', False)
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="content-type" content="text/html;chatset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{title}}</title>
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
    <div class="navbar navbar-fixed-top">
      <div class="container">
        <ul class="nav nav-pills pull-left">
          <!-- <li class="nav-title"><a href="/"><span class="glyphicon glyphicon-home"></span> 여우비 책방</a></li> -->
          <li class="nav-title"><a href="/">여우비 책방</a></li>
          <li><a href="/new">최신작</a></li>
          <li class="hidden-xs"><a href="/hot">인기작</a></li>
          <li><a href="#">추천작</a></li>
          <li><a href="/keywords">키워드</a></li>
        </ul>
        <ul class="nav nav-pills pull-right">
          <li><a href="#"><span class="glyphicon glyphicon-bookmark"></span></a></li>
        </ul>
      </div>
    </div>
    <div class="container">
