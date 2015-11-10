% include('admin_header.tpl')
      <div>
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
                  <td>{{ data['story_count'] }} 편</td>
                  <th>완결</th>
                  <td>
                  % if data['complete']:
                  완결
                  % else:
                  미완결
                  % end
                  </td>
                </tr>
                <tr>
                  <th>등록일</th>
                  <td>
                    <span title="{{ data['pub_date'] }}">{{ data['pub_date'].strftime('%Y/%m/%d') }}</span>
                  </td>
                  <th>최근 연재일</th>
                  <td>
                    <span title="{{ data['update_date'] }}">{{ data['update_date'].strftime('%Y/%m/%d') if data['update_date'] else '-' }}</span>
                  </td>
                </tr>
                <tr>
                  <th>조회수</th>
                  <td>{{ data['view_count'] if data['view_count'] else '0' }} 회</td>
                  <th>평균 추천수</th>
                  <td>약 {{ data['like_count'] if data['like_count'] else '0' }}</td>
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
      </div>
% include('footer.tpl')
