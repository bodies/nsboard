% include('header.tpl')
			<div class="page-main">
				<div class="row">
          <div class="main-panel col-sm-6">
            <h4 class="panel-title"><a class="link-normal" href="/new">새로 올라온 글</a>
            <div class="more-link pull-right"><a href="/new">more</a></div>
            </h4>
						<div class="panel panel-default panel-simple">
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
							</div>
						</div>  <!-- panel -->
					</div>
					<div class="main-panel col-sm-6">
            <h4 class="panel-title">추천 작품
            <div class="more-link pull-right"><a href="/">more</a></div>
            </h4>
						<div class="panel panel-default panel-simple">
							<div class="panel-body">
								...
							</div>
						</div>  <!-- panel -->
					</div>
				</div>  <!-- row -->
        <div class="row">
          <div class="main-panel col-sm-6">
          <h4 class="panel-title">키워드
          <div class="more-link pull-right"><a href="/keywords">more</a></div>
          </h4>
  				<div class="panel panel-default panel-simple">
  					<div class="panel-body">
  						...
  					</div>
  				</div>  <!-- panel -->
        </div>  <!-- row -->
			</div>  <!-- main-page -->
% include('footer.tpl')
