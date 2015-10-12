% include('header.tpl')
			<div class="list-new">
				% if not data:
				<p>등록된 작품이 없습니다.</p>
				% else:
				<div>
					<h3>키워드 '{{ keyword }}'</h3>
					<table class="table table-condensed">
						<thead>
							<tr>
								<th>작품번호</th>
								<th>작품명</th>
								<th>편수</th>
								<th>최근 등록일</th>
							</tr>
						</thead>
						<tbody>
							% for r in data:
							<tr>
								<td style="text-align:center">{{ r[0] }}</td>
								<td><a href="/b/{{ r[0] }}">{{ r[1] }}</a></td>
								<td>{{ r[3] }}편</td>
								<td>
									<span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span>
								</td>
							</tr>
							% end
						</tbody>
					</table>
				</div>
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

			</div>	<!-- list-new -->
% include('footer.tpl')
