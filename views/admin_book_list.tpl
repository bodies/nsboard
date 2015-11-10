% include('admin_header.tpl')
    <div class="main-panel">
      <h3>작품 목록</h3>
      <div class="panel panel-default panel-simple">
        <div class="panel-body">
        % if not data:
          <p>등록된 작품이 없습니다.</p>
        % else:
          <table class="table table-hover borderless">
            % for r in data:
            <tr>
              <td>
                {{ r['num'] }}.
                &nbsp;
                <a href="b/{{r['num']}}">{{ r['title'] }}</a>
                &nbsp;
                <span class="item-info">
                (총 {{ r['story_count'] }}편, 등록일:<span title="{{ r['pub_date'] }}">{{ r['pub_date'].strftime('%y/%m/%d') }}</span>, 최근 연재: <span title="{{ r['update_date'] }}">{{ r['update_date'].strftime('%y/%m/%d') if r['update_date'] else '-' }}</span>)
                </span>
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
    </div>  <!-- main-panel -->
% include('footer.tpl')
