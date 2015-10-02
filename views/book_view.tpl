% include('header.tpl')
			<div>
				<h3>{{ info['title'] }}</h3>
				% if not info:
				<p>작품 정보가 존재하지 않습니다.</p>
				% else:
				<table class="table table-condensed">
          <tr>
            <th>작품 구분</th>
            <td>{{ '장편' if info['series'] else '단편' }}</td>
            <th>공개</th>
            <td>
            % if info['public']:
            공개
            % else:
            <span style="font-color:red">비공개</span>
            % end
            </td>
          </tr>
          <tr>
            <th>연재</th>
            <td>{{ info['story_count'] }}</td>
            <th>최근 연재일</th>
            <td>
              <span title="{{ info['update_date'] }}">{{ info['update_date'].strftime('%Y/%m/%d') }}</span>
            </td>
          </tr>
          <tr>
            <th>등록일</th>
            <td>
              <span title="{{ info['pub_date'] }}">{{ info['pub_date'].strftime('%Y/%m/%d') }}</span>
            </td>
            <th>변경일</th>
            <td>
              <span title="{{ info['mod_date'] }}">{{ info['mod_date'].strftime('%Y/%m/%d') }}</span>
            </td>
          </tr>
          <tr>
            <th>키워드</th>
            <td colspan="3">{{ !', '.join(info['keywords']) }}</td>
          </tr>
          <tr>
            <th>작품 소개</th>
            <td colspan="3">{{ info['intro'] if info['intro'] else '-' }}</td>
          </tr>
        </table>
        % if not list:
        <p>등록된 글이 없습니다.</p>
        % else:
        <table class="table table-condensed">
        	<tr>
        		<th>#</th>
        		<th>제목</th>
				    <th>등록일</th>
        	</tr>
        	% for r in list:
        	<tr>
        		<td>{{ r['queue_num'] }}</td>
        		<td><a href="/s/{{ r['num'] }}">{{ r['title'] }}</a></td>
        		<td>
              <span title="{{ r['mod_date'] }}">{{ r['mod_date'].strftime('%Y/%m/%d') }}</span>
            </td>
        	</tr>
        	% end
        </table>
        % end
        % end
			</div>

% include('footer.tpl')
