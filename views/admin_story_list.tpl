% include('header.tpl')
% include('menu_admin.tpl')
<script>
$(document).ready(function() {
	$(".del_story").click(function() {
		if (confirm("정말 삭제하겠습니까?") ==  true) {
			return true;
		} else {
			return false;
		}
	})
})
</script>
			<div class="col-md-10">
				<div class="panel panel-default">
					<div class="panel-heading">
						<h4 class="panel-title">
							{{ book_title }}
						</h4>
					</div>
					<div class="panel-body">
					% if not data:
						<p>등록된 글이 없습니다.</p>
					% else:
						<table class="table table-condensed">
							<tr>
								<th>글번호</th>
								<th>회차</th>
								<th class="col-sm-4">회차 제목</th>
								<th>공개</th>
								<th>조회수</th>
								<th>추천수</th>
								<th>등록일</th>
								<th>수정일</th>
								<th>-</th>
							</tr>
							% for r in data:
							<tr>
								<td>{{ r['num'] }}</td>
								<td>{{ r['queue_num'] }}</td>
								<td><a href="/a/s/{{ r['num'] }}">{{ r['title'] }}</a></td>
								<td>{{ '공개' if r['public'] else '비공개' }}</td>
								<td>{{ r['view_count'] }}</td>
								<td>{{ r['like_count'] }}</td>
								<td>
									<span title="{{ r['pub_date'] }}">{{ r['pub_date'].strftime('%Y/%m/%d') }}</span>
								</td>
								<td>
									<span title="{{ r['mod_date'] }}">{{ r['mod_date'].strftime('%Y/%m/%d') }}</span>
								</td>
								<td>
									<a href="/a/s/{{ r['num'] }}/mod" class="btn btn-xs btn-warning" role="button">수정</a>
									<a href="/a/s/{{ r['num'] }}/delete" class="btn btn-xs btn-danger del_story" role="button">삭제</a>
								</td>
							</tr>
							% end
						</table>
					% end
						<div>
							<div class="pull-left">
								<a class="btn btn-sm btn-default" href="/a/book_list" role="button">작품 목록</a>
							</div>
							<div class="pull-right">
								<a href="/a/b/{{ book_num }}" class="btn btn-sm btn-default" role="button">작품 정보</a>
								<a href="/a/b/{{ book_num }}/write_story" class="btn btn-sm btn-primary" role="button">연재하기</a>
							</div>
						</div>
					</div>	<!-- panel-body-->
				</div>	<!-- panel -->
			</div>	<!-- col-sm-10 -->
% include('footer.tpl')
