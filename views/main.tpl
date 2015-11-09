% include('header.tpl')
      <div class="jumbotron">
        <h1>꿀단지</h1>
        <p>즐거운 어른 소설 창고</p>
      </div>
			<div class="page-main">
        <div class="main-panel">
          <h3>새로 등록된 작품</h3>
          % for r in new:
          <div class="list-preview">
            <h4><a href="/s/{{ r[0] }}">{{ r[1] }}</a> <small><span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span></small></h4>
            <p>{{ r[3] }}... (<a href="">더 보기</a>)</p>
          </div>
          % end
          <div class="list-preview-more">
          <a href="/new" class="btn btn-default btn-lg">새로운 작품 더 보기</a>
          </div>
        </div>  <!-- main-panel -->
      </div>  <!-- page-main -->
% include('footer.tpl')
