% include('header.tpl')
			<div class="list-new">
				% if not data:
				<p>등록된 작품이 없습니다.</p>
				% else:
				<div>
					<h3>키워드 '{{ keyword }}'</h3>
					<table class="table table-condensed table-list">
						<thead>
							<tr>
								<th>#</th>
								<th>제 목</th>
								<th style="width:40px;">편수</th>
								<th style="width:70px;">갱신일</th>
							</tr>
						</thead>
						<tbody>
							% for r in data:
							<tr>
								<td>{{ r[0] }}</td>
								<td style="text-align:left"><a href="/b/{{ r[0] }}">{{ r[1] }}</a></td>
								<td>{{ r[3] }}</td>
								<td>
									<span title="{{ r[2] }}">{{ r[2].strftime('%y/%m/%d') }}</span>
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
