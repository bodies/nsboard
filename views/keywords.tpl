% include('header.tpl')
			<div class="list-new">
				% if not data:
				<p>등록된 키워드가 없습니다.</p>
				% else:
				<div class="panel panel-warning">
					<div class="panel-heading">
						<h4 class="panel-title">전체 키워드 목록 <small>(가나다 순)</small></h4>
					</div>
					<div class="panel-body keyword-cloud">
						% for r in data:
						<a href="/k/{{ r[0] }}" class="btn btn-default btn-sm btn-keyword">{{ r[0] }}</a>&nbsp;
						% end
					</div>
				</div>
			</div>	<!-- list-new -->
% include('footer.tpl')
