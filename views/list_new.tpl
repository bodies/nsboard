% include('header.tpl')
			<div class="list-new">
				% if not data:
				<p>등록된 작품이 없습니다.</p>
				% else:
				<div>
					<table class="table table-condensed">
						<tbody>
							% for r in data:
							<tr>
								<td>{{ r[0] }}</td>
								<td><a href="/s/{{ r[0] }}">{{ r[1] }}</a></td>
								<td>
									<span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span>
								</td>
							</tr>
							% end
						</tbody>
					</table>
				</div>
			</div>	<!-- list-new -->
% include('footer.tpl')
