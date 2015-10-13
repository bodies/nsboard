% include('header.tpl')
			<div class="main-page">
				<div class="panel panel-warning">
					<div class="panel-heading">
						<h3 class="panel-title">최근 글</h3>
					</div>
					<div class="panel-body">
						<table class="table table-condensed">
							<tbody>
							% for r in new:
							<tr>
								<td><a href="/s/{{ r[0] }}">{{ r[1] }}</a></td>
								<td style="text-align:right">
									<span title="{{ r[2] }}">{{ r[2].strftime('%Y/%m/%d') }}</span>
								</td>
							</tr>
							% end
							</tbody>
						</table>
					</div>
				</div>  <!-- panel -->
				<div class="panel panel-warning">
					<div class="panel-heading">
						<h3 class="panel-title">추천작</h3>
					</div>
					<div class="panel-body">
						...
					</div>
				</div>  <!-- panel -->
				<div class="panel panel-warning">
					<div class="panel-heading">
						<h3 class="panel-title">키워드</h3>
					</div>
					<div class="panel-body">
						...
					</div>
				</div>  <!-- panel -->
			</div>  <!-- main-page -->
% include('footer.tpl')
