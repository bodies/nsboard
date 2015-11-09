% include('header.tpl')
    <div class="page-list-new">
      <div class="main-panel">
        <h3>키워드 '{{ keyword }}'에 해당하는 작품</h3>
        <div class="panel panel-default panel-simple">
          <div class="panel-body">
            % if not data:
            <p>등록된 작품이 없습니다.</p>
            % else:
            <table class="table table-hover borderless">
              % for r in data:
              <tr>
                <td>
                  <span title="{{ r[2] }}">{{ r[2].strftime('%y/%m/%d') }}</span>
                  &nbsp;
                  <a href="/b/{{ r[0] }}">{{ r[1] }}</a>
                  &nbsp;
                  <span class="item-info hidden-xs">(총 {{ r[3] }}편)</span>
                </td>
              </tr>
              %end
            </table>
            <nav class="pages">
              <ul class="pagination">
                % if not page['prev']:
                <li class="disabled">
                  <span aria-hidden="true">&laquo;</span>
                </li>
                % else:
                <li>
                  <a href="/new?p={{ page['prev'] }}" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                %end
                % for p in range(int(page['start']), int(page['end']) + 1):
                % str_active = ' class="active"' if page['page'] == p else ''
                  <li{{ !str_active }}><a href="/new?p={{ p }}">{{ p }}</a></li>
                % end
                % if not page['next']:
                <li class="disabled">
                  <span aria-hidden="true">&raquo;</span>
                </li>
                % else:
                <li>
                  <a href="/new?p={{ page['next'] }}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                  </a>
                </li>
                % end
              </ul>
            </nav>
          </div>  <!-- panel-body -->
        </div>  <!-- panel -->
      </div>
    </div>  <!-- list-new -->
% include('footer.tpl')
