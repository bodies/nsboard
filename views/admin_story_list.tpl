% include('admin_header.tpl')
<script>
$(document).ready(function() {
  $(".del_story").click(function() {
    if (confirm("정말 삭제하겠습니까?") ==  true) {
      return true;
    } else { return false; }
  })
})
</script>
      <div class="main-panel">
        <h3>{{ book_title }}</h3>
        <div class="panel panel-default panel-simple">
          <div class="panel-body">
          % if not data:
            <p>등록된 글이 없습니다.</p>
          % else:
            <table class="table table-hover borderless">
              <thead>
              <tr>
                <th></th>
                <th></th>
                <th class="col-sm-2"></th>
              </tr>
              </thead>
              <tbody>
              % for r in data:
              <tr>
                <td>
                  {{ r['queue_num'] }}.&nbsp;
                </td>
                <td>
                  <a href="/a/s/{{ r['num'] }}">{{ r['title'] }}</a>
                  <br />
                  <span class="item-info">
                  ({{ '공개' if r['public'] else '비공개' }},
                  등록: <span title="{{ r['pub_date'] }}">{{ r['pub_date'].strftime('%Y/%m/%d') }}</span>,
                  수정: <span title="{{ r['mod_date'] }}">{{ r['mod_date'].strftime('%Y/%m/%d') }}</span>,
                  조회: {{ r['view_count'] }}, 추천: {{ r['like_count'] }}
                  )
                  </span>
                </td>
                <td>
                  <a href="/a/s/{{ r['num'] }}/mod" class="btn btn-xs btn-warning" role="button">수정</a>
                  <a href="/a/s/{{ r['num'] }}/delete" class="btn btn-xs btn-danger del_story" role="button">삭제</a>
                </td>
              </tr>
              % end
              </tbody>
            </table>
            <div>
              <div class="pull-left">
                <a class="btn btn-sm btn-default" href="/a/book_list" role="button">작품 목록</a>
              </div>
              <div class="pull-right">
                <a href="/a/b/{{ book_num }}" class="btn btn-sm btn-default" role="button">작품 정보</a>
                <a href="/a/b/{{ book_num }}/write_story" class="btn btn-sm btn-primary" role="button">연재하기</a>
              </div>
            </div>
          </div>  <!-- panel-body-->
        </div>  <!-- panel -->
      </div>  <!-- main-panel -->
% include('footer.tpl')
