% include('header.tpl')
% include('menu_admin.tpl')
      <div class="col-md-10">
        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">{{ data['title'] }}</h3>
          </div>
          <div class="panel-body">
            % if not data:
              <p>작품 정보가 존재하지 않습니다.</p>
            % else:
              <table class="table table-condensed">
                <tr>
                  <th>작품 구분</th>
                  <td>{{ '장편' if data['series'] else '단편' }}</td>
                  <th>공개/비공개</th>
                  <td>
                  % if data['public']:
                  공개
                  % else:
                  <span style="font-color:red">비공개</span>
                  % end
                  </td>
                </tr>
                <tr>
                  <th>연재 횟수</th>
                  <td>{{ data['story_count'] }}</td>
                  <th>최근 연재일</th>
                  <td>{{ data['update_date'] }}</td>
                </tr>
                <tr>
                  <th>등록일</th>
                  <td>{{ data['pub_date'] }}</td>
                  <th>변경일</th>
                  <td>{{ data['mod_date'] }}</td>
                </tr>
                <tr>
                  <th>키워드</th>
                  <td colspan="3">{{', '.join(data['keywords']) }}</td>
                </tr>
                <tr>
                  <th>작품 소개</th>
                  <td colspan="3">{{ data['intro'] if data['intro'] else '-' }}</td>
                </tr>
              </table>
              <div>
                <div class="pull-left">
                  <a class="btn btn-sm btn-default" href="/a/book_list" role="button">작품 목록</a>
                </div>
                <div class="pull-right">
                  <a class="btn btn-sm btn-default" href="{{data['num']}}/mod" role="button">정보 수정</a>
                  <a class="btn btn-sm btn-default" href="{{data['num']}}/list" role="button">글 목록</a>
                  <a class="btn btn-sm btn-primary" href="{{data['num']}}/write_story" role="button">연재하기</a>
                </div>
              </div>
            % end
          </div>  <!-- panel-body -->
        </div>  <!-- panel -->
      </div>  <!-- col-md-10 -->
% include('footer.tpl')
