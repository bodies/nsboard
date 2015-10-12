% include('header.tpl')
			<div class="list-new">
				<h4>최근 등록된 작품</h4>
				% if not data:
				<p>등록된 작품이 없습니다.</p>
				% else:
				<div>
					<table class="table">
						<tbody>
							% for r in data:
							<tr>
								<td style="text-align:center">{{ r[0] }}</td>
								<td><a href="/s/{{ r[0] }}">{{ r[1] }}</a></td>
								<td style="text-align:right;">
									<span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span>
								</td>
							</tr>
							% end
						</tbody>
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
				</div>
			</div>	<!-- list-new -->
% include('footer.tpl')
