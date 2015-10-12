% include('header.tpl')
			<div class="main-page">
				<div class="panel panel-default">
					<div class="panel-heading">
						<h3 class="panel-title">최근 글</h3>
					</div>
					<div class="panel-body">
						<table class="table table-condensed">
							<tbody>
							% for r in new:
							<tr>
								<td>{{ r[1] }}</td>
								<td style="text-align:right">
									<span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span>
								</td>
							</tr>
							% end
							</tbody>
						</table>
					</div>
				</div>  <!-- panel -->
			</div>  <!-- main-page -->
% include('footer.tpl')
