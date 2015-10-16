% include('header.tpl')
			<div class="main-page">
				<div class="row">
					<div class="col-sm-6">
						<div class="panel panel-default panel-simple">
							<h4 class="panel-title">최근 글</h4>
							<div class="panel-body">
								<table class="table table-condensed table-hover borderless">
									<tbody>
									% for r in new:
									<tr>
                    <td>
                      <span title="{{ r[2] }}">{{ r[2].strftime('%m/%d') }}</span>&nbsp;&nbsp;
  										<a href="/s/{{ r[0] }}">{{ r[1] }}</a>
                    </td>
									</tr>
									% end
									</tbody>
								</table>
								<div class="more-link">
									<a href="/new">최근 글 보기</a>
								</div>
							</div>
						</div>  <!-- panel -->
					</div>
					<div class="col-sm-6">
						<div class="panel panel-default panel-simple">
							<h3 class="panel-title">추천작</h3>
							<div class="panel-body">
								...
							</div>
						</div>  <!-- panel -->
					</div>
				</div>  <!-- row -->
				<div class="panel panel-default panel-simple">
					<h3 class="panel-title">키워드</h3>
					<div class="panel-body">
						...
					</div>
				</div>  <!-- panel -->
			</div>  <!-- main-page -->
% include('footer.tpl')
