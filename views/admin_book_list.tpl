% include('header.tpl')
% include('menu_admin.tpl')
    <div class="col-md-10">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">작품 목록</h4>
        </div>
        <div class="panel-body">
        % if not data:
          <p>등록된 작품이 없습니다.</p>
        % else:
          <table class="table table-condensed">
            <tr>
              <th>작품 번호</th>
              <th>작품명</th>
              <th>연재 횟수</th>
              <th>최근 연재</th>
              <th>등록일</th>
            </tr>
            % for r in data:
            <tr>
              <td>{{ r['num'] }}</td>
              <td><a href="b/{{r['num']}}">{{ r['title'] }}</a></td>
              <td>{{ r['story_count'] }}</td>
              <td>
                <span title="{{ r['update_date'] }}">{{ r['update_date'].strftime('%Y/%m/%d') }}</span>
              </td>
              <td>
                <span title="{{ r['pub_date'] }}">{{ r['pub_date'].strftime('%Y/%m/%d') }}</span>
              </td>
            </tr>
            % end
          </table>
        % end
          <div class="form-group form-group-sm">
            <a href="/a/new_book" class="btn btn-sm btn-primary" role="button">새 작품 등록</a>
          </div>
        </div>  <!-- panel-body -->
      </div>  <!-- panel -->
    </div>  <!-- col-md-10 -->
% include('footer.tpl')
