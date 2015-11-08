% include('header.tpl')
      <div class="jumbotron">
        <h1>꿀단지</h1>
        <p>즐거운 어른 소설 창고</p>
      </div>
			<div class="page-main">
        <div class="main-panel">
          <h3>새로 올라온 작품</h3>
          % for r in new:
          <div class="list-preview">
            <h4><a href="/s/{{ r[0] }}">{{ r[1] }}</a> <small><span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span></small></h4>
            <p>{{ r[3] }}... (<a href="">더 보기</a>)</p>
          </div>
          % end
          <nav>
            <ul class="pager">
              <li class="previous"><a href="">이전</a></li>
              <li class="next"><a href="">다음</a></li>
            </ul>
          </nav>
        </div>  <!-- main-panel -->
      </div>  <!-- page-main -->
% include('footer.tpl')
