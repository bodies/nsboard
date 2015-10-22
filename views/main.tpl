% include('header.tpl')
			<div class="page-main">
        <div class="main-panel">
          <h3>새로 올라온 작품</h3>
          % for r in new:
          <div class="list-preview">
            <h4><a href="/s/{{ r[0] }}">{{ r[1] }}</a> <small><span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span></small></h4>
            <p>{{ r[3] }}... (<a href="">더 보기</a>)</p>
          </div>
          % end
          <div><a href="/new">전체 새 글 목록</a></div>
        </div>  <!-- main-panel -->
      </div>  <!-- page-main -->
% include('footer.tpl')
